'''
修改目录中后缀为SUFFIX_BEFORE的文件的后缀为SUFFIX_AFTER
'''

import os

path = 'D:\\Documents\\Downloads'
SUFFIX_BEFORE = '.docx'
SUFFIX_AFTER = '.doc'

files = os.listdir(path)

list_file = filter(lambda f: f.endswith(SUFFIX_BEFORE), files)
for file in list_file:
    file_name = os.path.splitext(file)[0]
    os.rename(os.path.join(path, file), os.path.join(path, file_name + SUFFIX_AFTER))