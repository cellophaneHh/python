from resources import settings, user_agent
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
import time
import traceback
import sys


def login_netease(login_type):
    sina_weibo_login = "https://music.163.com/"

    # 修改默认user-agent
    profile = webdriver.FirefoxProfile()
    profile.set_preference('general.useragent.override',
                           user_agent.USER_AGENT_FIREFOX)
    options = Options()
    # options.add_argument('-headless')
    browser = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver",
                                firefox_profile=profile, firefox_options=options)
    browser.get(sina_weibo_login)
    #打开登录窗口
    # 鼠标悬停
    xpath_login_ele = "//a[@data-action='login' and contains(text(), '登录')]"
    try:
        # 去掉selenium特征,window.navigator.webdriver为true改为false
        browser.execute_script("Object.defineProperties(navigator, {webdriver: {get:function(){return false}}})")
        print(browser.execute_script('window.navigator.webdriver'))
        print("-----------------")
        # 等待登录标记出现
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath_login_ele))
        )
        # TODO 打开控制台,没成功
        # browser.find_element_by_tag_name("body").send_keys(Keys.CONTROL + Keys.SHIFT + "k")
        # time.sleep(2)

        # 鼠标悬停在登录链接上弹出所有登录方式
        login_ele = browser.find_element_by_xpath(xpath_login_ele)
        ActionChains(browser).move_to_element(login_ele).perform()
        # 调用登录方法
        if login_type == 'email':
            login_email(browser)
        elif login_type == 'sina':
            login_sina(browser)
        else:
            pass
        print(browser.current_url)
        print(browser.get_cookies())
    except Exception as e:
        print(traceback.format_exc())
        print('登录失败..')
    finally:
        browser.quit()


def login_email(browser):
    '''邮箱登录方式'''
    # 邮箱登录元素标记
    xpath_login_email_content = '//a[@data-action="login"]/em[contains(text(), "网易邮箱帐号登录")]'
    # 邮箱登录链接, 用于打开登录窗口
    xpath_login_email_a = xpath_login_email_content + "/.."
    # 账号
    xpath_login_email = "//input[@placeholder='请输入帐号']"
    # 密码
    xpath_login_pwd = "//input[@placeholder='请输入密码']"
    # 登录按钮
    xpath_login_input = "//a[@data-action='login']/i[contains(text(), '登　录')]/.."
    # 打开登录窗口
    login_click_link = browser.find_element_by_xpath(xpath_login_email_a)
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
    time.sleep(5)


def login_sina(browser):
    '''新浪微博登录方式'''
    # 邮箱登录链接, 用于打开新浪微博授权登录页面
    xpath_login_sina_a = '//a[@data-action="login"]/em[contains(text(), "新浪微博登录")]/..'
    # 登录按钮
    xpath_login_input = "//div[@class='oauth_login_submit']/p/a[@action-type='submit']"
    # 打开登录窗口
    login_click_link = browser.find_element_by_xpath(xpath_login_sina_a)
    # login_click_link.click()
    sina_auth_url = login_click_link.get_attribute("href")
    browser.execute_script('window.open("{}")'.format(sina_auth_url))
    # 切换到新打开的窗口
    windows = browser.window_handles
    browser.switch_to.window(windows[-1])
    #等待登录框出现
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "userId"))
    )
    # 偶尔会出现placeholder没有清空的问题
    time.sleep(0.5)
    # 输入邮箱
    email_input = browser.find_element_by_id("userId")
    email_input.click()
    email_input.send_keys(settings.USER_NAME)
    # 输入密码
    password_input = browser.find_element_by_id("passwd")
    password_input.send_keys(settings.PASSWORD)
    # 直接点击会点击不到
    time.sleep(0.5)
    # 点击登录按钮
    # login_button = browser.find_element_by_xpath(xpath_login_input)
    # login_button.click()
    login_button_click_js = "document.getElementsByClassName('WB_btn_login formbtn_01')[0].click()"
    browser.execute_script(login_button_click_js)
    time.sleep(3)
    # 切换到新打开的窗口
    windows = browser.window_handles
    browser.switch_to.window(windows[0])


if __name__ == '__main__':
    login_type = sys.argv[0]
    login_netease(login_type)
