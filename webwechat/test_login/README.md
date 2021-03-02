# web企业微信自动化实战一 例子：test_login

一.利用浏览器复用实现登录操作，例如chrome 
    首先配置浏览器的环境变量：path：C:\Program Files\Google\Chrome\Application 
    运行cmd，打开浏览器：chrome -remote-debugging-port=9222，端口号9222可以改变 
    python函数里也要对应的端口号： 
        chrome_arg=webdriver.ChromeOptions()
        chrome_arg.debugger_address='127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=chrome_arg)
二.利用cookie实现登录操作 
    首先要获取cookie并且保存到文件方法二，代码如下：
        cookies = self.driver.get_cookies()
        with open('./cookies.txt','w',encoding='utf-8') as f:
          f.write(json.dumps(cookies))
    首先要获取cookie并且保存到文件方法一，代码如下： 
        cookies = self.driver.get_cookies()
        with open('./cookies.txt','w',encoding='utf-8') as f:
          json.dump(cookies,f)
    读取文件cookie进行登录操作方法一，代码如下： 
        with open('./cookies.txt','r',encoding='utf-8') as f:
          raw_cookies = f.read()
          cookies = json.loads(raw_cookies)
    读取文件cookie进行登录操作方法二，代码如下： 
        with open('./cookies.txt','r',encoding='utf-8') as f:
          cookies =json.load(f)
