from page_element.home_page_element import *
from page_element.mine_leavemap_allmap_element import *
from page_element.mine_page_element import *
from page.Assertion import *
from page_element.message_page_element import *
from comm.common import *
from page_element.login_page_element import *
from page_element.message_page_chat_place_element import *
from comm.config import MyConfig
myconfig = MyConfig()


def zh_login(self, driver):
    test_name = "mobile账号密码登录"
    mylogger.debug(test_name)  # 返回测试用例名称
    driver.implicitly_wait(5)
    mainChat_element(driver)
    mylogger.info("进入登录页面成功")
    driver.implicitly_wait(5)
    mobile_tile_element(driver)
    mylogger.info("切换成账号密码登录")
    driver.implicitly_wait(5)
    mobile_user_element(driver)
    mylogger.info("输入账号成功")
    mobile_password_element(driver)
    mylogger.info("输如密码成功")
    driver.implicitly_wait(5)
    mobile_login_element(driver)
    mylogger.info("触发登录")
    self.assertEqual(True, check_mobile_login(driver, test_name))
    mylogger.info("mobile 登录成功")


def logout(self, driver):
    """退出"""
    test_name = "mobile quit"
    driver.implicitly_wait(5)
    userAvatar_element(driver)
    mylogger.info("get into mine home page")
    time.sleep(3)
    swipeUp(driver=driver, t=4000)
    mylogger.info("向上滑动屏幕")
    driver.implicitly_wait(10)
    mine_setting(driver)
    driver.find_element_by_id("com.erlinyou.worldlist:id/btn_logout").click()
    mylogger.info("触发退出登录按钮")
    driver.implicitly_wait(5)
    driver.find_element_by_id("android:id/button1").click()
    mylogger.info("确认退出登录退出")
    time.sleep(3)
    allmap_back_element(driver)
    mylogger.info("返回我的页面")
    # self.driver.implicitly_wait(10)
    time.sleep(2)
    y = check_wx_logout(driver=self.driver, test_name=test_name)
    self.assertEqual(True, y)
    mylogger.info("登录退出成功")





def place_environment(driver):
    """进入message place environment"""
    driver.implicitly_wait(10)
    first_chat_element(driver)
    mylogger.info("进入与第一个联系人交互界面")
    driver.implicitly_wait(5)
    chat_img_more_element(driver)
    time.sleep(2)
    chat_add_all(driver=driver, n=7)
    mylogger.info("进入place 界面")


def place_environment_reset(driver):
    mylogger.info("start reset place environment")
    time.sleep(2)
    allmap_back_element(driver)
    time.sleep(2)
    message_back_element(driver)
    mylogger.info("end reset place environment")
    time.sleep(2)

