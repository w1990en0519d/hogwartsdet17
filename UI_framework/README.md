# UI框架的打造

* 首先搭建一个UI框架
* 把UI框架移植到新的业务
* 把业务代码重复性的功能封装，放入框架内
* 框架内包括：
    * 基础功能代码封装
    * 弹窗处理机制
    * 日志
    * 截图
    * 录屏
    * 报告

# 装饰器 例子：base_page.py

利用装饰器处理黑名单机制  
注意：

* 定义装饰器方法的时候不要传多余的参数，比如不要传self，如果去要的话需要从*args中取出该元素。
* *args，**kwargs两个参数是固定的，不能更改。
* *args是位置参数，**kwargs是关键字参数

# 关键字驱动

* 使用pyyaml加载yaml文件，读取测试的数据
* 使用分支实现不同的关键字
* 将需要的每个page页面创建一个yaml文件数据
* 将企业微信PO改造成关键字驱动，例如base_page.py

# 录屏 conftest.py

* 下载scrcp录屏工具:[scrcpy下载地址](https://github.com/Genymobile/scrcpy/)
* 配置环境变量
* 使用subprocess操作进行scrcpy录屏操作

# 截图

* 使用appium自带的程序进行截图操作，使用allure进行加载
* `allure.attach(instance.screenshot(),attachment_type=allure.attachment_type.PNG)`

# log定制

* log的配置文件，如：logger.py
  * 自己定义log的输出格式
  * 获取log的标识
  * 加入文件句柄和输出流句柄
  * 把文件句柄和输出流句柄加入log的标识
  * 定义log的级别：包括：
    ```CRITICAL: 'CRITICAL', 
    ERROR: 'ERROR',
    WARNING: 'WARNING',
    INFO: 'INFO',
    DEBUG: 'DEBUG',
    NOTSET: 'NOTSET'```
  * 获取log    
