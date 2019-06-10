"""发送动态"""
import unittest
from comm.usuallymodule import *
from comm.webDriver import *


class Test6(webDriver, unittest.TestCase):
    # def test_a_0(self):
    #     """zh 登录"""
    #     zh_login(self=self, driver=self.driver)
    #     self.driver.press_keycode(4)
    #     mylogger.info("返回home page")

    def test_a_1(self):
        """发送动态 图片和视频"""
        self.driver.implicitly_wait(5)
        dynamic(self.driver)
        mylogger.info("进入动态界面")
        self.driver.implicitly_wait(5)
        create_new_dynamic_element(self.driver)
        dynamic_input_box(self.driver)
        self.driver.implicitly_wait(5)
        dynamic_camera_element(self.driver)
        self.driver.implicitly_wait(5)
        dynamic_choice_picture(driver=self.driver, n=1)
        mylogger.info("启动照相机")
        dynamic_take_picture_taking(self.driver)
        self.driver.implicitly_wait(5)
        dynamic_take_picture_ok(self.driver)
        self.driver.implicitly_wait(5)
        self.driver.press_keycode(4)
        mylogger.info("添加拍摄照片完成")
        dynamic_choice_picture(driver=self.driver, n=2)
        dynamic_recoding_picture(self.driver)
        time.sleep(10)
        dynamic_take_picture_taking(self.driver)
        






