from comm.common import *
from page_element.mine_page_element import download_map
from comm.mylog import *


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
        # count_visitor = driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView[2]/android.widget.LinearLayout[5]/android.widget.TextView[1]").get_attribute("name")
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
        driver.find_element_by_id('com.erlinyou.worldlist:id/chat_img').click()
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
            return False
        else:
            return True
    except:
        screenShot(driver, test_name)
        print(True)
        return True