from page.element_error import element_error
from comm.config import MyConfig


def search_travel_element(driver):
    """旅行"""
    try:
        driver.find_element_by_id("com.erlinyou.worldlist:id/rl_myTrip").click()
    except Exception as e:
        element_error(driver, e)


def search_travel_strategy(driver):
    """旅游攻略"""
    try:
        driver.find_element_by_android_uiautomator('new UiSelector().textContains("旅游攻略")').click()
    except Exception as e:
        element_error(driver, e)


def search_travel_route(driver):
    """旅游路线"""
    try:
        driver.find_element_by_android_uiautomator('new UiSelector().textContains("旅游路线")').click()
    except Exception as e:
        element_error(driver, e)


def search_travel_mine_trip(driver):
    """我的行程"""
    try:
        driver.find_element_by_android_uiautomator('new UiSelector().textContains("我的行程")').click()
    except Exception as e:
        element_error(driver, e)


def mine_trip_add(driver):
    """新建我的行程"""
    try:
        driver.find_element_by_id("com.erlinyou.worldlist:id/create_trip").click()
    except Exception as e:
        element_error(driver, e)


def mine_trip_new_input(driver, n):
    """新建行程输入框"""
    try:
        myconfig = MyConfig()
        text = myconfig.get_new_trip_input_text(n)
        driver.find_element_by_id("com.erlinyou.worldlist:id/trip_edit_name").send_keys(text)
    except Exception as e:
        element_error(driver, e)


def mine_trip_new_finish(driver):
    """新建行程完成"""
    try:
        driver.find_element_by_id("com.erlinyou.worldlist:id/send_btn").click()
    except Exception as e:
        element_error(driver, e)


def mine_trip_new_add_place(driver):
    """新建行程添加地点  文字栏"""
    try:
        driver.find_element_by_id("com.erlinyou.worldlist:id/add_trip_place_btn").click()
    except Exception as e:
        element_error(driver, e)


def mine_trip_send_place(driver, n):
    """
    添加行程地点输入框
    :param driver:
    :param n:
    :return:
    """
    myconfig = MyConfig()
    place = myconfig.get_new_trip_add_place(n)
    driver.find_element_by_id("com.erlinyou.worldlist:id/search_edit").send_keys(place)


def mine_trip_add_place(driver):
    """为行程添加详细地点"""
    try:
        driver.find_element_by_id("com.erlinyou.worldlist:id/add_trip_point").click()
    except Exception as e:
        element_error(driver, e)
