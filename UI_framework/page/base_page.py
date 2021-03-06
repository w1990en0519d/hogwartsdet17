import logging

import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

# 基类，初始化driver的功能,find,finds,swipe_find
from selenium.common.exceptions import NoSuchElementException

from UI_framework.page.handle_black_list import handle_black
from UI_framework.page.logger import log


class BasePage:

    def __init__(self, driver: WebDriver = None):  # 类型提示功能
        self.driver = driver

    # 装饰器：黑名单处理机制，不需要传self，self必须是从*self中取出第0个元素
    '''def black_element(func):
        def run(*args, **kwargs):
            self = args[0]
            black_list = ['//*[@resource-id="com.xueqiu.android:id/iv_close"]']
            try:
                return func(*args, **kwargs)
            except Exception:
                for els_xpath in black_list:
                    eles = self.finds(MobileBy.XPATH, els_xpath)
                    if len(eles) > 0:
                        eles[0].click()
                        return func(*args, **kwargs)

        return run
        '''

    def find(self, locator, value):
        '''# 定义一个黑名单列表
        black_list = ['//*[@resource-id="com.xueqiu.android:id/iv_close"]']
        try:
            return self.driver.find_element(locator,value)
        except Exception:
            for els_xpath in black_list: # 对黑名单列表进行遍历
                eles = self.finds(MobileBy.XPATH,els_xpath)
                if len(eles)>0:
                    eles[0].click()
                    return self.find(locator,value)'''
        return self.driver.find_element(locator, value)

    def finds(self, locator, value):
        return self.driver.find_elements(locator, value)

    # @black_element
    @handle_black
    def find_and_click(self, locator, value):
        log.debug("find" + value)
        return self.find(locator, value).click()

    def find_and_sendkey(self, locator, value, content):
        return self.driver.find_element(locator, value).send_keys(content)

    def screenshot(self):
        return self.driver.get_screenshot_as_png()

    # 定义自己的滑动模块
    def swipe_find(self, text, num=3):
        for i in range(num):
            if i == num - 1:
                self.driver.implicitly_wait(5)
                raise NoSuchElementException(f'找到{num}次数，未找到。')
            self.driver.implicitly_wait(1)
            try:
                element = self.driver.find_element(MobileBy.XPATH, f'//*[@text="{text}"]')
                self.driver.implicitly_wait(5)
                return element
            except:
                print("未找到")
                size = self.driver.get_window_size()
                width = size.get('width')
                height = size.get("height")

                start_x = width / 2
                start_y = height * 0.8

                end_x = start_x
                end_y = height * 0.3
                self.driver.swipe(start_x, start_y, end_x, end_y, 1000)

    # 关键字驱动
    def parse(self, yaml_path, fun_name):
        """
        解析关键字，实现相应动作
        :param yaml_path:
        :param fun_name:
        :return:
        """

        with open(yaml_path, 'r', encoding="utf-8") as f:
            function = yaml.safe_load(f)
        steps = function.get(fun_name)
        for step in steps:
            if step.get("action") == "find_and_sendkey":
                self.find_and_sendkey(step.get("locator"), step.get("value"), step.get("concent"))

            elif step.get("action") == "find_and_click":
                self.find_and_click(step.get("locator"), step.get("value"))
