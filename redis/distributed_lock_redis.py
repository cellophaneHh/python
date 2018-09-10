import redis_pool
import redis

redis_client = redis.Redis(redis_pool.block_pool)

