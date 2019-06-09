import redis

pool = redis.ConnectionPool(host='127.0.0.1',
                            port=6379,
                            password='zh2683',
                            max_connections=20,
                            decode_responses=True)

redis_client = redis.Redis(connection_pool=pool)
