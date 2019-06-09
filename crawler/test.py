from redisclient.redis_pool import redis_client
import time
import random

result = redis_client.sscan("test_sscan", 0, count=10)
while True:
    a = random.randint(0, 1000)
    print("a: {}".format(a))
    redis_client.sadd("test_sscan", a)
    print(result)
    result = redis_client.sscan("test_sscan", result[0], count=10)
    if result[0] == 0:
        result = redis_client.sscan("test_sscan", 0, count=10)
    time.sleep(5)
