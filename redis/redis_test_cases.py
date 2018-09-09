import redis_pool
import redis


redis_client = redis.Redis(connection_pool=redis_pool.pool)

print(redis_client.get('my_name'))
for i in range(40):
    redis_client.set(str(i), str(i))

scan_result = redis_client.scan(0)
print(scan_result[1])
while scan_result[0] != 0:
    print('=========')
    scan_result = redis_client.scan(scan_result[0])
    print(scan_result[1])
