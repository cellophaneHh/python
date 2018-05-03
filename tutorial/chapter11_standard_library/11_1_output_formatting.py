"""
输出格式化
reprlib
pprint
textwrap
locale
"""

import reprlib

# 不会全部展示出来，省略了一部分
print(reprlib.repr(set('supercalifragilisticexpialidocious')))



import pprint

t = [[[['black','cyan'], 'white', ['green', 'red']], [['magenta', 'yellow'], 'blue']]]
# 换行输出，结果更清晰
pprint.pprint(t, width = 30)

import textwrap

doc = """The wrap() method is just like file() except that it returns a list of strings instead of one big string with newlines to separate the wrapped lines."""

# fill 返回整个按宽度换行后的字符串
print(textwrap.fill(doc, width=40))
print("---------------------")
# wrap()按宽度将整个字符串分割为一个list
print(textwrap.wrap(doc, width=40))


print("================locale===================")
import locale

# l = locale.setlocale(locale.LC_ALL, 'English_United States.1252')
# print(l)

conv = locale.localeconv()
print(conv)

x = 1234567.8
l = locale.format('%d', x, grouping=True)
print(l)
