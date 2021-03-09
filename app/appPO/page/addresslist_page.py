from appium.webdriver.common.mobileby import MobileBy

from app.appPO.page.addcontact_page import AddContactPage
from app.appPO.page.base_page import BasePage
from app.appPO.page.search_page import SearchPage


class AddressListPage(BasePage):
    """
    通讯录页面
    """

    def goto_click_addcontact(self):
        # 点击添加成员
        element = self.swipe_find("添加成员")
        element.click()

        return AddContactPage(self.driver)

    def goto_search(self):
        self.find(MobileBy.ID, 'com.tencent.wework:id/igk').click()
        return SearchPage(self.driver)
