# Architecture Decision Record: SQLite for Sprint Zero

**Date:** 2025-08-21  
**Status:** Proposed  
**Deciders:** Product Architect, Clive (Prompt Strategist)

## Context

Sprint Zero validation revealed dependencies on external services:
- Docker Desktop (not installed)
- PostgreSQL (not installed) 
- Redis (not installed)

These create unnecessary complexity for validating our toolset functionality.

## Decision

Replace external dependencies with SQLite for Sprint Zero:
- **SQLite** replaces PostgreSQL for data persistence
- **In-memory caching** replaces Redis
- **Node.js native** replaces Docker for initial validation

## Rationale

### Clive's Strategic Analysis
From a prompt engineering perspective, simpler systems produce more predictable outcomes:
1. **Reduced Variables**: Fewer external dependencies = fewer failure points
2. **Faster Iteration**: No service startup time = quicker validation cycles
3. **Portable Testing**: SQLite database is just a file = easy to reset/share
4. **Clear Prompts**: Simpler architecture = clearer agent instructions

### Product Architect's Confirmation
The architecture remains sound because:
1. **Prisma ORM abstracts database**: Switch from SQLite to PostgreSQL is configuration only
2. **Repository pattern intact**: Business logic doesn't know about storage
3. **Migration path clear**: When ready for production, swap providers
4. **YAGNI principle**: We don't need distributed caching for Sprint Zero

## Implementation

### Updated Prisma Configuration
```prisma
// For Sprint Zero
datasource db {
  provider = "sqlite"
  url      = "file:./dev.db"
}

// Future production (commented out)
// datasource db {
//   provider = "postgresql"
//   url      = env("DATABASE_URL")
// }
```

### In-Memory Cache Implementation
```typescript
// Simple cache for Sprint Zero
class InMemoryCache {
  private cache = new Map<string, any>()
  
  async get(key: string) { return this.cache.get(key) }
  async set(key: string, value: any) { this.cache.set(key, value) }
  async del(key: string) { this.cache.delete(key) }
}

// Future Redis implementation
// import Redis from 'ioredis'
// const cache = new Redis(process.env.REDIS_URL)
```

## Consequences

### Positive
- ✅ Zero external service dependencies
- ✅ Instant setup for new developers
- ✅ Validation script succeeds immediately
- ✅ Focus on tooling, not infrastructure
- ✅ Faster CI/CD pipeline (no service containers)

### Negative
- ⚠️ Will need migration when scaling
- ⚠️ No distributed caching testing
- ⚠️ SQLite limitations (no concurrent writes)

### Mitigation
- Keep PostgreSQL/Redis configuration commented in code
- Document migration path clearly
- Create feature flag for database provider
- Test PostgreSQL in Sprint One

## Validation Criteria

Sprint Zero succeeds if:
1. SQLite database creates and migrates
2. Data persists between runs
3. In-memory cache stores/retrieves
4. All tests pass with SQLite
5. CI/CD runs without external services

## Decision

**APPROVED** - Proceed with SQLite for Sprint Zero validation.

*"Simplicity is the ultimate sophistication in prompt engineering"* - Clive  
*"Build what you need today, architect for tomorrow"* - Product Architect