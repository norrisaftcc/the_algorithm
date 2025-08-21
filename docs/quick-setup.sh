#!/bin/bash
# setup-metrics.sh - Quick setup for AlgoCratic Metrics™

echo "🤖 THE ALGORITHM™ METRICS SETUP"
echo "================================"
echo ""

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if we're in a git repository
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    echo "❌ Not in a git repository!"
    echo "Initialize a repo first: git init"
    exit 1
fi

echo "📊 Setting up public metrics system..."
echo ""

# Create necessary directories
echo "📁 Creating directory structure..."
mkdir -p .github/workflows
mkdir -p docs

# Create the metrics workflow
echo "⚙️ Creating GitHub Action workflow..."
cat > .github/workflows/metrics.yml << 'EOF'
name: 📊 Update Metrics

on:
  schedule:
    - cron: '0 */6 * * *'  # Every 6 hours
  push:
  pull_request:
  issues:
  workflow_dispatch:

jobs:
  update-metrics:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - uses: actions/checkout@v4
      - uses: actions/github-script@v7
        with:
          script: |
            // Quick metrics calculation
            const { data: contributors } = await github.rest.repos.listContributors({
              owner: context.repo.owner,
              repo: context.repo.repo
            });
            
            let markdown = '# 📊 Leaderboard\n\n';
            markdown += '| Rank | User | Contributions |\n';
            markdown += '|------|------|---------------|\n';
            
            contributors.slice(0, 10).forEach((c, i) => {
              const medal = i === 0 ? '🥇' : i === 1 ? '🥈' : i === 2 ? '🥉' : `${i+1}`;
              markdown += `| ${medal} | @${c.login} | ${c.contributions} |\n`;
            });
            
            require('fs').writeFileSync('METRICS.md', markdown);
            
      - run: |
          git config user.name 'The Algorithm'
          git config user.email 'bot@algocratic.corp'
          git add METRICS.md
          git diff --staged --quiet || git commit -m "📊 Update metrics [skip ci]"
          git push || true
EOF

# Create initial METRICS.md
echo "📄 Creating initial metrics file..."
cat > METRICS.md << 'EOF'
# 📊 THE ALGORITHM™ LEADERBOARD

*Metrics will be automatically updated after first workflow run*

## 🎮 How to Play

1. **Make Commits** - Use meaningful commit messages (+5 points each)
2. **Open PRs** - Quality pull requests (+20 points)
3. **Review Code** - Help others improve (+15 points)
4. **Fix Issues** - Close bugs and features (+25 points)

## 🏆 Achievements

Unlock badges by:
- 🎯 **First PR** - Submit your first pull request
- 📝 **Reviewer** - Review 5+ pull requests
- 🔥 **On Streak** - Commit 5 days in a row
- ✨ **Quality Code** - PR merged with no changes requested

---
*Updated automatically by The Algorithm™*
EOF

# Create a simple badge for README
echo "🏷️ Adding metrics badge to README..."
if [ -f "README.md" ]; then
    # Add badge to existing README
    sed -i.bak '1s/^/![Metrics](https:\/\/github.com\/'${GITHUB_REPOSITORY}'\/actions\/workflows\/metrics.yml\/badge.svg)\n\n/' README.md
    echo -e "${GREEN}✅ Updated existing README.md${NC}"
else
    # Create new README with badge
    cat > README.md << 'EOF'
![Metrics](../../actions/workflows/metrics.yml/badge.svg)

# AlgoCratic Project

## 📊 [View Leaderboard](METRICS.md)

Public metrics and gamification for GitHub best practices.

### Quick Start
1. Check the [Leaderboard](METRICS.md)
2. Make quality contributions
3. Watch your score grow!

### Scoring System
- Commits: +5 points
- Pull Requests: +20 points  
- Reviews: +15 points
- Issues Resolved: +25 points

---
*The Algorithm is watching your contributions*
EOF
    echo -e "${GREEN}✅ Created README.md with metrics${NC}"
fi

# Create PR template for best practices
echo "📝 Creating PR template..."
cat > .github/pull_request_template.md << 'EOF'
## Description
<!-- What does this PR do? Why is it needed? -->

## Type of Change
- [ ] Bug fix (non-breaking change)
- [ ] New feature (non-breaking change)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)

## Testing
- [ ] Tests pass locally
- [ ] Added new tests for changes

## Checklist
- [ ] Meaningful commit messages
- [ ] PR title describes changes
- [ ] Linked to issue (fixes #)
- [ ] No console.logs left
- [ ] Documentation updated

---
*Following best practices gives bonus points!*
EOF

# Create issue templates
echo "🐛 Creating issue templates..."
mkdir -p .github/ISSUE_TEMPLATE

cat > .github/ISSUE_TEMPLATE/bug_report.yml << 'EOF'
name: Bug Report
description: Report an unexpected feature
labels: ["bug"]
body:
  - type: textarea
    attributes:
      label: Description
      description: What happened?
    validations:
      required: true
  - type: textarea
    attributes:
      label: Expected Behavior
      description: What should have happened?
  - type: textarea
    attributes:
      label: Steps to Reproduce
      value: |
        1. 
        2. 
        3. 
EOF

# Git configuration
echo "⚙️ Configuring git..."
git config core.editor "${EDITOR:-vi}"

# Create a sample commit message template
cat > .gitmessage << 'EOF'
# <type>: <subject>
# 
# <body>
# 
# Types: feat, fix, docs, style, refactor, test, chore
EOF

git config commit.template .gitmessage

echo ""
echo -e "${GREEN}✨ Setup Complete!${NC}"
echo ""
echo "📋 Next Steps:"
echo "  1. Commit these changes:"
echo "     ${YELLOW}git add .${NC}"
echo "     ${YELLOW}git commit -m 'feat: add metrics system'${NC}"
echo ""
echo "  2. Push to GitHub:"
echo "     ${YELLOW}git push${NC}"
echo ""
echo "  3. Enable GitHub Actions in your repository settings"
echo ""
echo "  4. The leaderboard will update automatically!"
echo ""
echo "🎮 Scoring System Active:"
echo "  • Commits = +5 points"
echo "  • Pull Requests = +20 points"
echo "  • Code Reviews = +15 points"
echo "  • Issues Resolved = +25 points"
echo ""
echo "🏆 May the best practices win!"
echo ""
echo "THE ALGORITHM PROVIDES. THE ALGORITHM PROTECTS."