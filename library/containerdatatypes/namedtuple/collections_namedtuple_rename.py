'''
rename参数会自动将无效参数名替换
替换规则好魔性啊，不统一。。。
'''
import collections

with_class = collections.namedtuple('Person', 'name class age', rename=True)
print(with_class._fields)

two_ages = collections.namedtuple('Person', 'name age ages', rename=True)
# 额，这个居然加了s
print(two_ages._fields)
