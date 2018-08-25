'''
采集颜色名对应的rgb值
'''
import requests
from lxml import etree
import json

url = 'http://tool.oschina.net/commons?type=3'

r = requests.get(url)

html = etree.HTML(r.text)
colornames = html.xpath('//table/tr/td[position() = 2 or position() = 6]/text()')
rgbvalues = html.xpath('//table/tr/td[position() = 3 or position() = 7]/text()')

for index, rgb in enumerate(rgbvalues):
    print(colornames[index], rgb)

color = {}
for index, colorname in enumerate(colornames):
    color[colorname] = rgbvalues[index]

with open('colorname.json', 'w') as f:
    json.dump(color, f, indent=4)

print('finished...')
