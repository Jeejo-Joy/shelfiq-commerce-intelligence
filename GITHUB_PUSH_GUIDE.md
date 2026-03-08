# GitHub Push Guide

## Quick Start (Automated)

```bash
# Make the script executable
chmod +x push-to-github.sh

# Run the script
./push-to-github.sh
```

The script will:
1. ✅ Clean up sensitive files
2. ✅ Initialize Git (if needed)
3. ✅ Add remote repository
4. ✅ Stage all files
5. ✅ Create commit
6. ✅ Push to GitHub

---

## Manual Steps (If Needed)

### 1. Clean Up Sensitive Files

```bash
# Remove deployment artifacts
rm -f prototype/backend/deployment-outputs.json
rm -f prototype/backend/s3-bucket.txt
rm -f prototype/frontend/.env
rm -f aws-requirements.txt
```

### 2. Initialize Git

```bash
git init
git remote add origin https://github.com/Jeejo-Joy/shelfiq-commerce-intelligence.git
```

### 3. Stage and Commit

```bash
git add .
git commit -m "Initial commit: ShelfIQ - AI-Powered Commerce Intelligence"
```

### 4. Push to GitHub

```bash
git branch -M main
git push -u origin main
```

---

## After Pushing

### 1. Update Repository Settings on GitHub

Go to: https://github.com/Jeejo-Joy/shelfiq-commerce-intelligence/settings

**About Section:**
- Description: "AI-Powered Commerce Intelligence for Indian E-commerce | Amazon Bedrock | AWS Serverless"
- Website: [Your demo URL]
- Topics: `aws`, `bedrock`, `ai`, `ecommerce`, `serverless`, `lambda`, `dynamodb`, `react`, `typescript`, `hackathon`

### 2. Add Demo Video

1. Upload your demo video to YouTube
2. Update README.md with the video link:
   ```markdown
   ## 🎥 Demo

   Watch our 2-minute demo: [YouTube Link](https://youtube.com/...)
   ```
3. Commit and push:
   ```bash
   git add README.md
   git commit -m "Add demo video link"
   git push
   ```

### 3. Create a Release

1. Go to: https://github.com/Jeejo-Joy/shelfiq-commerce-intelligence/releases/new
2. Tag version: `v1.0.0`
3. Release title: "ShelfIQ v1.0.0 - AWS AI for Bharat Hackathon Submission"
4. Description:
   ```
   ## ShelfIQ - AI-Powered Commerce Intelligence

   **Team OG404** submission for AWS AI for Bharat Hackathon 2026

   ### Features
   - AI-powered pricing recommendations using Amazon Bedrock
   - Real-time competitor analysis
   - Indian market focus with INR pricing
   - Fully serverless architecture on AWS

   ### Demo
   [YouTube Demo Link]

   ### Tech Stack
   - Amazon Bedrock (Claude 3 Sonnet)
   - AWS Lambda
   - Amazon DynamoDB
   - API Gateway
   - React + TypeScript

   ### Installation
   See [README.md](README.md) for setup instructions.
   ```
5. Click "Publish release"

### 4. Add Repository Banner (Optional)

Create a banner image with:
- ShelfIQ logo/name
- "AI-Powered Commerce Intelligence"
- "Team OG404"
- AWS + Bedrock logos

Upload to `docs/banner.png` and add to README:
```markdown
![ShelfIQ Banner](docs/banner.png)
```

---

## Troubleshooting

### Authentication Issues

If you get authentication errors:

**Option 1: Personal Access Token**
1. Go to: https://github.com/settings/tokens
2. Generate new token (classic)
3. Select scopes: `repo`, `workflow`
4. Use token as password when pushing

**Option 2: SSH**
```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "your_email@example.com"

# Add to GitHub
cat ~/.ssh/id_ed25519.pub
# Copy and add to: https://github.com/settings/keys

# Change remote to SSH
git remote set-url origin git@github.com:Jeejo-Joy/shelfiq-commerce-intelligence.git
```

### Large Files

If you get "file too large" errors:
```bash
# Check file sizes
find . -type f -size +50M

# Remove large files from git
git rm --cached path/to/large/file
echo "path/to/large/file" >> .gitignore
```

### Merge Conflicts

If remote has changes:
```bash
git pull origin main --rebase
# Resolve conflicts
git push origin main
```

---

## Files Included in Repository

✅ **Source Code**
- `prototype/backend/` - Lambda functions and SAM template
- `prototype/frontend/` - React application
- `prototype/scripts/` - Deployment and data scripts
- `prototype/sample-data/` - Sample CSV data

✅ **Documentation**
- `README.md` - Main documentation
- `DEMO_SCRIPT.md` - Demo presentation guide
- `SETUP_GUIDE.md` - Deployment instructions
- `CONTRIBUTING.md` - Contribution guidelines
- `LICENSE` - MIT License

✅ **Configuration**
- `.gitignore` - Git ignore rules
- `package.json` - Frontend dependencies
- `template.yaml` - AWS SAM template

❌ **Excluded (Sensitive)**
- `.env` files
- `deployment-outputs.json`
- `samconfig.toml`
- `node_modules/`
- `.aws-sam/`
- AWS credentials

---

## Verification Checklist

After pushing, verify:

- [ ] Repository is public
- [ ] README displays correctly
- [ ] All source files are present
- [ ] No sensitive data (credentials, tokens)
- [ ] .gitignore is working
- [ ] Demo script is included
- [ ] License file is present
- [ ] Repository has description and topics
- [ ] Demo video link is added (after recording)
- [ ] Release is created

---

## Need Help?

If you encounter issues:
1. Check the error message carefully
2. Verify your GitHub credentials
3. Ensure you have write access to the repository
4. Check `.gitignore` is working correctly

Good luck with your hackathon submission! 🚀
