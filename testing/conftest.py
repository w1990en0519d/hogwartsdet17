from typing import List

import pytest

from pythoncode.calculator import Calculator
from testing.test_calculator2 import get_datas

'''
fixture的用法，包括：前置条件，后置条件以及params和ids的用法
conftest.py名称不能更改，是固定的
'''


@pytest.fixture()
def cal_fixture():
    print(f"测试方法的前置条件：{'开始计算'}")
    # 实例化一个类
    calc = Calculator()
    yield calc
    print(f"测试类的后置条件：{'开算结束'}")


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
    print(items)
    items.reverse()


# 加法整数fixture参数化
@pytest.fixture(params=get_datas('add', 'int')[0], ids=get_datas('add', 'int')[1])
def add_int_datas(request):
    return request.param


# 加法小数数fixture参数化
@pytest.fixture(params=get_datas('add', 'float')[0], ids=get_datas('add', 'float')[1])
def add_float_datas(request):
    return request.param


# 减法整数fixture参数化
@pytest.fixture(params=get_datas('subt', 'int')[0], ids=get_datas('subt', 'int')[1])
def subt_int_datas(request):
    return request.param


# 减法小数fixture参数化
@pytest.fixture(params=get_datas('subt', 'float')[0], ids=get_datas('subt', 'float')[1])
def subt_float_datas(request):
    return request.param


# 乘法法整数fixture参数化
@pytest.fixture(params=get_datas('mult', 'int')[0], ids=get_datas('mult', 'int')[1])
def mult_int_datas(request):
    return request.param


# 乘法法小数fixture参数化
@pytest.fixture(params=get_datas('mult', 'float')[0], ids=get_datas('mult', 'float')[1])
def mult_float_datas(request):
    return request.param


# 除法整数fixture参数化
@pytest.fixture(params=get_datas('div', 'int')[0], ids=get_datas('div', 'int')[1])
def div_int_datas(request):
    return request.param


# 除法小数fixture参数化
@pytest.fixture(params=get_datas('div', 'float')[0], ids=get_datas('div', 'float')[1])
def div_float_datas(request):
    return request.param


# 除数为零fixture参数化
@pytest.fixture(params=get_datas('div', 'zero')[0], ids=get_datas('div', 'zero')[1])
def div_zero_datas(request):
    return request.param
