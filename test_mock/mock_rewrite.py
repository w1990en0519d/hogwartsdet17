# *coding:utf-8 *
"""
Basic skeleton of a mitmproxy addon.

Run as follows: mitmproxy -s anatomy.py
"""
import json

from mitmproxy import http


class Counter:

    def request(self, flow: http.HTTPFlow):
        pass

    def response(self, flow: http.HTTPFlow):
        '''
        使用response事件实现Rewrite
        :param flow:
        :return:
        '''
        # 判断请求的url是否包含指定的url
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t=" in flow.request.pretty_url:
            '''拿到响应数据信息
                flow.response.text是str属性，所以如果要是拿到这个对象的话，必须转换为python字典的数据结构，
                否则只能使用和str相关的用法
            '''
            data = json.loads(flow.response.text)  # 转换为json格式
            data["data"]["items"][0]["quote"]["name"] = "天华超净1234567890"
            data["data"]["items"][0]["quote"]["current"] = -2345678998654
            data["data"]["items"][0]["quote"]["percent"] = 0
            flow.response.text = json.dumps(data)  # 转换为原有的格式


# addons 是mitmproxy 的强制要求的规范
# 一定要使用此变量名存放类的实例
addons = [
    Counter()
]
