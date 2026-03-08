#!/bin/bash
set -e

echo "🚀 Deploying ShelfIQ Frontend to S3..."

# Get API URL
API_URL=$(aws cloudformation describe-stacks \
  --stack-name shelfiq-prototype \
  --query 'Stacks[0].Outputs[?OutputKey==`ApiEndpoint`].OutputValue' \
  --output text)

echo "API URL: $API_URL"

# Update .env file
cd ../frontend
echo "VITE_API_ENDPOINT=$API_URL" > .env

# Build frontend
echo "📦 Building frontend..."
npm run build

# Get frontend bucket name
FRONTEND_BUCKET=$(aws cloudformation describe-stacks \
  --stack-name shelfiq-prototype \
  --query 'Stacks[0].Outputs[?OutputKey==`FrontendBucket`].OutputValue' \
  --output text)

echo "Frontend Bucket: $FRONTEND_BUCKET"

# Deploy to S3
echo "☁️  Uploading to S3..."
aws s3 sync dist/ s3://$FRONTEND_BUCKET/ --delete

# Get frontend URL
FRONTEND_URL=$(aws cloudformation describe-stacks \
  --stack-name shelfiq-prototype \
  --query 'Stacks[0].Outputs[?OutputKey==`FrontendUrl`].OutputValue' \
  --output text)

echo ""
echo "✅ Frontend deployed successfully!"
echo ""
echo "🌐 Frontend URL: $FRONTEND_URL"
echo "📡 API URL: $API_URL"
echo ""
echo "Share this URL with others: $FRONTEND_URL"
