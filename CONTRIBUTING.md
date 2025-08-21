# Contributing to The Algorithm™

Thank you for your interest in contributing! This guide will help you contribute in a way that aligns with our values and processes.

## 🌟 Value-Driven Contributions

All contributions must align with our [core values](./VALUES.md):

### Before You Contribute, Ask Yourself:
- 🔒 **Security First**: Does this protect user data?
- 📈 **Continuous Growth**: What will we learn from this?
- 🤝 **Radical Transparency**: Is my reasoning clear?
- 🎯 **Purpose-Driven**: Does this add measurable value?
- 🧪 **Quality Prevention**: Am I preventing future problems?
- 🌟 **Sustainable Pace**: Is this maintainable long-term?
- 🎨 **Innovation Through Constraints**: Is this the simplest solution?

## 📋 Contribution Process

### 1. Find or Create an Issue
- Check existing issues first
- If creating new, use our issue templates
- Clearly describe the value being added
- Link to relevant user stories

### 2. Fork and Branch
```bash
# Fork the repository on GitHub
git clone https://github.com/YOUR_USERNAME/the_algorithm.git
cd the_algorithm

# Create a value-driven branch name
git checkout -b feature/[value]-[description]
# Examples:
# feature/security-add-encryption
# feature/quality-increase-coverage
# feature/growth-improve-metrics
```

### 3. Make Your Changes

#### Code Standards
- **TypeScript**: Strict mode, no `any` types
- **Testing**: Write tests first (TDD)
- **Coverage**: Maintain or increase coverage
- **Documentation**: Explain the why, not just what

#### Commit Messages
Follow our value-driven commit format:
```
[value]: Clear description of change

Longer explanation if needed.

Value Impact: How this embodies our values
Metrics: Measurable improvement
```

Examples:
```
security: Add input sanitization to cache adapter

Prevents potential injection attacks by validating 
all cache keys against whitelist pattern.

Value Impact: Security First - protecting user data
Metrics: 100% of inputs now validated
```

### 4. Test Your Changes
```bash
# Run tests
npm test

# Check coverage
npm run test:coverage

# Lint your code
npm run lint

# Type check
npm run typecheck

# Security scan
npm run security:scan
```

### 5. Submit Pull Request

Use our PR template and ensure:
- [ ] All value checkboxes are considered
- [ ] Tests are passing
- [ ] Documentation is updated
- [ ] No PII or secrets included
- [ ] Value impact statement provided

## 🎯 What We're Looking For

### High-Value Contributions
- 🚀 Performance improvements with metrics
- 🔒 Security enhancements
- 📚 Documentation improvements
- 🧪 Test coverage increases
- 🎨 Code simplification
- 📈 New metrics or insights

### Types of Contributions

#### Code Contributions
- Features that align with roadmap
- Bug fixes with root cause analysis
- Performance optimizations with benchmarks
- Refactoring that reduces complexity

#### Documentation Contributions
- Clear examples and tutorials
- API documentation
- Architecture diagrams
- Onboarding improvements

#### Testing Contributions
- Increase test coverage
- Add missing edge cases
- Performance benchmarks
- Security test scenarios

#### Process Contributions
- Workflow improvements
- Automation scripts
- Developer tools
- CI/CD enhancements

## 🚫 What We Won't Accept

### Value Violations
- ❌ Code without tests
- ❌ Features without clear value
- ❌ Complex solutions to simple problems
- ❌ Undocumented breaking changes
- ❌ Security vulnerabilities
- ❌ Unsustainable quick fixes

### Anti-Patterns
- God objects/functions
- Commented-out code
- Console.logs in production
- Hardcoded values
- Synchronous operations that should be async
- Premature optimization

## 🤝 Code Review Process

### What Reviewers Look For
1. **Value Alignment**: Does this embody our values?
2. **Correctness**: Does it work as intended?
3. **Security**: Are there any vulnerabilities?
4. **Performance**: Will this scale?
5. **Maintainability**: Can others understand it?
6. **Testing**: Is it properly tested?

### Review Etiquette
- Be kind and constructive
- Explain the why behind suggestions
- Celebrate learning opportunities
- Ask questions before assuming
- Suggest, don't demand

## 📊 Contribution Metrics

We track and celebrate:
- 🏆 First-time contributors
- 📈 Most improved code quality
- 🔒 Security issues prevented
- 📚 Best documentation
- 🧪 Highest test coverage
- 💡 Most innovative solution

## 🎓 Learning Resources

### For New Contributors
- [Sprint Zero Lessons](./docs/sprint-zero-lessons-learned.md)
- [STAR Framework Guide](./docs/star-agent-optimization-guide.md)
- [Output Style Guide](./docs/output-style-guide.md)
- [Architecture Decisions](./docs/architecture-decisions/)

### Development Setup
```bash
# Install dependencies
npm install

# Set up environment
cp .env.example .env

# Run development server
npm run dev

# Run validation
./validate-sprint-zero.sh
```

## 🤖 Agent Contributions

If you're contributing through an agent:
1. Use the STAR framework for prompts
2. Track contributions with agent-tracker
3. Include agent attribution in commits
4. Follow the same quality standards

## 📝 License

By contributing, you agree that your contributions will be licensed under the same [MIT License](./LICENSE) that covers the project.

## 🙏 Recognition

We maintain a [CONTRIBUTORS.md](./CONTRIBUTORS.md) file to recognize all contributors. Your contributions will be acknowledged!

## ❓ Questions?

- Open an issue with the `question` label
- Check our [documentation](./docs/)
- Review our [values](./VALUES.md)

## 🚀 Ready to Contribute?

1. Read our [VALUES.md](./VALUES.md)
2. Find an issue labeled `good first issue`
3. Comment that you're working on it
4. Follow the process above
5. Submit your PR
6. Celebrate your contribution!

---

*Remember: Every contribution, no matter how small, makes The Algorithm™ stronger. The Algorithm sees your contribution... and is pleased.*