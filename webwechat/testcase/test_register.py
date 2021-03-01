from time import sleep

from webwechat.login_page.wechatmain_page import WechatmainPage


class TestRegister:

    def test_register(self):
        main = WechatmainPage()
        main.goto_register().register()
        sleep(5)

    def test_login_register(self):
        main = WechatmainPage()
        main.goto_login().goto_register().register()
        sleep(5)
