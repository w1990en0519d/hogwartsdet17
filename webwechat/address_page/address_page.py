from selenium.webdriver.support.wait import WebDriverWait

from webwechat.address_page.add_member_page import AddMemberPage


class AddressPage:
    def __init__(self, driver):
        self.driver = driver

    def goto_add_member(self):
        """
        切换到添加成员界面
        :return:
        """

        def waitname(driver):
            self.driver.find_elements_by_xpath('//*[@class="qui_btn ww_btn js_add_member"]')[-1].click()

            els = driver.find_elements_by_xpath('//*[@class="member_edit_sec"]')

            return len(els) > 0

        WebDriverWait(self.driver, 10).until(waitname)
        return AddMemberPage(self.driver)
