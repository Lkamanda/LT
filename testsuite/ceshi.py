import unittest
from comm.webDriver import *
from comm.usuallymodule import *


class ZH_message(webDriver, unittest.TestCase):
    #    @unittest.skip('not need')
    #
    # 跳过该跳测试用例

    # def test1_dl_mobile_number(self):
    #     """登录手机账号密码"""
    #     print(self._testMethodName)  # 返回测试用例名称
    #     test_name = self._testMethodName
    #     self.driver.implicitly_wait(5)
    #     mainChat_element(self.driver)
    #     mylogger.info("进入登录页面成功")
    #     self.driver.implicitly_wait(5)
    #     mobile_tile_element(self.driver)
    #     mylogger.info("切换成账号密码登录")
    #     self.driver.implicitly_wait(5)
    #     mobile_user_element(self.driver)
    #     mylogger.info("输入账号成功")
    #     mobile_password_element(self.driver)
    #     mylogger.info("输如密码成功")
    #     self.driver.implicitly_wait(5)
    #     mobile_login_element(self.driver)
    #     mylogger.info("触发登录")
    #     self.assertEqual(True, check_mobile_login(self.driver, test_name))
    #     mylogger.info("登录成功")

    def test2_message(self):
        """与聊天page下第一个联系人发起回话"""
        test_name = self._testMethodName
        mylogger.debug(test_name)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('com.erlinyou.worldlist:id/chat_img').click()
        self.driver.implicitly_wait(20)
        first_chat_element(driver=self.driver)
        mylogger.info("进入与第一个联系人交互界面")
        self.driver.implicitly_wait(5)
        place_environment_reset(driver=self.driver)
        # chat_send_keys_element(driver=self.driver, chat_str=myconfig.get_chat_str(n=1))
        # # chat_send_keys_element(driver=self.driver, chat_str=myconfig.get_chat_str(n=1))
        # chat_send_all_element(self.driver)
        # time.sleep(5)

    # def test7_contacts_share_1(self):
    #     """分享联系人"""
    #     test_name = "分享联系人"
    #     mylogger.debug(test_name)
    #     chat_img_more_element(self.driver)
    #     mylogger.info("add")
    #     self.driver.implicitly_wait(5)
    #     chat_add_all(self.driver, n=6)
    #     mylogger.info("进入contacts page")
    #     time.sleep(1)
    #     chat_contacts_share(self.driver, n=1)
    #     mylogger.info("选择第一张contacts发送")
    #     self.driver.implicitly_wait(10)
    #     chat_img_more_element(driver=self.driver)
    #     mylogger.info("add")
    #     self.driver.implicitly_wait(5)
    #     chat_add_all(self.driver, n=6)
    #     mylogger.info("进入contacts page")
    #     time.sleep(1)
    #     chat_contacts_share(self.driver, n=2)
    #     mylogger.info("选择第一张contacts发送")
    #     time.sleep(3)
    #     screenShot(driver=self.driver, test_name=test_name)
    #
    # def test7_contacts_share_2(self):
    #     """查询到指定联系人并分享查询的第一个"""
    #     test_name = "查询到指定联系人并分享查询的第一个"
    #     mylogger.debug(test_name)
    #     chat_img_more_element(self.driver)
    #     mylogger.info("add")
    #     self.driver.implicitly_wait(5)
    #     chat_add_all(self.driver, n=6)
    #     mylogger.info("进入contacts page")
    #     self.driver.implicitly_wait(5)
    #     chat_location_contact_share_search(driver=self.driver, n=u"zhoujialin")
    #     time.sleep(3)
    #     chat_contacts_share(driver=self.driver, n=1)
    #     mylogger.info("选择查询到的第一张contacts发送")
    #     time.sleep(3)
    #     screenShot(driver=self.driver, test_name=test_name)
    #     # 返回首页
    #
    #
    # def test8_exit(self):
    #     """当前用户退出"""
    #     test_name = "当前用户退出"
    #     mylogger.debug(test_name)
    #     logout(self=self, driver=self.driver)
    #
    #
    #     # mylogger.info("消息已发送")
    #     # time.sleep(3)
    #     # screenShot(self.driver, test_name)
    #
    # #
    # # def test3_preview_send_photo(self):
    # #     """第一个联系人发送照片和视频，预览"""
    # #     self.driver.implicitly_wait(5)
    # #     chat_img_more_element(self.driver)
    # #     mylogger.info("点击+号")
    # #     self.driver.implicitly_wait(5)
    # #     chat_add_photo_album(self.driver)
    # #     mylogger.info("点击进入相册界面")
    # #     self.driver.implicitly_wait(5)
    # #     chat_add_photo_album_n(self.driver, n=2)
    # #     mylogger.info("选择照片/视频成功")
    # #     self.driver.implicitly_wait(5)
    # #     chat_add_photo_album_n(self.driver, n=7)
    # #     mylogger.info("选择照片/视频成功")
    # #     self.driver.implicitly_wait(5)
    # #     chat_add_photo_album_n(self.driver, n=12)
    # #     mylogger.info("选择照片/视频成功")
    # #     self.driver.implicitly_wait(5)
    # #     chat_add_photo_preview(self.driver)
    # #     mylogger.info("进入发送预览")
    # #     swipeLeft(self.driver, 1000)
    # #     self.driver.implicitly_wait(5)
    # #     swipeLeft(self.driver, 1000)
    # #     self.driver.implicitly_wait(5)
    # #     chat_add_photo_preview_send(self.driver)
    # #     # print(str_nowTime())
    # #     # time.sleep(30)
    # #     # print(str_nowTime())
    # #     self.driver.implicitly_wait(30)
    # #     mylogger.info("照片上传成功")
    #
    # def test4_send_photo(self):
    #     """直接发送照片"""
    #     print("进入test4")
    #     self.driver.implicitly_wait(30)
    #     self.driver.find_element_by_id("et_msg").click()      # com.erlinyou.worldlist:id/
    #     chat_img_more_element(self.driver)
    #     mylogger.info("点击+号")
    #     self.driver.implicitly_wait(15)
    #     chat_add_photo_album(self.driver)
    #     mylogger.info("点击进入相册界面")
    #     self.driver.implicitly_wait(10)
    #     chat_add_photo_album_n(self.driver, n=2)
    #     mylogger.info("选择照片/视频成功")
    #     self.driver.implicitly_wait(5)
    #     chat_add_photo_album_n(self.driver, n=7)
    #     mylogger.info("选择照片/视频成功")
    #     self.driver.implicitly_wait(5)
    #     chat_add_photo_album_n(self.driver, n=12)
    #     mylogger.info("选择照片/视频成功")
    #     self.driver.implicitly_wait(5)
    #     chat_add_photo_send(self.driver)
    #     self.driver.implicitly_wait(20)
    #     allmap_back_element(self.driver)
    #     print('返回上一层')
    #     self.driver.implicitly_wait(10)
    #     message_back_element(self.driver)

    # def test1_take_picture_1(self):
    #     """拍照后勾选所拍照片发送"""
    #     test_name = "拍照后勾选所拍照片发送"
    #     self.driver.implicitly_wait(20)
    #     self.driver.find_element_by_id('com.erlinyou.worldlist:id/chat_img').click()
    #     self.driver.implicitly_wait(20)
    #     first_chat_element(driver=self.driver)
    #     mylogger.info("进入与第一个联系人交互界面")
    #     time.sleep(4)
    #     # self.driver.find_element_by_xpath("//android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.EditText").click()
    #     # self.driver.find_element_by_id("et_msg").click()
    #     # time.sleep(2)
    #     chat_img_more_element(self.driver)
    #     mylogger.info("add")
    #     self.driver.implicitly_wait(5)
    #     chat_add_all(self.driver, n=6)
    #     mylogger.info("进入contacts page")
    #     time.sleep(1)
    #     chat_contacts_share(self.driver, n=1)
    #     mylogger.info("选择第一张contacts发送")
    #     chat_img_more_element(self.driver)
    #     mylogger.info("add")
    #     self.driver.implicitly_wait(5)
    #     chat_add_all(self.driver, n=6)
    #     mylogger.info("进入contacts page")
    #     time.sleep(1)
    #     chat_contacts_share(self.driver, n=2)
    #     mylogger.info("选择第一张contacts发送")
    #     time.sleep(3)
    #     screenShot(driver=self.driver, test_name=test_name)
    #
    # def test7_contacts_share_2(self):
    #     """查询到指定联系人并分享查询的第一个"""
    #     test_name = "查询到指定联系人并分享查询的第一个"
    #     mylogger.debug(test_name)
    #     chat_img_more_element(self.driver)
    #     mylogger.info("add")
    #     self.driver.implicitly_wait(5)
    #     chat_add_all(self.driver, n=6)
    #     mylogger.info("进入contacts page")
    #     self.driver.implicitly_wait(5)
    #     chat_location_contact_share_search(driver=self.driver, n="zhoujialin")
    #     time.sleep(3)
    #     chat_contacts_share(driver=self.driver, n=1)
    #     mylogger.info("选择查询到的第一张contacts发送")
    #     time.sleep(3)
    #     screenShot(driver=self.driver, test_name=test_name)
    #     time.sleep(2)
    #     allmap_back_element(self.driver)
    #     time.sleep(2)
    #     message_back_element(driver=self.driver)
    #     time.sleep(2)
    #
    #
    # def test8_exit(self):
    #     """当前用户退出"""
    #     logout(self=self, driver=self.driver)
    #

if __name__ == '__main__':
    unittest.main(verbosity=2)