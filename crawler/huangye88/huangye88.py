# -*- coding:utf-8 -*-
'''
黄页88网
'''
import typing
import requests
# from lxml import etree
# import config


class HuangYe88:
    def __init__(self):
        self.url = "http://b2b.huangye88.com/qiye1085519/company_detail.html"

    def downLoad(self):
        res = requests.get(self.url)
        res.encoding = 'utf-8'
        if res.status_code == 200:
            html = res.text
            with open('./qiye.html', 'w', encoding='utf-8') as file:
                file.write(html)
            return html
        else:
            raise Exception('请求失败, {}'.format(res.status_code))


hy88 = HuangYe88()
print(hy88.downLoad())
