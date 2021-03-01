from selenium import webdriver

from webwechat.login_page.login_page import LoginPage
from webwechat.login_page.register_page import RegisterPage


class WechatmainPage:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.get('https://work.weixin.qq.com/')

    def goto_login(self):
        self.driver.find_element_by_xpath('//*[@class="index_top_operation_loginBtn"]').click()
        # 将类初始化(实例化)成对象
        return LoginPage(self.driver)

    def goto_register(self):
        self.driver.find_element_by_xpath('//*[@class="index_head_info_pCDownloadBtn"]').click()
        return RegisterPage(self.driver)
