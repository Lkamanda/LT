# 导航详情页面元素
from page.element_error import element_error
from comm.config import *


def navigation_details_input_box_element(driver):
    """导航页面搜索框"""
    try:
        return driver.find_element_by_id("com.erlinyou.worldlist:id/searchtextview")
    except Exception as e:
        element_error(driver, e)


def navigation_details_goto_element(driver):
    """导航页面到这去"""
    try:
        driver.find_element_by_id("com.erlinyou.worldlist:id/top_map_mode_img").click()
    except Exception as e:
        element_error(driver, e)

