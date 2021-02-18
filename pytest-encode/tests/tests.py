'''
该文档测试该插件的简单用法
'''
import pytest


@pytest.mark.parametrize('name', ["哈尼", "哈利"])
def test_a(name):
    print(name)
