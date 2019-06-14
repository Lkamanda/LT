from appium import webdriver
import time
from comm.common import *

class webDriver:
    @classmethod
    def tearDownClass(cls):
        print('整个测试类结束')
        cls.driver.quit()
        print('driver quit')

    # 整个类开始和结束执行
    @classmethod
    def setUpClass(cls, serial, newPort, systemPort):
        """

        :param serial: udid  mobile_config[0][1]
        :param newPort:
        :param systemPort:
        :return:
        """
        global driver
        mobile_config = [("UEUNW16C29005125", "8.0.0"), ("a82ccd1d", "8.0.0")]
        mobile_config = get_android_devices()
        desired_caps = {'platformName': 'Android',     # 手机类型
                        'platformVersion': mobile_config[0][1],   # 被测试手机，   baa822b7
                        'deviceName': 'Android',
                        'udid': mobile_config[0][0],
                        'appPackage': 'com.erlinyou.worldlist',
                        'appActivity': 'com.erlinyou.map.Erlinyou',
                        'unicodeKeyboard': True,     # appium 传输中使用自己的输入法，可以传输中文
                        'resetKeyboard': True,      # 程序结束时重置原来的输入法
                        'noReset': True,       # 如果app存在则不重新安装
                        # 'autoGrantPermissions': 'True'
                        # 'app': r"C:\Users\zhoujialin\PycharmProjects\aut_LT\LT\apps\boobuz.apk"
                        # desired_caps['autoGrantPermissions'] = 'True'
                        }
        time.sleep(3)
        try:
            cls.driverc = webdriver.Remote('http://127.0.0.1;' + str(newPort) + '/wd/hub', desired_caps)
            # cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            # myLog.logger().info('driver加载成功 %s', cls.driver)
        except Exception as e:
            # myLog.logger().info('driver加载失败 %s', e)
            print(e)

    # 整个测试类结束执行
    # 每条测试用例开始都执行
    @staticmethod
    def setUp():
        print('test case start')

    # 每条测试用例结束都执行
    @staticmethod
    def tearDown():
        print('test case end ')


