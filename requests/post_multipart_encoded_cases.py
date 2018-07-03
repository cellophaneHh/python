"""
上传一个文件
"""
import requests

url = 'http://httpbin.org/post'

files = {'file': open('./download_case1.py', 'rb')}

r = requests.post(url, files=files)
print(r.text)

# 显示的设置文件名、文件类型和请求头

files = {'file': ('zh2683.txt', open('./download_case1.py', 'rb'), 'application/txt', {'Expires': '0'})}

r = requests.post(url, files=files)
print(r.text)

# 可以发送作为文件来接收的字符串

files = {'file': ('report.csv', 'some,data,to,send\nanother,row,to,send\n')}
r = requests.post(url, files=files)
print(r.text)
