"""
Intelligence Lambda Function
Handles AI-powered analysis using Amazon Bedrock
"""

import json
import os
import logging
import boto3
import hashlib
from datetime import datetime, timedelta
from typing import Dict, Any, Optional
from decimal import Decimal

# Configure logging
logger = logging.getLogger()
logger.setLevel(os.environ.get('LOG_LEVEL', 'INFO'))

# AWS clients
dynamodb = boto3.resource('dynamodb')
bedrock_runtime = boto3.client('bedrock-runtime', region_name=os.environ.get('BEDROCK_REGION', 'us-east-1'))

# Environment variables
PRODUCTS_TABLE = os.environ.get('PRODUCTS_TABLE', 'shelfiq-products')
RECOMMENDATIONS_TABLE = os.environ.get('RECOMMENDATIONS_TABLE', 'shelfiq-recommendations')
CACHE_TABLE = os.environ.get('CACHE_TABLE', 'shelfiq-analysis-cache')
BEDROCK_MODEL_ID = os.environ.get('BEDROCK_MODEL_ID', 'anthropic.claude-3-7-sonnet-20250219-v1:0')
MOCK_BEDROCK = os.environ.get('MOCK_BEDROCK', 'false').lower() == 'true'


def convert_floats_to_decimal(obj):
    """Recursively convert all float values to Decimal for DynamoDB"""
    if isinstance(obj, list):
        return [convert_floats_to_decimal(item) for item in obj]
    elif isinstance(obj, dict):
        return {key: convert_floats_to_decimal(value) for key, value in obj.items()}
    elif isinstance(obj, float):
        return Decimal(str(obj))
    else:
        return obj

