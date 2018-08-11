import os
import requests


proxies = {
    'http': 'http://124.235.208.252:443',
    'https': 'http://124.235.208.252:443'
}

res = requests.get(url='http://www.baidu.com/', proxies=proxies)

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

print('finished...')
