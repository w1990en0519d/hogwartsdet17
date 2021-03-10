import yaml
from appium import webdriver

from app.appPO.page.base_page import BasePage
from app.appPO.page.main_page import MainPage

'''with open("../datas_page/caps.yml","r",encoding="utf-8") as f:
    datas = yaml.safe_load(f)
    desires = datas['desirecaps']
    ip = datas['server']['ip']
    port = datas['server']['port']
'''


class App(BasePage):

    def start_app(self):
        if self.driver == None:

            # 启动app
            caps = {}
            caps["platformName"] = "android"  # 测试的设备系统
            caps["deviceName"] = "127.0.0.1:7555"  # 测试的手机名称
            caps["appPackage"] = "com.tencent.wework"  # 测试app的包名
            caps["appActivity"] = ".launch.LaunchSplashActivity"  # app的首页
            caps["noReset"] = "true"  # 去掉页面弹窗
            caps['settings[waitForIdleTimeout]'] = 1  # settings 控制 动态页面的等待时长
            # 跳过安装uiautomatar2server等服务
            caps['skipServerInstallation'] = "true"
            # 跳过设备的初始化
            # caps['skipDeviceInitialization'] = "ture"
            # 运行前不停止app
            # caps['dontStopAppOnReset'] = "true"

            # 客户端与appium 服务器建立连接的代码
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

            # self.driver = webdriver.Remote(f"http://{ip}:{port}/wd/hub", desires)
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
        return MainPage(self.driver)
