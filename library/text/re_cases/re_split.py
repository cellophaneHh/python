import re

rl = re.split('\W+', 'Words, Words, Words.')
print(rl)
# 这个。。。
rl = re.split('(\W+)', 'Words, Words, Words.')
print(rl)
# 不区分大小写
rl = re.split('(?i)[a-f]', '0a3B9')
print(rl)

# 字符串替换
# 作用: 将输入的字符串input_str中按pattern匹配到的，替换为replacement
input_str = 'hello crifan, nihao crifan'
replaced_str = re.sub('hello (?P<name>\w+), nihao (?P=name)', "\g<name>",
                            input_str)
print(replaced_str)
# 替换所有连续的数字串
print(re.sub('\d+', '-', 'asdf8asd99f'))
