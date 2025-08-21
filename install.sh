#!/usr/bin/env zsh
# The Algorithm™ Migration Installer
# Zsh-powered installation script with rollback capability

set -euo pipefail

# Colors for output
autoload -U colors && colors
RED=$fg[red]
GREEN=$fg[green]
YELLOW=$fg[yellow]
BLUE=$fg[blue]
MAGENTA=$fg[magenta]
CYAN=$fg[cyan]
RESET=$reset_color

# Installation tracking
typeset -A COMPLETED_STEPS
INSTALL_LOG="install.log"
ROLLBACK_SCRIPT="rollback.sh"

# Banner
print_banner() {
    echo "${CYAN}"
    cat << 'EOF'
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║     _____ _             _    _                  _ _     ║
║    |_   _| |__   ___   / \  | | __ _  ___  _ __(_) |_   ║
║      | | | '_ \ / _ \ / _ \ | |/ _` |/ _ \| '__| | __|  ║
║      | | | | | |  __// ___ \| | (_| | (_) | |  | | |_   ║
║      |_| |_| |_|\___/_/   \_\_|\__, |\___/|_|  |_|\__|  ║
║                                |___/      ™             ║
║                                                          ║
║          Learning Velocity Gamification Platform        ║
║                    Sprint Zero Installer                ║
╚══════════════════════════════════════════════════════════╝
EOF
    echo "${RESET}"
}

# Progress indicator
progress() {
    local step=$1
    local total=$2
    local message=$3
    local percent=$((step * 100 / total))
    
    printf "\r${BLUE}[%3d%%]${RESET} ${message}" $percent
    if [[ $step -eq $total ]]; then
        echo " ${GREEN}✓${RESET}"
    fi
}

# Error handler with rollback
error_handler() {
    local line_no=$1
    local exit_code=$2
    echo "\n${RED}❌ Error occurred at line $line_no with exit code $exit_code${RESET}"
    echo "Rolling back installation..."
    rollback
    exit $exit_code
}

trap 'error_handler ${LINENO} $?' ERR

# Rollback function
rollback() {
    echo "${YELLOW}🔄 Rolling back changes...${RESET}"
    
    for step in ${(Onk)COMPLETED_STEPS}; do
        case $step in
            "npm_install")
                echo "  Removing node_modules..."
                rm -rf node_modules package-lock.json
                ;;
            "database")
                echo "  Dropping database..."
                dropdb the_algorithm 2>/dev/null || true
                ;;
            "directories")
                echo "  Removing created directories..."
                rm -rf grids scripts/pii_scanner.py .agent-contributions.json
                ;;
            "git_hooks")
                echo "  Removing git hooks..."
                rm -f .git/hooks/pre-commit
                ;;
        esac
    done
    
    echo "${GREEN}✓ Rollback complete${RESET}"
}

