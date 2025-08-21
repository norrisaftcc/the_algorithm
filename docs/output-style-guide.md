# Claude Code Output Style Guide

## Overview

Output styles in Claude Code enable specialized formatting for different types of deliverables, increasing transparency and consistency across team outputs.

## Available Output Styles

### 1. Sprint Report (`sprint-report`)
**Purpose:** Sprint retrospectives, lessons learned, team reports  
**When to Use:** 
- End of sprint summaries
- Team performance reviews
- Stakeholder updates

**Command:**
```bash
# In Claude Code
/output-style:new sprint-report
```

**Key Features:**
- Executive summary
- Metrics tables
- Team attribution
- Actionable recommendations

### 2. Code Implementation (`code-implementation`)
**Purpose:** Technical implementation with comprehensive documentation  
**When to Use:**
- Writing new features
- Creating APIs
- Implementing algorithms

**Command:**
```bash
/output-style:new code-implementation
```

**Key Features:**
- Extensive inline documentation
- Test coverage included
- Error handling patterns
- Usage examples

### 3. Technical Analysis (`technical-analysis`)
**Purpose:** Architecture decisions, code reviews, investigations  
**When to Use:**
- Evaluating technology choices
- Performance analysis
- Security assessments

**Command:**
```bash
/output-style:new technical-analysis
```

**Key Features:**
- Systematic analysis
- Pros/cons comparison
- Performance benchmarks
- Evidence-based recommendations

### 4. Algorithm-Focused (`algorithm-focused`)
**Purpose:** Security-first development with PII protection  
**When to Use:**
- Grid visualizations
- Data processing
- Security-sensitive operations

**Key Features:**
- Mandatory PII checks
- Security gates
- Grid visualizations
- Progress indicators

## Creating Custom Output Styles

### Structure
```json
{
  "name": "Style Name",
  "description": "What this style is for",
  "guidelines": ["List of", "formatting rules"],
  "formatting": {
    "use_headers": true,
    "use_tables": true
  },
  "tone": {
    "style": "professional|technical|casual",
    "formality": "high|medium|low",
    "verbosity": "concise|balanced|detailed"
  }
}
```

### Location
Save custom styles to: `~/.claude/output-styles/[style-name].json`

## Workflow Examples

### Example 1: Sprint Reporting Workflow
```bash
# 1. Switch to report style
/output-style:new sprint-report

# 2. Generate sprint summary
"Create a sprint retrospective for Sprint Zero"

# 3. Output will be formatted as professional report
```

### Example 2: Code Review Workflow
```bash
# 1. Switch to analysis style
/output-style:new technical-analysis

# 2. Request code review
"Review the cache implementation for performance"

# 3. Receive structured analysis with benchmarks
```

### Example 3: Implementation Workflow
```bash
# 1. Switch to code style
/output-style:new code-implementation

# 2. Request implementation
"Implement user authentication module"

# 3. Get fully documented code with tests
```

## Benefits of Output Styles

### For Individual Contributors
- Consistent formatting
- Appropriate detail level
- Reduced cognitive load

### For Teams
- Standardized deliverables
- Clear communication
- Knowledge sharing

### For Stakeholders
- Professional reports
- Digestible summaries
- Actionable insights

## Best Practices

### 1. Match Style to Audience
- **Technical team:** code-implementation, technical-analysis
- **Management:** sprint-report
- **Security team:** algorithm-focused

### 2. Switch Styles Contextually
```bash
# Planning phase
/output-style:new technical-analysis

# Implementation phase
/output-style:new code-implementation

# Reporting phase
/output-style:new sprint-report
```

### 3. Combine Styles in Workflows
1. Analyze with `technical-analysis`
2. Implement with `code-implementation`
3. Report with `sprint-report`

## Style Selection Matrix

| Task Type | Recommended Style | Key Benefit |
|-----------|------------------|-------------|
| Sprint Planning | sprint-report | Structured goals |
| Feature Development | code-implementation | Complete documentation |
| Architecture Decision | technical-analysis | Systematic evaluation |
| Security Review | algorithm-focused | PII protection |
| Bug Investigation | technical-analysis | Root cause analysis |
| Team Updates | sprint-report | Clear metrics |
| API Design | code-implementation | Usage examples |
| Performance Tuning | technical-analysis | Benchmarks included |

## Tips for Custom Styles

### 1. Keep It Focused
Each style should serve one primary purpose well.

### 2. Include Examples
Add example patterns to guide formatting.

### 3. Test Iteratively
Refine styles based on actual usage.

### 4. Share with Team
Store custom styles in version control for consistency.

## Troubleshooting

### Style Not Loading
- Check JSON syntax
- Verify file location
- Restart Claude Code

### Inconsistent Output
- Ensure guidelines are specific
- Add more example patterns
- Check tone settings

### Wrong Style Active
```bash
# Check current style
/output-style

# Switch to different style
/output-style:new [style-name]
```

## Future Enhancements

### Planned Features
- Style inheritance
- Conditional formatting
- Template variables
- Export formats (PDF, HTML)

### Community Styles
Share your custom styles:
1. Create style JSON
2. Test thoroughly
3. Submit PR to team repository

## Conclusion

Output styles transform Claude Code from a coding assistant into a comprehensive development platform supporting the entire software lifecycle - from analysis through implementation to reporting.

---
*The Algorithm™ approves of structured communication*