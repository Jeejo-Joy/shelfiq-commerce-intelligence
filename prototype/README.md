# ShelfIQ Prototype MVP

A hackathon-ready prototype demonstrating AI-powered commerce intelligence using AWS services.

## 🏗️ Architecture Overview

ShelfIQ is built as a serverless AWS-native application:

- **Amazon Bedrock**: GenAI models (Claude 3 Sonnet) for pricing analysis and insights
- **AWS Lambda**: Serverless compute for data processing and intelligence generation
- **Amazon DynamoDB**: NoSQL database for products and recommendations
- **Amazon S3**: Object storage for sample data and frontend hosting
- **Amazon API Gateway**: REST API layer
- **React Frontend**: Web interface for dashboard and chat copilot

## 📁 Project Structure

```
prototype/
├── backend/                    # Python Lambda functions
│   ├── functions/
│   │   ├── ingestion/         # Data ingestion Lambda
│   │   ├── intelligence/      # AI analysis Lambda
│   │   └── api/               # API handler Lambda
│   ├── requirements.txt       # Lambda dependencies
│   ├── requirements-dev.txt   # Development dependencies
│   └── template.yaml          # AWS SAM template
├── frontend/                   # React web application
│   ├── src/
│   │   ├── components/        # React components
│   │   ├── services/          # API client
│   │   └── App.tsx            # Main app component
│   ├── package.json
│   └── vite.config.ts
├── scripts/                    # Utility scripts
│   └── generate_sample_data.py
├── sample-data/                # Sample CSV files
│   └── products.csv
└── docs/                       # Documentation
    └── impl/                   # Implementation notes
```

## 🚀 Quick Start

### Prerequisites

- **AWS Account** with Bedrock access enabled
- **Python 3.11+**
- **Node.js 18+**
- **AWS CLI** configured
- **AWS SAM CLI** installed

### 1. Set Up Python Environment

```bash
cd prototype/backend

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### 2. Generate Sample Data

```bash
cd prototype/scripts
python generate_sample_data.py
```

This creates `sample-data/products.csv` with 50 sample products.

### 3. Deploy Backend Infrastructure

```bash
cd prototype/backend

# Build Lambda functions
sam build

# Deploy (first time - guided)
sam deploy --guided

# Follow prompts:
# - Stack name: shelfiq-prototype
# - AWS Region: us-east-1 (or your preferred region)
# - Confirm changes: Y
# - Allow SAM CLI IAM role creation: Y
# - Save arguments to config: Y

# Subsequent deploys
sam deploy
```

### 4. Upload Sample Data

```bash
# Get S3 bucket name from SAM outputs
aws cloudformation describe-stacks \
  --stack-name shelfiq-prototype \
  --query 'Stacks[0].Outputs[?OutputKey==`DataBucket`].OutputValue' \
  --output text

# Upload sample data
aws s3 cp ../sample-data/products.csv s3://YOUR-BUCKET-NAME/sample-data/
```

### 5. Set Up Frontend

```bash
cd prototype/frontend

# Install dependencies
npm install

# Create .env file with API endpoint
echo "VITE_API_ENDPOINT=YOUR-API-GATEWAY-URL" > .env

# Start development server
npm run dev
```

Visit `http://localhost:5173` to see the dashboard.

## 🧪 Testing the API

### Get All Products

```bash
curl https://YOUR-API-GATEWAY-URL/products
```

### Get Pricing Analysis

```bash
curl -X POST https://YOUR-API-GATEWAY-URL/analyze/pricing/PROD-001
```

### Chat with Copilot

```bash
curl -X POST https://YOUR-API-GATEWAY-URL/chat \
  -H "Content-Type: application/json" \
  -d '{
    "message": "What should I price product PROD-001?",
    "conversation_id": "test-123"
  }'
```

## 📊 Sample Data

The prototype includes 50 sample products across 5 categories:
- Electronics
- Home & Kitchen
- Sports
- Books
- Toys

Each product has:
- Current price and cost
- 3-7 competitor prices
- Sales rank (100-10,000)
- Rating (3.5-5.0 stars)
- Review count (10-1,000)

## 🎯 Demo Scenarios

### Scenario 1: Pricing Recommendation
1. Navigate to product PROD-001 in dashboard
2. Click "Get Pricing Analysis"
3. View AI-generated recommendation with reasoning
4. See competitive positioning and expected impact

### Scenario 2: Chat Copilot
1. Open chat interface
2. Ask: "Which products are overpriced?"
3. Get AI analysis with actionable recommendations
4. Follow up: "Show me details for product X"

### Scenario 3: Competitor Analysis
1. Select a product from catalog
2. View competitor price distribution chart
3. See market position (percentile ranking)
4. Review pricing opportunities

## 💰 Cost Estimation

**Hackathon Budget (24-48 hours)**:
- Lambda: ~$0.50 (free tier)
- DynamoDB: ~$1.00 (free tier)
- S3: ~$0.10 (free tier)
- API Gateway: ~$0.50 (free tier)
- **Bedrock: ~$15.00** (main cost - Claude 3 Sonnet)
- CloudWatch: ~$0.50
- **Total: ~$18/day**

Cost optimization:
- Responses cached for 1 hour (reduces Bedrock calls by ~80%)
- DynamoDB on-demand pricing
- Minimal Lambda memory allocation

## 🔧 Development

### Running Tests

```bash
cd prototype/backend
pytest tests/ -v
```

### Code Formatting

```bash
black backend/functions/
flake8 backend/functions/
```

### Local Lambda Testing

```bash
sam local invoke IntelligenceFunction -e events/pricing-request.json
```

## 📚 Documentation

- **Requirements**: See `.kiro/specs/shelfiq-prototype-mvp/requirements.md`
- **Design**: See `.kiro/specs/shelfiq-prototype-mvp/design.md`
- **API Documentation**: See `docs/api.md` (to be created)
- **Architecture Diagram**: See `docs/architecture.png` (to be created)

## 🐛 Troubleshooting

### Bedrock Access Denied
Enable model access in AWS Console:
1. Go to Amazon Bedrock console
2. Navigate to "Model access"
3. Request access to Claude 3 Sonnet
4. Wait for approval (~2 minutes)

### Lambda Timeout
Increase timeout in `template.yaml`:
```yaml
Timeout: 30  # seconds
```

### DynamoDB Throttling
Switch to on-demand mode or increase provisioned capacity.

### CORS Errors
Ensure API Gateway has CORS enabled for your frontend domain.

## 🚀 Next Steps

After the hackathon, consider:
1. Implement frontend dashboard
2. Add authentication (Amazon Cognito)
3. Real-time data ingestion from marketplace APIs
4. Enhanced caching strategy
5. CI/CD pipeline
6. Automated testing suite
7. Multi-tenancy support

## 📝 License

This is a hackathon prototype for demonstration purposes.

## 👥 Team OG404

Built for AWS AI for Bharat Hackathon.
