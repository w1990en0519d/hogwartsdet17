# coding=utf-8

import pytest
import yaml

'''
第三种参数读取yml文件的参数化用法
fixture以及conftest.py公共文件的用法
'''


# 读取cal.yml文件的数据
def get_datas(name, type):
    with open('D:\HogwartsSDET17\\testing\data\cal.yml', encoding='utf-8') as f:
        all_datas = yaml.safe_load(f)
        datas = all_datas[name][type]['datas']
        ids = all_datas[name][type]['ids']
        return datas, ids


# 创建计算器的测试类
class TestCalc:

    # 加法整数测试用例
    def test_add_int(self, cal_fixture, add_int_datas):
        print(f'a={add_int_datas[0]},b={add_int_datas[1]},except_result={add_int_datas[2]}')
        f = add_int_datas
        assert f[2] == cal_fixture.add(f[0], f[1])

    # 加法小数测试用例
    def test_add_float(self, cal_fixture, add_float_datas):
        print(f'a={add_float_datas[0]},b={add_float_datas[1]},result={add_float_datas[2]}')
        f = add_float_datas
        assert f[2] == round(cal_fixture.add(f[0], f[1]), 2)

    # 减法整数测试用例
    def test_subt_int(self, cal_fixture, subt_int_datas):
        print(f'a={subt_int_datas[0]},b={subt_int_datas[1]},except_result={subt_int_datas[2]}')
        f = subt_int_datas
        assert f[2] == cal_fixture.subt(f[0], f[1])

    # 减法小数测试用例
    def test_subt_float(self, cal_fixture, subt_float_datas):
        print(f'a={subt_float_datas[0]},b={subt_float_datas[1]},result={subt_float_datas[2]}')
        f = subt_float_datas
        assert f[2] == round(cal_fixture.subt(f[0], f[1]), 2)

    # 乘法整数测试用例
    def test_mult_int(self, cal_fixture, mult_int_datas):
        print(f'a={mult_int_datas[0]},b={mult_int_datas[1]},except_result={mult_int_datas[2]}')
        f = mult_int_datas
        assert f[2] == cal_fixture.mult(f[0], f[1])

    # 乘法小数测试用例
    def test_mult_float(self, cal_fixture, mult_float_datas):
        print(f'a={mult_float_datas[0]},b={mult_float_datas[1]},result={mult_float_datas[2]}')
        f = mult_float_datas
        assert f[2] == round(cal_fixture.mult(f[0], f[1]), 2)

    # 除法除数不为零的整数测试用例
    def test_div_int(self, cal_fixture, div_int_datas):
        print(f'a={div_int_datas[0]},b={div_int_datas[1]},except_result={div_int_datas[2]}')
        f = div_int_datas
        assert f[2] == cal_fixture.div(f[0], f[1])

    # 除法除数不为零的小数测试用例
    def test_div_float(self, cal_fixture, div_float_datas):
        print(f'a={div_float_datas[0]},b={div_float_datas[1]},result={div_float_datas[2]}')
        f = div_float_datas
        assert f[2] == round(cal_fixture.div(f[0], f[1]), 2)

    # 除法除数为零的测试用例
    def test_div_zero(self, cal_fixture, div_zero_datas):
        print(f'a={div_zero_datas[0]},b={div_zero_datas[1]},result={div_zero_datas[2]}')
        with pytest.raises(ZeroDivisionError) as e:
            f = div_zero_datas
            cal_fixture.div(f[0], f[1])
        assert f[2] in str(e.value)


if __name__ == '__main__':
    pytest.main(-'vs')
