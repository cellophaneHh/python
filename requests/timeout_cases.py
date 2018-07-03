"""
请求超时设置
"""
import requests

requests.get('http://github.com', timeout=0.01)
