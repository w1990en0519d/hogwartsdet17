from selenium import webdriver

from webwechat.address_page.address_page import AddressPage


class MainPage:
    """
    登陆后的首页
    """

    def __init__(self):
        # 声明chrome的参数
        chrome_arg = webdriver.ChromeOptions()
        # 加入调式的地址
        chrome_arg.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=chrome_arg)
        self.driver.implicitly_wait(5)

    def goto_address(self):
        """
        切换到通讯录页面
        :return:
        """
        self.driver.find_element_by_xpath('//*[@id="menu_contacts"]').click()
        return AddressPage(self.driver)
