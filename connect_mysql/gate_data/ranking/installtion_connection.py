from appium import webdriver
import time


def get_size(driver):
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return x, y


def swipeUP(driver, t, x, y):
    """获取屏幕尺寸，向下滑动"""
    x1 = int(x*0.5)
    y1 = int(y*0.95)
    y2 = int(y*0.1)
    time.sleep(1)
    driver.swipe(x1, y1, x1, y2, t)


def swipeUP_map(driver, t, x, y):
    """获取屏幕尺寸，向上滑动 华为进入地图页面专用"""
    x1 = int(x*0.5)
    y1 = int(y*0.75)
    y2 = int(y*0.25)
    time.sleep(3)
    driver.swipe(x1, y1, x1, y2, t)


def connect_app(appPackage, appActivity):
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '8.0.0',
        'deviceName': "a82ccd1d",
        # 'com.huawei.appmarket.MainActivity'              'com.huawei.appmarket'
        'appPackage': appPackage,
        'appActivity': appActivity,
        # 'appPackage': 'com.huawei.appmarket',
        # 'appActivity': "com.huawei.appmarket.MainActivity",
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


def get_data_hw(driver, x, y):
    """
    获取华为应用市场旅图app排名
    :param driver: driver
    :param x: 手机屏幕尺寸x
    :param y: 手机屏幕尺寸y
    :return: 华为应用市场旅图app排名
    """
    driver.implicitly_wait(5)
    driver.find_element_by_android_uiautomator('new UiSelector().textContains("分类")').click()
    swipeUP(driver, t=5000, x=x, y=y)
    driver.find_element_by_android_uiautomator('new UiSelector().textContains("出行导航")').click()
    driver.implicitly_wait(5)
    swipeUP_map(driver, t=5000, x=x, y=y)
    driver.find_element_by_xpath("//android.widget.LinearLayout[3]/android.widget.LinearLayout/"
                                 "android.widget.LinearLayout/android.widget.LinearLayout[2]").click()
    hw = []
    global i, item_list
    while True:
        try:
            item_list = driver.find_elements_by_id("com.huawei.appmarket:id/ItemTitle")
        except:
            pass
        print(type(item_list))
        for i in item_list:
            hw.append(i.get_attribute("text"))
            print(i.get_attribute("text"))
        if "旅图" in hw:
            print("遍历结束")
            break
        swipeUP(driver, t=5000, x=x, y=y)

    new_hw = list(set(hw))
    new_hw.sort(key=hw.index)
    print(new_hw)
    print(len(new_hw))
    hw_sort = new_hw.index('旅图') + 1
    print(hw_sort)
    return hw_sort


def get_data_xm(driver, x, y):
    """获取小米应用市场旅图app排名"""
    pass




def run():
    app_dict = {
        'huawei': ["com.huawei.appmarket", "com.huawei.appmarket.MainActivity"],
        "xiaomi": ["com.xiaomi.market", "com.xiaomi.appmarket.MainActivity"],
        'oppo': ["1", "2"],
        '360': ["1", "2"],
    }
    for key in app_dict:
        print(key, app_dict[key])
        if key == "huawei":
            pass
            # driver = connect_app(appPackage=app_dict[key][0], appActivity=app_dict[key][1])
            # x, y = get_size(driver)
            # get_data_hw(driver=driver, x=x, y=y)
        elif key == "xiaomi":
            driver = connect_app(appPackage=app_dict[key][0], appActivity=app_dict[key][1])
            x, y = get_size(driver)
            get_data_xm(driver=driver, x=x, y=y)


if __name__ == '__main__':
    run()








