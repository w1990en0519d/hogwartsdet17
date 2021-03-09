from appium.webdriver.common.mobileby import MobileBy

from app.appPO.page.base_page import BasePage
from app.appPO.page.editmember_page import EditmemberPage


class PersonalPage(BasePage):
    """
    个人信息页面
    """

    def goto_editmember(self):
        self.find(MobileBy.ID, 'com.tencent.wework:id/igo').click()
        return EditmemberPage(self.driver)
