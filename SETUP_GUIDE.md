# ShelfIQ Prototype - Complete Setup Guide

## Prerequisites Checklist

- [ ] AWS Account with admin access
- [ ] AWS CLI installed (`aws --version`)
- [ ] AWS SAM CLI installed (`sam --version`)
- [ ] Python 3.11+ installed (`python --version`)
- [ ] Node.js 18+ installed (`node --version`)
- [ ] Conda installed (`conda --version`)
- [ ] Git installed (`git --version`)

---

## Step 1: Configure AWS Credentials

### Option A: Using AWS CLI Configure (Recommended)
```bash
aws configure
```

You'll be prompted for:
- **AWS Access Key ID**: `[Your Access Key]`
- **AWS Secret Access Key**: `[Your Secret Key]`
- **Default region name**: `us-east-1` (or your preferred region)
- **Default output format**: `json`

### Option B: Manual Configuration
Create/edit `~/.aws/credentials`:
```ini
[default]
aws_access_key_id = YOUR_ACCESS_KEY_ID
aws_secret_access_key = YOUR_SECRET_ACCESS_KEY
```

Create/edit `~/.aws/config`:
```ini
[default]
region = us-east-1
output = json
```

### Verify AWS Credentials
```bash
aws sts get-caller-identity
```

Expected output:
```json
{
    "UserId": "AIDXXXXXXXXXXXXXXXXXX",
    "Account": "123456789012",
    "Arn": "arn:aws:iam::123456789012:user/your-username"
}
```

---

## Step 2: Activate Conda Environment

```bash
# Navigate to project root
cd /Users/I335620/Projects/ShelfIQ

# List available conda environments
conda env list

# Activate your environment (replace with your env name)
conda activate shelfiq

# OR if you need to create a new environment:
conda create -n shelfiq python=3.11 -y
conda activate shelfiq
```

---

## Step 3: Install Python Dependencies

```bash
cd prototype/backend

# Install Lambda dependencies
pip install -r requirements.txt

# Install development dependencies
pip install -r requirements-dev.txt

# Verify installation
pip list | grep boto3
pip list | grep pandas
```

---

## Step 4: Generate Sample Data

```bash
cd ../scripts

# Run data generation script
python generate_sample_data.py

# Verify output
ls -lh ../sample-data/products.csv
head -n 5 ../sample-data/products.csv
```

Expected output: `products.csv` with 50 products across 5 categories.

---

## Step 5: Review and Validate SAM Template

```bash
cd ../backend

# Validate SAM template
sam validate

# Review template
cat template.yaml
```

If validation passes, proceed to deployment.

---

## Step 6: Build Lambda Functions

```bash
# Build all Lambda functions
sam build

# Expected output: Build successful for all functions
```

---

## Step 7: Deploy Infrastructure to AWS

### First-Time Deployment (Guided)
```bash
sam deploy --guided
```

**Prompts and Recommended Answers:**
```
Setting name: shelfiq-prototype
AWS Region: us-east-1
Confirm changes before deploy: Y
Allow SAM CLI IAM role creation: Y
Disable rollback: N
Save arguments to configuration file: Y
SAM configuration file: samconfig.toml
SAM configuration environment: default
```

### Subsequent Deployments
```bash
sam deploy
```

### Capture Important Outputs
After deployment completes, save these outputs:
```bash
# Get all stack outputs
aws cloudformation describe-stacks \
  --stack-name shelfiq-prototype \
  --query 'Stacks[0].Outputs' \
  --output table

# Save to file
aws cloudformation describe-stacks \
  --stack-name shelfiq-prototype \
  --query 'Stacks[0].Outputs' \
  --output json > deployment-outputs.json
```

**Important outputs to note:**
- `ApiUrl`: API Gateway endpoint URL
- `DataBucket`: S3 bucket name for data
- `FrontendBucket`: S3 bucket name for frontend
- `ProductsTable`: DynamoDB table name
- `RecommendationsTable`: DynamoDB table name

