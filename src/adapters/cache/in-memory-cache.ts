/**
 * In-Memory Cache Adapter
 * Simple cache implementation for Sprint Zero validation
 * Will be replaced with Redis in production
 */

export interface CacheAdapter {
  get<T>(key: string): Promise<T | null>
  set<T>(key: string, value: T, ttl?: number): Promise<void>
  del(key: string): Promise<void>
  clear(): Promise<void>
  has(key: string): Promise<boolean>
}

export class InMemoryCache implements CacheAdapter {
  private cache = new Map<string, { value: any; expires?: number }>()

  async get<T>(key: string): Promise<T | null> {
    const item = this.cache.get(key)
    
    if (!item) {
      return null
    }

    // Check if expired
    if (item.expires && Date.now() > item.expires) {
      this.cache.delete(key)
      return null
    }

    return item.value as T
  }

  async set<T>(key: string, value: T, ttl?: number): Promise<void> {
    const item: { value: T; expires?: number } = { value }
    
    if (ttl) {
      item.expires = Date.now() + ttl * 1000
    }

    this.cache.set(key, item)
  }

  async del(key: string): Promise<void> {
    this.cache.delete(key)
  }

  async clear(): Promise<void> {
    this.cache.clear()
  }

  async has(key: string): Promise<boolean> {
    const item = this.cache.get(key)
    
    if (!item) {
      return false
    }

    // Check expiration
    if (item.expires && Date.now() > item.expires) {
      this.cache.delete(key)
      return false
    }

    return true
  }

  // Sprint Zero validation methods
  getSize(): number {
    return this.cache.size
  }

  async validate(): Promise<boolean> {
    try {
      // Test basic operations
      await this.set('test-key', 'test-value')
      const value = await this.get<string>('test-key')
      await this.del('test-key')
      
      return value === 'test-value'
    } catch {
      return false
    }
  }
}

// Export singleton for Sprint Zero
export const cache = new InMemoryCache()

/**
 * Future Redis implementation (commented for reference):
 * 
 * import Redis from 'ioredis'
 * 
 * export class RedisCache implements CacheAdapter {
 *   private client: Redis
 *   
 *   constructor(url: string) {
 *     this.client = new Redis(url)
 *   }
 *   
 *   async get<T>(key: string): Promise<T | null> {
 *     const value = await this.client.get(key)
 *     return value ? JSON.parse(value) : null
 *   }
 *   
 *   async set<T>(key: string, value: T, ttl?: number): Promise<void> {
 *     const serialized = JSON.stringify(value)
 *     if (ttl) {
 *       await this.client.setex(key, ttl, serialized)
 *     } else {
 *       await this.client.set(key, serialized)
 *     }
 *   }
 *   
 *   // ... other methods
 * }
 */