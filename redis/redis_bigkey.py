import redis
import time

client = redis.StrictRedis(host='127.0.0.1',
                           port=6379,
                           password='zh2683',
                           decode_responses=True)

# 大key处理
client.delete('bigkey')

pipe = client.pipeline()
for i in range(100000000):
    pipe.sadd('bigkey', i)
    if i % 10000 == 0:
        pipe.execute()

print('finished')

client.delete('bigkey')

print('开始加入元素')
print(time.time())
client.sadd('bigkey', '1')
print(time.time())
