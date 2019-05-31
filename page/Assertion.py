from comm.common import *
from page_element.mine_page_element import download_map
from comm.mylog import *
from page_element.all_home_page_element import homepage_details_go_home_add, homepage_details_go_home_cancel_element


# 判断微信是否登录成功
def check_wx_login(driver, test_name):
    try:
        driver.implicitly_wait(5)
        download_map(driver)
        # driver.find_element_by_android_uiautomator('new UiSelector().text("离线地图")').click()
        mylogger.info("True")
        return True
    except Exception as e:
        mylogger.debug(e)
        screenShot(driver, test_name)
        return False


# 判断微信是否退出成功
def check_wx_logout(driver, test_name):
    try:
        mylogger.info("进入退出验证")
        time.sleep(2)
        driver.implicitly_wait(20)
        count_visitor = driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView[2]"
                                                     "/android.widget.LinearLayout[5]/android.widget.TextView[1]").text
        mylogger.info("定位成功")
        print(count_visitor)
        count_visitor = int(count_visitor)
        mylogger.info('获取访客数成功%s' % count_visitor)
        if count_visitor == 0:
            mylogger.info("True")
            return True
        else:
            mylogger.info("退出登录失败")
            return False

    except Exception as e:
        mylogger.debug(e)
        screenShot(driver, test_name)
        return False


# 验证手机账号密码登录
def check_mobile_login(driver, test_name):
    try:
        driver.implicitly_wait(5)
        driver.find_element_by_id('chat_img').click()
        mylogger.info("进入消息界面成功")
        return True
    except Exception as e:
        mylogger.debug(e)
        screenShot(driver, test_name)
        return False


# 验证共享位置结束成功
def check_share_location_stop(driver, test_name):
    try:
        ele = driver.find_element_by_id("stop").text
        if ele == "停止":
            mylogger.info("停止按钮未从页面消失")
            return False
        else:
            return True
    except:
        mylogger.info("停止按钮从页面消失，断言结果为True")
        return True
# def check_home_page_element(driver):
#     """
#     判断主页输入框详情页上 "回家" button状态是什么
#     :param driver:
#     :return: go_home_element , go_home_number
#     """
#     go_home_number = 0
#     try:
#         go_home_element = homepage_details_go_home_add(driver)
#         mylogger.info("当前账号并未添加回家地址")
#         go_home_number = go_home_number
#         return go_home_element, go_home_number
#     except:
#         go_home_element = homepage_details_go_home_cancel_element(driver)
#         mylogger.info("当前账号已经添加了回家地址")
#         go_home_number = go_home_number + 1
#         return go_home_element, go_home_number


def check_direct_go_home(driver, test_name):
    """设置回家是否成功"""
    try:
        ele = driver.find_element_by_id("com.erlinyou.worldlist:id/top_map_mode_img").text
        if ele == "到这去":
            return True
        else:
            return False
    except Exception as e:
        mylogger.info("%s" % e)
        screenShot(driver, test_name)
        return False


def check_cancel_go_home(driver, test_name):
    """通过是否能找到住宿这个button来判断取消回家成功"""
    try:
        ele = driver.find_element_by_id("com.erlinyou.worldlist:id/tv_house").text
        if ele == "住宿":
            return True
        else:
            return False
    except Exception as e:
        mylogger.info("%s" % e)
        screenShot(driver, test_name)
        driver.press_keycode(4)
        time.sleep(1)
        driver.press_keycode(4)
        mylogger.error("test2_a_1失败")
        return False