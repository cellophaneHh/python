'''
模拟登陆github并爬取数据
'''
import requests
from lxml import etree


class Login:
    '''实现github模拟登陆'''
    def __init__(self):
        self.headers = {
            'Referer': 'https://github.com/',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0',
            'Host': 'github.com'
        }
        self.login_url = 'https://github.com/login'
        self.post_url = 'https://github.com/session'
        self.logined_url = 'https://github.com/settings/profile'
        # 自己保存一个session，之后的请求会自动加上cookie
        self.session = requests.Session()

    def token(self):
        # 请求之后session自动保存了cookie
        response = self.session.get(self.login_url, headers=self.headers)
        if (response.status_code == 200):
            text = response.text
            selector = etree.HTML(text)
            token = selector.xpath("//input[@name='authenticity_token']/@value")
        else:
            print(response.status_code)
            print(response.reason)
        return token

    def dynamics(self, html):
        selector = etree.HTML(html)
        dynamics = selector.xpath('//div[contains(@class, "news")]//div[contains(@class, "alert")]')
        if not dynamics:
            print('dynamics没有解析到数据')
            return
        for item in dynamics:
            dynamic = ' '.join(item.xpath('.//div[@class="title"]//text()').stripe())
            print(dynamic)

    def profile(self, html):
        selector = etree.HTML(html)
        name = selector.xpath('//input[@id="user_profile_name"]/@value')[0]
        email = selector.xpath('//select[@id="user_profile_email"]/option[@value!=""]/text()')
        print(name, email)

    def login(self, user, password):
        token = self.token()
        if not token:
            print('获取token失败..')
            return
        # 登录url，post请求
        login_form = {
            'authenticity_token': self.token(),
            'commit': 'Sign+in',
            'login': user,
            'password': password,
            'utf8': '✓'
        }
        response = self.session.post(self.post_url, data=login_form, headers=self.headers)
        if response.status_code == 200:
            self.dynamics(response.text)
        else:
            print('')

        response = self.session.get(self.logined_url, headers=self.headers)
        if response.status_code == 200:
            self.profile(response.text)
        else:
            print('请求profile失败..')


github_login = Login()
github_login.login('zhangheng2683@gmail.com', 'neu20102683@@.')
