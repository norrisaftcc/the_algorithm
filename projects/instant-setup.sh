#!/bin/bash
# 🚀 The Algorithm™ Growth Velocity System - Instant Setup
# Run this script in any GitHub repository to add growth gamification

set -e

echo "
╔══════════════════════════════════════════════════════════════╗
║     🚀 THE ALGORITHM™ GROWTH VELOCITY SYSTEM                ║
║     Gamifying Growth Mindset with AI-First Development      ║
╚══════════════════════════════════════════════════════════════╝
"

# Color codes for pretty output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check prerequisites
echo "📋 Checking prerequisites..."

if ! git rev-parse --git-dir > /dev/null 2>&1; then
    echo "❌ Not in a git repository!"
    echo "   Please run this from your project root."
    exit 1
fi

if [ ! -d ".git" ]; then
    echo "❌ Not in repository root!"
    echo "   Please run from the root directory of your repository."
    exit 1
fi

echo -e "${GREEN}✅ Git repository detected${NC}"

# Create directory structure
echo ""
echo "📁 Creating directory structure..."
mkdir -p .github/workflows
mkdir -p .github/ISSUE_TEMPLATE
mkdir -p docs/growth

# Create the main workflow
echo "⚙️  Installing Growth Velocity Tracker..."
cat > .github/workflows/growth-tracker.yml << 'WORKFLOW_EOF'
name: 🚀 The Algorithm™ Growth Velocity System

on:
  pull_request:
    types: [opened, synchronize]
  push:
    branches: [main, master, develop]
  schedule:
    - cron: '0 */6 * * *'
  workflow_dispatch:

jobs:
  calculate-velocity:
    name: 📊 Measure Growth Velocity
    runs-on: ubuntu-latest
    permissions:
      contents: write
      pull-requests: write
      
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
          
      - uses: actions/github-script@v7
        id: velocity
        with:
          script: |
            const author = context.actor;
            const threeWeeksAgo = new Date(Date.now() - 21 * 24 * 60 * 60 * 1000);
            
            const { data: commits } = await github.rest.repos.listCommits({
              owner: context.repo.owner,
         