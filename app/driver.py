# -*-coding:utf-8-*-
from appium import webdriver
import time
from config.configure import Config

class Driver():
    def __init__(self):
        config = Config ()
        self.desired_caps = {'platformName': 'Android',
                    # 'platformVersion': '4.4.2',#夜神
                    # 'deviceName': '127.0.0.1:52001',
                    # 'appPackage': 'com.cubic.autohome',#汽车之家
                    # 'appActivity': '.LogoActivity',
                    'platformVersion': '5.1',  # 真机版本，
                    'deviceName': '85EABNJG8D3Q',  # 设备名称:随便起
                    # 'appPackage': 'com.yonyou.buyer',
                    # 'appActivity': '.ui.guide.ACT_Splash',
                    # 'appPackage': 'com.yonyou.merchart',
                    # 'appActivity': '.ui.guide.ACT_Splash',
                    'appPackage': config.app_package,
                    'appActivity': '.ui.guide.ACT_Splash',
                    'unicodeKeyboard': True,
                    'resetKeyboard': True,
                    'noReset': False,
                    }

    # dr = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    # dr.implicitly_wait(30)

    def connect_appium(self):
        try:
            dr = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
            dr.implicitly_wait(30)
            # logger.info ('appium连接成功，开始启动app')
            # time.sleep(20)
            return dr
        except BaseException as e:
            # logger.error ('appium连接失败，app启动失败! ' + str (e))
            return None
        # return dr

if __name__ == '__main__':
    Driver().connect_appium().quit()
    # Driver().quit()
    time.sleep(2)

    # d.quit()

