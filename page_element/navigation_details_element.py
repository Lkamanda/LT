# 导航详情页面元素
from page.element_error import element_error
from comm.config import *
from comm.usuallymodule import mylogger

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
        driver.find_element_by_id("com.erlinyou.worldlist:id/ll_quit").click()
    except Exception as e:
        element_error(driver, e)


def navigation_details_trip_mode(driver, mode):
    """
    出行方式的选择
    :param driver: self.driver
    :param mode:
    mode = 2 : 汽车
    mode = 3 ：公交
    mode = 4 ：地铁
    mode = 5 ：步行
    mode = 6 : 自行车
    :return:
    """
    try:
        driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView/android.widget.LinearLayout[%s]/android.widget.ImageView" % mode).click()
    except Exception as e:
        element_error(driver, e)


def navigation_details_collection(driver):
    """收藏"""
    try:
        ele = driver.find_element_by_id("com.erlinyou.worldlist:id/favorite_tv").text
        mylogger.info("ele:%s" % ele)
        if ele == "收藏":
            mylogger.info("该景点未收藏")
            driver.implicitly_wait(5)
            driver.find_element_by_id("com.erlinyou.worldlist:id/favorite_layout").click()
        elif ele == "已收藏":
            mylogger.info("该地点已收藏")
    except Exception as e:
        element_error(driver, e)

