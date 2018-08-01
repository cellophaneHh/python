'''
selenium打开淘宝。。。
'''
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument('-headless')

url = 'https://www.taobao.com/'
cookies = []
firefox = webdriver.Firefox(firefox_options=options)
try:
    firefox.get(url)
    firefox.execute_script("document.documentElement.scrollTop = document.body.scrollHeight")
    # 不等待的话会立即返回，达不到效果。。。。。。。。
    time.sleep(3)
    html_source = firefox.page_source
    print(html_source)
    with open('taobao.html', 'w+', encoding='utf-8') as f:
        f.write(html_source)
finally:
    firefox.close()
