# coding: utf-8

"""
获取一张图片
"""

import requests
import os
import re
from log import logger
import time
import random

# 定义源码目录
_source_dir = './html'
_img_dir = './img'
_headers = {'user-agent': ('Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:61.0) '
                           'Gecko/20100101 Firefox/61.0')}

# 常量定义
_IMG_SUFFIX_DEFAULT = '.jpg'
_HTML_SOURCE_SUFFIX_DEFAULT = '.html'


def init():
    if not os.path.exists(_source_dir):
        logger.info('新建源码目录:' + _source_dir)
        os.makedirs(_source_dir)

    if not os.path.exists(_img_dir):
        logger.info('新建图片目录:' + _img_dir)
        os.makedirs(_img_dir)


def get_timestamp():
    '''
    获取当前时间戳: ms
    '''
    return round(time.time() * 1000)


def download_html(url):
    """根据url下载网页源码文件"""
    if not url:
        return

    l_tmp = url.split('/')
    html_source_file_name = l_tmp[len(l_tmp) - 1]
    if not html_source_file_name:
        html_source_file_name = (str(get_timestamp())
                                 + _HTML_SOURCE_SUFFIX_DEFAULT)
    file_path = _source_dir + os.path.sep + html_source_file_name
    try:
        r = requests.get(url, headers=_headers)
        # 源码文件备份, win需要设置encoding，否则默认文件为gbk会导致编码错误
        with open(file_path, mode='w+', encoding='utf-8') as file:
            file.write(r.text)
        logger.info("源码保存路径: {}".format(file_path))
        return r.text
    except requests.RequestException as e:
        logger.error('下载源码异常: {}'.format(url), e)
    except UnicodeEncodeError as e:
        logger.error('保存源码异常: {}'.format(url), e)
    except UnicodeError as e:
        logger.error('保存源码异常: {}'.format(url), e)


def get_urls(source_url, html_source, pattern):
    """
    根据正则提取url
    """
    if not source_url or not html_source:
        return

    all_url = pattern.findall(html_source)

    if not all_url:
        return

    # 取第一个元素判断结果是否是元组(正则中存在多个分组)
    first_group = all_url[0]
    # 只取第一个分组
    if isinstance(first_group, tuple):
        all_url = list(map(lambda tu: tu[0], all_url))
    return list(map(relative_to_absolute, all_url,
                    [source_url for i in range(len(all_url))]))


def get_contents(html_source, pattern):
    """
    根据正则提取内容，和get_urls不同的是不需要相对url转绝对url
    """
    contents = pattern.findall(html_source)

    if not contents:
        return

    # 取第一个元素判断结果是否是元组(正则中存在多个分组)
    first_group = contents[0]
    # 只取第一个分组
    if isinstance(first_group, tuple):
        all_content = list(map(lambda tu: tu[0], contents))
    return list(all_content)


def relative_to_absolute(relative_url, page_url):
    """
    根据相对url和当前页面链接将相对url转为绝对url
    :param relative_url: 相对url
    :param page_url: 当前页面链接
    :return:
    """
    if relative_url.startswith('http'):
        return relative_url

    http_prefix = "http://"
    relative_list = relative_url.split("/")

    # 排除url最后的一层:http://docs.python-requests.org/zh_CN/latest/index.html
    if os.path.splitext(page_url)[1]:
        page_url = os.path.split(page_url)[0]

    url_list = page_url.replace(http_prefix, "").split("/")
    # 不是以. 和.. 开头的url，直接以/开头的url，从域名开始算起
    if relative_url.startswith('/'):
        url_concat = http_prefix + url_list[0] + "/" + relative_url
        return url_concat

    relative_url_final = ''
    # 标记是否继续处理.和..
    last_flag = True
    for item in relative_list:
        if last_flag and item == '..' and len(url_list) > 0:
            url_list.pop(len(url_list) - 1)
        elif last_flag and item == '.':
            pass
        else:
            relative_url_final += item + '/'
            last_flag = False
    # 拼接
    url_final = ''
    for l in url_list:
        url_final += l + "/"
    url_final = http_prefix + url_final + relative_url_final

    # 图片链接去掉最后的/
    if url_final.endswith('/'):
        url_final = url_final[0:-1]

    return url_final


