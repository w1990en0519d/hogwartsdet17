from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class TestAddress:

    def test_address(self):
        # 声明chrome的参数
        chrome_arg = webdriver.ChromeOptions()
        # 加入调式的地址
        chrome_arg.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=chrome_arg)
        self.driver.implicitly_wait(5)
        # 点击通讯录
        self.driver.find_element_by_xpath('//*[@id="menu_contacts"]').click()

        # 不可交互的元素，选用显示等待
        # 1、元素被遮挡：元素前面还有其他不可见元素
        # 2、元素有多个，需要人工挑选合适的元素
        def waitname(driver):
            driver.find_elements_by_xpath('//*[@class="qui_btn ww_btn js_add_member"]')[1].click()
            els = driver.find_elements_by_xpath('//*[@class="member_edit_sec"]')
            if len(els) > 0:
                return True
            else:
                return False
            # return len(els)>0

        WebDriverWait(self.driver, 10).until(waitname)
        # 输入姓名
        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys("哈利")
        # 输入账号
        self.driver.find_element_by_xpath('//*[@id="memberAdd_acctid"]').send_keys("wend")
        # 输入手机号
        self.driver.find_element_by_xpath('//*[@id="memberAdd_phone"]').send_keys("15903239876")
        # 点击保存
        self.driver.find_element_by_xpath('//*[@class="qui_btn ww_btn js_btn_save"]').click()
