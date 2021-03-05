# mumu模拟器连接方式

win版

* adb connect 127.0.0.1:7555  
  adb devices  
  adb shell

mac版

* adb kill-server && adb server && adb shell

# apk的安装两种方式

1.将下载好的apk拖拽到手机里  
2.使用adb install命令安装

* adb install -r apk的路径

# 查看android日志

1.查看全部的日志

* adb logcat

2.查看安装的apk的包名和启动首页

* Windows:adb logcat ActivityManager:I | findstr "cmp"
* mac/Linux： adb logcat ActivityManager:I | grep "cmp"

# DesireCapability

settings 控制 动态页面的等待时长

