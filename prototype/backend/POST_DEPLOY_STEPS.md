# Post-Deployment Steps

After running `sam deploy`, you need to manually configure the S3 trigger for the data ingestion Lambda function.

## Configure S3 Event Notification

### Option 1: Using AWS CLI

```bash
# Get the Lambda function ARN
LAMBDA_ARN=$(aws lambda get-function --function-name shelfiq-data-ingestion --query 'Configuration.FunctionArn' --output text)

# Get the S3 bucket name
BUCKET_NAME=$(aws cloudformation describe-stacks --stack-name shelfiq-prototype --query 'Stacks[0].Outputs[?OutputKey==`DataBucket`].OutputValue' --output text)

# Add Lambda permission for S3 to invoke it
aws lambda add-permission \
  --function-name shelfiq-data-ingestion \
  --statement-id s3-trigger-permission \
  --action lambda:InvokeFunction \
  --principal s3.amazonaws.com \
  --source-arn arn:aws:s3:::$BUCKET_NAME

# Create S3 event notification configuration
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

echo "S3 trigger configured successfully!"
```

### Option 2: Using AWS Console

1. Go to AWS Lambda Console
2. Open the `shelfiq-data-ingestion` function
3. Click **Add trigger**
4. Select **S3**
5. Choose the bucket: `shelfiq-data-{account-id}`
6. Event type: **All object create events**
7. Prefix: `sample-data/`
8. Suffix: `.csv`
9. Click **Add**

## Verify Configuration

```bash
# Check S3 notification configuration
aws s3api get-bucket-notification-configuration --bucket $BUCKET_NAME

# Test by uploading a file
aws s3 cp ../sample-data/products.csv s3://$BUCKET_NAME/sample-data/

# Check Lambda logs
aws logs tail /aws/lambda/shelfiq-data-ingestion --follow
```

## Why This Step is Needed

The S3 event trigger was removed from the SAM template to avoid a circular dependency error during deployment. CloudFormation cannot resolve:
- Lambda function depends on S3 bucket (for event source)
- S3 bucket depends on Lambda function (for notification configuration)
- Log group depends on Lambda function name

By configuring the S3 trigger post-deployment, we break this circular dependency.
