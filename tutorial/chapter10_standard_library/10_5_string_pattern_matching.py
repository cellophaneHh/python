"""
字符匹配
re模块提供了正则表达式工具
"""

import re

pa = re.compile(r'\bf[a-z]*')
print(type(pa))
# print(dir(pa))

l = pa.findall('which foot or hand fell fastest')
print(l)


s = re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
print(s)

ll = 'tea for too'.replace('too', 'two')
print(ll)

