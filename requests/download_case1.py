import os
import requests

res = requests.get('http://www.baidu.com/')

source_file = './sources/baidu.html'

dir_path, file_name = os.path.split(source_file)

if not os.path.exists(dir_path):
    os.makedirs(dir_path)

if not os.path.exists(source_file):
    with open(source_file, 'w+') as source:
        pass

# 写入下载的源码
with open(source_file, 'w') as source:
    source.write(res.text)
