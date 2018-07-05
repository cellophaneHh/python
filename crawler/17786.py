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

def init():
    if not os.path.exists(source_dir):
        print('新建源码目录:' + source_dir)
        os.makedirs(source_dir)

    if not os.path.exists(img_dir):
        print('新建图片目录:' + img_dir)
        os.makedirs(img_dir)


def download_html(url):
    """根据url下载网页源码文件"""
    url = 'http://www.17786.com/7939_1.html'
    l_tmp = url.split('/')
    file_path = source_dir + os.path.sep + l_tmp[len(l_tmp) - 1]
    print("源码保存路径: {}".format(file_path))
    try:
        r = requests.get(url)
        # 源码文件备份
        with open(file_path, 'w+') as file:
            file.write(r.text)
        return r.text
    except requests.RequestException as e:
        print('下载源码异常: {}'.format(url))


def get_img_urls(html_source):
    """
    根据源码提取图片链接
    :return 存放图片链接的可迭代类型
    """
    # 获取源码
    source = download_html("")
    # 提取图片url的正则
    reg_img = '<img class="IMG_show" src="(.*?)" alt=".*?" />'
    return re.findall(reg_img, source)

def handle_img_url(img_urls):
    """
    处理所有获取到的url
    """
    if img_urls:
        for img_url in img_urls:
            try:
                print('开始下载: {0}'.format(img_url))
                download_and_save_img(img_url)
            except Exception as e:
                print("下载失败: {}".format(img_url))



def download_and_save_img(img_url):
    """
    根据链接下载病保存图片
    """
    file_suffix = os.path.splitext(img_url)[1]
    file_name = os.path.split(img_url)[1]
    try:
        img_path = img_dir + os.path.sep + file_name
        img_response = requests.get(img_url)
        if img_response.status_code == 200:
            with open(img_path, 'wb') as img:
                img.write(img_response.content)
        print('保存成功:{0}, {1}'.format(file_name, img_url))
    except requests.RequestException as e:
        print('保存失败:{0}, {1}'.format(file_name, img_url))


init()
html_source=download_html("")
img_urls = get_img_urls(html_source)
handle_img_url(img_urls)
