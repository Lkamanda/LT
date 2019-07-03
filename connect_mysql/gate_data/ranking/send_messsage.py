from appium import webdriver
# "com.huawei.appmarket/.MarketActivity:"
import time
import os



def connect_app():
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '8.0.0',
        'deviceName': "a82ccd1d",
        'appPackage': 'com.erlinyou.worldlist',
        'appActivity': 'com.erlinyou.map.Erlinyou',
        # 'appPackage': 'com.huawei.appmarket',
        # 'appActivity': "com.huawei.MarketActivity",
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


def send_content(driver, content):
    # driver.implicitly_wait(5)
    # driver.find_element_by_id("chat_img").click()
    # driver.find_element_by_android_uiautomator('new UiSelector().textContains("账号密码登录") ').click()
    # time.sleep(4)
    # adb1 = 'adb shell ime set com.sohu.inputmethod.sogou.xiaomi/.SogouIME'
    # adb3 = 'adb shell ime set io.appium.android.ime/.UnicodeIME'
    # os.system(adb1)
    # driver.implicitly_wait(5)
    # driver.find_element_by_id("com.erlinyou.worldlist:id/et_username").send_keys("13231533164")
    # os.system(adb3)
    # driver.find_element_by_id("com.erlinyou.worldlist:id/et_pwd").send_keys(u"5211314")
    # driver.find_element_by_id("com.erlinyou.worldlist:id/submit").click()
    driver.implicitly_wait(5)
    driver.find_element_by_id('chat_img').click()
    time.sleep(1)
    driver.implicitly_wait(20)
    adb1 = 'adb shell ime set com.sohu.inputmethod.sogou.xiaomi/.SogouIME'
    adb3 = 'adb shell ime set io.appium.android.ime/.UnicodeIME'
    os.system(adb3)
    driver.find_element_by_android_uiautomator('new UiSelector().textContains("zhoujialin")').click()
    driver.find_element_by_id("et_msg").send_keys(content)
    time.sleep(3)
    os.system(adb1)
    driver.find_element_by_id("com.erlinyou.worldlist:id/btnSend").click()
    # driver.press_keycode(4)
    # time.sleep(1)
    # driver.press_keycode(4)
    # driver.find_element_by_id('com.erlinyou.worldlist:id/user_avatar_img').click()
    # x = driver.get_window_size()['width']
    # y = driver.get_window_size()['height']
    # t=6000
    # x1 = int(x * 0.5)  # x坐标
    # y1 = int(y * 0.75)  # 起始y坐标
    # y2 = int(x * 0.25)  # 终点y坐标
    # time.sleep(3)
    # driver.swipe(x1, y1, x1, y2, t)
#
# a = u"""
# our track, 30th  June situation:
# boobuz
#
# 360:0 - 51 - 258th
# Baidu:0 - 7 - no
# Huawei:0 - 39 -40th
# Mi:0 - 35 - 36th
# OPPO:0 - 6 - 113th
# Tencent:0 - 27 - no
# VIVO:0 - 44 - no
# WDJ:0 - 10 - no
#
# Apple:0 - 35- 169th
#
# total download: 254
# """

if __name__ == '__main__':
    send_content(driver=connect_app(),content=a)