from appium.webdriver.common.mobileby import MobileBy

from app.appPO.page.base_page import BasePage


class DelmemberPage(BasePage):
    """
    删除成员页面
    """

    def delmember(self):
        self.find(MobileBy.XPATH, '//*[@text="删除成员"]').click()
        self.find(MobileBy.XPATH, '//*[@text="确定"]').click()

    def verfy_ok(self):
        assert self.find(MobileBy.XPATH, '//*[@text="无搜索结果"]')
