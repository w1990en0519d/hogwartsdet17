import yaml
from appium.webdriver.common.mobileby import MobileBy

from UI_framework.page.base_page import BasePage
from UI_framework.page.search_page import Search


class Market(BasePage):
    def goto_search(self):
        # self.find_and_click(MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/action_search"]')
        self.parse("../data_page/marker_page.yaml", "goto_search")
        return Search(self.driver)
