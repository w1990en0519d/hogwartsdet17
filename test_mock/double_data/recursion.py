import json


def handle_data(data):
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
        data = [handle_data(item) for item in data]

    elif isinstance(data, dict):
        for key, value in data.items():
            data[key] = handle_data(value)

    elif isinstance(data, str):
        data = data + "A"

    elif isinstance(data, bool):
        data = data
    elif isinstance(data, (int, float)):
        data = data * 2
    else:
        data = data

    return data


if __name__ == '__main__':
    data = handle_data(json.load(open("../xueqiu.json", encoding="utf-8")))
    with open("../xueqiu1.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
