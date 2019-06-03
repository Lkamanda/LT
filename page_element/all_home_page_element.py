# home page 输入框详情页
from page.element_error import element_error
from comm.config import *


# def homepage_input_box_details(driver, n):
#     """
#     详情页输入框
#     :param driver:
#     :param n:
#     n = 1 : 输入框内输入：家的地址
#     :return:
#     """
#     try:
#         myconfig = MyConfig()
#         place = myconfig.get_homepage_input(n)
#         driver.find_element_by_id("details").send_key(place)
#     except Exception as e:
#         element_error(driver, e)


def homepage_details_go_home_element(driver):
    """详情页回家"""
    driver.find_element_by_id("rl_home").click()


def homepage_details_go_home_cancel_element(driver):
    """详情页取消回家按钮"""
    driver.find_element_by_id("com.erlinyou.worldlist:id/iv_home_delete")


def homepage_details_go_home_cancel_element_1(driver):
    """详情页取消回家按钮"""
    driver.find_element_by_id("com.erlinyou.worldlist:id/iv_home_delete").click()


def homepage_details_go_home_add(driver):
    """详情页未添加回家"""
    driver.find_element_by_id("com.erlinyou.worldlist:id/tv_home_set").click()


def homepage_details_go_home_add_1(driver):
    """详情页未添加回家"""
    driver.find_element_by_id("com.erlinyou.worldlist:id/tv_home_set")


def homepage_details_go_company_element(driver):
    """详情页回公司"""
    driver.find_element_by_id("com.erlinyou.worldlist:id/rl_company").click()


def homepage_details_go_company_add_element(driver):
    """添加公司"""
    driver.find_element_by_id("com.erlinyou.worldlist:id/tv_company_set").click()


def homepage_details_go_company_cancel_element(driver):
    """取消公司"""
    driver.find_element_by_id("com.erlinyou.worldlist:id/iv_company_delete")
