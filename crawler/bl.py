'''
爬取三层图片网站
'''
import requests
import threading
import multiprocessing
from lxml import etree
import json
from redisclient.redis_pool import pool
import redis
from resources import user_agent
from log_handler import LogHandler
import time
import os

headers = {'user-agent': user_agent.USER_AGENT_CHROME}
# redis 客户端
redis_client = redis.Redis(connection_pool=pool)
# 初始url
START_PAGE_URL = 'http://www.beautylegmm.com/index-1.html'
# redis中存放图片列表页url的列表
DETAIL_URLS = 'detail_urls'
# redis中存放从图片列表也采集到的图片的信息列表, 包含人名，时间等分类信息和url，json存储
IMAGE_INFO = 'image_info'
log = LogHandler('bl')


def get_url_byxpath(html_source, xpath):
    '''根据网页源码和xpath获取数据并返回'''
    html = etree.HTML(html_source)
    return html.xpath(xpath)


def get_detail_urls(start_url):
    '''获取所有图片列表页url'''
    response = requests.get(start_url, headers=headers)
    if response.status_code != 200:
        return
    else:
        detail_urls = get_url_byxpath(response.text, '//div[@class="post_weidaopic"]/a/@href')
        log.info('采集到细览页url个数: {}'.format(len(detail_urls)))
        # 存入redis
        redis_client.rpush(DETAIL_URLS, *detail_urls)
        next_pages = get_url_byxpath(response.text,
                                    '//div[@id="pages"]//li[@class="next"]/a/@href')
        if next_pages:
            for next_page in next_pages:
                get_detail_urls(next_page)


def get_detail_urls_task():
    '''采集细览页url任务'''
    t = threading.Thread(target=get_detail_urls, args=(START_PAGE_URL,))
    t.setDaemon(True)
    t.start()
    t.join()


def get_imageInfo(url):
    '''获取所有图片列表页url'''
    # url = 'http://www.beautylegmm.com/Stephy/beautyleg-1652.html'
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return
    else:
        image_urls = get_url_byxpath(response.text, '//div[@class="post"]/a/@href')
        log.info('采集到图片链接数量: {}'.format(len(image_urls)))
        title = get_url_byxpath(response.text, '//div[@class="title"]/h2/text()')[0]
        title_info = title.split(' ')
        image_info = {}
        image_info['name'] = title_info[3]
        image_info['date'] = title_info[4]
        for image_url in image_urls:
            image_info['url'] = 'http://www.beautylegmm.com' + image_url
            redis_client.rpush(IMAGE_INFO, json.dumps(image_info))
        next_pages = get_url_byxpath(response.text, '//div[@class="archives_page_bar"]/a[@class="next"]/@href')
        if next_pages:
            log.info('细览页下一页: {}'.format(next_pages[0]))
            time.sleep(3)
            get_imageInfo(next_pages[0])


def get_image_target():
    while True:
        url = redis_client.lpop(DETAIL_URLS)
        if url:
            get_imageInfo(url)
        else:
            log.info('无细览页链接，休眠..')
            time.sleep(10)


def get_image_task():
    processes = []
    for i in range(4):
        print(1)
        process = multiprocessing.Process(
            target=get_image_target,
            daemon=True
        )
        processes.append(process)
    for p in processes:
        p.start()


def download_image():
    '''从image_info中取图片信息进行下载'''
    while True:
        image_info = redis_client.lpop(IMAGE_INFO)
        if not image_info:
            log.info('无图片信息, 休眠..')
            time.sleep(10)
        else:
            image_info_json = json.loads(image_info)
            name = image_info_json['name']
            date = image_info_json['date']
            url = image_info_json['url']
            try:
                img_response = requests.get(url, headers=headers)
                if not img_response.status_code == 200:
                    log.error('下载失败: {}, {}, {}'.format(name, date, url))
                else:
                    dir_name = './blimg/' + name + '/' + date + '/'
                    if not os.path.exists(dir_name):
                        os.makedirs(dir_name)

                    file_name = os.path.split(url)[1]
                    file_path = dir_name + file_name
                    with open(file_path, 'wb') as img:
                        img.write(img_response.content)
                    log.info('下载成功: {}, {}, {}'.format(name, date, url))
            except Exception as e:
                redis_client.rpush(IMAGE_INFO, image_info)
                log.error(e)


def download_image_task():
    processes = []
    for i in range(10):
        process = multiprocessing.Process(
            target=download_image,
            daemon=True
        )
        processes.append(process)
    for p in processes:
        p.start()


def block_task():
    '''阻塞程序，不让退出'''
    while True:
        time.sleep(1000)


if __name__ == '__main__':
    urls = ['http://www.beautylegmm.com/Tina/beautyleg-1655.html']
    for url in urls:
        get_imageInfo(url)
    download_image_task()
    # get_image_task()
    # get_detail_urls_task()
    t = threading.Thread(target=block_task)
    t.start()
    t.join()
