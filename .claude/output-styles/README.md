# Claude Output Styles Library

This directory contains JSON configuration files for Claude Code's `/output-style` feature, enabling standardized communication formats across team workflows.

## Quick Start

To use an output style in Claude Code:
```
/output-style [style-name]
```

Example:
```
/output-style sprint-report
```

## Available Styles

### Production Styles (Ready for Daily Use)
- **`sprint-report`** - Sprint retrospectives and team reports
- **`code-implementation`** - Technical implementation with documentation
- **`technical-analysis`** - Architecture decisions and investigations
- **`star-agent-optimization`** - Agent performance optimization

### Beta Styles (Recently Added)
- **`bug-report`** - Structured bug reporting with reproduction steps
- **`test-plan`** - Comprehensive test planning documentation
- **`api-documentation`** - OpenAPI/Swagger-style API docs
- **`security-audit`** - Security assessment reports
- **`performance-analysis`** - Performance profiling and optimization

## Style Selection Guide

### By Role
- **Developers:** `code-implementation`, `bug-report`, `api-documentation`
- **QA Engineers:** `bug-report`, `test-plan`, `security-audit`
- **Project Managers:** `sprint-report`, `test-plan`
- **DevOps:** `security-audit`, `performance-analysis`
- **AI Engineers:** `star-agent-optimization`, `performance-analysis`

### By Frequency
- **Daily:** `code-implementation`, `bug-report`
- **Weekly:** `sprint-report`, `test-plan`, `technical-analysis`
- **Monthly:** `security-audit`, `performance-analysis`, `star-agent-optimization`

## File Structure

```
.claude/output-styles/
├── index.json              # Style library catalog
├── README.md              # This file
├── sprint-report.json     # Sprint retrospective format
├── code-implementation.json # Technical implementation docs
├── technical-analysis.json  # Architecture decision format
├── star-agent-optimization.json # AI optimization reports
├── bug-report.json        # Bug reporting structure
├── test-plan.json         # Test planning template
├── api-documentation.json # API documentation format
├── security-audit.json    # Security assessment format
└── performance-analysis.json # Performance analysis template
```

## JSON Configuration Format

Each style is defined with:
- **name** - Unique identifier for the style
- **description** - Brief explanation of purpose
- **target_audience** - Intended users/roles
- **format** - Structure, tone, and verbosity settings
- **template** - Markdown template with placeholders
- **usage_examples** - Common use cases
- **best_practices** - Guidelines for effective use

## Creating Custom Styles

1. **Copy an existing style** as a starting point
2. **Modify the configuration** to match your needs
3. **Test the style** with Claude Code
4. **Share with the team** for feedback
5. **Submit for inclusion** via GitHub issue

## Contributing New Styles

We welcome community contributions! To suggest a new style:

1. **Comment on [Issue #4](https://github.com/norrisaftcc/the_algorithm/issues/4)** with your suggestion
2. **Use the suggestion template** provided in the issue
3. **Include real-world examples** of when you'd use the style
4. **Get community feedback** through voting and discussion

Top-voted styles will be implemented and added to the library.

## Documentation

- **[Output Style Guide](../docs/output-style-guide.md)** - Comprehensive usage guide
- **[Sprint Zero Lessons](../docs/sprint-zero-lessons-learned.md)** - Team learnings and metrics
- **[GitHub Issue #4](https://github.com/norrisaftcc/the_algorithm/issues/4)** - Community suggestions

## Support

For questions or issues:
- Check the [Output Style Guide](../docs/output-style-guide.md)
- Comment on [Issue #4](https://github.com/norrisaftcc/the_algorithm/issues/4)
- Reach out to the team leads monitoring the issue

---

*This library is continuously evolving based on team needs and community feedback.*