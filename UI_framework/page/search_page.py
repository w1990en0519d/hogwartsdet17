import yaml
from appium.webdriver.common.mobileby import MobileBy

from UI_framework.page.base_page import BasePage


class Search(BasePage):
    def search(self):
        # self.find_and_sendkey(MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/search_input_text"]', 'alibaba')
        # self.find_and_click(MobileBy.XPATH, '//*[@text="BABA"]')
        self.parse("../data_page/search_page.yaml", "search")
