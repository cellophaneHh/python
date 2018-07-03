"""
获取原始响应数据
r.raw
"""
import requests

r = requests.get('https://api.github.com/events', stream=True)

print(r.raw)
# print(r.raw.read(10))

# 响应写文件
with open('./sources/res_raw', 'wb') as fd:
    for chunk in r.iter_content(1024):
        fd.write(chunk)
    print('finished')
