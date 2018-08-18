from resources import settings, user_agent
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

sina_weibo_login = "https://weibo.com/"

# 修改默认user-agent

profile = webdriver.FirefoxProfile()
profile.set_preference('general.useragent.override',
                       user_agent.USER_AGENT_FIREFOX)

browser = webdriver.Firefox(firefox_profile=profile)
browser.get(sina_weibo_login)
try:
    # 等待直到用户名输入框出现，最多10s
    element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, 'loginname'))
    )
    print('等待结束。。。')
    # 填充用户名密码
    login_input = browser.find_element_by_id('loginname')
    login_input.send_keys(settings.USER_NAME)
    password_input = browser.find_element_by_xpath('//div[@node-type="password_box"]//input[@name="password"]')
    password_input.send_keys(settings.PASSWORD)
    # 点击登录按钮
    login_button = browser.find_element_by_xpath('//div[contains(@class, "login_btn")]/a[@tabindex="6"]')
    login_button.click()
except Exception as e:
    print(e)
    print('登录失败..')
finally:
    time.sleep(3)
    print(browser.current_url)
    print(browser.get_cookies())
    browser.quit()
