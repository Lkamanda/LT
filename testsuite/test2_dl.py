import unittest
from comm.webDriver import *
from comm.common import *
from page_element.home_page_element import *
from page_element.login_page_element import *
from page_element.message_page_element import *
from page_element.mine_page_element import *
from page_element.mine_leavemap_allmap_element import *
from comm.logging import *
from page.Assertion import *


class ZH_message(webDriver, unittest.TestCase):
    # @unittest.skip('not need')  跳过该跳测试用例
    def test1_dl_mobile_number(self):
        """登录手机账号密码"""
        print(self._testMethodName)  # 返回测试用例名称
        test_name = self._testMethodName
        self.driver.implicitly_wait(5)
        mainChat_element(self.driver)
        mylogger.info("进入登录页面成功")
        self.driver.implicitly_wait(5)
        mobile_tile_element(self.driver)
        mylogger.info("切换成账号密码登录")
        self.driver.implicitly_wait(5)
        mobile_user_element(self.driver)
        mylogger.info("输入账号成功")
        mobile_password_element(self.driver)
        mylogger.info("输如密码成功")
        self.driver.implicitly_wait(5)
        mobile_login_element(self.driver)
        mylogger.info("触发登录")
        self.assertEqual(True, check_mobile_login(self.driver, test_name))
        mylogger.info("登录成功")

    def test2_message(self):
        """与聊天page下第一个联系人发起回话"""
        test_name = self._testMethodName
        # self.driver.implicitly_wait(5)
        # self.driver.find_element_by_id('com.erlinyou.worldlist:id/chat_img').click()
        self.driver.implicitly_wait(5)
        first_chat_element(self.driver)
        mylogger.info("进入与第一个联系人交互界面")
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("com.erlinyou.worldlist:id/et_msg").click()
        print(str_nowTime())
        # self.driver.implicitly_wait(10)
        # self.driver.find_element_by_id("com.erlinyou.worldlist:id/et_msg").send_keys("123abc")
        print(str_nowTime())
        # chat_sendkeys_element(self.driver)
        # mylogger.info("在聊天窗口输入send_str")
        # self.driver.implicitly_wait(5)
        # chat_send_all_elment(self.driver)
        mylogger.info("消息已发送")
        screenShot(self.driver, test_name)

    def test3_preview_send_photo(self):
        """第一个联系人发送照片和视频，预览"""
        self.driver.implicitly_wait(5)
        chat_img_more_element(self.driver)
        mylogger.info("点击+号")
        self.driver.implicitly_wait(5)
        chat_add_photo_album(self.driver)
        mylogger.info("点击进入相册界面")
        self.driver.implicitly_wait(5)
        chat_add_photo_album_n(self.driver, n=2)
        mylogger.info("选择照片/视频成功")
        self.driver.implicitly_wait(5)
        chat_add_photo_album_n(self.driver, n=7)
        mylogger.info("选择照片/视频成功")
        self.driver.implicitly_wait(5)
        chat_add_photo_album_n(self.driver, n=12)
        mylogger.info("选择照片/视频成功")
        self.driver.implicitly_wait(5)
        chat_add_photo_preview(self.driver)
        mylogger.info("进入发送预览")
        swipeLeft(self.driver, 1000)
        swipeLeft(self.driver, 1000)
        self.driver.implicitly_wait(5)
        chat_add_photo_preview_send(self.driver)
        time.sleep(10)
        mylogger.info("照片上传成功")

    def test4_send_photo(self):
        """直接发送照片"""
        time.sleep(5)
        # self.driver.implicitly_wait(20)
        # chat_img_more_element(self.driver)
        # mylogger.info("点击+号")
        self.driver.implicitly_wait(5)
        chat_add_photo_album(self.driver)
        mylogger.info("点击进入相册界面")
        self.driver.implicitly_wait(5)
        chat_add_photo_album_n(self.driver, n=2)
        mylogger.info("选择照片/视频成功")
        self.driver.implicitly_wait(5)
        chat_add_photo_album_n(self.driver, n=7)
        mylogger.info("选择照片/视频成功")
        self.driver.implicitly_wait(5)
        chat_add_photo_album_n(self.driver, n=12)
        mylogger.info("选择照片/视频成功")
        self.driver.implicitly_wait(5)
        chat_add_photo_send(self.driver)
        allmap_back_element(self.driver)
        allmap_back_element(self.driver)

    def test5_exite(self):
        """当前用户退出"""
        # 测试账号被访问数必须不为0
        test_name = "当前用户退出"
        self.driver.implicitly_wait(3)
        userAvatar_element(self.driver)
        mylogger.info("get into mine home page")
        swipeUp(driver=self.driver, t=1000)
        mylogger.info("向上滑动屏幕")
        self.driver.implicitly_wait(4)
        mine_setting(self.driver)
        self.driver.find_element_by_id("com.erlinyou.worldlist:id/btn_logout").click()
        mylogger.info("触发退出登录按钮")
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("android:id/button1").click()
        mylogger.info("确认退出登录退出")
        allmap_back_element(self.driver)
        mylogger.info("返回我的页面")
        self.assertEqual(True, check_wx_logout(driver=self.driver, test_name=test_name))
        mylogger.info("登录退出成功")


if __name__ == '__main__':
    unittest.main(verbosity=2)