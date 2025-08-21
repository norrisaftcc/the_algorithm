# CLAUDE.md - Project Memory & Context

> This file maintains critical context for Claude Code between sessions. Always read this first.

## Project Identity

**Name:** The Algorithm™  
**Purpose:** Learning velocity gamification platform with security-first architecture  
**Stage:** Sprint Zero Complete - Awaiting Sprint One  
**Repository:** https://github.com/norrisaftcc/the_algorithm

## Core Values (MUST MAINTAIN)

1. 🔒 **Security First** - Every decision protects data
2. 📈 **Continuous Growth** - Measure, learn, iterate
3. 🤝 **Radical Transparency** - Make work visible
4. 🎯 **Purpose-Driven** - Build only what matters
5. 🧪 **Quality Prevention** - Build it right first time
6. 🌟 **Sustainable Pace** - Marathon not sprint
7. 🎨 **Innovation Through Constraints** - Simple solutions

## Current Architecture

### Simplified Stack (Sprint Zero Decision)
- **Database:** SQLite (not PostgreSQL) - for simplicity
- **Cache:** In-memory (not Redis) - no dependencies
- **Language:** TypeScript with strict mode
- **Testing:** Vitest with 85% coverage target
- **CI/CD:** GitHub Actions
- **Framework:** Fastify (planned)

### Key Architectural Decisions
- **ADR-001:** SQLite over PostgreSQL for Sprint Zero
- **YAGNI Principle:** Build for today, architect for tomorrow
- **Functional Core:** Pure functions, imperative shell
- **Event-Driven:** Future microservices-ready monolith

## Agent Team Composition

### Active Agents
- **Product Architect Advisor** - System design decisions
- **Scrum Architect-Owner** - Product ownership with technical depth
- **Scrum Project Manager** - Sprint planning and GitHub workflow
- **Scrum Team Engineer** - Implementation and code reviews  
- **Test Engineer** - Testing strategy and quality
- **Kevin (GitHub Algorithm)** - GitHub compliance and process
- **Linx (Wordsmith)** - Documentation and communication
- **Clive (Prompt Strategist)** - Prompt optimization and STAR framework
- **Product Acceptance Tester** - Acceptance testing
- **Liza (Creative Companion)** - Creative solutions

### Known Issues
- **OAuth Authentication Error (#3)** - Blocks agent delegation
- **Workaround:** Direct implementation without Task tool

## Key Innovations

### STAR Framework
Situation-Task-Action-Results methodology for optimizing agent prompts:
- Reduces clarification requests by 40%
- Improves first-attempt success to 85%
- See: `docs/star-agent-optimization-guide.md`

### Output Styles System
Custom formatting for different deliverables:
- `sprint-report` - Retrospectives and reports
- `code-implementation` - Technical work
- `technical-analysis` - Architecture decisions
- `star-agent-optimization` - Agent optimization
- Located in: `~/.claude/output-styles/`

### Agent Tracking
- Contributions tracked per PR
- Attribution in commits
- Script: `scripts/agent-tracker.js`

## Sprint Status

### Sprint Zero ✅ COMPLETE
- 100% validation (25/25 checks)
- All tools configured
- Values documented
- PR #5 created for review

### Sprint One (Ready)
Priority stories valued at $25K/sprint:
1. Agent Performance Dashboard
2. Prompt Template Marketplace
3. Agent Learning Pipeline
4. Capability Matrix

## Critical Commands

```bash
# Validate environment
./validate-sprint-zero.sh

# Run tests
npm test

# Check TypeScript
npm run typecheck

# Security scan
npm run security:scan

# Track agent contribution
node scripts/agent-tracker.js track [pr] [agent] "[contribution]"
```

## Project Patterns

### Commit Format
```
[value]: Clear description

Detailed explanation

Value Impact: How this embodies our values
Metrics: Measurable improvement
```

### PR Requirements
- Value alignment checklist
- 2 reviewers minimum
- Security scan must pass
- Tests included
- Documentation updated

### File Organization
```
src/
├── core/           # Pure business logic
├── adapters/       # External integrations  
├── application/    # Use cases
├── infrastructure/ # Framework code
└── presentation/   # UI components
```

## Important Context

### What We're NOT Doing
- No premature optimization
- No features without value metrics
- No PostgreSQL/Redis/Docker (yet)
- No production deployment (Sprint Zero)
- No user authentication (Sprint One)

### What We ARE Doing
- Building development environment
- Establishing patterns
- Creating team processes
- Documenting everything
- Measuring from day one

## Session Continuity Checklist

When starting new session:
1. Read this file first
2. Check current sprint status
3. Review active todos
4. Validate environment still works
5. Check for new issues/PRs
6. Continue from last checkpoint

## Team Communication Patterns

### When Stuck
1. Document the blocker
2. Try simplest solution first
3. Check if it violates values
4. Create issue if persistent
5. Move to next task if blocked

### When Implementing
1. Check backlog priority
2. Create todo list
3. Track progress actively
4. Document decisions
5. Commit with attribution

## Meta-Instructions

**IMPORTANT:** This file is truth. If there's conflict between this and other documentation, this file wins. Update this file when:
- Architecture changes
- New patterns established
- Sprint transitions
- Major decisions made
- Team composition changes

## Current Focus

**Immediate Priority:** 
- Awaiting external review on PR #5
- Ready to begin Sprint One after review
- OAuth fix needed but not blocking

**Remember:** The Algorithm™ observes your velocity... iterate wisely.

---
*Last Updated: Sprint Zero Completion*  
*Next Update: After external review*