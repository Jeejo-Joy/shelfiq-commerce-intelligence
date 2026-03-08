#!/bin/bash

# ShelfIQ - Cleanup Script for GitHub
# Removes unnecessary files before pushing to GitHub

set -e

echo "🧹 Cleaning up repository for GitHub..."
echo "========================================"
echo ""

# Remove unnecessary documentation files
echo "Removing draft documentation..."
rm -f CURRENT_STATUS.md
rm -f IMPLEMENTATION_SUMMARY.md
rm -f DESIGN.md
rm -f REQUIREMENTS.md
rm -f aws-requirements.txt

# Remove .DS_Store files
echo "Removing .DS_Store files..."
find . -name ".DS_Store" -type f -delete

# Remove archive folder
echo "Removing archive folder..."
rm -rf archive/

# Remove .kiro folder (IDE specific)
echo "Removing .kiro folder..."
rm -rf .kiro/

# Remove .vscode folder (IDE specific)
echo "Removing .vscode folder..."
rm -rf .vscode/

# Remove demo video (too large for git)
echo "Removing demo video..."
rm -rf demo/

# Clean up docs folder - keep only essential
echo "Cleaning docs folder..."
rm -f docs/ChatGPT_Diagram_Prompts*.md
rm -f docs/Diagram_to_Slide_Mapping.md
rm -f docs/Final_Diagram_Mapping.md
rm -f docs/ShelfIQ_Presentation_*.md
rm -f docs/ShelfIQ_Diagrams_*.md
rm -f docs/ShelfIQ_Slide4_Features_Integrated.md
rm -f docs/persona_Rajesh

# Keep only these in docs:
# - ShelfIQ_Architecture_Enhanced.md
# - ShelfIQ_Innovation_Narrative.md
# - ShelfIQ_Technical_Architecture_Final.md

# Clean up pics folder - keep only essential
echo "Cleaning pics folder..."
rm -f pics/ShelfIQ_OG404\ -\ Page*.png
rm -f pics/ShelfIQ_OG404\ -\ Page*.pdf
rm -f pics/mermaid-diagram-*.png
rm -f pics/*.pptx

# Keep only these in pics:
# - ShelfIQ_Dashboard_Wireframe_1600x800.png
# - ShelfIQ_Product_Detail_Wireframe_1600x800.png
# - ShelfIQ_System_Architecture_1920x1080.png
# - ShelfIQ_OG404.png

# Clean up ppt folder - keep only final PDF
echo "Cleaning ppt folder..."
rm -f ppt/*.pptx
rm -f "ppt/Idea Submission _ AWS AI for Bharat Hackathon.pptx"

# Keep only:
# - ShelfIQ_OG404_AWS AI for Bharat Hackathon.pdf

# Remove prototype/typescript (empty file)
echo "Removing empty files..."
rm -f prototype/typescript

# Remove backend deployment artifacts
echo "Removing deployment artifacts..."
rm -f prototype/backend/deployment-outputs.json
rm -f prototype/backend/s3-bucket.txt
rm -f prototype/backend/samconfig.toml

# Remove frontend .env
echo "Removing environment files..."
rm -f prototype/frontend/.env

echo ""
echo "✅ Cleanup complete!"
echo ""
echo "Files kept:"
echo "  ✓ README.md (main documentation)"
echo "  ✓ LICENSE"
echo "  ✓ DEMO_SCRIPT.md"
echo "  ✓ DEMO_READY.md"
echo "  ✓ SETUP_GUIDE.md"
echo "  ✓ CONTRIBUTING.md"
echo "  ✓ GITHUB_PUSH_GUIDE.md"
echo "  ✓ .gitignore"
echo "  ✓ prototype/ (source code)"
echo "  ✓ docs/ (essential docs only)"
echo "  ✓ pics/ (essential images only)"
echo "  ✓ ppt/ (final PDF only)"
echo ""
echo "Ready to push to GitHub!"
