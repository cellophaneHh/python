'''
采集颜色名对应的rgb值
'''
import requests
from lxml import etree
import json

url = 'http://tool.oschina.net/commons?type=3'

r = requests.get(url)

html = etree.HTML(r.text)
colorname1 = html.xpath('//table/tr/td[2]/text()')
rgbvalue1 = html.xpath('//table/tr/td[3]/text()')
colorname2 = html.xpath('//table/tr/td[6]/text()')
rgbvalue2 = html.xpath('//table/tr/td[7]/text()')

colorname1.extend(colorname2)
rgbvalue1.extend(rgbvalue2)

color = {}
for i in range(0, len(colorname1)):
    color[colorname1[i]] = rgbvalue1[1]

with open('colorname.json', 'w') as f:
    json.dump(color, f, indent=4)

print('finished...')
