import pytest
import yaml

from app.appPO.page.app import App


def get_datas():
    with open('../datas/member.yml', 'r', encoding="utf-8") as f:
        all_datas = yaml.safe_load(f)
        return all_datas['datas']


class TestAddContact:
    datas = get_datas()

    def setup(self):
        self.app = App().start_app()
        self.main = self.app.goto_main()

    def teardown(self):
        self.app.stop_app()

    @pytest.mark.parametrize('name,phone', datas)
    def test_addcontact(self, name, phone):
        editpage = self.main.goto_addresslist().goto_click_addcontact().addcontact_menual()
        editpage.addcontact(name, phone)
        editpage.verfy_ok()
