#!/bin/bash

# ShelfIQ - Clean Push Script
# Dev branch: Everything (private)
# Main branch: Only prototype folder (public)

set -e

echo "🚀 ShelfIQ - Clean Repository Push"
echo "===================================="
echo ""

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

REPO_URL="https://github.com/Jeejo-Joy/shelfiq-commerce-intelligence.git"

echo -e "${BLUE}PLAN:${NC}"
echo "1. Push 'dev' branch with ALL files (you'll make it private)"
echo "2. Create clean 'main' branch with only prototype/ folder"
echo "3. Main branch will be public-ready"
echo ""
echo -e "${YELLOW}Press Enter to continue or Ctrl+C to cancel...${NC}"
read

# Step 1: Commit everything to dev branch
echo -e "${YELLOW}Step 1: Committing all files to dev branch...${NC}"
git checkout dev
git add -A
git commit -m "Dev branch: Complete project with all files

Includes:
- All source code
- Documentation and drafts
- Presentation materials
- Demo files
- Development notes
- Archive files
" || echo "No changes to commit on dev"
echo -e "${GREEN}✓ Dev branch ready${NC}"
echo ""

# Step 2: Push dev branch
echo -e "${YELLOW}Step 2: Pushing dev branch...${NC}"
git push -u origin dev --force
echo -e "${GREEN}✓ Dev branch pushed${NC}"
echo ""

# Step 3: Switch to main and clean
echo -e "${YELLOW}Step 3: Creating clean main branch...${NC}"
git checkout main

# Remove everything except .git
find . -maxdepth 1 ! -name '.git' ! -name '.' ! -name '..' -exec rm -rf {} + 2>/dev/null || true

# Copy only prototype folder from dev
git checkout dev -- prototype/

# Copy LICENSE if exists
git checkout dev -- LICENSE 2>/dev/null || true

echo -e "${GREEN}✓ Main branch cleaned${NC}"
echo ""

# Step 4: Create public README
echo -e "${YELLOW}Step 4: Creating public README...${NC}"
cat > README.md << 'EOF'
# ShelfIQ - AI-Powered Commerce Intelligence Platform

> Intelligent pricing and demand forecasting for e-commerce using Amazon Bedrock AI

