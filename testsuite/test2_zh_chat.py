"""
模拟mobile账号登录后对message下功能进行测试:
相册， 拍照， 分享位置， 联系人
"""

import unittest
from comm.webDriver import *
from comm.usuallymodule import *


class Message_zh(webDriver, unittest.TestCase):
    #    @unittest.skip('not need')
    # 跳过该跳测试用例

    def test1_dl_mobile_number(self):
        """登录手机账号密码"""
        zh_login(self=self, driver=self.driver)

    def test2_message(self):
        """与聊天page下第一个联系人发起回话"""
        test_name = self._testMethodName
        mylogger.debug(test_name)
        # self.driver.implicitly_wait(10)
        # self.driver.find_element_by_id('com.erlinyou.worldlist:id/chat_img').click()
        self.driver.implicitly_wait(20)
        first_chat_element(driver=self.driver)
        mylogger.info("进入与第一个联系人交互界面")
        self.driver.implicitly_wait(5)
        chat_send_keys_element(driver=self.driver, chat_str=myconfig.get_chat_str(n=1))
        time.sleep(3)
        chat_send_all_element(self.driver)
        mylogger.info("消息已发送")
        time.sleep(3)
        screenShot(self.driver, test_name)

    def test3_preview_send_photo(self):
        """第一个联系人发送照片和视频，预览"""
        test_name = self._testMethodName
        mylogger.debug(test_name)
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
        test_name = self._testMethodName
        mylogger.debug(test_name)
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
        self.driver.implicitly_wait(60)
        allmap_back_element(self.driver)
        print('返回上一层')
        self.driver.implicitly_wait(10)
        message_back_element(self.driver)

    def test5_take_picture(self):
        """拍照后勾选所拍照片发送"""
        test_name = "拍照后勾选所拍照片发送"
        mylogger.debug(test_name)
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
        chat_take_picture_sure(driver=self.driver, n=2)
        self.driver.implicitly_wait(20)
        # chat_take_picture_album(self.driver)
        # mylogger.info("进入相册选择界面")
        # self.driver.implicitly_wait(10)
        # chat_add_photo_send(self.driver)
        # mylogger.info("触发发送")
        self.driver.press_keycode(4)
        time.sleep(3)
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
        mylogger.debug(test_name)
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
        test_name = "共享位置返回聊天停止"
        mylogger.debug(test_name)
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("et_msg").click()
        chat_img_more_element(self.driver)
        chat_add_all(self.driver, n=5)
        self.driver.implicitly_wait(5)
        chat_location_share_get_back(self.driver)
        # self.driver.find_element_by_id("et_msg").click()
        # self.driver.implicitly_wait(10)
        # self.driver.find_element_by_id("et_msg").send_keys("123")
        # mylogger.info("输入成功")
        chat_send_all_element(self.driver)
        chat_location_share_stop(self.driver)
        mylogger.info("聊天终止")

    def test7_contacts_share_1(self):
        """分享联系人"""
        test_name = "分享联系人"
        mylogger.debug(test_name)
        chat_img_more_element(self.driver)
        mylogger.info("add")
        self.driver.implicitly_wait(5)
        chat_add_all(self.driver, n=6)
        mylogger.info("进入contacts page")
        time.sleep(1)
        chat_contacts_share(self.driver, n=1)
        mylogger.info("选择第一张contacts发送")
        self.driver.implicitly_wait(10)
        chat_img_more_element(driver=self.driver)
        mylogger.info("add")
        self.driver.implicitly_wait(5)
        chat_add_all(self.driver, n=6)
        mylogger.info("进入contacts page")
        time.sleep(1)
        chat_contacts_share(self.driver, n=2)
        mylogger.info("选择第一张contacts发送")
        time.sleep(3)
        screenShot(driver=self.driver, test_name=test_name)

    def test7_contacts_share_2(self):
        """查询到指定联系人并分享查询的第一个"""
        test_name = "查询到指定联系人并分享查询的第一个"
        mylogger.debug(test_name)
        chat_img_more_element(self.driver)
        mylogger.info("add")
        self.driver.implicitly_wait(5)
        chat_add_all(self.driver, n=6)
        mylogger.info("进入contacts page")
        self.driver.implicitly_wait(5)
        chat_location_contact_share_search(driver=self.driver, n=u"zhoujialin")
        time.sleep(3)
        chat_contacts_share(driver=self.driver, n=1)
        mylogger.info("选择查询到的第一张contacts发送")
        screenShot(driver=self.driver, test_name=test_name)
        # 返回首页
        chat_environment_reset(driver=self.driver)

    # 应返回home page 页面在执行
    def test8_exit(self):
        """当前用户退出"""
        test_name = "当前用户退出"
        mylogger.debug(test_name)
        logout(self=self, driver=self.driver)


if __name__ == '__main__':
    unittest.main(verbosity=2)