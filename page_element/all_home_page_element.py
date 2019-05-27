# home page element
from page.element_error import element_error
from comm.config import *


def homepage_roam_element(driver):
    """点击主页漫游页面"""
    try:
        driver.find_element_by_xpath("//android.widget.LinearLayout/android.widget.LinearLayout"
                                 "/android.widget.ImageView").click()
    except Exception as e:
        element_error(driver, e)


def homepage_input_box(driver):
    """主页面输入框"""
    try:
        driver.find_element_by_id("searchtextview").click()
    except Exception as e:
        element_error(driver, e)


def homepage_input_box_details(driver, n):
    """
    详情页输入框
    :param driver:
    :param n:
    n = 1 : 输入框内输入：家的地址
    :return:
    """
    try:
        myconfig = MyConfig()
        place = myconfig.get_homepage_input(n)
        driver.find_element_by_id("details").send_key(place)
    except Exception as e:
        element_error(driver, e)
