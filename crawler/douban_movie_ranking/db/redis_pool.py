import redis
from config.setting import redis_info

pool = redis.BlockingConnectionPool(max_connections=50,
                                    timeout=10,
                                    host=redis_info["host"],
                                    port=redis_info["port"],
                                    password=redis_info["password"],
                                    decode_responses=True)

redis_client = redis.Redis(connection_pool=pool)
