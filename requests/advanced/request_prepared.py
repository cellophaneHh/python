"""
准备的请求
"""

from requests import Request, Session

url = 'http://httpbin.org/headers'
data = {'name': 'zh'}
headers = {'x-test': 'true'}

s = Session()
req = Request("GET", url,
              data=data,
              headers=headers)
# 获得一个PreparedRequest请求
# prepped = req.prepare() # 不能存储Session级别的状态
prepped = s.prepare_request(req) # 此种方式可以存储session级别的状态

stream = None
verify = None
proxies = None
cert = None
timeout = None
resp = s.send(prepped,
              stream=stream,
              verify=verify,
              proxies=proxies,
              cert=cert,
              timeout=timeout)
print(resp.stauts_code)
