#!/usr/bin/env python3
"""
Script to load sample data directly into DynamoDB
Bypasses the Lambda ingestion function
"""

import csv
import boto3
from datetime import datetime
from decimal import Decimal

# DynamoDB client
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('shelfiq-products')

def load_csv_to_dynamodb(csv_file):
    """Load CSV data into DynamoDB"""
    print(f"Loading data from {csv_file}...")

    loaded_count = 0

    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)

        # Batch write items
        with table.batch_writer() as batch:
            for row in reader:
                try:
                    # Parse competitor prices and names (comma-separated strings)
                    comp_prices_str = row['competitor_prices'].strip()
                    comp_names_str = row['competitor_names'].strip()

                    competitor_prices = [Decimal(str(p.strip())) for p in comp_prices_str.split(',') if p.strip()]
                    competitor_names = [n.strip() for n in comp_names_str.split(',') if n.strip()]

                    item = {
                        'product_id': row['product_id'],
                        'name': row['name'],
                        'category': row['category'],
                        'current_price': Decimal(str(row['current_price'])),
                        'cost': Decimal(str(row['cost'])),
                        'competitor_prices': competitor_prices,
                        'competitor_names': competitor_names,
                        'sales_rank': int(row['sales_rank']),
                        'rating': Decimal(str(row['rating'])),
                        'review_count': int(row['review_count']),
                        'last_updated': datetime.utcnow().isoformat()
                    }

                    batch.put_item(Item=item)
                    loaded_count += 1

                    if loaded_count % 10 == 0:
                        print(f"Loaded {loaded_count} products...")

                except Exception as e:
                    print(f"Error loading row: {e}")
                    continue

    print(f"\n✅ Successfully loaded {loaded_count} products to DynamoDB!")
    return loaded_count

if __name__ == '__main__':
    csv_file = '../sample-data/products.csv'
    load_csv_to_dynamodb(csv_file)
