import re

rl = re.split('\W+', 'Words, Words, Words.')
print(rl)
# 这个。。。
rl = re.split('(\W+)', 'Words, Words, Words.')
print(rl)
# 不区分大小写
rl = re.split('(?i)[a-f]', '0a3B9')
print(rl)