def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    Lambda handler for intelligence requests
    Routes to appropriate analysis handler
    """
    logger.info(f"Received event: {json.dumps(event)}")

    try:
        # Parse request
        path = event.get('path', '')
        product_id = event.get('pathParameters', {}).get('product_id')

        logger.info(f"Path: {path}, Product ID: {product_id}")

        # Route to appropriate handler
        if '/analyze/pricing/' in path:
            result = handle_pricing_analysis(product_id)
        elif '/analyze/demand/' in path:
            result = handle_demand_analysis(product_id)
        elif '/analyze/competitors/' in path:
            result = handle_competitor_analysis(product_id)
        elif '/chat' in path:
            body = json.loads(event.get('body', '{}'))
            result = handle_chat(body)
        else:
            return error_response(400, 'Invalid analysis type')

        return success_response(result)

    except Exception as e:
        logger.error(f"Error in intelligence handler: {str(e)}", exc_info=True)
        return error_response(500, str(e))


def handle_pricing_analysis(product_id: str) -> Dict[str, Any]:
    """Generate pricing recommendation using Bedrock"""
    logger.info(f"Pricing analysis for product: {product_id}")

    # Check cache
    cache_key = f"pricing_{product_id}"
    cached = get_from_cache(cache_key)
    if cached:
        logger.info("Returning cached pricing analysis")
        return cached

    # Get product data
    product = get_product(product_id)
    if not product:
        raise ValueError(f"Product not found: {product_id}")

    # Calculate competitor statistics
    competitor_prices = product.get('competitor_prices', [])
    if competitor_prices:
        comp_stats = {
            'min': min(competitor_prices),
            'max': max(competitor_prices),
            'median': sorted(competitor_prices)[len(competitor_prices) // 2],
            'avg': sum(competitor_prices) / len(competitor_prices)
        }
    else:
        comp_stats = {'min': 0, 'max': 0, 'median': 0, 'avg': 0}

    # Create pricing prompt
    prompt = create_pricing_prompt(product, comp_stats)

    # Invoke Bedrock
    analysis = invoke_bedrock(prompt, 'pricing')

    # Store recommendation
    recommendation = {
        'product_id': product_id,
        'timestamp': datetime.utcnow().isoformat(),
        'analysis_type': 'pricing',
        'current_price': float(product['current_price']),
        'suggested_price': analysis.get('suggested_price'),
        'reasoning': analysis.get('reasoning'),
        'competitive_position': analysis.get('competitive_position'),
        'expected_impact': analysis.get('expected_impact'),
        'confidence_score': analysis.get('confidence_score'),
        'ttl': int((datetime.utcnow() + timedelta(days=7)).timestamp())
    }

    store_recommendation(recommendation)
    store_in_cache(cache_key, recommendation)

    return recommendation


def handle_demand_analysis(product_id: str) -> Dict[str, Any]:
    """Generate demand insights using Bedrock"""
    logger.info(f"Demand analysis for product: {product_id}")

    cache_key = f"demand_{product_id}"
    cached = get_from_cache(cache_key)
    if cached:
        return cached

    product = get_product(product_id)
    if not product:
        raise ValueError(f"Product not found: {product_id}")

    prompt = create_demand_prompt(product)
    analysis = invoke_bedrock(prompt, 'demand')

    result = {
        'product_id': product_id,
        'timestamp': datetime.utcnow().isoformat(),
        'analysis_type': 'demand',
        'demand_trend': analysis.get('demand_trend'),
        'forecast_7d': analysis.get('forecast_7d'),
        'forecast_30d': analysis.get('forecast_30d'),
        'key_drivers': analysis.get('key_drivers'),
        'recommendations': analysis.get('recommendations')
    }

    store_in_cache(cache_key, result)
    return result


def handle_competitor_analysis(product_id: str) -> Dict[str, Any]:
    """Generate competitor analysis"""
    logger.info(f"Competitor analysis for product: {product_id}")

    product = get_product(product_id)
    if not product:
        raise ValueError(f"Product not found: {product_id}")

    competitor_prices = product.get('competitor_prices', [])
    competitor_names = product.get('competitor_names', [])
    current_price = float(product['current_price'])

    if not competitor_prices:
        return {
            'product_id': product_id,
            'competitive_position': 'no_data',
            'message': 'No competitor data available'
        }

    # Calculate position
    sorted_prices = sorted(competitor_prices)
    rank = sum(1 for p in competitor_prices if p < current_price) + 1
    percentile = (rank / (len(competitor_prices) + 1)) * 100

    # Determine position
    if percentile > 75:
        position = 'overpriced'
        action = 'Consider lowering price to improve competitiveness'
    elif percentile < 25:
        position = 'underpriced'
        action = 'Opportunity to increase price and improve margins'
    else:
        position = 'competitive'
        action = 'Price is well-positioned in the market'

    return {
        'product_id': product_id,
        'current_price': current_price,
        'competitor_count': len(competitor_prices),
        'price_rank': rank,
        'percentile': round(percentile, 1),
        'competitive_position': position,
        'min_competitor_price': min(competitor_prices),
        'max_competitor_price': max(competitor_prices),
        'median_competitor_price': sorted_prices[len(sorted_prices) // 2],
        'recommended_action': action,
        'competitors': [
            {'name': name, 'price': price}
            for name, price in zip(competitor_names, competitor_prices)
        ]
    }


def handle_chat(body: Dict[str, Any]) -> Dict[str, Any]:
    """Handle chat copilot requests"""
    message = body.get('message', '')
    conversation_id = body.get('conversation_id', 'default')
    history = body.get('history', [])

    logger.info(f"Chat request: {message}")

    # Simple keyword-based context retrieval for prototype
    context_data = {}
    if 'product' in message.lower() or 'price' in message.lower():
        # Get sample products for context
        products = scan_products(limit=10)
        context_data['products'] = products

    prompt = create_chat_prompt(message, history, context_data)
    response = invoke_bedrock(prompt, 'chat')

    return {
        'conversation_id': conversation_id,
        'message': response.get('response', 'I can help you with pricing and product analysis.'),
        'timestamp': datetime.utcnow().isoformat()
    }


def create_pricing_prompt(product: Dict, comp_stats: Dict) -> str:
    """Create prompt for pricing analysis"""
    return f"""You are an AI pricing analyst for the Indian e-commerce market. Analyze this product and provide pricing recommendations.

