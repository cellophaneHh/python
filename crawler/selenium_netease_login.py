from resources import settings, user_agent
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
import time

sina_weibo_login = "https://music.163.com/"

# 修改默认user-agent
profile = webdriver.FirefoxProfile()
profile.set_preference('general.useragent.override',
                       user_agent.USER_AGENT_FIREFOX)

browser = webdriver.Firefox(firefox_profile=profile)
browser.get(sina_weibo_login)
#打开登录窗口
# 鼠标悬停
xpath_login_ele = "//a[@data-action='login' and contains(text(), '登录')]"
# 邮箱登录元素标记, 用于判断元素是否存在
xpath_login_email_content = '//a[@data-action="login"]/em[contains(text(), "网易邮箱帐号登录")]'
# 邮箱登录链接, 用于打开登录窗口
xpath_login_email_a = xpath_login_email_content + "/.."

# 登录窗口相关
# 账号
xpath_login_email = "//input[@placeholder='请输入帐号']"
# 密码
xpath_login_pwd = "//input[@placeholder='请输入密码']"
# 登录按钮
xpath_login_input = "//a[@data-action='login']/i[contains(text(), '登　录')]/.."
try:
    # 去掉selenium特征,window.navigator.webdriver为true改为false
    browser.execute_script("Object.defineProperties(navigator, {webdriver: {get:function(){return false}}})")
    print(browser.execute_script('window.navigator.webdriver'))
    print("-----------------")
    # 等待邮箱登录标记出现
    element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath_login_ele))
    )
    print('等待结束。。。')

    # TODO 打开控制台,没成功
    # browser.find_element_by_tag_name("body").send_keys(Keys.CONTROL + Keys.SHIFT + "k")
    # time.sleep(2)

    # 鼠标悬停在登录链接上弹出所有登录方式
    login_ele = browser.find_element_by_xpath(xpath_login_ele)
    ActionChains(browser).move_to_element(login_ele).perform()
    # 打开登录窗口
    login_click_link = browser.find_element_by_xpath(xpath_login_email_a)
    print(type(login_click_link))
    login_click_link.click()

    # 输入邮箱
    email_input = browser.find_element_by_xpath(xpath_login_email)
    email_input.send_keys(settings.NETEASE_USER_NAME)
    # 输入密码
    password_input = browser.find_element_by_xpath(xpath_login_pwd)
    password_input.send_keys(settings.NETEASE_PWD)

    # 点击登录按钮
    login_button = browser.find_element_by_xpath(xpath_login_input)
    login_button.click()
    time.sleep(2)
    print(browser.current_url)
    print(browser.get_cookies())
except Exception as e:
    print(e)
    print('登录失败..')
finally:
    browser.quit()
