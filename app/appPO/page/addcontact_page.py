from appium.webdriver.common.mobileby import MobileBy

from app.appPO.page.base_page import BasePage
from app.appPO.page.editcontact_page import EditContactPage


class AddContactPage(BasePage):
    """
    添加成员页面
    """

    def addcontact_menual(self):
        self.find(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()

        return EditContactPage(self.driver)
