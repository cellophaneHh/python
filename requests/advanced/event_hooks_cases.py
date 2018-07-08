"""
事件钩子
response中可以挂一个钩子，请求完成生成响应时会执行这个钩子
"""
import requests


def print_url(r, *args, **kwargs):
    print(r.url, r.status_code)


hooks = dict(response=print_url)
requests.get('http://httpbin.org', hooks=hooks)
