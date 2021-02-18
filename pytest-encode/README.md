# 插件开发

该插件是对收集上来的用例集的名字进行中文编码以及 单独执行某个模块的用例集，比如：add

# 打包需要安装的插件

1、setuptools 2、pip install wheel

# 打包命令

python setup.py sdist bdist_wheel

# 打包完成之后的文件描述

1、pytest_encode-1.0.tar.gz这个是该插件的源码包 2、pytest_encode-1.0-py3-none-any.whl这个是该插件的安装包

# 安装pytest_encode插件

pip install dist\pytest_encode-1.0-py3-none-any.whl