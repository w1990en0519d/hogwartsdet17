# coding=utf-8

import pytest
import yaml

# 在导入包之前导入包的路径
import sys

sys.path.append('..')

from pythoncode.calculator import Calculator

'''
第二种读取yml文件参数化方法
setup和teardown以及装饰器@pytest.mark.parametrize的用法
'''


# 定义一个读取yml文件的函数，返回yml文件中数组
def get_datas():
    with open("D:\HogwartsSDET17\\testing\data\cal1.yml", 'r', encoding='utf-8') as f:
        datas = yaml.safe_load(f)
        return (datas['add_int']['datas'], datas['add_int']['ids'],
                datas['add_float']['datas'], datas['add_float']['ids'],
                datas['subt_int']['datas'], datas['subt_int']['ids'],
                datas['subt_float']['datas'], datas['subt_float']['ids'],
                datas['mult_int']['datas'], datas['mult_int']['ids'],
                datas['mult_float']['datas'], datas['mult_float']['ids'],
                datas['div_int']['datas'], datas['div_int']['ids'],
                datas['div_float']['datas'], datas['div_float']['ids'],
                datas['div_zero']['datas'], datas['div_zero']['ids'])


class TestCator:
    datas: list = get_datas()

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
    @pytest.mark.parametrize("a, b, except_result", datas[0], ids=datas[1])
    def test_add_int(self, a, b, except_result):
        result = self.calc.add(a, b)
        print(f"a={a},b={b},except_result={except_result},result={result}")
        assert except_result == result

    # 参数化加法小数测试用例
    @pytest.mark.parametrize("a, b, except_result", datas[2], ids=datas[3])
    def test_add_float(self, a, b, except_result):
        result = self.calc.add(a, b)
        result = float(format(result, ".2f"))
        print(f"a={a},b={b},except_result={except_result},result={result}")
        assert except_result == result

    # 参数化减法整数测试用例
    @pytest.mark.parametrize("a, b, except_result", datas[4], ids=datas[5])
    def test_subt_int(self, a, b, except_result):
        result = self.calc.subt(a, b)
        print(f"a={a},b={b},except_result={except_result},result={result}")
        assert except_result == result

    # 参数化减法小数测试用例
    @pytest.mark.parametrize("a, b, except_result", datas[6], ids=datas[7])
    def test_subt_float(self, a, b, except_result):
        result = self.calc.subt(a, b)
        result = float(format(result, ".2f"))
        print(f"a={a},b={b},except_result={except_result},result={result}")
        assert except_result == result

    # 参数化乘法测试用例
    @pytest.mark.parametrize("a, b, except_result", datas[8], ids=datas[9])
    def test_mult_int(self, a, b, except_result):
        result = self.calc.mult(a, b)
        print(f"a={a},b={b},except_result={except_result},result={result}")
        assert except_result == result

    # 参数化乘法测试用例
    @pytest.mark.parametrize("a, b, except_result", datas[10], ids=datas[11])
    def test_mult_float(self, a, b, except_result):
        result = self.calc.mult(a, b)
        result = float(format(result, ".2f"))
        print(f"a={a},b={b},except_result={except_result},result={result}")
        assert except_result == result

    # 参数化除数不为零整数的测试用例
    @pytest.mark.parametrize('a, b, except_result', datas[12], ids=datas[13])
    def test_div_int(self, a, b, except_result):
        result = self.calc.div(a, b)
        print(f"a={a},b={b},except_result={except_result},result={result}")
        assert except_result == result

    # 参数化除数不为零小数的测试用例
    @pytest.mark.parametrize('a, b, except_result', datas[14], ids=datas[15])
    def test_div_float(self, a, b, except_result):
        result = self.calc.div(a, b)
        result = float(format(result, ".2f"))
        print(f"a={a},b={b},except_result={except_result},result={result}")
        assert except_result == result

    # 参数化除数为零的测试用例
    @pytest.mark.parametrize('a, b, except_result', datas[16], ids=datas[17])
    def test_div_zero(self, a, b, except_result):
        with pytest.raises(ZeroDivisionError) as e:
            self.calc.div(a, b)
        print(f"a={a},b={b},except_result={except_result},e.value={e.value}")
        assert except_result in str(e.value)


if __name__ == '__main__':
    pytest.main('-v', '-s')