IMPORTANT: All prices are in Indian Rupees (INR/₹). Consider Indian market dynamics and purchasing power.

Product Details:
- Name: {product['name']}
- Category: {product['category']}
- Current Price: ₹{product['current_price']:.2f}
- Cost: ₹{product['cost']:.2f}
- Current Margin: {((product['current_price'] - product['cost']) / product['current_price'] * 100):.1f}%
- Sales Rank: {product['sales_rank']}
- Rating: {product['rating']}/5.0 ({product['review_count']} reviews)

Competitor Pricing (in INR):
- Minimum: ₹{comp_stats['min']:.2f}
- Maximum: ₹{comp_stats['max']:.2f}
- Median: ₹{comp_stats['median']:.2f}
- Average: ₹{comp_stats['avg']:.2f}

Provide a pricing recommendation in JSON format with these fields:
- suggested_price: recommended price in INR (number, must be realistic for Indian market)
- reasoning: explanation of recommendation considering Indian market context (string)
- competitive_position: "overpriced", "competitive", or "underpriced" (string)
- expected_impact: expected revenue/margin impact (string)
- confidence_score: confidence in recommendation 0-1 (number)
- risks: potential risks (array of strings)
- opportunities: potential opportunities (array of strings)

Respond with ONLY valid JSON, no other text."""


def create_demand_prompt(product: Dict) -> str:
    """Create prompt for demand analysis"""
    return f"""Analyze demand trends for this product in the Indian e-commerce market:

Product: {product['name']}
Category: {product['category']}
Current Price: ₹{product['current_price']:.2f} (Indian Rupees)
Sales Rank: {product['sales_rank']} (lower is better)
Rating: {product['rating']}/5.0
Reviews: {product['review_count']}

Provide demand insights in JSON format:
- demand_trend: "increasing", "stable", or "decreasing"
- forecast_7d: 7-day sales forecast (string)
- forecast_30d: 30-day sales forecast (string)
- key_drivers: factors affecting demand (array)
- recommendations: actionable recommendations (array)

Respond with ONLY valid JSON."""


def create_chat_prompt(message: str, history: list, context: Dict) -> str:
    """Create prompt for chat copilot"""
    context_str = json.dumps(context, indent=2) if context else "No specific context"

    return f"""You are ShelfIQ, an AI commerce intelligence assistant. Help users with pricing and product analysis.

Context Data:
{context_str}

User Message: {message}

Provide a helpful, concise response. If asked about specific products or pricing, use the context data.

Respond in JSON format:
- response: your message to the user (string)

