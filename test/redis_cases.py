import redis
import zlib

# 连接redis, decode_response需要设置为True，否则返回二进制数据
r = redis.Redis(host='127.0.0.1',
                port=6379,
                password='zh2683',
                db=0,
                socket_timeout=10,
                decode_responses=True)

s = "asdfasdfasdf"
result = zlib.compress(s.encode(encoding='utf-8'), level=6)
r.set('asdf', result)

print(r.get('asdf'))
if r.exists('asdf'):
    r.delete('asdf')
