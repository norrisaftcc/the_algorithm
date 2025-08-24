# Output Style Guide

## Overview

Claude Code's `/output-style` feature allows teams to standardize communication formats across different workflows and team roles. This guide explains how to use existing output styles and create new ones.

## Using Output Styles

To use an output style in Claude Code, simply add the `/output-style` command followed by the style name:

```
/output-style sprint-report
```

## Available Output Styles

### Current Implemented Styles

#### `sprint-report`
- **Purpose:** Sprint retrospectives and team reports
- **Best for:** Scrum masters, team leads, stakeholders
- **Format:** Structured retrospective with achievements, challenges, and next steps

#### `code-implementation`
- **Purpose:** Technical implementation with comprehensive documentation
- **Best for:** Developers, technical leads, code reviewers
- **Format:** Code with detailed explanations, architecture decisions, and usage examples

#### `technical-analysis`
- **Purpose:** Architecture decisions and technical investigations
- **Best for:** Solution architects, senior developers, technical decision-makers
- **Format:** In-depth analysis with pros/cons, recommendations, and implementation considerations

#### `star-agent-optimization`
- **Purpose:** Agent performance optimization and tuning
- **Best for:** AI/ML engineers, performance optimization teams
- **Format:** Performance metrics, optimization strategies, and implementation guidelines

## Creating Custom Output Styles

### JSON Configuration Format

Output styles are defined as JSON configuration files in the `.claude/output-styles/` directory. Each style includes:

```json
{
  "name": "style-name",
  "description": "Brief description of the style",
  "purpose": "What this style is used for",
  "target_audience": ["role1", "role2"],
  "format": {
    "structure": "Outline of the format",
    "tone": "professional|casual|technical",
    "verbosity": "brief|detailed|comprehensive",
    "sections": ["section1", "section2"]
  },
  "template": "Template or example output"
}
```

### Best Practices

1. **Clear Purpose:** Each style should have a specific, well-defined use case
2. **Consistent Structure:** Follow predictable formatting patterns
3. **Target Audience:** Consider who will read and use the output
4. **Appropriate Tone:** Match the communication style to the context
5. **Right Level of Detail:** Balance comprehensiveness with readability

## Community Contributions

### How to Suggest New Styles

1. **Use the GitHub Issue:** Comment on the community input issue with your suggestion
2. **Follow the Format:** Use the standardized suggestion template
3. **Provide Examples:** Include real-world use cases and sample output
4. **Get Community Feedback:** Engage with other contributors for refinement

### Suggestion Template

```
### Style Name: [descriptive-name]
**Purpose:** What this style would be used for
**Key Features:** 
- Specific formatting elements
- Tone and verbosity
- Required sections
**Use Cases:**
- When you would use this style
- Who would benefit
**Example Output:**
A brief example of what output would look like
```

### Implementation Process

Top-voted community suggestions will be:

1. **Reviewed by the team** for feasibility and alignment
2. **Implemented as JSON configurations** following our standard format
3. **Added to the output style library** for team use
4. **Documented with usage examples** in this guide
5. **Shared with the community** for broader adoption

## High-Priority Styles Needed

Based on team feedback, we particularly need styles for:

- **Bug Report Formatting** - Structured issue reporting with reproduction steps
- **Test Plan Templates** - Comprehensive test documentation
- **API Documentation** - OpenAPI/Swagger-style formatting
- **Security Audit Reports** - Vulnerability assessments and remediation
- **Performance Analysis** - Profiling and optimization reports

## Support and Feedback

For questions, suggestions, or feedback:
- Comment on the [Community Input Issue](https://github.com/norrisaftcc/the_algorithm/issues/4)
- Reach out to team members monitoring the issue
- Submit pull requests for documentation improvements

---

*This guide is living documentation that evolves with our team's needs and community contributions.*