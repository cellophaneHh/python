"""
获取json数据
"""
import requests

# 内置json解码器

r = requests.get('https://api.github.com/events')
# 打印结果(响应太大，会造成控制台卡顿)
# print(r.json())
print(r.raise_for_status())
print(r.status_code)

if r.status_code == 200 and r.raise_for_status() == None:
    print('下载成功.')
else:
    print('下载失败.')
