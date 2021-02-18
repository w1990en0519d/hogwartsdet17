# 项目作业

测试开发作业 1、使用pytest写测试用例 2、主要使用@pytest.mark.parametrize参数化测试用例 3、学习yml文件的用法以及读写yml文件获取数据 4、float精度的控制： round 例子：pi ronud(
pi,2) 结果是3.14 Decimal,使用decimal必须导入Decimal from decimal import Decimal 例子：decimal('0.1')+decimal('0.2')
format(pi, ".2f") 结果是3.14 5、进行异常测试，例如除数为零的时候 with pytest.raises(ZeroDivisionError):
except_result = a/b

# pytest的前置条件和后置条件的几种用法

模块级别的：setup_module/teardown_module 在整个模块的开始和结尾执行一次 函数级别的：set_function/teardown_function 只对不在类中的函数用例生效
类级别的：set_class/teardown_class 在整个类中的开始和结尾执行一次 方法级别的：setup_method/teardown_method,或者setup/teardown,都是在类里面的，
只不过是在每个测试方法前后都执行一次

# 命令行pytest运行

1.执行测试文件：pytest test_xxx.py 2.显示测试过程的详细信息：pytest test_xxx.py -vs 3.只收集测试用例而不执行：pytest collect-only 4.生成执行结果文件：pytest
--junitxml=./result.xml 5.匹配所有用例名称中包含‘add’的测试用例：pytest -k -"add"
6.标签用法： 在用例中加上标签之后:@pytest.mark.xxx xxx表示可以用自带的标签也可以用自己定义的标签 比如login 表示登录的标签 配置可以识别的自定以的标签 定义pytest.ini
[pytest]
markers = login search 就可以使用以下命令运行某一些特定的测试用例 pytest -m "login"
7.回溯fixture的执行过程：pytest --setup-show

# git命令

-创建git本地仓库，初始化本地仓库：git init -查看提交状态：git status 提交到暂存区：git add 文件名 提交到本地库：git commit -m "日志信息"  文件名 查看日志：1.git log 2.git
log --pretty=oneline 3.git log --oneline 4.git reflog 查看某个版本：git reset --hard 版本的索引值

# 在pycharm中配置git

1.打开file——》setting——》version control——》git 2.打开git的界面，选择path to git executable，配置git的安装路径中的cmd\git.exe
3.打开github的界面，配置你的github远程仓库的地址 4.打开tools中的terminal界面配置shell path路径，跟git的一致就行，最后重启pycharm

# allure下载安装

下载地址：https://github.com/allure-framework/allure2/releases/tag/2.13.8
1、先配置jdk的环境 2、配置path系统环境变量，例如：D:\installing\Python38\allure-2.13.8\allure-2.13.8\bin

# allure 用法

为测试用例分类： @allure.feature("name")
@allure.story("name")
为测试 用例加标题 @allure.title()
生成测试报告 Allure2 解析过程：

1. 安装 allure2
2. Allure help 帮助文档
3. 生成 allure 测试结果 ：pytest —alluredir=./report/
4. 展示报告：allure serve ./report
5. 生成最终版本的报告： allure generate ./report 在本地搭建一个网站服务（例如：Django） python manage.py runserver  (http://127.0.0.1:8000/)

# pytest 常用的插件

pip install pytest-ordering 控制用例的执行顺序 pip install pytest-dependency 控制用例的依赖关系 pip install pytest-xdist 分布式并发执行测试用例 pip
install pytest-rerunfailures 失败重跑 pip install pytest-assume 多重较验 pip install pytest-random-order 用例随机执行 pip intall
pytest-html 测试报告

# pytest.ini 的用法

参考pytest --help

Demo:
[pytest]
markers = login search python_files = check_* test_*
python_functions = check_* test_*
addopts = -vs --alluredir=./result

# Fixture 用法

Fixture 是为了测试⽤例的执⾏，初始化⼀些数据和⽅法 1、类似 setUp, tearDown 功能，但⽐ setUp, tearDown 更灵活 2、直接通过函数名字调⽤或使用装饰器@pytest.mark.usefixtures(
‘test1’)
3、允许使用多个Fixture 4、使用 autouse 自动应用，如果要返回值，需要传fixture函数名 5、作用域（session>module>class>function） 6、也可以提供测试数据，实现参数化的功能
7、Fixture也可以调用Fixture -setup-show 回溯 fixture 的执行过程

# conftest.py 用法

1、数据共享的文件，名字是固定的，不能修改 2、可以存放fixture , hook 函数 3、就近生效（如果不在同一个文件夹下，离测试文件最近的conftest.py 生效） 4、当前目录一定要有__init__.py
文件，也就是要创建一个包