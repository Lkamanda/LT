"""
message 下chat 位置页面 element api
"""
from comm.usuallymodule import element_error

def chat_place_search_place(driver, place):
    """
    place page search
    :param driver:
    :param place: where you want to go
    """
    driver.find_element_by_id("com.erlinyou.worldlist:id/search_edit").send_keys(place)


def chat_place_get_back(driver):
    """place get back button """
    driver.find_element_by_id("com.erlinyou.worldlist:id/btnBack").click()


def chat_place_sleep(driver):
    """ place page Sleep button """
    # com.erlinyou.worldlist:id/tv_house
    driver.find_element_by_id("tv_house").click()


def chat_place_eat(driver):
    """place page Eat button"""
    driver.find_element_by_id("com.erlinyou.worldlist:id/tv_food").click()


def chat_place_visit(driver):
    """place page visit button """
    driver.find_element_by_id("com.erlinyou.worldlist:id/tv_play").click()


def chat_place_move(driver):
    """place page move button"""
    try:
        driver.find_element_by_id("com.erlinyou.worldlist:id/tv_out").click()
    except Exception as e:
        element_error(driver, e)


def chat_place_service(driver):
    """place page service button"""
    try:
        driver.find_element_by_id("	com.erlinyou.worldlist:id/tv_service").click()
    except Exception as e:
        element_error(driver, e)


def chat_place_nearby(driver):
    """place page nearby button """
    try:
        driver.find_element_by_id("com.erlinyou.worldlist:id/tv_more").click()
    except Exception as e:
        element_error(driver, e)


def chat_place_favorite(driver):
    """ place page favorite button 收藏"""
    # Interactions are not available for this element
    try:
        driver.find_element_by_id("com.erlinyou.worldlist:id/rl_favorite").click()
    except Exception as e:
        element_error(driver, e)


def chat_place_onmap(driver):
    """place page on map choice """
    try:
        driver.find_element_by_id("com.erlinyou.worldlist:id/rl_select").click()
    except Exception as e:
        element_error(driver, e)



