from resources import settings, user_agent
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


def login_netease(login_type):
    sina_weibo_login = "https://music.163.com/"

    # 修改默认user-agent
    profile = webdriver.FirefoxProfile()
    profile.set_preference('general.useragent.override',
                           user_agent.USER_AGENT_FIREFOX)
    options = Options()
    # options.add_argument('-headless')
    browser = webdriver.Firefox(executable_path="D:/software/geckodriver-v0.21.0-win64/geckodriver.exe",
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
        print('等待结束。。。')

        # TODO 打开控制台,没成功
        # browser.find_element_by_tag_name("body").send_keys(Keys.CONTROL + Keys.SHIFT + "k")
        # time.sleep(2)

        # 鼠标悬停在登录链接上弹出所有登录方式
        login_ele = browser.find_element_by_xpath(xpath_login_ele)
        ActionChains(browser).move_to_element(login_ele).perform()
        # TODO 调用登录方法
        if login_type == 'email':
            login_email(browser)
        elif login_type == 'sina':
            login_sina(browser)
        else:
            pass
        time.sleep(5)
        print(browser.current_url)
        print(browser.get_cookies())
    except Exception as e:
        print(e)
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


def login_sina(browser):
    '''新浪微博登录方式'''
    # 邮箱登录链接, 用于打开新浪微博授权登录页面
    xpath_login_sina_a = '//a[@data-action="login"]/em[contains(text(), "新浪微博登录")]/..'
    # 登录按钮
    xpath_login_input = "//div[@class='oauth_login_submit']/p/a[@action-type='submit']"
    # 打开登录窗口
    login_click_link = browser.find_element_by_xpath(xpath_login_sina_a)
    sina_auth_url = login_click_link.get_attribute("href")
    browser.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
    browser.get(sina_auth_url)
    #等待登录按钮出现
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath_login_input))
    )
    # 输入邮箱
    email_input = browser.find_element_by_id("userId")
    print("userId: ", email_input)
    email_input.send_keys(settings.USER_NAME)
    # 输入密码
    password_input = browser.find_element_by_id("passwd")
    password_input.send_keys(settings.PASSWORD)

    # 点击登录按钮
    login_button = browser.find_element_by_xpath(xpath_login_input)
    login_button.click()


# login_netease('sina')

if __name__ == '__main__':
    # login_netease('email')
    login_netease('sina')
