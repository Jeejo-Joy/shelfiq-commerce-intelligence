#!/bin/bash
set -e

echo "Configuring S3 trigger for Data Ingestion Lambda..."

# Get the Lambda function ARN
LAMBDA_ARN=$(aws lambda get-function \
  --function-name shelfiq-data-ingestion \
  --query 'Configuration.FunctionArn' \
  --output text)

echo "Lambda ARN: $LAMBDA_ARN"

# Get the S3 bucket name
BUCKET_NAME=$(aws cloudformation describe-stacks \
  --stack-name shelfiq-prototype \
  --query 'Stacks[0].Outputs[?OutputKey==`DataBucket`].OutputValue' \
  --output text)

echo "Bucket Name: $BUCKET_NAME"

# Add Lambda permission for S3 to invoke it
echo "Adding Lambda permission for S3..."
aws lambda add-permission \
  --function-name shelfiq-data-ingestion \
  --statement-id s3-trigger-permission \
  --action lambda:InvokeFunction \
  --principal s3.amazonaws.com \
  --source-arn arn:aws:s3:::$BUCKET_NAME \
  2>/dev/null || echo "Permission already exists, continuing..."

# Create S3 event notification configuration
echo "Creating S3 notification configuration..."
cat > /tmp/s3-notification.json << EOF
{
  "LambdaFunctionConfigurations": [
    {
      "Id": "DataIngestionTrigger",
      "LambdaFunctionArn": "$LAMBDA_ARN",
      "Events": ["s3:ObjectCreated:*"],
      "Filter": {
        "Key": {
          "FilterRules": [
            {
              "Name": "prefix",
              "Value": "sample-data/"
            },
            {
              "Name": "suffix",
              "Value": ".csv"
            }
          ]
        }
      }
    }
  ]
}
EOF

# Apply the notification configuration
aws s3api put-bucket-notification-configuration \
  --bucket $BUCKET_NAME \
  --notification-configuration file:///tmp/s3-notification.json

echo "✅ S3 trigger configured successfully!"
echo ""
echo "To test, re-upload the CSV file:"
echo "aws s3 cp ../sample-data/products.csv s3://$BUCKET_NAME/sample-data/"
echo ""
echo "Then check logs:"
echo "aws logs tail /aws/lambda/shelfiq-data-ingestion --follow"
