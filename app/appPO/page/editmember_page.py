from appium.webdriver.common.mobileby import MobileBy

from app.appPO.page.base_page import BasePage
from app.appPO.page.delmember_page import DelmemberPage


class EditmemberPage(BasePage):
    """
    编辑成员页面
    """

    def goto_delmember(self):
        self.find(MobileBy.XPATH, '//*[@text="编辑成员"]').click()
        return DelmemberPage(self.driver)