# System requirements check
check_requirements() {
    local missing=()
    
    echo "${CYAN}📋 Checking system requirements...${RESET}"
    
    # Node.js 20+
    if command -v node &>/dev/null; then
        local node_version=$(node --version | cut -d'v' -f2 | cut -d'.' -f1)
        if [[ $node_version -lt 20 ]]; then
            missing+=("Node.js 20+ (found v$node_version)")
        else
            echo "  ${GREEN}✓${RESET} Node.js $(node --version)"
        fi
    else
        missing+=("Node.js 20+")
    fi
    
    # PostgreSQL
    if command -v psql &>/dev/null; then
        echo "  ${GREEN}✓${RESET} PostgreSQL $(psql --version | awk '{print $3}')"
    else
        missing+=("PostgreSQL")
    fi
    
    # Redis
    if command -v redis-cli &>/dev/null; then
        echo "  ${GREEN}✓${RESET} Redis $(redis-cli --version | awk '{print $2}')"
    else
        missing+=("Redis")
    fi
    
    # Python 3.11+
    if command -v python3 &>/dev/null; then
        local python_version=$(python3 --version | awk '{print $2}' | cut -d'.' -f1,2)
        if [[ $python_version < "3.11" ]]; then
            missing+=("Python 3.11+ (found $python_version)")
        else
            echo "  ${GREEN}✓${RESET} Python $(python3 --version)"
        fi
    else
        missing+=("Python 3.11+")
    fi
    
    # GitHub CLI
    if command -v gh &>/dev/null; then
        echo "  ${GREEN}✓${RESET} GitHub CLI $(gh --version | head -1)"
    else
        missing+=("GitHub CLI")
    fi
    
    if [[ ${#missing[@]} -gt 0 ]]; then
        echo "\n${RED}❌ Missing requirements:${RESET}"
        for req in $missing; do
            echo "  - $req"
        done
        echo "\n${YELLOW}Please install missing requirements and try again.${RESET}"
        exit 1
    fi
    
    echo "${GREEN}✓ All requirements met${RESET}\n"
}

# Setup environment
setup_environment() {
    echo "${CYAN}🔧 Setting up environment...${RESET}"
    
    if [[ ! -f .env ]]; then
        cp .env.example .env
        echo "  ${GREEN}✓${RESET} Created .env file (please configure)"
    else
        echo "  ${BLUE}ℹ${RESET} .env file already exists"
    fi
    
    # Generate secure keys if not present
    if grep -q "your-jwt-secret" .env; then
        local jwt_secret=$(openssl rand -base64 32)
        local encryption_key=$(openssl rand -base64 32)
        
        # Use sed for macOS/BSD compatibility
        sed -i '' "s/your-jwt-secret-here-min-32-chars/$jwt_secret/" .env
        sed -i '' "s/your-encryption-key-here-min-32-chars/$encryption_key/" .env
        echo "  ${GREEN}✓${RESET} Generated secure keys"
    fi
}

# Install dependencies
install_dependencies() {
    echo "${CYAN}📦 Installing dependencies...${RESET}"
    
    npm install --silent 2>&1 | tee -a $INSTALL_LOG > /dev/null &
    local npm_pid=$!
    
    local i=0
    while kill -0 $npm_pid 2>/dev/null; do
        i=$((i + 1))
        progress $i 100 "Installing npm packages..."
        sleep 0.5
    done
    
    wait $npm_pid
    COMPLETED_STEPS[npm_install]=1
    echo "  ${GREEN}✓${RESET} NPM packages installed"
    
    # Python dependencies for PII scanning
    echo "  Installing Python dependencies..."
    pip3 install --quiet presidio-analyzer presidio-anonymizer 2>&1 | tee -a $INSTALL_LOG > /dev/null
    echo "  ${GREEN}✓${RESET} Python packages installed"
}

# Setup database
setup_database() {
    echo "${CYAN}🗄️  Setting up database...${RESET}"
    
    # Check if PostgreSQL is running
    if ! pg_isready -q; then
        echo "  ${YELLOW}⚠${RESET} PostgreSQL is not running. Starting..."
        if [[ "$OSTYPE" == "darwin"* ]]; then
            brew services start postgresql@15 2>/dev/null || true
        else
            sudo systemctl start postgresql 2>/dev/null || true
        fi
        sleep 2
    fi
    
    # Create database
    createdb the_algorithm 2>/dev/null || echo "  ${BLUE}ℹ${RESET} Database already exists"
    COMPLETED_STEPS[database]=1
    
    # Run migrations
    npx prisma generate
    npx prisma migrate deploy 2>&1 | tee -a $INSTALL_LOG > /dev/null
    echo "  ${GREEN}✓${RESET} Database configured and migrated"
}

# Setup git hooks
setup_git_hooks() {
    echo "${CYAN}🔒 Setting up git hooks...${RESET}"
    
    npx husky install
    chmod +x .husky/pre-commit
    COMPLETED_STEPS[git_hooks]=1
    echo "  ${GREEN}✓${RESET} Git hooks configured"
}

# Create necessary directories
create_directories() {
    echo "${CYAN}📁 Creating project directories...${RESET}"
    
    local dirs=(
        "grids"
        "artifacts"
        "logs"
        "scripts"
    )
    
    for dir in $dirs; do
        mkdir -p $dir
        echo "  ${GREEN}✓${RESET} Created $dir/"
    done
    
    COMPLETED_STEPS[directories]=1
}

# Initialize agent tracking
init_agent_tracking() {
    echo "${CYAN}🤖 Initializing agent tracking...${RESET}"
    
    cat > .agent-contributions.json << 'EOF'
{
  "installer": {
    "agents": {
      "installer-script": {
        "contributions": [
          {
            "description": "Automated project setup and migration",
            "timestamp": "$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
          }
        ]
      }
    },
    "timestamp": "$(date -u +"%Y-%m-%dT%H:%M:%SZ")",
    "branch": "main"
  }
}
EOF
    
    echo "  ${GREEN}✓${RESET} Agent tracking initialized"
}

# Run initial tests
run_tests() {
    echo "${CYAN}🧪 Running initial tests...${RESET}"
    
    npm run typecheck 2>&1 | tee -a $INSTALL_LOG > /dev/null
    echo "  ${GREEN}✓${RESET} TypeScript compilation successful"
    
    npm run lint 2>&1 | tee -a $INSTALL_LOG > /dev/null
    echo "  ${GREEN}✓${RESET} Linting passed"
}

# Final summary
print_summary() {
    echo "\n${GREEN}╔══════════════════════════════════════════════════════════╗${RESET}"
    echo "${GREEN}║            Installation Complete! 🎉                      ║${RESET}"
    echo "${GREEN}╚══════════════════════════════════════════════════════════╝${RESET}"
    
    echo "\n${CYAN}Next steps:${RESET}"
    echo "  1. Configure your ${YELLOW}.env${RESET} file with your settings"
    echo "  2. Run ${YELLOW}npm run dev${RESET} to start development server"
    echo "  3. Visit ${BLUE}http://localhost:3000${RESET}"
    echo "  4. Check ${YELLOW}docs/README.md${RESET} for documentation"
    
    echo "\n${MAGENTA}The Algorithm™ observes your velocity... iterate wisely.${RESET}"
}

# Main installation flow
main() {
    print_banner
    
    # Create install log
    echo "Installation started at $(date)" > $INSTALL_LOG
    
    check_requirements
    setup_environment
    install_dependencies
    create_directories
    setup_database
    setup_git_hooks
    init_agent_tracking
    run_tests
    
    print_summary
    
    echo "\n${GREEN}✓${RESET} Installation log saved to ${YELLOW}$INSTALL_LOG${RESET}"
}

# Run installer
main "$@"