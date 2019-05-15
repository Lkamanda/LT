from page_element.home_page_element import *
from page_element.mine_leavemap_allmap_element import *
from page_element.mine_page_element import *
from page.Assertion import *
from page_element.message_page_element import *
from comm.common import *
from comm.logs import myLog
from page_element.login_page_element import *


def logout(self, driver):
    test_name = "mobile quit"
    driver.implicitly_wait(5)
    userAvatar_element(driver)
    mylogger.info("get into mine home page")
    driver.implicitly_wait(5)
    swipeUp(driver=driver, t=5000)
    mylogger.info("向上滑动屏幕")
    driver.implicitly_wait(10)
    mine_setting(driver)
    driver.find_element_by_id("com.erlinyou.worldlist:id/btn_logout").click()
    mylogger.info("触发退出登录按钮")
    driver.implicitly_wait(5)
    driver.find_element_by_id("android:id/button1").click()
    mylogger.info("确认退出登录退出")
    driver.implicitly_wait(5)
    allmap_back_element(driver)
    mylogger.info("返回我的页面")
    self.driver.implicitly_wait(20)
    y = check_wx_logout(driver=self.driver, test_name=test_name)
    self.assertEqual(True, y)
    mylogger.info("登录退出成功")


def element_error(driver, e):
    mylogger.error(e)
    test_name = ""
    screenShot(driver, test_name)

