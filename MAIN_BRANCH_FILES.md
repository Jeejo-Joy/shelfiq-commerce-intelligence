# Main Branch - Essential Files Only

## Files included on main branch (for demo/evaluation):

### 📄 Root Documentation
- `README.md` - Project overview and documentation
- `LICENSE` - MIT License
- `SETUP_GUIDE.md` - Setup and deployment instructions
- `CONTRIBUTING.md` - Contribution guidelines
- `.gitignore` - Git ignore rules

### 📊 Presentation
- `ShelfIQ_OG404_AWS AI for Bharat Hackathon_v4.pdf` - Final presentation

### 🖼️ Essential Images (pics/)
- `ShelfIQ_System_Architecture_1920x1080.png` - System architecture
- `ShelfIQ_Dashboard_Wireframe_1600x800.png` - Dashboard wireframe
- `ShelfIQ_Product_Detail_Wireframe_1600x800.png` - Product detail wireframe

### 🔧 Backend (prototype/backend/)
```
prototype/backend/
├── template.yaml                    # AWS SAM template
├── requirements.txt                 # Python dependencies
├── requirements-dev.txt             # Dev dependencies
├── pytest.ini                       # Test configuration
├── POST_DEPLOY_STEPS.md            # Post-deployment guide
├── configure-s3-trigger.sh          # S3 trigger setup
├── functions/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── handler.py
│   │   └── requirements.txt
│   ├── ingestion/
│   │   ├── __init__.py
│   │   ├── handler.py
│   │   └── requirements.txt
│   └── intelligence/
│       ├── __init__.py
│       ├── handler.py
│       └── requirements.txt
└── tests/
    ├── __init__.py
    └── conftest.py
```

### 💻 Frontend (prototype/frontend/)
```
prototype/frontend/
├── package.json
├── package-lock.json
├── tsconfig.json
├── tsconfig.node.json
├── vite.config.ts
├── index.html
├── .env.example
└── src/
    ├── main.tsx
    ├── App.tsx
    ├── App.css
    ├── vite-env.d.ts
    ├── services/
    │   └── api.ts
    ├── types/
    │   └── index.ts
    └── utils/
        └── currency.ts
```

### 🔨 Scripts (prototype/scripts/)
- `setup.sh` - Initial setup
- `deploy.sh` - Backend deployment
- `deploy-frontend.sh` - Frontend deployment
- `generate_sample_data.py` - Sample data generator
- `load_data_to_dynamodb.py` - Data loader

### 📊 Sample Data (prototype/sample-data/)
- `products.csv` - 50 sample products with Indian pricing

### 📖 Prototype Documentation
- `prototype/README.md` - Prototype-specific documentation

---

## Files on dev branch ONLY (not on main):

### Draft Documentation
- `DEMO_SCRIPT.md`
- `DEMO_READY.md`
- `GITHUB_PUSH_GUIDE.md`
- `REPOSITORY_STRUCTURE.md`
- `GITHUB_FILES_SUMMARY.md`
- `CURRENT_STATUS.md`
- `IMPLEMENTATION_SUMMARY.md`
- `DESIGN.md`
- `REQUIREMENTS.md`

### Development Files
- `.kiro/` - IDE configuration
- `archive/` - Old files
- `demo/` - Demo videos
- `docs/` - Draft documentation
- `ppt/` - PowerPoint files
- `pics/` - Additional images (slide exports, diagrams)
- `cleanup-for-github.sh`
- `push-to-github.sh`
- `git-push-plan.sh`

---

## Why this structure?

**Main branch** = Clean, professional, ready for:
- Hackathon judges to evaluate
- Demo presentation
- Public viewing
- Future contributors

**Dev branch** = Complete development history:
- All drafts and iterations
- Development notes
- Internal documentation
- Demo materials
- Archive files

This keeps main branch focused and professional while preserving all work in dev branch.
