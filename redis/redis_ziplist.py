import redis

client = redis.StrictRedis(host='127.0.0.1',
                           port=6379,
                           password='zh2683',
                           decode_responses=True)

# 键数量到一定长度时存储结构会变化
client.delete('world')

for i in range(512):
    client.hset('world', str(i), str(i))

print('')
print(client.object('encoding', 'world'))
client.hset('world', '512', '512')
print(client.object('encoding', 'world'))


# value到一定长度，存储结构会变化
client.delete('world')

for i in range(64):
    client.hset('world', str(i), '0' * (i + 1))

print(client.object('encoding', 'world'))
client.hset('world', '512', '0' * 65)
print(client.object('encoding', 'world'))
