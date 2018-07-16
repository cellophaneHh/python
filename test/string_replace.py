import re

str_info = 'abcdefgabcedaaa'

print(str_info.replace('a', 'A', 2))
print(str_info)
print()
# sub返回替换后的字符串
print(re.sub('a', 'A', str_info, 2))
print(str_info)

# subn返回一个元组，第一个元素为替换后的字符串，第二个元素为替换的次数
str_info = 'abcdefgabcedaaa'
print(re.subn('a', 'A', str_info, 2))
