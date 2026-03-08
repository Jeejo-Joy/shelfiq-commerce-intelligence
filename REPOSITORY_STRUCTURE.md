# Repository Structure

## Current Organization (After Cleanup)

```
shelfiq-commerce-intelligence/
│
├── 📄 README.md                    # Main documentation
├── 📄 LICENSE                      # MIT License
├── 📄 .gitignore                   # Git ignore rules
├── 📄 DEMO_SCRIPT.md              # Demo presentation guide
├── 📄 DEMO_READY.md               # Demo checklist
├── 📄 SETUP_GUIDE.md              # Deployment instructions
├── 📄 CONTRIBUTING.md             # Contribution guidelines
├── 📄 GITHUB_PUSH_GUIDE.md        # GitHub push instructions
├── 🔧 push-to-github.sh           # Automated push script
├── 🔧 cleanup-for-github.sh       # Cleanup script
│
├── 📁 prototype/                   # Main application code
│   ├── 📁 backend/                # AWS Lambda backend
│   │   ├── 📁 functions/
│   │   │   ├── api/              # API handler Lambda
│   │   │   ├── intelligence/     # Bedrock AI Lambda
│   │   │   └── ingestion/        # Data ingestion Lambda
│   │   ├── template.yaml         # AWS SAM template
│   │   └── README.md
│   │
│   ├── 📁 frontend/               # React frontend
│   │   ├── 📁 src/
│   │   │   ├── App.tsx           # Main component
│   │   │   ├── services/         # API client
│   │   │   ├── types/            # TypeScript types
│   │   │   └── utils/            # Utilities
│   │   ├── package.json
│   │   └── vite.config.ts
│   │
│   ├── 📁 sample-data/            # Sample CSV data
│   │   └── products.csv
│   │
│   └── 📁 scripts/                # Deployment scripts
│       ├── deploy-frontend.sh
│       ├── generate_sample_data.py
│       └── load_data_to_dynamodb.py
│
├── 📁 docs/                        # Documentation
│   ├── ShelfIQ_Architecture_Enhanced.md
│   ├── ShelfIQ_Innovation_Narrative.md
│   └── ShelfIQ_Technical_Architecture_Final.md
│
├── 📁 pics/                        # Images and diagrams
│   ├── ShelfIQ_Dashboard_Wireframe_1600x800.png
│   ├── ShelfIQ_Product_Detail_Wireframe_1600x800.png
│   ├── ShelfIQ_System_Architecture_1920x1080.png
│   └── ShelfIQ_OG404.png
│
└── 📁 ppt/                         # Presentation
    └── ShelfIQ_OG404_AWS AI for Bharat Hackathon.pdf
```

## Files Excluded (via .gitignore)

```
❌ .DS_Store                        # macOS files
❌ .kiro/                           # IDE config
❌ .vscode/                         # IDE config
❌ archive/                         # Old files
❌ demo/                            # Video files (too large)
❌ node_modules/                    # Dependencies
❌ .aws-sam/                        # Build artifacts
❌ .env                             # Environment variables
❌ deployment-outputs.json          # Deployment artifacts
❌ samconfig.toml                   # SAM config (has account info)
❌ CURRENT_STATUS.md                # Draft docs
❌ IMPLEMENTATION_SUMMARY.md        # Draft docs
❌ aws-requirements.txt             # Sensitive
```

## Key Files Explained

### Root Level
- **README.md** - Main entry point, comprehensive documentation
- **LICENSE** - MIT License for open source
- **DEMO_SCRIPT.md** - Step-by-step demo guide for video recording
- **SETUP_GUIDE.md** - Deployment and setup instructions
- **.gitignore** - Prevents sensitive files from being committed

### prototype/backend/
- **template.yaml** - AWS SAM Infrastructure as Code
- **functions/** - Lambda function code (Python 3.11)
  - `api/` - REST API handler
  - `intelligence/` - Bedrock AI integration
  - `ingestion/` - Data loading

### prototype/frontend/
- **src/** - React application (TypeScript)
- **package.json** - Dependencies and scripts
- **vite.config.ts** - Build configuration

### prototype/scripts/
- **deploy-frontend.sh** - Automated frontend deployment
- **generate_sample_data.py** - Creates sample product data
- **load_data_to_dynamodb.py** - Loads data to DynamoDB

### docs/
- Architecture diagrams and technical documentation
- Innovation narrative for hackathon judges

### pics/
- Wireframes and system architecture diagrams
- Logo and branding assets

### ppt/
- Final presentation PDF for hackathon submission

## File Sizes (Approximate)

```
Total Repository Size: ~15 MB

Breakdown:
- Source Code: ~500 KB
- Documentation: ~200 KB
- Images: ~10 MB
- PDF: ~4 MB
- Scripts: ~50 KB
```

## Clean Repository Checklist

Before pushing to GitHub, ensure:

- [ ] No `.env` files
- [ ] No `deployment-outputs.json`
- [ ] No `samconfig.toml` (contains account ID)
- [ ] No `node_modules/`
- [ ] No `.aws-sam/` build artifacts
- [ ] No `.DS_Store` files
- [ ] No personal AWS credentials
- [ ] No large video files (>100MB)
- [ ] All sensitive data removed

## How to Clean Up

Run the cleanup script:

```bash
chmod +x cleanup-for-github.sh
./cleanup-for-github.sh
```

Then verify:

```bash
# Check what will be committed
git status

# Check file sizes
du -sh *

# Check for sensitive data
grep -r "aws_access_key" .
grep -r "aws_secret" .
```

## Repository Best Practices

✅ **DO Include:**
- Source code
- Documentation
- Sample data (small files)
- Configuration templates
- Deployment scripts
- Architecture diagrams
- License file

❌ **DON'T Include:**
- Credentials or secrets
- Large binary files (>50MB)
- Build artifacts
- IDE-specific configs
- Personal notes
- Draft documents
- Deployment outputs

---

**Last Updated:** March 8, 2026
**Repository:** https://github.com/Jeejo-Joy/shelfiq-commerce-intelligence
