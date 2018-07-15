import collections


def default_factory():
    return 'default value'


# defaultdict给不存在的key一个默认值
d = collections.defaultdict(default_factory, foo='bar')

print('d:', d)
print('foo =>', d['foo'])
# 不存在的取默认值
print('bar =>', d['bar'])


d = {'foo': 'bar'}

print(d['foo'])
# 默认字典不存在的key获取会报错
missing_key = 'bar'
try:
    print(d[missing_key])
except KeyError as e:
    print('{}不存在'.format(missing_key))

# 默认字典实现默认值需要调用setdefault设置某个键的默认值
d.setdefault('bar', 'bar')
print(d['bar'])
