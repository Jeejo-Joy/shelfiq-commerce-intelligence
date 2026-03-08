# ShelfIQ - AI-Powered Commerce Intelligence

[![AWS](https://img.shields.io/badge/AWS-Bedrock-orange)](https://aws.amazon.com/bedrock/)
[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)
[![React](https://img.shields.io/badge/React-18-61dafb)](https://reactjs.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

> **Jeejo Joy** | AWS AI for Bharat Hackathon 2026

ShelfIQ is an AI-powered pricing intelligence platform designed for Indian e-commerce sellers. It leverages Amazon Bedrock to provide real-time competitor analysis and intelligent pricing recommendations.

## 🎯 Problem Statement

Indian e-commerce sellers struggle with:
- Manual competitor price tracking
- Suboptimal pricing decisions
- Lack of AI-powered insights
- Time-consuming market analysis

## 💡 Solution

ShelfIQ provides:
- **AI-Powered Pricing Recommendations** using Amazon Bedrock (Claude)
- **Real-time Competitor Analysis** with market positioning
- **Indian Market Focus** with INR pricing and local context
- **Actionable Insights** for immediate business decisions

## 🏗️ Architecture

```
┌─────────────┐
│   React     │
│  Frontend   │ ← S3 + CloudFront
└──────┬──────┘
       │
       ↓
┌─────────────┐
│ API Gateway │
└──────┬──────┘
       │
       ↓
┌─────────────────────────────────┐
│      Lambda Functions           │
│  ┌──────────┬──────────────┐   │
│  │   API    │ Intelligence │   │
│  │ Handler  │   (Bedrock)  │   │
│  └──────────┴──────────────┘   │
└─────────────────────────────────┘
       │              │
       ↓              ↓
┌─────────────┐  ┌──────────────┐
│  DynamoDB   │  │   Bedrock    │
│   Tables    │  │   (Claude)   │
└─────────────┘  └──────────────┘
```

## 🚀 Features

### 1. Product Dashboard
- Browse 50+ products across categories
- Real-time pricing in Indian Rupees (₹)
- Sales rank and customer ratings

### 2. AI Pricing Recommendations
- Powered by Amazon Bedrock (Claude 3 Sonnet)
- Confidence scores and detailed reasoning
- Market position analysis

### 3. Competitor Intelligence
- Min/Median/Max competitor pricing
- Price rank and percentile
- Actionable recommendations

### 4. Serverless Architecture
- Fully serverless on AWS
- Auto-scaling and cost-effective
- Infrastructure as Code (AWS SAM)

## 🛠️ Tech Stack

### Backend
- **Amazon Bedrock** - AI/ML inference (Claude 3 Sonnet)
- **AWS Lambda** - Serverless compute
- **Amazon DynamoDB** - NoSQL database
- **API Gateway** - REST API
- **AWS SAM** - Infrastructure as Code

### Frontend
- **React 18** - UI framework
- **TypeScript** - Type safety
- **Vite** - Build tool
- **Axios** - HTTP client

### DevOps
- **AWS SAM CLI** - Deployment
- **GitHub Actions** - CI/CD (optional)
- **CloudWatch** - Monitoring and logs

## 📦 Project Structure

```
shelfiq-commerce-intelligence/
├── prototype/
│   ├── backend/
│   │   ├── functions/
│   │   │   ├── api/              # API handler Lambda
│   │   │   ├── intelligence/     # Bedrock AI Lambda
│   │   │   └── ingestion/        # Data ingestion Lambda
│   │   ├── template.yaml         # SAM template
│   │   └── samconfig.toml        # SAM configuration
│   ├── frontend/
│   │   ├── src/
│   │   │   ├── App.tsx           # Main application
│   │   │   ├── services/         # API client
│   │   │   ├── types/            # TypeScript types
│   │   │   └── utils/            # Utilities
│   │   └── package.json
│   ├── sample-data/
│   │   └── products.csv          # Sample product data
│   └── scripts/
│       ├── deploy-frontend.sh    # Frontend deployment
│       ├── generate_sample_data.py
│       └── load_data_to_dynamodb.py
├── docs/                         # Documentation
├── DEMO_SCRIPT.md               # Demo presentation guide
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- AWS Account with Bedrock access
- AWS CLI configured
- AWS SAM CLI installed
- Node.js 18+ and npm
- Python 3.11+

### 1. Clone Repository

```bash
git clone https://github.com/Jeejo-Joy/shelfiq-commerce-intelligence.git
cd shelfiq-commerce-intelligence
```

### 2. Deploy Backend

```bash
cd prototype/backend

# Build and deploy
sam build
sam deploy --guided

# Note the API endpoint from outputs
```

### 3. Load Sample Data

```bash
cd prototype/scripts

# Generate sample data
python3 generate_sample_data.py

# Load to DynamoDB
python3 load_data_to_dynamodb.py
```

### 4. Deploy Frontend

```bash
cd prototype/frontend

# Install dependencies
npm install

# Update .env with API endpoint
echo "VITE_API_ENDPOINT=<your-api-endpoint>" > .env

# Build and deploy
npm run build

# Deploy to S3 (automated)
cd ../scripts
./deploy-frontend.sh
```

### 5. Access Application

Open the Frontend URL from CloudFormation outputs:
```
http://shelfiq-frontend-<account-id>.s3-website-us-east-1.amazonaws.com
```

## 🔑 Environment Variables

### Backend (Lambda)
- `BEDROCK_MODEL_ID` - Claude model ID
- `BEDROCK_REGION` - AWS region for Bedrock
- `PRODUCTS_TABLE` - DynamoDB products table
- `RECOMMENDATIONS_TABLE` - DynamoDB recommendations table
- `CACHE_TABLE` - DynamoDB cache table

### Frontend
- `VITE_API_ENDPOINT` - API Gateway endpoint URL

## 📊 Sample Data

The platform includes 50 sample products with:
- Realistic Indian market prices (₹149 - ₹3,113)
- Multiple categories (Electronics, Sports, Books, Toys, Home & Kitchen)
- Competitor pricing data (3-7 competitors per product)
- Sales metrics and customer ratings

## 🎥 Demo

Watch our 2-minute demo: [YouTube Link]

Or follow the [DEMO_SCRIPT.md](DEMO_SCRIPT.md) to create your own demo.

## 🧪 Testing

### Test API Endpoints

```bash
# Health check
curl https://<api-endpoint>/prod/health

# Get products
curl https://<api-endpoint>/prod/products

# Get pricing analysis
curl -X POST https://<api-endpoint>/prod/analyze/pricing/PROD-001
```

### Test Bedrock Integration

```bash
# Check Lambda logs
aws logs tail /aws/lambda/shelfiq-intelligence --follow
```

## 📈 AWS Services Used

| Service | Purpose | Cost Estimate |
|---------|---------|---------------|
| Amazon Bedrock | AI inference | ~$0.003/1K tokens |
| AWS Lambda | Compute | Free tier eligible |
| DynamoDB | Database | Free tier eligible |
| API Gateway | REST API | Free tier eligible |
| S3 | Frontend hosting | ~$0.023/GB |
| CloudWatch | Monitoring | Free tier eligible |

**Estimated Monthly Cost:** < $5 for prototype usage

## 🔒 Security

- API Gateway with CORS enabled
- DynamoDB encryption at rest
- Lambda IAM roles with least privilege
- No hardcoded credentials
- Environment variables for configuration

## 🚧 Future Enhancements

- [ ] User authentication (Cognito)
- [ ] Historical price tracking
- [ ] Email alerts for price changes
- [ ] Multi-marketplace support (Amazon, Flipkart)
- [ ] Mobile app (React Native)
- [ ] Advanced analytics dashboard
- [ ] Bulk product import
- [ ] API rate limiting

## 👨‍💻 Developer

**Jeejo Joy** - Full Stack Development & AWS Architecture

Solo developer submission for AWS AI for Bharat Hackathon 2026

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- AWS AI for Bharat Hackathon
- Amazon Bedrock team
- AWS Serverless team
- Open source community

## 📞 Contact

- GitHub: [@Jeejo-Joy](https://github.com/Jeejo-Joy)
- Project Link: [https://github.com/Jeejo-Joy/shelfiq-commerce-intelligence](https://github.com/Jeejo-Joy/shelfiq-commerce-intelligence)

---

**Built with ❤️ for Indian E-commerce Sellers**

*Empowering sellers with AI-driven pricing intelligence*
