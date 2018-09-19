import redis_pool
import redis

redis_client = redis.Redis(connection_pool=redis_pool.pool)

name = 'zhangheng'
redis_client.execute_command('bf.add codehole {}'.format(name))
res = redis_client.execute_command('bf.exists codehole {}'.format(name))


