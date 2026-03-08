#!/bin/bash
# ShelfIQ Prototype Setup Script

set -e

echo "🚀 ShelfIQ Prototype Setup"
echo "=========================="
echo ""

# Check prerequisites
echo "📋 Checking prerequisites..."

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed"
    exit 1
fi
echo "✅ Python 3: $(python3 --version)"

# Check Node.js
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed"
    exit 1
fi
echo "✅ Node.js: $(node --version)"

# Check AWS CLI
if ! command -v aws &> /dev/null; then
    echo "❌ AWS CLI is not installed"
    exit 1
fi
echo "✅ AWS CLI: $(aws --version)"

# Check SAM CLI
if ! command -v sam &> /dev/null; then
    echo "⚠️  AWS SAM CLI is not installed (optional for local testing)"
else
    echo "✅ SAM CLI: $(sam --version)"
fi

echo ""
echo "📦 Setting up Python environment..."

# Create virtual environment
cd backend
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✅ Created Python virtual environment"
else
    echo "✅ Virtual environment already exists"
fi

# Activate virtual environment
source venv/bin/activate

# Install dependencies
echo "📥 Installing Python dependencies..."
pip install -q --upgrade pip
pip install -q -r requirements.txt
pip install -q -r requirements-dev.txt
echo "✅ Python dependencies installed"

cd ..

echo ""
echo "📦 Setting up Frontend..."

cd frontend
if [ ! -d "node_modules" ]; then
    echo "📥 Installing Node.js dependencies..."
    npm install
    echo "✅ Node.js dependencies installed"
else
    echo "✅ Node.js dependencies already installed"
fi

# Create .env file if it doesn't exist
if [ ! -f ".env" ]; then
    cp .env.example .env
    echo "✅ Created .env file (update with your API endpoint)"
else
    echo "✅ .env file already exists"
fi

cd ..

echo ""
echo "📊 Generating sample data..."
cd scripts
python3 generate_sample_data.py
cd ..

echo ""
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Configure AWS credentials: aws configure"
echo "2. Enable Bedrock model access in AWS Console"
echo "3. Deploy backend: cd backend && sam build && sam deploy --guided"
echo "4. Update frontend/.env with API endpoint"
echo "5. Start frontend: cd frontend && npm run dev"
echo ""
