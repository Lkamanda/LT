# home page 输入框详情页
from page.element_error import element_error
from comm.config import *


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


def homepage_details_go_home_element(driver):
    """详情页回家"""
    driver.find_element_by_id("rl_home").click()


def homepage_details_go_home_cancel_element(driver):
    """详情页取消回家按钮"""
    driver.find_element_by_id("com.erlinyou.worldlist:id/iv_home_delete")


def homepage_details_go_home_add(driver):
    """详情页未添加回家"""
    driver.find_element_by_id("com.erlinyou.worldlist:id/tv_home_set").click()

