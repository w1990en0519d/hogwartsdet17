from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from app.appPO.page.addresslist_page import AddressListPage
from app.appPO.page.base_page import BasePage


class MainPage(BasePage):
    """
    app首页页面
    """
    addresslist_element = (MobileBy.XPATH, '//*[@text="通讯录"]')

    def goto_addresslist(self):
        # 点击通讯录
        # self.find(*self.addresslist_element) # 解元组

        self.find(MobileBy.XPATH, '//*[@text="通讯录"]').click()

        return AddressListPage(self.driver)
