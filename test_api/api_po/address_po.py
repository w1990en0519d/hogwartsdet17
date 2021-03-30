# *coding:utf-8 *


import requests

from test_api.api_po.base import Base


class MemberPO(Base):

    def get_acquire_member(self, user_id):
        '''
        获取某个成员信息
        :return:
        '''
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get"
        params = {

            "userid": user_id
        }
        r = self.send("GET", url, params=params)
        return r.json()

    def get_address_member(self, user_id: str, name: str, mobile: str, department: list):
        '''
        添加一个成员
        :return:
        '''
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create"
        data = {
            'userid': user_id,
            'name': name,
            'mobile': mobile,
            'department': department
        }
        r = self.send("POST", url, json=data)
        return r.json()

    def get_update_member(self, user_id, mobile):
        '''
        更改某个成员的信息
        :return:
        '''
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update"
        data = {
            'userid': user_id,
            'mobile': mobile
        }
        r = self.send("POST", url, json=data)
        return r.json()

    def get_delete_member(self, user_id):
        '''
        删除某一个成员
        :return:
        '''

        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete"
        params = {
            "userid": user_id
        }
        r = self.send("GET", url, params=params)
        return r.json()
