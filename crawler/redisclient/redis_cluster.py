'''
redis集群
'''
from rediscluster import StrictRedisCluster


nodes = [
    dict(host='127.0.0.1', port=7000),
    dict(host='127.0.0.1', port=7001),
    dict(host='127.0.0.1', port=7002),
    dict(host='127.0.0.1', port=7003),
    dict(host='127.0.0.1', port=7004),
    dict(host='127.0.0.1', port=7005),
]
password = 'foobared'

redis_cluster_client = StrictRedisCluster(host='127.0.0.1',
                                          port='7000',
                                          startup_nodes=nodes,
                                          max_connections=100,
                                          max_connections_per_node=20,
                                          password=password,
                                          decode_responses=True)

# redis_cluster_client.execute_command('bf.add', 'codehole', '1')
# print(redis_cluster_client.execute_command('bf.exists', 'codehole', '2'))
