#!/bin/bash
# ShelfIQ Backend Deployment Script

set -e

echo "🚀 ShelfIQ Backend Deployment"
echo "=============================="
echo ""

# Check if we're in the right directory
if [ ! -f "template.yaml" ]; then
    echo "❌ Error: template.yaml not found"
    echo "Please run this script from the backend directory"
    exit 1
fi

# Check if SAM CLI is installed
if ! command -v sam &> /dev/null; then
    echo "❌ AWS SAM CLI is not installed"
    echo "Install it from: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html"
    exit 1
fi

# Check if AWS CLI is configured
if ! aws sts get-caller-identity &> /dev/null; then
    echo "❌ AWS credentials not configured"
    echo "Run: aws configure"
    exit 1
fi

echo "✅ Prerequisites check passed"
echo ""

# Build Lambda functions
echo "📦 Building Lambda functions..."
sam build
echo "✅ Build complete"
echo ""

# Deploy
echo "🚀 Deploying to AWS..."
if [ -f "samconfig.toml" ]; then
    echo "Using existing SAM configuration..."
    sam deploy
else
    echo "First time deployment - running guided setup..."
    sam deploy --guided
fi

echo ""
echo "✅ Deployment complete!"
echo ""

# Get outputs
echo "📋 Stack Outputs:"
aws cloudformation describe-stacks \
    --stack-name shelfiq-prototype \
    --query 'Stacks[0].Outputs' \
    --output table

echo ""
echo "Next steps:"
echo "1. Upload sample data: aws s3 cp ../sample-data/products.csv s3://\$(aws cloudformation describe-stacks --stack-name shelfiq-prototype --query 'Stacks[0].Outputs[?OutputKey==\`DataBucket\`].OutputValue' --output text)/sample-data/"
echo "2. Check CloudWatch logs for data ingestion"
echo "3. Test API endpoints"
echo "4. Update frontend .env with API endpoint"
echo ""
