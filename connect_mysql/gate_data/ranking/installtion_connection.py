from appium import webdriver
import time


def swipeUP(driver, t):
    """获取屏幕尺寸，向下滑动"""
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    x1 = int(x*0.5)
    y1 = int(y*0.5)
    y2 = int(y*0.75)
    time.sleep(3)
    driver.swipe(x1, y1, x1, y2, t)


def connect_app(appPackage, appActivity):
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '8.0.0',
        'deviceName': "a82ccd1d",
        # 'appPackage': 'com.erlinyou.worldlist',
        # 'appActivity': 'com.erlinyou.map.Erlinyou',
        # 'com.huawei.appmarket.MainActivity'              'com.huawei.appmarket'
        'appPackage': 'com.huawei.appmarket',
        'appActivity': "com.huawei.appmarket.MainActivity",
        'unicodeKeyboard': True,
        'resetKeyboard': True,
        'noReset': True,
    }

    # time.sleep(3)
    try:
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        # myLog.logger().info('driver加载成功 %s', cls.driver)
        return driver
    except Exception as e:
        # myLog.logger().info('driver加载失败 %s', e)
        print(e)


def get_data_hw(driver):
    driver.implicitly_wait(5)
    driver.find_element_by_android_uiautomator('new UiSelector().textContains("分类")').click()
    swipeUP(driver, t=5000)
    driver.find_element_by_android_uiautomator('new UiSelector().textContains("出行导航")').click()




def run():
    app_list = {
        'huawei': ["com.huawei.appmarket", "com.huawei.appmarket.MainActivity"],
    }
    for i in app_list:
        pass







if __name__ == '__main__':
    get_data_hw(driver=connect_app())
