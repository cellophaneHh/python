import re

# def前面是abc
m = re.search('(?<=abc)(def)', 'abcdefabcdef')
print(m.group(1))

m = re.search(r'(?<=-)\w+', 'spam-egg')
print(m.group(0))

# (?(id/name)yes-pattern|no-pattern)会使第一个分组不见了
# m.group(1)获取为None
# 为什么？
reg_email = "(<)?(\w+@\w+(?:\.\w+)+)(?(1)>|$)"
s = "<user@host.com"
m = re.search(reg_email, s)
print(m.group(0))
print(m.group(1))

reg_str = "(a)(b)(c)"
s = "abchhhhh"
m = re.search(reg_str, s)
print(m.group(0), m.group(1), m.group(2), m.group(3))