---

## Step 8: Enable Amazon Bedrock Model Access

### Via AWS Console:
1. Open AWS Console: https://console.aws.amazon.com/bedrock/
2. Navigate to **Model access** in left sidebar
3. Click **Manage model access** button
4. Find **Anthropic** section
5. Check the box for **Claude 3 Sonnet**
6. Click **Request model access** at bottom
7. Wait for approval (usually 2-5 minutes)

### Verify Model Access:
```bash
aws bedrock list-foundation-models \
  --by-provider anthropic \
  --query 'modelSummaries[?modelId==`anthropic.claude-3-sonnet-20240229-v1:0`]' \
  --output table
```

---

## Step 9: Upload Sample Data to S3

```bash
# Get S3 bucket name
DATA_BUCKET=$(aws cloudformation describe-stacks \
  --stack-name shelfiq-prototype \
  --query 'Stacks[0].Outputs[?OutputKey==`DataBucket`].OutputValue' \
  --output text)

echo "Data Bucket: $DATA_BUCKET"

# Upload sample data
aws s3 cp ../sample-data/products.csv s3://$DATA_BUCKET/sample-data/

# Verify upload
aws s3 ls s3://$DATA_BUCKET/sample-data/
```

---

## Step 10: Verify Data Ingestion

```bash
# Check CloudWatch logs for ingestion Lambda
aws logs tail /aws/lambda/shelfiq-prototype-DataIngestion --follow

# Query DynamoDB to verify data loaded
PRODUCTS_TABLE=$(aws cloudformation describe-stacks \
  --stack-name shelfiq-prototype \
  --query 'Stacks[0].Outputs[?OutputKey==`ProductsTable`].OutputValue' \
  --output text)

aws dynamodb scan \
  --table-name $PRODUCTS_TABLE \
  --select COUNT

# Expected: Count should be 50
```

---

## Step 11: Test Backend API

```bash
# Get API Gateway URL
# API_URL=$(aws cloudformation describe-stacks \
#   --stack-name shelfiq-prototype \
#   --query 'Stacks[0].Outputs[?OutputKey==`ApiUrl`].OutputValue' \
#   --output text)

# echo "API URL: $API_URL"
API_URL=$(aws cloudformation describe-stacks \
  --stack-name shelfiq-prototype \
  --query 'Stacks[0].Outputs[?OutputKey==`ApiEndpoint`].OutputValue' \
  --output text)

echo "API URL: $API_URL"


# Test health endpoint
curl $API_URL/health

# Test products endpoint
curl $API_URL/products | jq '.'

# Test pricing analysis (replace PROD-001 with actual product ID)
curl -X POST $API_URL/analyze/pricing/PROD-001 | jq '.'
```

---

## Step 12: Set Up Frontend

```bash
cd ../frontend

# Install Node.js dependencies
npm install

# Get API Gateway URL
API_URL=$(aws cloudformation describe-stacks \
  --stack-name shelfiq-prototype \
  --query 'Stacks[0].Outputs[?OutputKey==`ApiEndpoint`].OutputValue' \
  --output text)

# Create .env file
cat > .env << EOF
VITE_API_ENDPOINT=$API_URL
EOF

# Verify .env file
cat .env
```

---

## Step 13: Start Frontend Development Server

```bash
# Start Vite dev server
npm run dev
```

Expected output:
```
VITE v5.x.x  ready in xxx ms

➜  Local:   http://localhost:5173/
➜  Network: use --host to expose
```

Open browser to: **http://localhost:5173**

---

## Step 14: Test Frontend Features

### Dashboard View
- [ ] Products list loads successfully
- [ ] Can filter by category
- [ ] Can search products
- [ ] Click on product navigates to detail view

### Product Detail View
- [ ] Product information displays correctly
- [ ] Click "Get Pricing Analysis" triggers AI analysis
- [ ] Pricing recommendation appears with reasoning
- [ ] Competitor chart displays price distribution

