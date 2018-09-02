import redis
from redis_pool import pool


r = redis.Redis(connection_pool=pool)

l = ['1', '2']

r.sadd('nameset', tuple(l))

print(r.scard('nameset'))
print(r.sscan('nameset', 0))
