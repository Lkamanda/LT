# 导航详情页面元素
from page.element_error import element_error
from comm.config import *


def navigation_details_input_box_element(driver):
    """导航页面搜索框"""
    try:
        driver.find_element_by_id("com.erlinyou.worldlist:id/searchtextview").click()
    except Exception as e:
        element_error(driver, e)


def navigation_details_goto_element(driver):
    """导航页面到这去"""
    try:
        driver.find_element_by_id("com.erlinyou.worldlist:id/top_map_mode_img").click()
    except Exception as e:
        element_error(driver, e)


def navigation_details_simulation_navigation_element(driver):
    """导航页模拟导航"""
    try:
        driver.find_element_by_id("com.erlinyou.worldlist:id/ll_analog_navi").click()
    except Exception as e:
        element_error(driver, e)


def navigation_details_consult_map_element(driver):
    """查看地图"""
    try:
        driver.find_element_by_id("com.erlinyou.worldlist:id/ll_view_map").click()
    except Exception as e:
        element_error(driver, e)


def navigation_details_navigation_element(driver):
    """导航页导航"""
    try:
        driver.find_element_by_id("com.erlinyou.worldlist:id/ll_navi").click()
    except Exception as e:
        element_error(driver, e)


def navigation_details_quit(driver):
    """导航页退出"""
    try:
        driver.find_element_by_id("com.erlinyou.worldlist:id/quit").click()
    except Exception as e:
        element_error(driver, e)