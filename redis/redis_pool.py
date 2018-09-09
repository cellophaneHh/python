import redis

pool = redis.ConnectionPool(host='127.0.0.1',
                            port=6379,
                            password='zh2683',
                            max_connections=20,
                            decode_responses=True)

block_pool = redis.BlockingConnectionPool(host='127.0.0.1',
                                          port=6379,
                                          password='zh2683',
                                          decode_responses=True)


