import os, time, unittest
from appium import webdriver


class LT(unittest.TestCase):

    @classmethod
    def setUp(self):
        # 连接手机app，初始化一些东西
        desired_caps = {}
        # 手机类型
        desired_caps['platformName'] = 'Android'
        # 被测试手机，版本
        desired_caps['platformVersion'] = '6.0'
        # baa822b7   a82ccd1d Q8JNNNGUOF8L4PON   127.0.0.1:62001 ，
        #  设备名称， adb devices
        desired_caps['deviceName'] = 'Q8JNNNGUOF8L4PON'
        desired_caps['app'] = r'D:\apk\boobuz.apk'
        desired_caps['appPackage'] = 'com.erlinyou.worldlist'
        desired_caps['appActivity'] = 'com.erlinyou.map.MapActivity' #/@0xda50b9
        # appium 传输中使用自己的输入法，可以传输中文
        desired_caps['unicodKeyboard'] = 'True'
        # 程序结束时重置原来的输入法
        desired_caps['resetKeyboard'] = 'True'
        desired_caps['noReset'] = 'True'
        time.sleep(5)
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(10)

    @classmethod
    def tearDown(self):
        self.driver.close()

    def test_1(self):
        print('test1')
