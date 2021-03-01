class AddMemberPage:
    def __init__(self, dirver):
        self.driver = dirver

    def add_member(self):
        """
        添加成员界面
        :return:
        """
        # 输入姓名
        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys("哈利")
        # 输入账号
        self.driver.find_element_by_xpath('//*[@id="memberAdd_acctid"]').send_keys("wend")
        # 输入手机号
        self.driver.find_element_by_xpath('//*[@id="memberAdd_phone"]').send_keys("15903239876")
        # 点击保存
        self.driver.find_element_by_xpath('//*[@class="qui_btn ww_btn js_btn_save"]').click()
