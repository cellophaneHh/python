import redis
import zlib

pool = redis.ConnectionPool(host='127.0.0.1',
                            port=6379,
                            password='zh2683',
                            max_connections=20,
                            decode_responses=True)

redis_client = redis.Redis(connection_pool=pool)

# result = redis_client.execute_command("bf.reserve {} {} {}".format(
#     "newFilter", 0.001, 100000000))
# print(result)

# result = redis_client.execute_command("bf.add {} {}".format("newFilter", "张恒"))
# print(result)

# result = redis_client.execute_command("bf.exists {} {}".format(
#     "newFilter", "foo"))
# print(result)

# result = redis_client.execute_command("bf.exists {} {}".format(
#     "newFilter", "foo1"))
# print(result)
