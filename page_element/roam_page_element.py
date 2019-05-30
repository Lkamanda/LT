from page.element_error import element_error
from comm.config import *


def roam_page_look_more_element(driver):
    """漫游页面查看更多"""
    try:
        driver.find_element_by_id("com.erlinyou.worldlist:id/rl_heli_look_more").click()
    except Exception as e:
        element_error(driver, e)


def roam_page_goto_element(driver):
    """到这去"""
    try:
        driver.find_element_by_id("com.erlinyou.worldlist:id/ll_top_map_mode_img").click()
    except Exception as e:
        element_error(driver, e)


def roam_page_choice_ldmark(driver, n):
    """选择当前页的第几个landmark"""
    try:
        driver.find_element_by_xpath("//android.widget.RelativeLayout[%s]/android.widget.RelativeLayout/android.widget.ImageView" % n).click()
    except Exception as e:
        element_error(driver, e)

