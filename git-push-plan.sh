#!/bin/bash

# ShelfIQ - Git Push Plan
# Main branch: Essential files for demo/evaluation
# Dev branch: All development files and drafts

set -e

echo "🚀 ShelfIQ - Git Repository Organization"
echo "========================================="
echo ""

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

REPO_URL="https://github.com/Jeejo-Joy/shelfiq-commerce-intelligence.git"

echo -e "${BLUE}PLAN:${NC}"
echo "1. Create 'dev' branch with ALL files"
echo "2. Clean main branch to keep only essential files"
echo "3. Push both branches to GitHub"
echo ""
echo -e "${YELLOW}Press Enter to continue or Ctrl+C to cancel...${NC}"
read

# Step 1: Unstage the demo video file
echo -e "${YELLOW}Step 1: Removing demo video from staging...${NC}"
git restore --staged "demo/Screen Recording 2026-03-08 at 9.12.47 PM.mov" 2>/dev/null || true
echo -e "${GREEN}✓ Demo video unstaged${NC}"
echo ""

# Step 2: Create dev branch with ALL current files
echo -e "${YELLOW}Step 2: Creating 'dev' branch with all files...${NC}"
git checkout -b dev 2>/dev/null || git checkout dev
git add .
git commit -m "Dev branch: All development files, drafts, and documentation

Includes:
- All source code
- Draft documentation
- Design files
- Presentation materials
- Demo videos
- Archive files
- Development notes
" || echo "No changes to commit on dev branch"
echo -e "${GREEN}✓ Dev branch created with all files${NC}"
echo ""

# Step 3: Switch back to main and clean up
echo -e "${YELLOW}Step 3: Switching to main branch...${NC}"
git checkout main
echo -e "${GREEN}✓ On main branch${NC}"
echo ""

# Step 4: Reset staging area
echo -e "${YELLOW}Step 4: Resetting staging area...${NC}"
git reset
echo -e "${GREEN}✓ Staging area reset${NC}"
echo ""

# Step 5: Add only essential files for main branch
echo -e "${YELLOW}Step 5: Adding essential files for demo/evaluation...${NC}"

# Core documentation
git add README.md
git add LICENSE
git add SETUP_GUIDE.md
git add CONTRIBUTING.md
git add .gitignore

# Presentation (final PDF only)
git add "ShelfIQ_OG404_AWS AI for Bharat Hackathon_v4.pdf"

# Backend code
git add prototype/backend/template.yaml
git add prototype/backend/requirements.txt
git add prototype/backend/requirements-dev.txt
git add prototype/backend/pytest.ini
git add prototype/backend/POST_DEPLOY_STEPS.md
git add prototype/backend/configure-s3-trigger.sh
git add prototype/backend/functions/

# Frontend code
git add prototype/frontend/package.json
git add prototype/frontend/package-lock.json
git add prototype/frontend/tsconfig.json
git add prototype/frontend/tsconfig.node.json
git add prototype/frontend/vite.config.ts
git add prototype/frontend/index.html
git add prototype/frontend/.env.example
git add prototype/frontend/src/

# Scripts
git add prototype/scripts/

# Sample data
git add prototype/sample-data/products.csv

# Tests
git add prototype/backend/tests/

# Essential docs
git add prototype/README.md

# Essential architecture images
git add pics/ShelfIQ_System_Architecture_1920x1080.png
git add pics/ShelfIQ_Dashboard_Wireframe_1600x800.png
git add pics/ShelfIQ_Product_Detail_Wireframe_1600x800.png

echo -e "${GREEN}✓ Essential files added${NC}"
echo ""

# Step 6: Commit main branch
echo -e "${YELLOW}Step 6: Committing main branch...${NC}"
git commit -m "Initial commit: ShelfIQ - AI-Powered Commerce Intelligence

Essential files for demo and evaluation:
- Complete serverless backend (AWS SAM + Lambda)
- React TypeScript frontend
- Amazon Bedrock AI integration
- Sample data with 50 Indian market products
- Deployment scripts and documentation
- Architecture diagrams

Developed by Jeejo Joy (Team OG404)
AWS AI for Bharat Hackathon 2026

Tech Stack:
- Backend: Python, AWS Lambda, DynamoDB, Bedrock
- Frontend: React, TypeScript, Vite
- Infrastructure: AWS SAM, CloudFormation
- AI: Amazon Bedrock (Claude 3 Haiku)
"
echo -e "${GREEN}✓ Main branch committed${NC}"
echo ""

# Step 7: Show summary
echo -e "${BLUE}=========================================${NC}"
echo -e "${GREEN}✓ Repository organized successfully!${NC}"
echo -e "${BLUE}=========================================${NC}"
echo ""
echo -e "${YELLOW}BRANCHES:${NC}"
echo "  • main - Essential files for demo/evaluation (clean, professional)"
echo "  • dev  - All development files, drafts, notes (complete history)"
echo ""
echo -e "${YELLOW}NEXT STEPS:${NC}"
echo "1. Review the changes:"
echo "   git log --oneline -3"
echo "   git diff origin/main"
echo ""
echo "2. Push both branches:"
echo "   git push -u origin main --force"
echo "   git push -u origin dev"
echo ""
echo "3. Set main as default branch on GitHub"
echo ""
echo -e "${YELLOW}Repository: ${NC}$REPO_URL"
echo ""
echo -e "${GREEN}Ready to push! Run the commands above when ready.${NC}"
