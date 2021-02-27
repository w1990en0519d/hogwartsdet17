import json
from time import sleep

from selenium import webdriver


class TestLogin():

    def setup(self):
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_logintmp(self):
        """
        复用浏览器调试
        chrome_arg = webdriver.ChromeOptions()
        chrome_arg.debugger_address ='127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=chrome_arg)
        :return:
        """
        chrome_arg = webdriver.ChromeOptions()
        chrome_arg.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=chrome_arg)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element_by_xpath("//*[@class='ww_indexImg ww_indexImg_AddMember']").click()
        self.driver.find_element_by_id("username").send_keys("哈尼")
        self.driver.find_element_by_id("memberAdd_english_name").send_keys("hali")
        self.driver.find_element_by_id("memberAdd_acctid").send_keys("w1990end")
        sleep(5)

        # 获取cookie值并使用json.dumps()把cookie存入文件
        # cookies = self.driver.get_cookies()
        # with open('./cookies.txt','w',encoding='utf-8') as f:
        #     f.write(json.dumps(cookies))

        # 获取cookie值并使用json.dump()把cookie存入文件
        cookies = self.driver.get_cookies()
        with open('./cookies.txt', 'w', encoding='utf-8') as f:
            json.dump(cookies, f)

    def test_login_cookie(self):
        """
        利用cookie进行登录操作
        :return:
        """
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # 使用json.loads()读取cookies
        # with open('./cookies.txt','r',encoding='utf-8') as f:
        #     raw_cookies = f.read()
        #     # 序列化
        #     cookies = json.loads(raw_cookies)
        # 使用json.load()读取cookies
        with open('./cookies.txt', 'r', encoding='utf-8') as f:
            cookies = json.load(f)
        for i in cookies:
            self.driver.add_cookie(i)
        self.driver.refresh()
