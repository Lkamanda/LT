"""
提供一些公共的方法
"""
import time
import os
import re


def screenShot(driver, test_name):
    """对当前页面进行截屏，并存储"""
    # imPath = filePath + '/result/image/' + rq + '.png'
    rq = str_nowTime()
    p = "/report/img_result/"
    imPath = (os.path.dirname(os.path.dirname(__file__)) + p + rq + '%s.png') % test_name
    # print(imPath)
    driver.get_screenshot_as_file(imPath)


def str_nowTime():
    """返回当前时间以字符串形式返回"""
    return time.strftime('%Y-%m-%d %H-%M-%S')


# def case_time():
#     """返回测试日志使用的时间"""
#     return time.strftime('%Y-%M-%d %H')


def get_mobile_size(driver):
    """获取手机屏幕尺寸"""
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return x, y


def swipeUp(driver, t):
    """
    屏幕向上滑动
    :param driver: self.driver
    :param t: 实现滑动的时间
    """
    x, y = get_mobile_size(driver)
    x1 = int(x * 0.5)    # x坐标
    y1 = int(y * 0.75)   # 起始y坐标
    y2 = int(x * 0.25)   # 终点y坐标
    time.sleep(3)
    driver.swipe(x1, y1, x1, y2, t)


def swipeDown(driver, t):
    """屏幕向下滑动"""
    x, y = get_mobile_size(driver)
    x1 = int(x * 0.5)
    y1 = int(y * 0.25)
    y2 = int(y * 0.75)
    driver.swipe(x1, y1, x1, y2, t)


def swipeLeft(driver, t):
    """屏幕向左滑动"""
    x, y = get_mobile_size(driver)
    x1 = int(x * 0.75)
    y1 = int(y * 0.5)
    x2 = int(x * 0.05)
    driver.swipe(x1, y1, x2, y1, t)


def swipeRight(driver, t):
    """屏幕向右滑动"""
    x, y = get_mobile_size(driver)
    x1 = int(x * 0.05)
    y1 = int(y * 0.5)
    x2 = int(x * 0.75)
    driver.swipe(x1, y1, x2, y1, t)


def chat_swipeLeft(driver, t):
    """屏幕向左滑动"""
    x, y = get_mobile_size(driver)
    x1 = int(x * 0.75)
    y1 = int(y * 0.8)
    x2 = int(x * 0.05)
    driver.swipe(x1, y1, x2, y1, t)


def clean_text(driver, length):
    """
    清空输入框
    :param driver: self.driver
    :param length: 输入框内容长度
    :return:
    """
    driver.keyevent(123)  # 123代表光标移动到末尾键
    for i in range(0, length):
        driver.keyevent(67)  # 67退格键


def check_clean_text(length):
    """
    校验清空输入框是否成功
    :param length:
    :return:
    """
    if length == 0:
        return True
    else:
        return False


def get_android_devices():
    android_devices_list = []
    device_config = []
    b = os.popen('adb devices')
    device_text = b.read()
    # 根据换行符对str进行切片

    # print(type(device_text))
    # print(device_text)
    b.close()
    # print(re.split(r'[\s]\s*', device_text))
    device_list = re.split(r'[\n]\n*', device_text)[1:-1]
    for i in device_list:
        print(re.split(r'[\s]\s*', i)[0])
        andoid_devices = re.split(r'[\s]\s*', i)[0]
        android_devices_list.append(andoid_devices)
    print(android_devices_list)
    mobile_config = {
                    "UEUNW16C29005125": "8.0.0",
                     "a82ccd1d": "8.0.0"
                     }
    for i in android_devices_list:
        if i in mobile_config.keys():
            device_config.append((i, mobile_config[i]))
    print(device_config)
    return device_config


if __name__ == '__main__':
    get_android_devices()