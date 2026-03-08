"""
API Handler Lambda Function
Handles CRUD operations for products and recommendations
Routes analysis requests to Intelligence function
"""

import json
import os
import logging
import boto3
from typing import Dict, Any, Optional
from decimal import Decimal

# Configure logging
logger = logging.getLogger()
logger.setLevel(os.environ.get('LOG_LEVEL', 'INFO'))

# AWS clients
dynamodb = boto3.resource('dynamodb')
lambda_client = boto3.client('lambda')

# Environment variables
PRODUCTS_TABLE = os.environ.get('PRODUCTS_TABLE', 'shelfiq-products')
RECOMMENDATIONS_TABLE = os.environ.get('RECOMMENDATIONS_TABLE', 'shelfiq-recommendations')
INTELLIGENCE_FUNCTION = 'shelfiq-intelligence'


def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    Lambda handler for API requests
    Routes requests to appropriate handler functions
    """
    logger.info(f"Received event: {json.dumps(event)}")

    try:
        # Parse request
        http_method = event.get('httpMethod')
        path = event.get('path', '')
        path_params = event.get('pathParameters') or {}

        logger.info(f"Method: {http_method}, Path: {path}")

        # Route to appropriate handler
        if path == '/health':
            return handle_health()

        elif path == '/products' and http_method == 'GET':
            return handle_get_products()

        elif '/products/' in path and http_method == 'GET':
            product_id = path_params.get('id')
            return handle_get_product(product_id)

        elif '/recommendations/' in path and http_method == 'GET':
            product_id = path_params.get('product_id')
            return handle_get_recommendations(product_id)

        elif '/analyze/' in path and http_method == 'POST':
            # Forward to Intelligence function
            return invoke_intelligence_function(event)

        elif path == '/chat' and http_method == 'POST':
            # Forward to Intelligence function
            return invoke_intelligence_function(event)

        else:
            return error_response(404, 'Endpoint not found')

    except Exception as e:
        logger.error(f"Error in API handler: {str(e)}", exc_info=True)
        return error_response(500, str(e))


def handle_health() -> Dict[str, Any]:
    """Health check endpoint"""
    return success_response({
        'status': 'healthy',
        'service': 'ShelfIQ API',
        'timestamp': datetime_now()
    })


def handle_get_products() -> Dict[str, Any]:
    """Get all products (limited to 100 for prototype)"""
    try:
        table = dynamodb.Table(PRODUCTS_TABLE)
        response = table.scan(Limit=100)

        items = response.get('Items', [])

        # Convert to summary format
        products = [
            {
                'product_id': item['product_id'],
                'name': item['name'],
                'category': item['category'],
                'current_price': float(item['current_price']),
                'sales_rank': int(item['sales_rank']),
                'rating': float(item['rating']),
                'review_count': int(item['review_count'])
            }
            for item in items
        ]

        logger.info(f"Retrieved {len(products)} products")

        return success_response({
            'count': len(products),
            'products': products
        })

    except Exception as e:
        logger.error(f"Error getting products: {str(e)}")
        return error_response(500, 'Error retrieving products')


def handle_get_product(product_id: str) -> Dict[str, Any]:
    """Get single product by ID"""
    if not product_id:
        return error_response(400, 'Product ID is required')

    try:
        table = dynamodb.Table(PRODUCTS_TABLE)
        response = table.get_item(Key={'product_id': product_id})

        item = response.get('Item')
        if not item:
            return error_response(404, f'Product not found: {product_id}')

        # Convert Decimal to float for JSON serialization
        product = convert_decimals(item)

        logger.info(f"Retrieved product: {product_id}")

        return success_response(product)

    except Exception as e:
        logger.error(f"Error getting product {product_id}: {str(e)}")
        return error_response(500, 'Error retrieving product')


def handle_get_recommendations(product_id: str) -> Dict[str, Any]:
    """Get recommendation history for a product"""
    if not product_id:
        return error_response(400, 'Product ID is required')

    try:
        table = dynamodb.Table(RECOMMENDATIONS_TABLE)
        response = table.query(
            KeyConditionExpression='product_id = :pid',
            ExpressionAttributeValues={':pid': product_id},
            ScanIndexForward=False,  # Sort by timestamp descending
            Limit=10
        )

        items = response.get('Items', [])
        recommendations = [convert_decimals(item) for item in items]

        logger.info(f"Retrieved {len(recommendations)} recommendations for {product_id}")

        return success_response({
            'product_id': product_id,
            'count': len(recommendations),
            'recommendations': recommendations
        })

    except Exception as e:
        logger.error(f"Error getting recommendations for {product_id}: {str(e)}")
        return error_response(500, 'Error retrieving recommendations')


def invoke_intelligence_function(event: Dict[str, Any]) -> Dict[str, Any]:
    """Forward request to Intelligence Lambda function"""
    try:
        logger.info(f"Invoking Intelligence function for path: {event.get('path')}")

        response = lambda_client.invoke(
            FunctionName=INTELLIGENCE_FUNCTION,
            InvocationType='RequestResponse',
            Payload=json.dumps(event)
        )

        payload = json.loads(response['Payload'].read())
        logger.info(f"Intelligence function response: {payload.get('statusCode')}")

        return payload

    except Exception as e:
        logger.error(f"Error invoking Intelligence function: {str(e)}")
        return error_response(500, 'Error processing analysis request')


def convert_decimals(obj):
    """Convert DynamoDB Decimal types to float for JSON serialization"""
    if isinstance(obj, list):
        return [convert_decimals(item) for item in obj]
    elif isinstance(obj, dict):
        return {key: convert_decimals(value) for key, value in obj.items()}
    elif isinstance(obj, Decimal):
        return float(obj)
    else:
        return obj


def datetime_now() -> str:
    """Get current datetime as ISO string"""
    from datetime import datetime
    return datetime.utcnow().isoformat()


def success_response(data: Dict) -> Dict:
    """Format success response with CORS headers"""
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
            'Access-Control-Allow-Methods': 'GET,POST,OPTIONS'
        },
        'body': json.dumps(data, default=str)
    }


def error_response(status_code: int, message: str) -> Dict:
    """Format error response with CORS headers"""
    return {
        'statusCode': status_code,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
            'Access-Control-Allow-Methods': 'GET,POST,OPTIONS'
        },
        'body': json.dumps({'error': message})
    }
