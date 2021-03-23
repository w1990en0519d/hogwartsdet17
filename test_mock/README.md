# mitmproxy介绍

* 安装
    * 建议直接使用: pip install mitmproxy==5.2.0 (新版本不稳定)
    * windows
        * 在 windows 中，以管理员身份运行 cmd 或 power shell
        * 命令：
            * pip install pipx
            * pipx install mitmproxy
    * mac
        * brew install mitmproxy
    * 检查是否安装成功
        * mitmdump --version

* 证书
    * pc端证书安装
        * 设置proxy
        * 输入 mitmdump， 要保证监听端口和设置端口一致
        * 进入mitm.it
        * 选择系统下载证书并安装
        * 验证https 的包是否可以抓取成功
    * 手机端
        * 设置proxy， 手机端的监听端口设置一致
        * 输入 mitmdump， 要保证监听端口和设置端口一致
        * 进入mitm.it
        * 选择系统下载证书并安装
        * 验证https 的包是否可以抓取成功

* 工具使用
    * mitmproxy： 命令行可交互式工具，仅适用于mac
    * mitmweb： 网页端的工具
    * mitmdump： 命令行显示工具

* mitmproxy官网介绍
    * [插件链接](https://docs.mitmproxy.org/stable/addons-overview/)
        * addons 是mitmproxy 的强制要求的规范,一定要使用此变量名存放类的实例
        ```
      addons = [
            Counter()
      ]
      ```
    * [事件链接](https://docs.mitmproxy.org/stable/addons-events/)
        * 事件的命名不要随便修改，严格遵循mitmproxy的规范

* mitmdump 常用参数
    * -s：指定关联的python脚本
    * -p：指定监听端口