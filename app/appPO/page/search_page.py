from appium.webdriver.common.mobileby import MobileBy

from app.appPO.page.base_page import BasePage
from app.appPO.page.personal_page import PersonalPage


class SearchPage(BasePage):
    """
    搜索页面
    """

    def goto_Personalmation(self):
        self.find(MobileBy.XPATH, '//*[@text="搜索"]').send_keys('aa')
        elements = self.finds(MobileBy.XPATH, '//*[@text="aa"]')
        if len(elements) > 1:
            elements[1].click()
            return PersonalPage(self.driver)