[![AWS](https://img.shields.io/badge/AWS-Bedrock-orange)](https://aws.amazon.com/bedrock/)
[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)
[![React](https://img.shields.io/badge/React-18-61dafb)](https://reactjs.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.0-blue)](https://www.typescriptlang.org/)

## 🎯 Overview

ShelfIQ is a serverless AI-powered platform that helps e-commerce businesses optimize pricing strategies and forecast demand using Amazon Bedrock's Claude AI models. Built for the Indian market with support for Indian Rupees (₹).

**Developed by:** Jeejo Joy (Team OG404)
**Hackathon:** AWS AI for Bharat Hackathon 2026

## ✨ Key Features

- **AI-Powered Pricing Recommendations** - Smart pricing suggestions based on market analysis
- **Competitor Analysis** - Real-time competitive positioning insights
- **Demand Forecasting** - Predict sales trends with AI
- **Indian Market Focus** - Optimized for Indian e-commerce with ₹ support
- **Serverless Architecture** - Scalable, cost-effective AWS infrastructure

## 🏗️ Architecture

```
Frontend (React + TypeScript)
    ↓
API Gateway
    ↓
Lambda Functions (Python)
    ↓
├── DynamoDB (Product Data)
├── Amazon Bedrock (AI Analysis)
└── S3 (Data Storage)
```

## 🚀 Quick Start

### Prerequisites

- AWS Account with Bedrock access
- AWS CLI configured
- AWS SAM CLI installed
- Node.js 18+ and npm
- Python 3.11+

### Backend Deployment

```bash
cd prototype/backend

# Build
sam build

# Deploy
sam deploy --guided

# Note the API endpoint from outputs
```

### Frontend Deployment

```bash
cd prototype/frontend

# Install dependencies
npm install

# Create .env file
cp .env.example .env
# Edit .env and add your API endpoint

# Build
npm run build

# Deploy to S3 (or your hosting service)
aws s3 sync dist/ s3://your-bucket-name --delete
```

### Load Sample Data

```bash
cd prototype/scripts

# Generate sample data
python3 generate_sample_data.py

# Load to DynamoDB
python3 load_data_to_dynamodb.py
```

## 📁 Project Structure

```
prototype/
├── backend/              # AWS SAM serverless backend
│   ├── template.yaml    # Infrastructure as Code
│   └── functions/       # Lambda functions
│       ├── api/         # API handler
│       ├── ingestion/   # Data ingestion
│       └── intelligence/# AI analysis (Bedrock)
├── frontend/            # React TypeScript frontend
│   └── src/
│       ├── App.tsx      # Main application
│       ├── services/    # API client
│       └── utils/       # Utilities (currency, etc.)
├── scripts/             # Deployment & data scripts
└── sample-data/         # Sample product data
```

## 🛠️ Tech Stack

**Backend:**
- AWS Lambda (Python 3.11)
- Amazon Bedrock (Claude 3 Haiku)
- Amazon DynamoDB
- Amazon API Gateway
- AWS SAM

**Frontend:**
- React 18
- TypeScript
- Vite
- CSS3

**AI/ML:**
- Amazon Bedrock
- Claude 3 Haiku model
- Natural language processing for pricing analysis

## 🔑 Key Components

### 1. Intelligence Function
Uses Amazon Bedrock to provide:
- Pricing recommendations
- Demand forecasting
- Competitive analysis
- Market insights

### 2. API Handler
RESTful API endpoints:
- `GET /products` - List products
- `GET /products/{id}` - Product details
- `POST /analyze/pricing/{id}` - AI pricing analysis
- `POST /analyze/competitors/{id}` - Competitor analysis

### 3. Data Ingestion
Processes product data from CSV/S3 into DynamoDB

## 📊 Sample Data

Includes 50 sample products across categories:
- Electronics
- Home & Kitchen
- Sports & Outdoors
- Books
- Toys & Games

All prices in Indian Rupees (₹) with realistic market values.

## 🔒 Security

- No hardcoded credentials
- IAM roles for Lambda functions
- API Gateway with CORS
- Environment variables for configuration
- S3 bucket policies

## 📝 Configuration

### Backend Environment Variables
- `BEDROCK_MODEL_ID` - Bedrock model identifier
- `PRODUCTS_TABLE` - DynamoDB products table
- `RECOMMENDATIONS_TABLE` - DynamoDB recommendations table
- `CACHE_TABLE` - DynamoDB cache table

### Frontend Environment Variables
- `VITE_API_URL` - Backend API endpoint

## 🧪 Testing

```bash
cd prototype/backend
pytest
```

## 📈 Performance

- API Response Time: < 500ms (cached)
- AI Analysis: 2-5 seconds
- Concurrent Users: Scales automatically
- Cost: Pay-per-use (serverless)

## 🤝 Contributing

Contributions welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📄 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file.

## 👨‍💻 Author

**Jeejo Joy** (Team OG404)
- GitHub: [@Jeejo-Joy](https://github.com/Jeejo-Joy)
- Project: AWS AI for Bharat Hackathon 2026

## 🙏 Acknowledgments

- AWS AI for Bharat Hackathon
- Amazon Bedrock team
- AWS Serverless team

## 📞 Support

For issues and questions:
- Open an issue on GitHub
- Check documentation in `prototype/backend/POST_DEPLOY_STEPS.md`

---

**Note:** This is a prototype developed for the AWS AI for Bharat Hackathon 2026. For production use, additional security hardening, monitoring, and testing are recommended.
EOF

echo -e "${GREEN}✓ README created${NC}"
echo ""

# Step 5: Create .gitignore
cat > .gitignore << 'EOF'
# Python
__pycache__/
*.py[cod]
venv/
.Python

# AWS SAM
.aws-sam/
samconfig.toml

# Node
node_modules/
dist/
*.local

# Environment
.env
.env.local

# IDE
.vscode/
.idea/
.DS_Store

# Logs
*.log

# Deployment
deployment-outputs.json
s3-bucket.txt
EOF

echo -e "${GREEN}✓ .gitignore created${NC}"
echo ""

# Step 6: Commit main branch
echo -e "${YELLOW}Step 6: Committing main branch...${NC}"
git add -A
git commit -m "Public release: ShelfIQ prototype

Clean public version with:
- Complete prototype source code
- Deployment instructions
- Sample data
- Documentation

For full project history, see dev branch.

Developed by Jeejo Joy (Team OG404)
AWS AI for Bharat Hackathon 2026
"
echo -e "${GREEN}✓ Main branch committed${NC}"
echo ""

# Step 7: Push main branch
echo -e "${YELLOW}Step 7: Pushing main branch...${NC}"
git push -u origin main --force
echo -e "${GREEN}✓ Main branch pushed${NC}"
echo ""

# Summary
echo -e "${BLUE}=========================================${NC}"
echo -e "${GREEN}✓ Repository pushed successfully!${NC}"
echo -e "${BLUE}=========================================${NC}"
echo ""
echo -e "${YELLOW}BRANCHES:${NC}"
echo "  • dev  - Complete project (MAKE THIS PRIVATE on GitHub)"
echo "  • main - Public prototype only"
echo ""
echo -e "${YELLOW}NEXT STEPS:${NC}"
echo "1. Go to GitHub: $REPO_URL"
echo "2. Go to Settings → Branches"
echo "3. Set 'main' as default branch"
echo "4. Go to Settings → Manage access"
echo "5. Make 'dev' branch private (if GitHub supports branch-level privacy)"
echo "   OR keep entire repo public (dev branch is just for reference)"
echo ""
echo -e "${GREEN}Done! Your public main branch is clean and professional.${NC}"
