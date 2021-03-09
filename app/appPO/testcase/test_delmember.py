from app.appPO.page.app import App


class TestDelmember:

    def setup(self):
        self.app = App().start_app()
        self.main = self.app.goto_main()

    def teardown(self):
        self.app.stop_app()

    def test_delmember(self):
        element = self.main.goto_addresslist().goto_search().goto_Personalmation().goto_editmember().goto_delmember()
        element.delmember()
        element.verfy_ok()