Respond with ONLY valid JSON."""


def invoke_bedrock(prompt: str, analysis_type: str) -> Dict[str, Any]:
    """Invoke Bedrock model or return mock response"""
    if MOCK_BEDROCK:
        logger.info("Using mock Bedrock response (MOCK_BEDROCK=true)")
        return get_mock_response(analysis_type)

    try:
        # Format request for Claude
        request_body = {
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 2000,
            "temperature": 0.7,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }

        logger.info(f"Invoking Bedrock model: {BEDROCK_MODEL_ID}")
        logger.info(f"Request body: {json.dumps(request_body)[:500]}...")

        response = bedrock_runtime.invoke_model(
            modelId=BEDROCK_MODEL_ID,
            body=json.dumps(request_body)
        )

        response_body = json.loads(response['body'].read())
        content = response_body['content'][0]['text']

        logger.info(f"Bedrock response received successfully: {content[:200]}...")

        # Parse JSON from response
        parsed_response = json.loads(content)
        logger.info(f"Parsed response: {json.dumps(parsed_response)[:300]}...")
        return parsed_response

    except Exception as e:
        logger.error(f"BEDROCK ERROR - Type: {type(e).__name__}")
        logger.error(f"BEDROCK ERROR - Message: {str(e)}")
        logger.error(f"BEDROCK ERROR - Returning mock response for analysis_type: {analysis_type}")
        import traceback
        logger.error(f"BEDROCK ERROR - Traceback: {traceback.format_exc()}")
        return get_mock_response(analysis_type)


def get_mock_response(analysis_type: str) -> Dict[str, Any]:
    """Return mock response for testing"""
    if analysis_type == 'pricing':
        return {
            'suggested_price': 89.99,
            'reasoning': 'Based on competitor analysis and market position, a slight price adjustment is recommended.',
            'competitive_position': 'competitive',
            'expected_impact': '+5% revenue, +2% margin',
            'confidence_score': 0.85,
            'risks': ['Potential competitor response'],
            'opportunities': ['Improved market share']
        }
    elif analysis_type == 'demand':
        return {
            'demand_trend': 'stable',
            'forecast_7d': 'Expected 50-60 units',
            'forecast_30d': 'Expected 200-250 units',
            'key_drivers': ['Seasonal demand', 'Competitive pricing'],
            'recommendations': ['Monitor competitor pricing', 'Consider promotional campaigns']
        }
    elif analysis_type == 'chat':
        return {
            'response': 'I can help you analyze product pricing and market trends. What would you like to know?'
        }
    return {}


def get_product(product_id: str) -> Optional[Dict]:
    """Retrieve product from DynamoDB"""
    try:
        table = dynamodb.Table(PRODUCTS_TABLE)
        response = table.get_item(Key={'product_id': product_id})
        return response.get('Item')
    except Exception as e:
        logger.error(f"Error getting product: {str(e)}")
        return None


def scan_products(limit: int = 10) -> list:
    """Scan products table"""
    try:
        table = dynamodb.Table(PRODUCTS_TABLE)
        response = table.scan(Limit=limit)
        return response.get('Items', [])
    except Exception as e:
        logger.error(f"Error scanning products: {str(e)}")
        return []


def store_recommendation(recommendation: Dict):
    """Store recommendation in DynamoDB"""
    try:
        table = dynamodb.Table(RECOMMENDATIONS_TABLE)
        # Convert floats to Decimal for DynamoDB
        item = convert_floats_to_decimal(recommendation)
        table.put_item(Item=item)
    except Exception as e:
        logger.error(f"Error storing recommendation: {str(e)}")


def get_from_cache(cache_key: str) -> Optional[Dict]:
    """Get cached analysis"""
    try:
        table = dynamodb.Table(CACHE_TABLE)
        response = table.get_item(Key={'cache_key': cache_key})
        item = response.get('Item')

        if item and item.get('ttl', 0) > datetime.utcnow().timestamp():
            logger.info(f"Cache hit for {cache_key}")
            return item.get('data')

        return None
    except Exception as e:
        logger.error(f"Error getting from cache: {str(e)}")
        return None


def store_in_cache(cache_key: str, data: Dict):
    """Store analysis in cache"""
    try:
        table = dynamodb.Table(CACHE_TABLE)
        # Convert floats to Decimal for DynamoDB
        cache_data = convert_floats_to_decimal(data)
        table.put_item(Item={
            'cache_key': cache_key,
            'data': cache_data,
            'ttl': int((datetime.utcnow() + timedelta(hours=1)).timestamp())
        })
    except Exception as e:
        logger.error(f"Error storing in cache: {str(e)}")


def success_response(data: Dict) -> Dict:
    """Format success response"""
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(data, default=str)
    }


def error_response(status_code: int, message: str) -> Dict:
    """Format error response"""
    return {
        'statusCode': status_code,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({'error': message})
    }
