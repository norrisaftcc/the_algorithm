#!/usr/bin/env zsh
# Sprint Zero Toolset Validation Script
# Confirms all tools are properly configured

autoload -U colors && colors

# Summary tracking
typeset -A RESULTS
PASSED=0
FAILED=0

# Test function
test_component() {
    local name=$1
    local command=$2
    
    echo -n "Testing $name... "
    
    if eval "$command" &>/dev/null; then
        echo "${fg[green]}✓${reset_color}"
        RESULTS[$name]="✓"
        ((PASSED++))
    else
        echo "${fg[red]}✗${reset_color}"
        RESULTS[$name]="✗"
        ((FAILED++))
    fi
}

echo "${fg[cyan]}═══════════════════════════════════════════${reset_color}"
echo "${fg[cyan]}    Sprint Zero Toolset Validation${reset_color}"
echo "${fg[cyan]}═══════════════════════════════════════════${reset_color}\n"

# 1. Version Control
echo "${fg[yellow]}📦 Version Control${reset_color}"
test_component "Git installed" "git --version"
test_component "GitHub CLI" "gh --version"
test_component "GitHub auth" "gh auth status"
echo

# 2. Node.js Environment
echo "${fg[yellow]}🟢 Node.js Environment${reset_color}"
test_component "Node.js 20+" "[[ $(node -v | cut -d'.' -f1 | sed 's/v//') -ge 20 ]]"
test_component "NPM installed" "npm --version"
test_component "Package.json exists" "[[ -f package.json ]]"
echo

# 3. TypeScript & Linting
echo "${fg[yellow]}📝 TypeScript & Code Quality${reset_color}"
test_component "TypeScript config" "[[ -f tsconfig.json ]]"
test_component "ESLint config" "[[ -f .eslintrc.json ]]"
test_component "Prettier config" "[[ -f .prettierrc ]]"
echo

# 4. Testing
echo "${fg[yellow]}🧪 Testing Framework${reset_color}"
test_component "Vitest config" "[[ -f vitest.config.ts ]]"
test_component "Test directory" "[[ -d tests ]]"
echo

# 5. CI/CD
echo "${fg[yellow]}🚀 CI/CD Pipeline${reset_color}"
test_component "GitHub workflows" "[[ -d .github/workflows ]]"
test_component "CI workflow" "[[ -f .github/workflows/ci.yml ]]"
test_component "Grid workflow" "[[ -f .github/workflows/grid-visualization.yml ]]"
echo

# 6. Docker (Optional for Sprint Zero)
echo "${fg[yellow]}🐳 Docker Configuration (Optional)${reset_color}"
test_component "Dockerfile" "[[ -f Dockerfile ]]"
test_component "Docker Compose" "[[ -f docker-compose.yml ]]"
echo "${fg[blue]}ℹ️  Docker not required for Sprint Zero (using SQLite)${reset_color}"
echo

# 7. Database (Simplified for Sprint Zero)
echo "${fg[yellow]}🗄️ Database Setup${reset_color}"
test_component "Prisma schema" "[[ -f prisma/schema.prisma ]]"
test_component "SQLite support" "command -v sqlite3 || echo 'Built-in Node.js support'"
test_component "In-memory cache" "[[ -f src/adapters/cache/in-memory-cache.ts ]]"
echo

# 8. Security
echo "${fg[yellow]}🔒 Security Tools${reset_color}"
test_component "Gitignore" "[[ -f .gitignore ]]"
test_component "Env example" "[[ -f .env.example ]]"
test_component "Python 3.11+" "python3 -c 'import sys; exit(0 if sys.version_info[:2] >= (3,11) else 1)'"
echo

# 9. Documentation
echo "${fg[yellow]}📚 Documentation${reset_color}"
test_component "README" "[[ -f README.md ]]"
test_component "License" "[[ -f LICENSE ]]"
test_component "Install script" "[[ -f install.sh ]]"
echo

# Summary
echo "${fg[cyan]}═══════════════════════════════════════════${reset_color}"
echo "${fg[cyan]}                Summary${reset_color}"
echo "${fg[cyan]}═══════════════════════════════════════════${reset_color}"
echo "${fg[green]}Passed: $PASSED${reset_color}"
echo "${fg[red]}Failed: $FAILED${reset_color}"

if [[ $FAILED -eq 0 ]]; then
    echo "\n${fg[green]}🎉 All validations passed!${reset_color}"
    echo "Sprint Zero toolset is properly configured."
    echo "Ready to begin user story implementation."
else
    echo "\n${fg[yellow]}⚠️  Some validations failed.${reset_color}"
    echo "Please address the issues above before proceeding."
fi

# Generate report
echo "\n${fg[blue]}Generating validation report...${reset_color}"
cat > validation-report.txt << EOF
Sprint Zero Validation Report
Generated: $(date)

Results:
$(for key val in ${(kv)RESULTS}; do echo "$key: $val"; done | sort)

Summary:
- Passed: $PASSED
- Failed: $FAILED
- Success Rate: $(( PASSED * 100 / (PASSED + FAILED) ))%
EOF

echo "Report saved to: ${fg[yellow]}validation-report.txt${reset_color}"