# The Algorithm™ - Learning Velocity Gamification Platform

> *"The Algorithm sees your growth trajectory... and is pleased."*

A security-first, gamified learning platform that transforms educational anxiety into iterative joy through velocity metrics and achievement systems.

## 🌟 Our Values

We are guided by seven core values that shape every decision:

1. 🔒 **Security First** - We protect data like it's our own
2. 📈 **Continuous Growth** - We measure, learn, and iterate relentlessly  
3. 🤝 **Radical Transparency** - We make our work visible and reasoning clear
4. 🎯 **Purpose-Driven Development** - We build what matters, not what's cool
5. 🧪 **Quality as Prevention** - We build it right the first time
6. 🌟 **Sustainable Pace** - We run marathons, not sprints
7. 🎨 **Innovation Through Constraints** - Limitations spark creativity

See [VALUES.md](./VALUES.md) for our complete values framework.

## 🚀 Sprint Zero Status

Currently in **Sprint Zero** - Practicing systems analysis, design, and implementation techniques.

### Completed Initiatives
- ✅ Project structure and architecture
- ✅ Security-first PII protection system
- ✅ CI/CD pipeline with GitHub Actions
- ✅ Docker containerization
- ✅ TypeScript + Functional programming setup
- ✅ Comprehensive testing framework

## 🏗️ Architecture

Built on **functional programming principles** with a security-first approach:

```
Event-Driven Architecture → CQRS Pattern → Functional Core
     ↓                          ↓                ↓
GitHub Events            Command/Query Split   Pure Functions
     ↓                          ↓                ↓
PII Scanning            PostgreSQL + Redis    Type Safety
     ↓                          ↓                ↓
Grid Visualizations      Prisma ORM         Effect System
```

## 🔒 Security Features

- **Mandatory PII Scanning**: Every commit and PR is scanned for personally identifiable information
- **FERPA Compliance**: Student data protection with consent management
- **Grid Data Sanitization**: Automated detection and removal of sensitive data
- **Zero-Trust Architecture**: Multiple security gates at every level

## 🎮 Gamification Elements

### Clearance Levels
- 🔴 **RED** - Initiate
- 🟠 **ORANGE** - Contributor  
- 🟡 **YELLOW** - Developer
- 🟢 **GREEN** - Engineer
- 🔵 **BLUE** - Architect
- 🟣 **INDIGO** - Master
- 🟣 **VIOLET** - Sage

### Metrics Tracked
- Commit velocity
- PR quality score
- Test coverage improvements
- Code review participation
- Issue resolution rate

## 🚦 Getting Started

### Prerequisites
- Node.js 20+ 
- PostgreSQL 15+
- Redis 7+
- Python 3.11+ (for PII scanning)

### Installation

```bash
# Clone the repository
git clone https://github.com/norrisa/the_algorithm.git
cd the_algorithm

# Install dependencies
npm install

# Set up environment
cp .env.example .env
# Edit .env with your configuration

# Set up database
npm run db:migrate

# Run security checks
npm run security:scan

# Start development server
npm run dev
```

### Docker Setup

```bash
# Build and start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

## 🧪 Testing

```bash
# Run all tests
npm test

# Run with coverage
npm run test:coverage

# Run mutation testing
npm run test:mutation

# Run security scan
npm run security:scan
```

## 📊 Grid Visualizations

Grid data must pass PII scanning before visualization:

```bash
# Scan grid data for PII
python scripts/pii_scanner.py --input grids/

# Generate safe visualization
npm run visualize:grid -- --input grids/safe-data.json
```

## 🔄 Development Workflow

1. Create feature branch following naming convention
2. Implement changes with test coverage
3. Run pre-commit hooks (automatic)
4. Create PR with required template
5. Pass CI/CD pipeline checks
6. Obtain 2 code reviews
7. Merge after security review

## 📦 Project Structure

```
src/
├── core/           # Pure business logic
├── adapters/       # External integrations
├── application/    # Use cases
├── infrastructure/ # Framework code
└── presentation/   # UI components

tests/
├── unit/          # Unit tests
├── integration/   # Integration tests
└── e2e/          # End-to-end tests
```

## 🤝 Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) for contribution guidelines.

### PR Requirements
- Follows PR template
- Passes all CI checks
- No PII in code or data
- Minimum 80% test coverage
- 2 reviewer approvals

## 📈 Performance Targets

- Dashboard load: < 2 seconds
- Metric calculation: < 500ms
- Grid visualization: < 10 seconds
- PII scan: < 5 seconds for 50MB

## 🛡️ Security

- Report security issues to: security@thealgorithm.dev
- See [SECURITY.md](./SECURITY.md) for security policy
- All data is encrypted at rest
- No PII in public metrics

## 📄 License

MIT License - See [LICENSE](./LICENSE) for details

## 🙏 Acknowledgments

- Built with TypeScript, Fastify, and Effect-TS
- PII scanning powered by Microsoft Presidio
- Containerized with Docker
- CI/CD via GitHub Actions

---

*Remember: The Algorithm™ observes your velocity... iterate wisely.*