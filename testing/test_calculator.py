# coding=utf-8

import pytest
import yaml

# 在导入包之前导入包的路径
import sys

sys.path.append('..')

from pythoncode.calculator import Calculator

'''
第一种读取yml文件参数化方法
setup和teardown以及装饰器@pytest.mark.parametrize的用法
'''


# 定义一个读取yml文件的函数，返回yml文件中数组
def get_datas(name, type):
    with open("D:\HogwartsSDET17\\testing\data\cal.yml", 'r', encoding='utf-8') as f:
        all_datas = yaml.safe_load(f)
        datas = all_datas[name][type]['datas']
        ids = all_datas[name][type]['ids']
        return (datas, ids)


class TestCator:
    # datas: list = get_datas()
    add_int = get_datas('add', 'int')
    add_float = get_datas('add', 'float')
    subt_int = get_datas('subt', 'int')
    subt_float = get_datas('subt', 'float')
    mult_int = get_datas('mult', 'int')
    mult_float = get_datas('mult', 'float')
    div_int = get_datas('div', 'int')
    div_float = get_datas('div', 'float')
    div_zero = get_datas('div', 'zero')

    # 测试类的前置条件
    def setup_class(self):
        print(f"测试类前置条件：{'开始计算'}")

    # 测试类的后置条件
    def teardown_class(self):
        print(f"测试类的后置条件：{'开算结束'}")

    # 测试方法的前置条件
    def setup(self):
        print(f"测试方法的前置条件：{'开始计算'}")
        # 实例化一个类
        self.calc = Calculator()

    # 测试方法的后置条件
    def teardown(self):
        print(f"测试方法的后置条件：{'计算结束'}")

    # 参数化加法整数测试用例
    @pytest.mark.parametrize("a, b, except_result", add_int[0], ids=add_int[1])
    def test_add_int(self, a, b, except_result):
        result = self.calc.add(a, b)
        print(f"a={a},b={b},except_result={except_result},result={result}")
        assert except_result == result

    # 参数化加法小数测试用例
    @pytest.mark.parametrize('a, b, except_result', add_float[0], ids=add_float[1])
    def test_add_loat(self, a, b, except_result):
        result = self.calc.add(a, b)
        result = float(format(result, ".2f"))
        print(f"a={a},b={b},except_result={except_result},result={result}")
        assert except_result == result

    # 参数化减法整数测试用例
    @pytest.mark.parametrize('a, b, except_result', subt_int[0], ids=subt_int[1])
    def test_subt_int(self, a, b, except_result):
        result = self.calc.subt(a, b)
        print(f"a={a},b={b},except_result={except_result},result={result}")
        assert except_result == result

    # 参数化减法小数测试用例
    @pytest.mark.parametrize('a, b, except_result', subt_float[0], ids=subt_float[1])
    def test_subt_float(self, a, b, except_result):
        result = self.calc.subt(a, b)
        result = float(format(result, ".2f"))
        print(f"a={a},b={b},except_result={except_result},result={result}")
        assert except_result == result

    # 参数化乘法整数测试用例
    @pytest.mark.parametrize('a, b, except_result', mult_int[0], ids=mult_int[1])
    def test_mult_int(self, a, b, except_result):
        result = self.calc.mult(a, b)
        print(f"a={a},b={b},except_result={except_result},result={result}")
        assert except_result == result

    # 参数化乘法小数测试用例
    @pytest.mark.parametrize('a, b, except_result', mult_float[0], ids=mult_float[1])
    def test_mult_float(self, a, b, except_result):
        result = self.calc.mult(a, b)
        result = float(format(result, ".2f"))
        print(f"a={a},b={b},except_result={except_result},result={result}")
        assert except_result == result

    # 参数化除法不为零的整数的测试用例
    @pytest.mark.parametrize('a, b, except_result', div_int[0], ids=div_int[1])
    def test_div_int(self, a, b, except_result):
        result = self.calc.div(a, b)
        print(f"a={a},b={b},except_result={except_result},result={result}")
        assert except_result == result

    # 参数化除法不为零的小数的测试用例
    @pytest.mark.parametrize('a, b, except_result', div_float[0], ids=div_float[1])
    def test_div_float(self, a, b, except_result):
        result = self.calc.div(a, b)
        result = float(format(result, ".2f"))
        print(f"a={a},b={b},except_result={except_result},result={result}")
        assert except_result == result

    # 参数化除数为零的测试用例
    @pytest.mark.parametrize('a, b, except_result', div_zero[0], ids=div_zero[1])
    def test_div_zero(self, a, b, except_result):
        with pytest.raises(ZeroDivisionError) as e:
            self.calc.div(a, b)
        print(f"a={a},b={b},except_result={except_result},e.value={e.value}")
        assert except_result in str(e.value)


if __name__ == '__main__':
    pytest.main('-v', '-s')
