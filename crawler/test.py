import os
import re


print(os.path.sep)

url = 'http://www.17786.com/7939_1.jpg'

l = list(url.split('/'))

print(l[len(l) - 1])

img_url = "http://img.sc601.com/photo_files/news/20160614/e1bf0e1d-2e99-44ba-bb54-1c0673690fd8.jpg"
print(os.path.splitext(img_url))
print(os.path.split(img_url))

print('asdf{0}, {1}'.format(1, 0))

source_html = "imgasdfasdfimg"
imgs = re.findall(r'(img)', source_html)
for img in imgs:
    print('-' + img)
