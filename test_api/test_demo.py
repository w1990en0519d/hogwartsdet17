# *coding:utf-8 *
import requests


class TestMember:

    def setup(self):
        # 设置token为前置条件
        self.token = self.get_token()
        # 设置一个代理
        self.proxies = {
            "https": "http://127.0.0.1:8080"
        }

    def get_token(self):
        '''
        获取access_token信息
        :return:
        '''
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={'ww2125bc5c6daa14bb'}&corpsecret={'JWlSUwyQL0GfdhOKj4ZHFq3lUCtUObDfOpQQN8NQ-J0'}"
        r = requests.get(url)
        return r.json()['access_token']

    def test_acquire_member(self):
        '''
        获取某个成员信息
        :return:
        '''
        user_id = 'ZhangSan'
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid={user_id}"
        r = requests.get(url)
        assert r.json()["name"] == "张三"
        print(r.json())

    def test_address_member(self):
        '''
        添加一个成员
        :return:
        '''
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}"
        data = {
            'userid': 'a0001',
            'name': '苏檀儿',
            'mobile': '+86 18700000012',
            'department': [1]
        }
        # proxies：采用http，https代理     verify：是否开启ssl代理
        r = requests.post(url, json=data, proxies=self.proxies, verify=False)
        assert r.json()["errmsg"] == 'created'
        print(r.json())

    def test_update_member(self):
        '''
        更改某个成员的信息
        :return:
        '''
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}"
        data = {
            'userid': 'a0001',
            'mobile': '18711111111'
        }
        r = requests.post(url, json=data)
        assert r.json()['errmsg'] == 'updated'
        print(r.json())

    def test_delete_member(self):
        '''
        删除某一个成员
        :return:
        '''
        user_id = 'a0001'
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid={user_id}"
        r = requests.get(url)
        assert r.json()['errmsg'] == 'deleted'
        print(r.json())
