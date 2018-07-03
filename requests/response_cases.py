import requests
from PIL import Image
from io import BytesIO

r = requests.get('https://api.github.com/events')
# print(r.text)
print(r.encoding)


r = requests.get('http://www.beautylegmm.com/photo/beautyleg/2018/1626/beautyleg-1626-0001.jpg')
i = Image.open(BytesIO(r.content))

i.save('./sources/0001.jpg')

print('finished.')
