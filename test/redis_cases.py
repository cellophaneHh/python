import redis

# 连接redis, decode_response需要设置为True，否则返回二进制数据
r = redis.Redis(host='127.0.0.1',
                port=6379,
                password='zh2683',
                db=0,
                socket_timeout=10,
                decode_responses=True)
r.set('name', '张恒')
# print(r.get('name').decode(encoding='utf-8'))
print(r.get('name'))
print(r.dbsize())
