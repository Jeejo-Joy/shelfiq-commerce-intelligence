"""
Data Ingestion Lambda Function
Processes CSV files from S3 and loads data into DynamoDB
"""

import json
import os
import logging
import boto3
import pandas as pd
from datetime import datetime
from io import StringIO
from typing import Dict, Any, List

# Configure logging
logger = logging.getLogger()
logger.setLevel(os.environ.get('LOG_LEVEL', 'INFO'))

# AWS clients
s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

# Environment variables
PRODUCTS_TABLE = os.environ.get('PRODUCTS_TABLE', 'shelfiq-products')


def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    Lambda handler for S3 CSV ingestion
    Triggered by S3 ObjectCreated events
    """
    logger.info(f"Received event: {json.dumps(event)}")

    try:
        # Parse S3 event
        for record in event.get('Records', []):
            bucket = record['s3']['bucket']['name']
            key = record['s3']['object']['key']

            logger.info(f"Processing file: s3://{bucket}/{key}")

            # Download CSV from S3
            csv_content = download_csv_from_s3(bucket, key)

            # Parse and validate CSV
            products = parse_csv(csv_content)

            # Load into DynamoDB
            loaded_count = load_to_dynamodb(products)

            logger.info(f"Successfully loaded {loaded_count} products to DynamoDB")

        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Data ingestion completed successfully',
                'products_loaded': loaded_count
            })
        }

    except Exception as e:
        logger.error(f"Error processing file: {str(e)}", exc_info=True)
        raise


def download_csv_from_s3(bucket: str, key: str) -> str:
    """Download CSV file from S3"""
    try:
        response = s3_client.get_object(Bucket=bucket, Key=key)
        csv_content = response['Body'].read().decode('utf-8')
        logger.info(f"Downloaded {len(csv_content)} bytes from S3")
        return csv_content
    except Exception as e:
        logger.error(f"Error downloading from S3: {str(e)}")
        raise


def parse_csv(csv_content: str) -> List[Dict[str, Any]]:
    """Parse CSV content and validate data"""
    try:
        # Read CSV into pandas DataFrame
        df = pd.read_csv(StringIO(csv_content))

        logger.info(f"Parsed CSV with {len(df)} rows and columns: {list(df.columns)}")

        # Validate required columns
        required_columns = [
            'product_id', 'name', 'category', 'current_price', 'cost',
            'competitor_prices', 'competitor_names', 'sales_rank', 'rating', 'review_count'
        ]

        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            raise ValueError(f"Missing required columns: {missing_columns}")

        # Convert DataFrame to list of dicts
        products = []
        for _, row in df.iterrows():
            try:
                product = {
                    'product_id': str(row['product_id']),
                    'name': str(row['name']),
                    'category': str(row['category']),
                    'current_price': float(row['current_price']),
                    'cost': float(row['cost']),
                    'competitor_prices': json.loads(row['competitor_prices']) if isinstance(row['competitor_prices'], str) else row['competitor_prices'],
                    'competitor_names': json.loads(row['competitor_names']) if isinstance(row['competitor_names'], str) else row['competitor_names'],
                    'sales_rank': int(row['sales_rank']),
                    'rating': float(row['rating']),
                    'review_count': int(row['review_count']),
                    'last_updated': datetime.utcnow().isoformat()
                }

                # Validate data types
                if not (0 <= product['rating'] <= 5):
                    logger.warning(f"Invalid rating for {product['product_id']}: {product['rating']}")
                    continue

                if product['current_price'] <= 0 or product['cost'] <= 0:
                    logger.warning(f"Invalid price/cost for {product['product_id']}")
                    continue

                products.append(product)

            except Exception as e:
                logger.warning(f"Error parsing row: {str(e)}")
                continue

        logger.info(f"Successfully parsed {len(products)} valid products")
        return products

    except Exception as e:
        logger.error(f"Error parsing CSV: {str(e)}")
        raise


def load_to_dynamodb(products: List[Dict[str, Any]]) -> int:
    """Load products into DynamoDB using batch write"""
    try:
        table = dynamodb.Table(PRODUCTS_TABLE)

        loaded_count = 0
        batch_size = 25  # DynamoDB batch write limit

        # Process in batches
        for i in range(0, len(products), batch_size):
            batch = products[i:i + batch_size]

            with table.batch_writer() as writer:
                for product in batch:
                    writer.put_item(Item=product)
                    loaded_count += 1

            logger.info(f"Loaded batch {i // batch_size + 1}: {len(batch)} items")

        return loaded_count

    except Exception as e:
        logger.error(f"Error loading to DynamoDB: {str(e)}")
        raise
