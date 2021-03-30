import requests


class Base:
    def __init__(self):
        self.s = requests.Session()
        self.token = self.get_token()
        self.s.params = {
            "access_token": self.token
        }

    def get_token(self):
        '''
        获取access_token信息
        :return:
        '''
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        params = {
            "corpid": "ww2125bc5c6daa14bb",
            "corpsecret": "JWlSUwyQL0GfdhOKj4ZHFq3lUCtUObDfOpQQN8NQ-J0"
        }
        r = self.s.get(url, params=params)
        return r.json()['access_token']

    def send(self, *args, **kwargs):
        return self.s.request(*args, **kwargs)
