"""
爬图片
"""
import requests
import os
import re
from PIL import Image
import sys


# 源码目录
source_dir = './html'
img_dir = './img'
if not os.path.exists(source_dir):
    print('新建源码目录:' + source_dir)
    os.makedirs(source_dir)

if not os.path.exists(img_dir):
    print('新建图片目录:' + img_dir)
    os.makedirs(img_dir)

url = 'http://www.17786.com/7939_1.html'
# 文件
l_tmp = url.split('/')
file_path = source_dir + os.path.sep + l_tmp[len(l_tmp) - 1]
print(file_path)

try:
    r = requests.get(url)
    with open(file_path, 'w+') as file:
        file.write(r.text)
except requests.RequestException as e:
    print('下载异常....')
    sys.exit(0)

# 获取源码
source = r.text
reg_img = '<img class="IMG_show" src="(.*?)" alt="(.*?)" />'
m = re.search(reg_img, source)

groups = m.groups()
if groups:
    img_url = groups[0]
    file_suffix = os.path.splitext(img_url)[1]
    file_name = os.path.split(img_url)[1]
    try:
        print('图片链接:' + img_url)
        img_path = img_dir + os.path.sep + file_name
        print('保存路径: ' + img_path)
        img_response = requests.get(img_url)
        if img_response.status_code == 200:
            with open(img_path, 'wb') as img:
                img.write(img_response.content)
        print('保存成功')
    except requests.RequestException as e:
        print('保存失败..')
else:
    print('没有匹配到链接')

