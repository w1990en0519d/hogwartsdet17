import json

from test_api.api_po.address_po import MemberPO


class TestMember:

    def setup_class(self):
        self.member = MemberPO()
        self.user_id = "a0005"
        self.name = "苏檀儿"
        self.mobile = "18700000142"
        self.department = [1]

    def setup(self):
        self.member.get_delete_member(self.user_id)

    def test_get_memeber(self):
        self.member.get_address_member(self.user_id, self.name, self.mobile, self.department)
        r = self.member.get_acquire_member(self.user_id)
        print(r)
        assert r["errmsg"] == "ok"
        assert r["errcode"] == 0
        self.member.get_delete_member(self.user_id)

    def test_creat_member(self):
        r = self.member.get_address_member(self.user_id, self.name, self.mobile, self.department)
        print(r)
        assert r["errmsg"] == "created"
        assert r["errcode"] == 0
        info = self.member.get_acquire_member(self.user_id)
        assert info["name"] == "苏檀儿"
        self.member.get_delete_member(self.user_id)

    def test_updata_member(self):
        self.member.get_address_member(self.user_id, self.name, self.mobile, self.department)
        new_mobile = "18700000111"
        r = self.member.get_update_member(self.user_id, new_mobile)
        assert r["errcode"] == 0
        assert r["errmsg"] == "updated"

        info = self.member.get_acquire_member(self.user_id)
        assert info["mobile"] == new_mobile
        self.member.get_delete_member(self.user_id)

    def test_delete_member(self):
        self.member.get_address_member(self.user_id, self.name, self.mobile, self.department)
        r = self.member.get_delete_member(self.user_id)
        assert r["errcode"] == 0
        assert r["errmsg"] == "deleted"

        info = self.member.get_acquire_member(self.user_id)
        assert info["errcode"] == 60111
        self.member.get_address_member(self.user_id, self.name, self.mobile, self.department)
