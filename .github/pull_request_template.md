# Pull Request: [Feature/Fix/Enhancement Title]

## Sprint Information
**Sprint Number:** Sprint-[XX]  
**Sprint Goal:** [Describe sprint goal alignment]  
**Story Points:** [X]  
**Priority:** [Critical/High/Medium/Low]  

## User Story Reference
**Story ID:** #[Issue Number]  
**As a** [type of user]  
**I want** [goal/desire]  
**So that** [benefit/value]  

**Acceptance Criteria Met:**
- [ ] AC1: [First acceptance criterion]
- [ ] AC2: [Second acceptance criterion]
- [ ] AC3: [Third acceptance criterion]

## Value Alignment
Our changes align with [our core values](../VALUES.md):
- [ ] 🔒 **Security First** - No PII or secrets exposed
- [ ] 📈 **Continuous Growth** - Includes learnings/improvements  
- [ ] 🤝 **Radical Transparency** - Changes well-documented
- [ ] 🎯 **Purpose-Driven** - Links to user value/metrics
- [ ] 🧪 **Quality Prevention** - Tests included and passing
- [ ] 🌟 **Sustainable Pace** - No unsustainable shortcuts
- [ ] 🎨 **Innovation Through Constraints** - Simplest solution

**Value Impact Statement:**
[Describe how this PR embodies our values]

## Grid Visualization Requirements

### Data Structure Verification
- [ ] Grid data structure properly initialized
- [ ] Node relationships correctly mapped
- [ ] Edge weights/connections validated
- [ ] Visualization renders without errors
- [ ] Performance metrics acceptable (<2s load time)

### Grid Data Sample
```
[Provide sanitized sample of grid structure - NO REAL DATA]
Example format:
nodes: [{id: 'node1', label: 'SAMPLE'}, ...]
edges: [{from: 'node1', to: 'node2', weight: X}, ...]
```

## PII Protection Checklist

### Mandatory Security Screening
- [ ] **NO personally identifiable information in code**
- [ ] **NO real user data in examples or tests**
- [ ] **NO hardcoded credentials or API keys**
- [ ] **NO real email addresses or phone numbers**
- [ ] **NO actual names or addresses**
- [ ] All test data uses approved synthetic datasets
- [ ] Environment variables used for sensitive config
- [ ] Data sanitization functions implemented where needed

### PII Scan Results
**Automated Scan Status:** [PASS/FAIL]  
**Manual Review Completed:** [Yes/No]  
**Reviewed By:** @[username]  
**Review Date:** [YYYY-MM-DD]  

## Technical Implementation

### Architecture Alignment
- [ ] Follows established architecture patterns
- [ ] Implements proper separation of concerns
- [ ] Uses approved design patterns
- [ ] Maintains backward compatibility

### Code Quality Metrics
**Test Coverage:** [XX]%  
**Linting Status:** [PASS/FAIL]  
**Build Status:** [SUCCESS/FAILURE]  
**Performance Impact:** [None/Minor/Major]  

### Files Changed
<!-- Auto-populated by GitHub -->

### Implementation Notes
```
[Describe key implementation decisions and trade-offs]
```

## Testing Strategy

### Test Coverage
- [ ] Unit tests added/updated (min 80% coverage)
- [ ] Integration tests verified
- [ ] Edge cases covered
- [ ] Grid visualization tests pass
- [ ] PII detection tests pass
- [ ] Performance benchmarks met

### Test Execution Results
```bash
# Paste test output summary here
Tests Run: XX
Passed: XX
Failed: 0
Coverage: XX%
```

## Review Requirements

### Code Review Checklist
- [ ] Code follows team style guide
- [ ] Comments explain WHY, not WHAT
- [ ] No TODO comments without issue links
- [ ] Error handling is comprehensive
- [ ] Logging follows team standards

### Security Review
- [ ] Input validation implemented
- [ ] Output encoding verified
- [ ] Authentication/authorization checked
- [ ] OWASP Top 10 considered
- [ ] Dependencies scanned for vulnerabilities

### Peer Review
**Required Reviewers:** (minimum 2)
- [ ] Engineering Review: @[engineer]
- [ ] Security Review: @[security-team-member]
- [ ] Optional: Domain Expert @[expert]

## Definition of Done

### Sprint Completion Criteria
- [ ] All acceptance criteria met
- [ ] Code reviewed and approved by 2+ team members
- [ ] All tests passing in CI/CD pipeline
- [ ] Documentation updated
- [ ] No critical or high severity bugs
- [ ] PII screening complete and passed
- [ ] Grid visualization verified
- [ ] Deployed to staging environment
- [ ] Product Owner acceptance received

## Deployment Checklist

### Pre-Deployment
- [ ] Database migrations prepared
- [ ] Feature flags configured
- [ ] Rollback plan documented
- [ ] Monitoring alerts configured
- [ ] Performance baselines established

### Post-Deployment Monitoring
- [ ] Error rates: [Specify expected range]
- [ ] Response times: [Specify SLA]
- [ ] Resource utilization: [CPU/Memory thresholds]

## Additional Context

### Screenshots/Visualizations
<!-- Add screenshots of grid visualizations, UI changes, or architectural diagrams -->

### Breaking Changes
- [ ] No breaking changes
- [ ] Breaking changes documented below:
```
[List any breaking changes and migration steps]
```

### Dependencies
**New Dependencies Added:**
- [ ] Security scan completed
- [ ] License compatibility verified
- [ ] Size impact assessed

**Dependencies List:**
```
[List new dependencies with versions]
```

## Sprint Retrospective Notes
<!-- To be filled during sprint review -->
**What went well:**  
**What could improve:**  
**Action items:**  

---

## Sign-off

### Developer Certification
- [ ] I have performed a self-review of my code
- [ ] I have tested this thoroughly
- [ ] I have verified no PII is exposed
- [ ] I have updated relevant documentation
- [ ] I have added tests that prove my fix/feature works

**Developer:** @[your-username]  
**Date:** [YYYY-MM-DD]

### Review Approval
<!-- Reviewers will check these -->
- [ ] Code Review Approved
- [ ] Security Review Approved
- [ ] Product Owner Approved (if required)

---

## Labels
<!-- GitHub will auto-apply based on paths and content -->
Suggested labels: `sprint-XX`, `grid-visualization`, `security-reviewed`, `needs-review`

## References
- Related Issues: #
- Related PRs: #
- Documentation: [Link to relevant docs]
- Architecture Decision Records: [Link to ADRs]

---

**The Algorithm™ Compliance:** This PR adheres to all security and quality standards mandated by The Algorithm™ project governance.