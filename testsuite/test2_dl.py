import unittest
from comm.webDriver import *
from comm.usuallymodule import *


class ZH_message(webDriver, unittest.TestCase):
    #    @unittest.skip('not need')
    #
    # 跳过该跳测试用例

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
        # self.driver.implicitly_wait(10)
        # self.driver.find_element_by_id('com.erlinyou.worldlist:id/chat_img').click()
        self.driver.implicitly_wait(20)
        first_chat_element(driver=self.driver)
        mylogger.info("进入与第一个联系人交互界面")
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("et_msg").click()   # com.erlinyou.worldlist:id/
        print(str_nowTime())
        self.driver.implicitly_wait(10)
        # self.driver.find_element_by_id("com.erlinyou.worldlist:id/et_msg").send_keys("123")
        print(str_nowTime())
        # chat_sendkeys_element(self.driver)
        # mylogger.info("在聊天窗口输入send_str")
        # self.driver.implicitly_wait(5)
        # chat_send_all_element(self.driver)
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
        self.driver.implicitly_wait(5)
        swipeLeft(self.driver, 1000)
        self.driver.implicitly_wait(5)
        chat_add_photo_preview_send(self.driver)
        self.driver.implicitly_wait(30)
        mylogger.info("照片上传成功")

    def test4_send_photo(self):
        """直接发送照片"""
        print("进入test4")
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id("et_msg").click()      # com.erlinyou.worldlist:id/
        chat_img_more_element(self.driver)
        mylogger.info("点击+号")
        self.driver.implicitly_wait(15)
        chat_add_photo_album(self.driver)
        mylogger.info("点击进入相册界面")
        self.driver.implicitly_wait(10)
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
        self.driver.implicitly_wait(20)
        allmap_back_element(self.driver)
        print('返回上一层')
        self.driver.implicitly_wait(10)
        message_back_element(self.driver)

    def test5_take_picture(self):
        """拍照后勾选所拍照片发送"""
        test_name = "拍照后勾选所拍照片发送"
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id('com.erlinyou.worldlist:id/chat_img').click()
        self.driver.implicitly_wait(20)
        first_chat_element(driver=self.driver)
        mylogger.info("进入与第一个联系人交互界面")
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id("com.erlinyou.worldlist:id/et_msg").click()
        time.sleep(2)
        mylogger.info("触发聊天成功")
        self.driver.implicitly_wait(10)
        chat_img_more_element(self.driver)
        self.driver.implicitly_wait(10)
        chat_add_all(driver=self.driver, n=2)
        mylogger.info("进入拍摄page")
        time.sleep(2)
        self.driver.implicitly_wait(10)
        chat_take_picture_start(self.driver)
        mylogger.info("触发拍摄按钮")
        self.driver.implicitly_wait(5)
        chat_take_piucture_sure(driver=self.driver, n=2)
        self.driver.implicitly_wait(20)
        # chat_take_picture_album(self.driver)
        # mylogger.info("进入相册选择界面")
        # self.driver.implicitly_wait(10)
        # chat_add_photo_send(self.driver)
        # mylogger.info("触发发送")
        self.driver.press_keycode(4)
        screenShot(driver=self.driver, test_name=test_name)

    # def test_take_picture_2(self):
    #     """拍照后发送"""
    # def test_take_picture_3(self):
    #     """拍摄视频后发送"""
    # def test_take_picture_4(self):
    #     """拍摄照片后再拍摄视频发送"""

    def test6_location_share_1(self):
        """共享位置直接停止"""
        test_name = "共享位置直接停止"
        self.driver.find_element_by_id("et_msg").click()
        chat_img_more_element(self.driver)
        chat_add_all(self.driver, n=5)
        self.driver.implicitly_wait(10)
        chat_location_share_stop(self.driver)
        self.assertEqual(True, check_share_location_stop(driver=self.driver, test_name=test_name))
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('chat_img').click()
        self.driver.implicitly_wait(20)
        first_chat_element(driver=self.driver)
        mylogger.info("进入与第一个联系人交互界面")

    def test6_location_share_2(self):
        """共享位置返回聊天停止"""
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("et_msg").click()
        chat_img_more_element(self.driver)
        chat_add_all(self.driver, n=5)
        self.driver.implicitly_wait(5)
        chat_location_share_get_back(self.driver)
        self.driver.find_element_by_id("et_msg").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("et_msg").send_keys("123")
        mylogger.info("输入成功")
        chat_send_all_element(self.driver).click()
        chat_location_share_stop(self.driver)





    # def test5_exit(self):
    #     """当前用户退出"""
    #     logout(self=self, driver=self.driver)


if __name__ == '__main__':
    unittest.main(verbosity=2)