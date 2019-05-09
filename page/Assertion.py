from comm.common import *
from page_element.mine_page_element import download_map
from comm.logging import *


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
        driver.implicitly_wait(5)
        visitor_element = driver.find_element_by_xpath("//android.widget.LinearLayout[5]/android.widget.TextView[1]")
        count_visitor = int(visitor_element.get_attribute("text"))
        mylogger.info('获取访客数成功')
        if count_visitor == 0:
            mylogger.info("True")
            return True
        else:
            mylogger.info("退出登录失败")
            return False

    except Exception as e:
        mylogger(e)
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

