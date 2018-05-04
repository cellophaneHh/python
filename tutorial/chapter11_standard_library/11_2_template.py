"""
模板
Template
"""
import pprint
from string import Template

# 以$开头的标识符作为占位符，$$穿件一个单独的$
t = Template('${village}folk send $$10 to $cause.')
s = t.substitute(village='Nottingham', cause='the ditch fund')
print(s)
# key没有提供完整时会报错
# s = t.substitute(village='s')

# safe_substitute() 在没有提供完整key时不会报错，会保留没有提供的key
t = Template('Return the $item to $owner')
d = dict(item='unladen swallow')
s = t.safe_substitute(d)
print(s)
pprint.pprint(s)

# 模板子类可以制定自定义分隔符

import time, os.path

photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']

class BatchRename(Template):
    delimiter = '%'

fmt = input("Enter rename style (%d-date %n-seqnum %f-format): ")

t = BatchRename(fmt)
date = time.strftime('%d%b%y')
date = time.strftime('%Y/%m/%d')
print(type(date))
print(date)
for i, filename in enumerate(photofiles):
    base, ext = os.path.splitext(filename)
    newname = t.substitute(d=date, n=i, f=ext)
    print('{0} --> {1}'.format(filename, newname))
