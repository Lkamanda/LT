
from comm.mylog import mylogger, screenShot


def element_error(driver, e):
    """对定位元素异常的处理"""
    mylogger.error(e)
    test_name = "定位失败"
    screenShot(driver, test_name)