def handle_img_url(img_urls):
    """
    处理所有获取到的url
    """
    if img_urls:
        for img_url in img_urls:
            download_and_save_img(img_url)
            # 隔几秒下一次
            time.sleep(random.randint(3, 5))
    else:
        logger.warn("图片链接为空!")


def download_and_save_img(img_url):
    """
    根据链接下载并保存图片
    """
    file_name = os.path.split(img_url)[1]
    if '.' not in file_name:
        file_name += '.jpg'
    try:
        img_path = _img_dir + os.path.sep + file_name
        img_response = requests.get(img_url, headers=_headers)
        if img_response.status_code == 200:
            with open(img_path, 'wb') as img:
                img.write(img_response.content)
            logger.info('下载成功: {0}, {1}'.format(img_path, img_url))
        else:
            logger.warn('下载失败: {0}, {1}'.format(
                        img_response.status_code, img_url))
    except requests.RequestException as e:
        logger.error('保存失败: {0}'.format(img_url), e)
    except UnicodeError as e:
        logger.error('保存失败: {0}'.format(img_url), e)


def execute():
    """
    采集入口
    """
    # 初始化
    init()

    # 下载网页
    homepage_url = 'http://www.beautylegmm.com/'
    # 1. 下载首页源码
    homepage_source = download_html(homepage_url)
    # 1.1. 获得第一页的目录入口链接
    detail_url_pattern = re.compile(('<div class="post_weidaopic">[\s\S]*?<a href="(.*?)"'))
    detail_urls = get_urls(homepage_url, homepage_source, detail_url_pattern)
    # 1.2 收集其他页的目录入口链接
    next_page_pattern = re.compile('<a href="([^"]*?)">下一页</a>')
    get_next_page_urls(homepage_url, homepage_source, next_page_pattern,
                       detail_url_pattern, detail_urls)
    logger.info('所有细览页链接个数: {}'.format(len(detail_urls)))
    # 2. 处理所有细览页
    if detail_urls:
        logger.info('细览页个数: {0}'.format(len(detail_urls)))
        img_url_pattern = re.compile('<a href="(.*?.jpg)"')
        next_page_pattern = re.compile('<a class="next" href="(.*?)">下一页</a>')
        for detail_url in detail_urls:
            img_url_all = []
            detail_source = download_html(detail_url)
            # 图片链接
            img_urls = get_urls(detail_url, detail_source, img_url_pattern)
            if img_urls:
                logger.info('采集到图片链接: {0}'.format(len(img_urls)))
                # handle_img_url(img_urls)
                len_img_url_all = len(img_url_all)
                img_url_all[len_img_url_all:len_img_url_all] = img_urls
            else:
                logger.info('没有图片url匹配: {}'.format(detail_url))
                continue
            # 翻页链接
            get_next_page_urls(detail_url, detail_source, next_page_pattern,
                               img_url_pattern, img_url_all)
            logger.info('图片链接数: {0}'.format(len(img_url_all)))
            handle_img_url(img_url_all)
        logger.info("爬取正常结束。")
    else:
        print('没有匹配,爬取结束。')


def get_next_page_urls(root_url, html_source, next_page_pattern,
                       url_pattern, urls):
    """
    获取下一页链接
    """
    next_page_urls = get_urls(root_url, html_source, next_page_pattern)
    if next_page_urls:
        logger.info('下一页: {0}'.format(next_page_urls))
        next_page_url = next_page_urls[0]
        next_page_source = download_html(next_page_url)
        next_page_urls = get_urls(next_page_url, next_page_source,
                                  url_pattern)
        if next_page_urls:
            logger.info('采集到链接: {0}'.format(len(next_page_urls)))
            len_img_urls = len(urls)
            urls[len_img_urls:len_img_urls] = next_page_urls
            time.sleep(random.randint(1, 4))
            get_next_page_urls(next_page_url, next_page_source,
                               next_page_pattern, url_pattern, urls)
        else:
            logger.info('没有url匹配: {}'.format(next_page_url))
    else:
        logger.info('翻页完成。')


execute()
