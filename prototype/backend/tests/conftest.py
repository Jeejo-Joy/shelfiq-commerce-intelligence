"""
Pytest configuration and fixtures for ShelfIQ tests
"""

import os
import pytest
import boto3
from moto import mock_dynamodb, mock_s3


@pytest.fixture(scope='function')
def aws_credentials():
    """Mock AWS credentials for testing"""
    os.environ['AWS_ACCESS_KEY_ID'] = 'testing'
    os.environ['AWS_SECRET_ACCESS_KEY'] = 'testing'
    os.environ['AWS_SECURITY_TOKEN'] = 'testing'
    os.environ['AWS_SESSION_TOKEN'] = 'testing'
    os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'


@pytest.fixture(scope='function')
def dynamodb_mock(aws_credentials):
    """Mock DynamoDB for testing"""
    with mock_dynamodb():
        yield boto3.resource('dynamodb', region_name='us-east-1')


@pytest.fixture(scope='function')
def s3_mock(aws_credentials):
    """Mock S3 for testing"""
    with mock_s3():
        yield boto3.client('s3', region_name='us-east-1')


@pytest.fixture(scope='function')
def products_table(dynamodb_mock):
    """Create mock products table"""
    table = dynamodb_mock.create_table(
        TableName='test-products',
        KeySchema=[
            {'AttributeName': 'product_id', 'KeyType': 'HASH'}
        ],
        AttributeDefinitions=[
            {'AttributeName': 'product_id', 'AttributeType': 'S'}
        ],
        BillingMode='PAY_PER_REQUEST'
    )
    return table


@pytest.fixture(scope='function')
def sample_product():
    """Sample product data for testing"""
    return {
        'product_id': 'PROD-001',
        'name': 'Test Product',
        'category': 'Electronics',
        'current_price': 79.99,
        'cost': 45.00,
        'competitor_prices': [74.99, 82.99, 79.00],
        'competitor_names': ['CompA', 'CompB', 'CompC'],
        'sales_rank': 1523,
        'rating': 4.5,
        'review_count': 342,
        'last_updated': '2024-01-15T10:30:00Z'
    }
