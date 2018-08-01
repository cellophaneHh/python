from selenium import webdriver
import time

url = 'https://www.taobao.com'

cookies = []
firefox = webdriver.Firefox()
try:
    firefox.get(url)
    time.sleep(3)
    html_source = firefox.page_source
    with open('taobao.html', 'w+', encoding='utf-8') as f:
        f.write(html_source)
except Exception as e:
    print(e)
finally:
    firefox.close()
