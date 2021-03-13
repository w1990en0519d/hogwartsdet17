from UI_framework.page.app import App


class TestUiDemo:

    def setup(self):
        self.app = App().start_app()

    def teardown(self):
        pass

    def test_uidemo(self):
        self.app.goto_main().goto_market()
