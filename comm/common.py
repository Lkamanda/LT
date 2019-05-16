"""
提供一些公共的方法
"""
import time
import os


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
    driver.implicitly_wait(5)
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

