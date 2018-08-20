'''
新浪微博模拟登陆，验证码问题还未解决
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

sina_weibo_login = "https://weibo.com/"

# 修改默认user-agent
profile = webdriver.FirefoxProfile()
profile.set_preference('general.useragent.override',
                       user_agent.USER_AGENT_FIREFOX)
# 设置firefox不显示界面
ff_option = Options()
ff_option.add_argument('-headless')

browser = webdriver.Firefox(firefox_profile=profile, options=ff_option)
browser.get(sina_weibo_login)
try:
    # 等待直到用户名输入框出现，最多10s
    element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, 'loginname'))
    )
    log.info('等待结束。。。')
    # 填充用户名密码
    login_input = browser.find_element_by_id('loginname')
    login_input.send_keys(settings.USER_NAME)
    password_input = browser.find_element_by_xpath(
        '//div[@node-type="password_box"]//input[@name="password"]'
    )
    password_input.send_keys(settings.PASSWORD)
    # 点击登录按钮
    login_button = browser.find_element_by_xpath(
        '//div[contains(@class, "login_btn")]/a[@tabindex="6"]'
    )
    login_button.click()
    time.sleep(3)
except Exception as e:
    log.exception('登录失败!', e)
finally:
    log.info('cookies: %s', browser.get_cookies())
    browser.quit()
