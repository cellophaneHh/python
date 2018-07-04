"""
正则re
"""
import re

m = re.search('(?P<prefix>name)(.*?)((?P=prefix))', 'nameasdfname')
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.groups())