### Chat Interface
- [ ] Can send messages
- [ ] AI responds with relevant insights
- [ ] Suggested questions work
- [ ] Conversation history maintained

---

## Step 15: Deploy Frontend to S3 (Optional)

```bash
# Build production frontend
npm run build

# Get frontend bucket name
FRONTEND_BUCKET=$(aws cloudformation describe-stacks \
  --stack-name shelfiq-prototype \
  --query 'Stacks[0].Outputs[?OutputKey==`FrontendBucket`].OutputValue' \
  --output text)

# Sync build to S3
aws s3 sync dist/ s3://$FRONTEND_BUCKET/ --delete

# Get frontend URL
echo "Frontend URL: http://$FRONTEND_BUCKET.s3-website-us-east-1.amazonaws.com"
```

---

## Troubleshooting

### Issue: AWS Credentials Not Found
```bash
# Check credentials file exists
cat ~/.aws/credentials

# Check AWS CLI can access credentials
aws configure list
```

### Issue: Bedrock Access Denied
```bash
# Verify model access status
aws bedrock list-foundation-models --by-provider anthropic

# If no models returned, request access via console
```

### Issue: Lambda Function Timeout
Edit `template.yaml` and increase timeout:
```yaml
Timeout: 60  # Increase from 30 to 60 seconds
```

Then redeploy:
```bash
sam build && sam deploy
```

### Issue: DynamoDB Table Not Found
```bash
# List all tables
aws dynamodb list-tables

# Check CloudFormation stack status
aws cloudformation describe-stacks --stack-name shelfiq-prototype
```

### Issue: CORS Errors in Frontend
Check API Gateway CORS configuration in `template.yaml`:
```yaml
Cors:
  AllowOrigin: "'*'"
  AllowHeaders: "'Content-Type,X-Amz-Date,Authorization,X-Api-Key'"
  AllowMethods: "'GET,POST,OPTIONS'"
```

### Issue: Frontend Can't Connect to API
```bash
# Verify API URL in .env
cat prototype/frontend/.env

# Test API directly
curl $API_URL/health
```

---

## Cost Monitoring

### Check Current Costs
```bash
# Get cost for last 7 days
aws ce get-cost-and-usage \
  --time-period Start=2026-03-01,End=2026-03-08 \
  --granularity DAILY \
  --metrics BlendedCost \
  --group-by Type=SERVICE
```

### Set Up Billing Alert
1. Go to AWS Billing Console
2. Navigate to **Budgets**
3. Create budget: $50/month
4. Set alert at 80% threshold

---

## Cleanup (When Done)

### Delete CloudFormation Stack
```bash
# Delete all resources
aws cloudformation delete-stack --stack-name shelfiq-prototype

# Wait for deletion to complete
aws cloudformation wait stack-delete-complete --stack-name shelfiq-prototype
```

### Empty S3 Buckets First (if deletion fails)
```bash
# Empty data bucket
aws s3 rm s3://$DATA_BUCKET --recursive

# Empty frontend bucket
aws s3 rm s3://$FRONTEND_BUCKET --recursive

# Then retry stack deletion
aws cloudformation delete-stack --stack-name shelfiq-prototype
```

---

## Quick Reference Commands

```bash
# Activate environment
conda activate shelfiq

# Deploy backend
cd prototype/backend && sam build && sam deploy

# Start frontend
cd prototype/frontend && npm run dev

# View logs
aws logs tail /aws/lambda/shelfiq-prototype-Intelligence --follow

# Test API
curl $API_URL/health
```

---

## Support

For issues or questions:
1. Check CloudWatch Logs for Lambda errors
2. Review CloudFormation Events for deployment issues
3. Verify AWS credentials and permissions
4. Check Bedrock model access status

---

**Last Updated**: March 8, 2026
**Team**: OG404
**Hackathon**: AWS AI for Bharat
