import yaml
from appium.webdriver.common.mobileby import MobileBy

from UI_framework.page.base_page import BasePage
from UI_framework.page.market_page import Market


class MainPage(BasePage):

    def goto_market(self):
        """
        1.进入雪球app首页
        2.点击右下角的蓝色笔
        3.调用黑名单处理机制，消除黑名单
        4.点击行情按钮，进入雪球app行情页面
        5.点击搜索按钮并输入alibaba并点击
        :return:
        """

        # self.find(MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/post_status"]').click()
        # self.find_and_click(MobileBy.XPATH, '//*[@text="行情"]')
        self.parse("../data_page/main_page.yaml", "goto_market")
        return Market(self.driver)
