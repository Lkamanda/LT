import os, time, unittest
from appium import webdriver
# from LT.base.public_element import Public_element


class LT(unittest.TestCase):

    # def __init__(self):
    #     self.element = Public_element()

    @classmethod
    def setUp(self):
        #PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
        # 连接手机app，初始化一些东西
        desired_caps = {}
        # 手机类型
        desired_caps['platformName'] = 'Android'
        # 被测试手机，版本
        desired_caps['platformVersion'] = '6.0'
        # baa822b7   a82ccd1d Q8JNNNGUOF8L4PON   127.0.0.1:62001 ，
        #  设备名称， adb devices
        desired_caps['deviceName'] = 'Q8JNNNGUOF8L4PON'
        #\desired_caps['app'] = PATH('D:\\apk\\boobuz.apk')
        desired_caps['app'] = r'D:\apk\boobuz.apk'
        #desired_caps['appPackage'] = 'com.erlinyou.worldlist'
        # com.erlinyou.worldlist/com.erlinyou.map.MapActivity/@0xaa1e354
        #desired_caps['appActivity'] = 'com.erlinyou.map.MapActivity' #/@0xda50b9
        # appium 传输中使用自己的输入法，可以传输中文
        desired_caps['unicodKeyboard'] = 'True'
        # 程序结束时重置原来的输入法
        desired_caps['resetKeyboard'] = 'True'
        desired_caps['noReset'] = 'True'
        # desired_caps['autoGrantPermissions'] = 'True'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(10)

    @classmethod
    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

    def test_1(self):
        print('test1')
        self.driver.find_element_by_id("user_avatar_img").click()
        self.driver.find_element_by_id("user_name_tv").click()
        self.driver.find_element_by_id("iv_other_login").click()
        self.driver.find_element_by_id("iv_other_login").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.EditText").send_keys("1599200510")
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//android.widget.LinearLayout[2]/android.widget.EditText").send_keys("5211314zxy.")
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("com.tencent.mm:id/ch7").click()
        time.sleep(10)


if __name__ == '__main__':
    unittest.main(verbosity=2)