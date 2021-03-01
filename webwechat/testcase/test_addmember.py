from webwechat.address_page.main_page import MainPage


class TestAddmember:

    def test_add_member(self):
        main = MainPage()
        main.goto_address().goto_add_member().add_member()
