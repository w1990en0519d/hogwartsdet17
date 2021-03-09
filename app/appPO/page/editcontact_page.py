from appium.webdriver.common.mobileby import MobileBy

from app.appPO.page.base_page import BasePage


class EditContactPage(BasePage):
    """
    手动输入添加成员页面
    """

    def addcontact(self, name, phone):
        self.find(MobileBy.XPATH, '//*[contains(@text,"姓名")]/..//*[@text="必填"]').send_keys(name)
        self.find(MobileBy.XPATH, '//*[contains(@text,"手机")]/..//*[@text="必填"]').send_keys(phone)
        self.find(MobileBy.XPATH, '//*[@text="保存"]').click()

    def verfy_ok(self):
        assert self.find(MobileBy.XPATH, '//*[@text="添加成功"]')
