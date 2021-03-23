import json

from mitmproxy import http


class Counter:
    def request(self, flow):
        pass

    def response(self, flow: http.HTTPFlow):
        '''
        使用递归算法实现倍增响应信息数据
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
            data = self.handle_data(data)
            flow.response.text = json.dumps(data)  # 转换为原有的格式

    def handle_data(self, data):
        """
        递归算法，如果是list就继续遍历列表中的元素
        如果是dict就继续遍历key对应的value
        如果是bool就继续遍历
        如果是整型或者float，做倍增
        如果是str，做 + "A"操作
        :param data: 传入的数据信息
        :return: 递归过后的数据信息
        """
        # 1.罗列各种情况 2.针对不同的数据结构做不同的数据处理
        if isinstance(data, list):
            # data_new = []
            # for item in data:
            #    data_new.append(handle_data(item))
            # 把原本的遍历列表操作使用列表推导式表达出来
            data = [self.handle_data(item) for item in data]

        elif isinstance(data, dict):
            for key, value in data.items():
                data[key] = self.handle_data(value)

        elif isinstance(data, str):
            data = data

        elif isinstance(data, bool):
            data = data
        elif isinstance(data, (int, float)):
            data = data * 3
        else:
            data = data

        return data


# addons 是mitmproxy 的强制要求的规范
# 一定要使用此变量名存放类的实例
addons = [
    Counter()
]
