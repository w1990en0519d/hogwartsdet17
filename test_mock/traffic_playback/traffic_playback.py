# *coding:utf-8 *

from mitmproxy import http


class Counter:
    '''
    录制接口自动化测试脚本
        1.接口请求的数据信息:
            mitmproxy 拿到请求过程中的数据信息
        2.接口请求的脚本模板:
            事先定义好一个脚本模板
    '''

    def request(self, flow: http.HTTPFlow):
        url = flow.request.pretty_url
        method = flow.request.method
        with open("template.txt") as f:
            # 拿到文本字符串数据
            data = f.read()
            new_data = data.format(method=method, url=url)
        # 将替换好的数据信息紫萼如模板文件
        with open("./template.py", "w", encoding="utf-8") as f:
            f.write(new_data)

    def response(self, flow: http.HTTPFlow):
        pass


# addons 是mitmproxy 的强制要求的规范
# 一定要使用此变量名存放类的实例
addons = [
    Counter()
]
