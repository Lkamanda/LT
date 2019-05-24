"""
message 下chat 位置页面 element api
"""

from page.element_error import element_error

from comm.config import MyConfig


def chat_place_search_place(driver, n):
    """
    place page search
    :param driver:
    :param n: where you want to go  类型 1,2,3
    """
    myconfig = MyConfig()
    place = myconfig.get_place_share_search(n)
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
        # driver.implicitly_wait(5)
        driver.find_element_by_id("tv_service").click()
        print("t")
    except Exception as e:
        print("f")
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


def chat_place_on_map(driver):
    """place page on map choice """
    try:
        driver.find_element_by_id("com.erlinyou.worldlist:id/rl_select").click()
    except Exception as e:
        element_error(driver, e)


def chat_place_on_map_sure(driver):
    """place page on map 确定"""
    try:
        driver.find_element_by_id("detail_set_tv").click()
    except Exception as e:
        element_error(driver, e)


def chat_place_on_map_GPS(driver):
    """place page GPS"""
    try:
        driver.find_element_by_id("rl_current").click()
    except Exception as e:
        element_error(driver, e)



def chat_place_type(driver, n):
    """
    搜素框下地点类型
    :param driver: self.driver
    :param n:
    n = 1 :  综合
    n = 2 ： 城市
    n = 3 :  地址
    n = 4 :  地点
    n = 5 :  酒店
    n = 6 :  美食
    """
    try:
        driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView/android.widget.LinearLayout[%s]"
                                     "/android.widget.TextView" % n).click()
    except Exception as e:
        element_error(driver, e)


def chat_place_choice_Address(driver, n):
    """
    搜索框下 地点 第n个位置信息
    :param driver: self.driver
    :param n: 第几个查询寻结果
    :return:
    """
    try:
        driver.find_element_by_xpath("//android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView"
                                     "/android.widget.LinearLayout[%s]"% n).click()
    except Exception as e:
        element_error(driver, e)


def chat_place_choice_All(driver, n):
    """搜索框下 全部 第n个位置信息"""
    try:
        driver.find_element_by_xpath("//android.support.v4.view.ViewPager/android.widget.RelativeLayout/"
                                     "android.support.v7.widget.RecyclerView/android.widget.LinearLayout[%s]" % n)\
            .click()
    except Exception as e:
        element_error(driver, e)


def chat_place_choice_City(driver, n):
    """
    搜索框下 城市下 第n个数据
    :param driver:
    :param n:
    :return:
    """
    try:
        driver.find_element_by_xpath("//android.widget.ListView/android.widget.LinearLayout[%s]" % n).click()
    except Exception as e:
        element_error(driver, e)


def chat_place_surrounding_share(driver, n):
    """
    对 place type 周边兴趣点列表数据获取
    :param driver:
    :param n: 周边兴趣点列表分享 1 or 2
    :return:
    """
    try:
        driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[%s]" % n)\
            .click()
    except Exception as e:
        element_error(driver, e)


def chat_send_file_element(driver):
    """message send file element"""
    try:
        driver.find_element_by_id("img_icon").click()
    except Exception as e:
        element_error(driver, e)

