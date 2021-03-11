# DesireCapability 设置

appium:

* skipServerInstallation 跳过UIautomator2 server安装
* skipDeviceInitialization 跳过设备的初始化
* dontStopAppOnReset 测试之前不停止app运行

# appium定位方式

* ID定位:速度快，但是ID定位不建议在appium中用（因为不同的系统的id有可能会不一致）
* XPath定位:该定位方式（速度慢，定位灵活）
* Accessibility ID定位：Accessibility ID在Android上面就是针对'content-desc'属性,在iOS中等针对'name'属性。
* Uiautomator定位： 原生定位方式(速度快，语法复杂)
    * [Uiautomator定位官网](https://developer.android.com/reference/android/support/test/uiautomator/UiSelector.html)  
      Uiautomator 定位
        * 写法：’new UiSelector().text(“text")’

      滚动查找：
        * new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text(“查找的文本”)
          .instance(0));

# PO封装 例子：appPO

1、app.py 封装起来(应用的启动，关闭，重启)  
2、将各个页面以Page页的形式封装起来   
3、driver 复用，封装base_page.py 将__init__方法，find(),finds(), swipe_find() 底层常用的一些方法封装起来，driver 不要暴露出来。   
4、将页面的动态数据可以写成页面数据驱动(yaml文件)

# 日志 收集

设置日志级别

logging.basicConfig(level=logging.INFO)

打印日志

logging.info("find")
logging.info(locator,value)
logging 日志级别划分

```python
_nameToLevel = {
    'CRITICAL': CRITICAL,
    'FATAL': FATAL,
    'ERROR': ERROR,
    'WARN': WARNING,
    'WARNING': WARNING,
    'INFO': INFO,
    'DEBUG': DEBUG,
    'NOTSET': NOTSET,
```

python 会收集当前级别及以上级别的日志。