'''
redis实现简单限流
'''
import redis
import time
import threading
import random
import log_handler


class RadisRateLimit:
    '''
    redis实现简单限流
    host: ip
    port: 端口
    password: 密码
    period: 时间间隔
    limit: 限制次数
    '''
    def __init__(self, host, port, password):
        self.host = host
        self.port = port
        self.password = password
        self.pool = redis.ConnectionPool(host=self.host,
                            port=self.port,
                            password=self.password,
                            decode_responses=True)
        self.client = redis.Redis(connection_pool=self.pool)

    def is_allow(self, user_id, action_key, period, max_count):
        '''
        判定是否允许
        '''
        key = "history:{}:{}".format(user_id, action_key)
        # 毫秒
        now_mill = int(time.time() * 1000)
        with self.client.pipeline() as pipe:
            pipe.zadd(key, now_mill, now_mill)
            pipe.zremrangebyscore(key, 0, now_mill - period * 1000)
            pipe.zcard(key)

            # 设置period超时，防止冷用户
            pipe.expire(key, period + 1)

            _, _, count, _ = pipe.execute()
        return count < max_count


log = log_handler.LogHandler('rate_limit')


def test_task():
    '''测试任务'''
    rl = RadisRateLimit('127.0.0.1', 6379, 'zh2683')
    user_id = "test"
    action_key = "search"
    period = 10
    max_count = 4000
    thread_name = threading.current_thread().getName()
    while True:
        if rl.is_allow(user_id, action_key, period, max_count):
            log.info('{} allow {}'.format(str(time.time()), thread_name))
        else:
            log.warn('{} not allow {}'.format(str(time.time()), thread_name))
        time.sleep(random.uniform(0, 0.1))


threads = []
for i in range(8):
    t = threading.Thread(target=test_task,
                         name='thread-{}'.format(str(i)))
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()
