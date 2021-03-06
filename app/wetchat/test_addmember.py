import pytest
import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


def get_datas():
    """
    读取yml参数数据
    :return:
    """
    with open('./member.yml', 'r', encoding='utf-8') as f:
        all_datas = yaml.safe_load(f)
        return all_datas['datas']


class TestAddmember:
    datas = get_datas()

    def setup(self):
        caps = {}
        caps["platformName"] = "android"  # 测试的设备系统
        caps["deviceName"] = "127.0.0.1:7555"  # 测试的手机名称
        caps["appPackage"] = "com.tencent.wework"  # 测试app的包名
        caps["appActivity"] = ".launch.LaunchSplashActivity"  # app的首页
        caps["noReset"] = "true"  # 去掉页面弹窗
        caps['settings[waitForIdleTimeout]'] = 1  # settings 控制 动态页面的等待时长

        # 客户端与appium 服务器建立连接的代码
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize('name, phone', datas)
    def test_addmember(self, name, phone):
        """
        前提条件: 已登录状态（ noReset=True）
        添加联系人用例：
        1、打开【企业微信】应用
        2、进入通讯录
        3、点击添加成员
        4、点击手动输入添加
        5、输入姓名，手机号，点击保存
        6、退出【企业微信】应用
        :param name:
        :param phone:
        :return:
        """
        self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="添加成员"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/b7m').send_keys(name)
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/fwi').send_keys(phone)
        self.driver.find_element(MobileBy.XPATH, '//*[@text="保存"]').click()
