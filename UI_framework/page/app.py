import yaml
from appium import webdriver

from UI_framework.page.base_page import BasePage
from UI_framework.page.main_page import MainPage

with open("../data_page/caps.yml", "r", encoding="utf-8") as f:
    datas = yaml.safe_load(f)
    desires = datas['desirecaps']
    ip = datas['server']['ip']
    port = datas['server']['port']


class App(BasePage):

    def start_app(self):
        """
        利用数据驱动，读取yml文件中的数据，该数据是启动app准备数据，并进行参数传递。
        :return:
        """
        if self.driver == None:

            self.driver = webdriver.Remote(f"http://{ip}:{port}/wd/hub", desires)
            self.driver.implicitly_wait(5)
        else:
            self.driver.launch_app()
        return self

    def restart_app(self):
        # 重启app
        self.driver.close_app()
        self.driver.launch_app()

    def stop_app(self):
        # 停止app
        self.driver.quit()

    def goto_main(self):
        # 进入首页页面
        return MainPage(self.driver)
