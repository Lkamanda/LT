"""
message module  share software, file test, long_press send voice
"""
import unittest
from comm.usuallymodule import *
from comm.webDriver import *


class Message_share(webDriver, unittest.TestCase):
    def test1(self):
        """zh login """
        zh_login(self=self, driver=self.driver)
        message_back_element(self.driver)
        mylogger.info("返回home page")

    def test2_share_software(self):
        """message share software"""
        test_name = "地图上发送默认地点"
        mylogger.debug("%s start" % test_name)
        self.driver.implicitly_wait(10)
        mainChat_element(self.driver)
        first_chat_element(self.driver)
        mylogger.info("进入与第一个联系人交互界面")
        self.driver.implicitly_wait(5)
        chat_img_more_element(self.driver)
        time.sleep(2)
        chat_add_all(self.driver, n=8)
        mylogger.info("触发分享app发送")
        screenShot(self.driver, test_name)
        chat_environment_reset(self.driver)

    def test3_send_file(self):
        """message share file"""
        test_name = "发送文件"
        mylogger.debug("%s start" % test_name)
        self.driver.implicitly_wait(10)
        mainChat_element(self.driver)
        first_chat_element(self.driver)
        mylogger.info("进入与第一个联系人交互界面")
        for i in range(1, 6):
            if i == 1:
                self.driver.implicitly_wait(5)
                chat_img_more_element(self.driver)
                time.sleep(2)
                chat_swipeLeft(driver=self.driver, t=5000)
                mylogger.info("触发chat左滑")
            else:
                self.driver.implicitly_wait(5)
                chat_img_more_element(self.driver)
            self.driver.implicitly_wait(5)
            chat_send_file_element(self.driver)
            self.driver.implicitly_wait(5)
            # 从文件管理中选取管理文件
            chat_send_file_type(self.driver, n=3)
            chat_send_file_choice_folder(driver=self.driver, x=4, y=4, z=i)
            mylogger.info("发送文件第%s" % i)
            screenShot(self.driver, test_name="%s发送第%s" % (str_nowTime(), i))
        chat_environment_reset(self.driver)

    def test4_send_voice_1(self):
        """message send voice """
        test_name = "发送语音时长为10s"
        mylogger.debug("%s start" % test_name)
        self.driver.implicitly_wait(10)
        mainChat_element(self.driver)
        first_chat_element(self.driver)
        mylogger.info("进入与第一个联系人交互界面")
        chat_voice_element(self.driver).click()
        self.driver.implicitly_wait(5)
        chat_send_voice_element(driver=self.driver, t=10000)
        # time.sleep(5)
        chat_environment_reset(self.driver)

    def test4_send_voice_2(self):
        """message send voice """
        test_name = "发送语音时长为180s"
        mylogger.debug("%s start" % test_name)
        self.driver.implicitly_wait(10)
        mainChat_element(self.driver)
        first_chat_element(self.driver)
        mylogger.info("进入与第一个联系人交互界面")
        chat_voice_element(self.driver).click()
        self.driver.implicitly_wait(5)
        t = 60000
        chat_send_voice_element(driver=self.driver, t=t)
        mylogger.info("发送语音时长为%s" % t)
        # time.sleep(5)
        chat_environment_reset(self.driver)


if __name__ == '__main__':
    unittest.main(verbosity=2)
