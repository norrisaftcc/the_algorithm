import { beforeAll, afterAll, beforeEach, afterEach } from 'vitest'

// Mock environment variables for testing
process.env.NODE_ENV = 'test'
process.env.DATABASE_URL = 'postgresql://test:test@localhost:5432/test_db'
process.env.REDIS_URL = 'redis://localhost:6379/1'
process.env.JWT_SECRET = 'test-jwt-secret-for-testing-only-32-chars'
process.env.ENCRYPTION_KEY = 'test-encryption-key-for-testing-32-chars'

// Global test setup
beforeAll(async () => {
  console.log('🧪 Starting test suite...')
})

afterAll(async () => {
  console.log('✅ Test suite completed')
})

// Reset mocks between tests
beforeEach(() => {
  // Clear all mocks
})

afterEach(() => {
  // Clean up after each test
})