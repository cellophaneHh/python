'''
测试ubuntu无图形界面百度首页打开
'''
from resources import settings, user_agent
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import time
import log_handler

# 初始化日志
log = log_handler.LogHandler("weibo_log")

baidu_homepae = "http://www.baidu.com/"

# 修改默认user-agent
profile = webdriver.FirefoxProfile()
profile.set_preference('general.useragent.override',
                       user_agent.USER_AGENT_FIREFOX)
# 设置firefox不显示界面
ff_option = Options()
ff_option.add_argument('-headless')

browser = webdriver.Firefox(firefox_profile=profile, options=ff_option)
browser.get(baidu_homepae)
with open('baidu_homepae.html', 'w') as f:
    f.write(browser.page_source)
browser.quit()
print('结束..')
