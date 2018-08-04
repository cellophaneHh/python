import redis
from redis_pool import pool


r = redis.Redis(connection_pool=pool)

r.sadd('nameset', 'zhangheng')
name_seq = ['1', '3', '5', '7']

print(r.sismember('nameset', 'zhangheng'))
