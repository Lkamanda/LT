from comm.config import MyConfig
from page.element_error import element_error


def userAvatar_element(driver):
    """点击首页用户头像"""
    try:
        driver.find_element_by_id('user_avatar_img').click()
    except Exception as e:
        element_error(driver, e)


def mainChat_element(driver):
    """主页消息入口 main_chat  id"""
    driver.find_element_by_id("chat_img").click()


def homepage_roam_element(driver):
    """点击主页漫游页面"""
    try:
        driver.find_element_by_id("com.erlinyou.worldlist:id/iv_starthelicopter").click()
    except Exception as e:
        element_error(driver, e)


def homepage_input_box(driver):
    """主页面输入框"""
    try:
        driver.find_element_by_id("searchtextview").click()
    except Exception as e:
        element_error(driver, e)


def homepage_location_element(driver):
    """首页定位自身，和旋转"""
    try:
        driver.find_element_by_id("com.erlinyou.worldlist:id/recenter_img").click()
    except Exception as e:
        element_error(driver, e)


def homepage_amplification_element(driver):
    """首页放大"""
    try:
        driver.find_element_by_id("com.erlinyou.worldlist:id/iv_zoom_in").click()
    except Exception as e:
        element_error(driver, e)


def homepage_narrow_element(driver):
    """首页缩小"""
    try:
        driver.find_element_by_id("com.erlinyou.worldlist:id/iv_zoom_in").click()
    except Exception as e:
        element_error(driver, e)


def homepage_2d_3d(driver):
    """2d 3d"""
    try:
        driver.find_element_by_id("com.erlinyou.worldlist:id/ll_2d3dSwitch").click()
    except Exception as e:
        element_error(driver, e)