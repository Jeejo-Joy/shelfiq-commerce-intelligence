#!/bin/bash

# ShelfIQ - Push to GitHub Script
# This script prepares and pushes the repository to GitHub

set -e

echo "🚀 ShelfIQ - GitHub Push Script"
echo "================================"
echo ""

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Repository URL
REPO_URL="https://github.com/Jeejo-Joy/shelfiq-commerce-intelligence.git"

echo -e "${YELLOW}Step 1: Cleaning up sensitive files...${NC}"
# Remove sensitive files
rm -f prototype/backend/deployment-outputs.json
rm -f prototype/backend/s3-bucket.txt
rm -f aws-requirements.txt
rm -f prototype/frontend/.env
echo -e "${GREEN}✓ Cleaned up sensitive files${NC}"
echo ""

echo -e "${YELLOW}Step 2: Checking Git status...${NC}"
# Check if git is initialized
if [ ! -d ".git" ]; then
    echo -e "${YELLOW}Initializing Git repository...${NC}"
    git init
    echo -e "${GREEN}✓ Git initialized${NC}"
else
    echo -e "${GREEN}✓ Git already initialized${NC}"
fi
echo ""

echo -e "${YELLOW}Step 3: Adding remote repository...${NC}"
# Check if remote exists
if git remote | grep -q "origin"; then
    echo -e "${YELLOW}Remote 'origin' already exists. Updating URL...${NC}"
    git remote set-url origin $REPO_URL
else
    git remote add origin $REPO_URL
fi
echo -e "${GREEN}✓ Remote repository configured${NC}"
echo ""

echo -e "${YELLOW}Step 4: Staging files...${NC}"
# Add all files
git add .
echo -e "${GREEN}✓ Files staged${NC}"
echo ""

echo -e "${YELLOW}Step 5: Creating commit...${NC}"
# Commit
COMMIT_MSG="Initial commit: ShelfIQ - AI-Powered Commerce Intelligence

- Complete serverless backend with AWS SAM
- React frontend with TypeScript
- Amazon Bedrock integration for AI pricing
- DynamoDB for data storage
- Sample data and deployment scripts
- Comprehensive documentation

Team OG404 | AWS AI for Bharat Hackathon 2026"

git commit -m "$COMMIT_MSG"
echo -e "${GREEN}✓ Commit created${NC}"
echo ""

echo -e "${YELLOW}Step 6: Checking branch...${NC}"
# Ensure we're on main branch
CURRENT_BRANCH=$(git branch --show-current)
if [ "$CURRENT_BRANCH" != "main" ]; then
    echo -e "${YELLOW}Renaming branch to 'main'...${NC}"
    git branch -M main
fi
echo -e "${GREEN}✓ On main branch${NC}"
echo ""

echo -e "${YELLOW}Step 7: Pushing to GitHub...${NC}"
echo -e "${YELLOW}You may be prompted for GitHub credentials${NC}"
echo ""

# Push to GitHub
git push -u origin main

echo ""
echo -e "${GREEN}================================${NC}"
echo -e "${GREEN}✓ Successfully pushed to GitHub!${NC}"
echo -e "${GREEN}================================${NC}"
echo ""
echo -e "Repository URL: ${YELLOW}$REPO_URL${NC}"
echo ""
echo -e "${YELLOW}Next steps:${NC}"
echo "1. Visit your repository on GitHub"
echo "2. Add a repository description"
echo "3. Add topics/tags: aws, bedrock, ai, ecommerce, serverless"
echo "4. Update README with demo video link"
echo "5. Create a release for the hackathon submission"
echo ""
echo -e "${GREEN}Good luck with the hackathon! 🎉${NC}"
