from resources import settings, user_agent
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

sina_weibo_login = "http://www.httpbin.org/user-agent"

# 修改默认user-agent

profile = webdriver.FirefoxProfile()
profile.set_preference('general.useragent.override',
                       user_agent.USER_AGENT_FIREFOX)

browser = webdriver.Firefox(firefox_profile=profile)
browser.get(sina_weibo_login)
browser.implicitly_wait(10)

print(browser.page_source)

time.sleep(3)
browser.quit()
