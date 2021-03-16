import allure
from appium.webdriver.common.mobileby import MobileBy


# 定义一个黑名单方法
def handle_black(fun):
    def run(*args, **kwargs):
        # 相当于self
        instance = args[0]
        black_list = ['//*[@resource-id="com.xueqiu.android:id/iv_close"]']
        try:
            return fun(*args, **kwargs)
        except Exception:
            # 截屏操作
            allure.attach(instance.screenshot(), attachment_type=allure.attachment_type.PNG)
            for els_xpath in black_list:
                eles = instance.finds(MobileBy.XPATH, els_xpath)
                if len(eles) > 0:
                    eles[0].click()
                    return fun(*args, **kwargs)

    return run
