"""
在message下对place模块下功能进行测试
"""
import unittest
from comm.usuallymodule import *
from comm.webDriver import *


class Message_zh(webDriver, unittest.TestCase):

    # def test_1(self):
    #     """zh login """
    #     zh_login(self=self, driver=self.driver)

    def test2_search_place_1(self):
        """通过搜索分享地点"""
        test_name = "通过搜索分享地点"
        mylogger.info("%s start" % test_name)
        self.driver.implicitly_wait(5)
        mainChat_element(self.driver)
        place_environment(driver=self.driver)
        time.sleep(2)
        self.driver.implicitly_wait(10)
        chat_place_search_place(driver=self.driver, n=1)
        mylogger.info("触发：输入框输入")
        self.driver.implicitly_wait(5)
        chat_place_type(driver=self.driver, n=3)
        mylogger.info("选择地点类型为地点")
        chat_place_choice_Address(driver=self.driver, n=1)
        mylogger.info("位置信息发送")
        self.driver.implicitly_wait(5)
        screenShot(driver=self.driver, test_name=test_name)
        self.driver.implicitly_wait(5)
        place_environment_reset(self.driver)

    def test2_search_place_2(self):
        """通过搜索分享街道"""
        test_name = "通过搜索分享街道"
        mylogger.debug("%s start" % test_name)
        self.driver.implicitly_wait(5)
        mainChat_element(self.driver)
        place_environment(driver=self.driver)
        time.sleep(2)
        self.driver.implicitly_wait(10)
        chat_place_search_place(driver=self.driver, n=2)
        mylogger.info("触发：输入框输入")
        self.driver.implicitly_wait(5)
        chat_place_type(driver=self.driver, n=1)
        mylogger.info("选择地点类型为全部")
        chat_place_choice_All(driver=self.driver, n=1)
        mylogger.info("位置信息发送")
        self.driver.implicitly_wait(5)
        screenShot(driver=self.driver, test_name=test_name)
        self.driver.implicitly_wait(5)
        place_environment_reset(self.driver)

    def test2_search_place_3(self):
        """通过搜索分享城市"""
        test_name = "通过搜索分享城市"
        mylogger.debug("%s start" % test_name)
        self.driver.implicitly_wait(5)
        mainChat_element(self.driver)
        place_environment(driver=self.driver)
        time.sleep(2)
        self.driver.implicitly_wait(10)
        chat_place_search_place(driver=self.driver, n=3)
        mylogger.info("触发：输入框输入")
        self.driver.implicitly_wait(5)
        chat_place_type(driver=self.driver, n=2)
        mylogger.info("选择地点类型为城市")
        chat_place_choice_City(driver=self.driver, n=1)
        mylogger.info("位置信息发送")
        self.driver.implicitly_wait(5)
        screenShot(driver=self.driver, test_name=test_name)
        self.driver.implicitly_wait(5)
        place_environment_reset(self.driver)

    def test3_place_Sleep(self):
        """进入 place 住宿 并分享周边兴趣列表位置"""
        test_name = "住宿下分享"
        mylogger.debug("%s start" % test_name)
        self.driver.implicitly_wait(5)
        mainChat_element(self.driver)
        place_environment(driver=self.driver)
        self.driver.implicitly_wait(5)
        chat_place_sleep(self.driver)
        self.driver.implicitly_wait(5)
        chat_place_surrounding_share(self.driver, n=1)
        mylogger.info("分享位置触发")
        time.sleep(2)
        screenShot(driver=self.driver, test_name=test_name)
        self.driver.implicitly_wait(5)
        place_environment_reset(self.driver)

    def test4_place_Food(self):
        """进入 place food 并分享周边兴趣列表位置"""
        test_name = "美食下分享"
        mylogger.debug("%s start" % test_name)
        self.driver.implicitly_wait(5)
        mainChat_element(self.driver)
        place_environment(driver=self.driver)
        self.driver.implicitly_wait(5)
        chat_place_eat(self.driver)
        self.driver.implicitly_wait(5)
        chat_place_surrounding_share(self.driver, n=1)
        mylogger.info("分享位置触发")
        time.sleep(2)
        screenShot(driver=self.driver, test_name=test_name)
        self.driver.implicitly_wait(5)
        place_environment_reset(self.driver)

    def test5_place_Visit(self):
        """进入 place visit 并分享周边兴趣列表位置"""
        test_name = "游玩出行下分享"
        mylogger.debug("%s start" % test_name)
        self.driver.implicitly_wait(5)
        mainChat_element(self.driver)
        place_environment(driver=self.driver)
        self.driver.implicitly_wait(5)
        chat_place_visit(self.driver)
        self.driver.implicitly_wait(5)
        chat_place_surrounding_share(self.driver, n=1)
        mylogger.info("分享位置触发")
        time.sleep(2)
        screenShot(driver=self.driver, test_name=test_name)
        self.driver.implicitly_wait(5)
        place_environment_reset(self.driver)

    def test6_place_Move(self):
        """进入 place move 并分享周边兴趣列表位置"""
        test_name = "出行下分享"
        mylogger.debug("%s start" % test_name)
        self.driver.implicitly_wait(5)
        mainChat_element(self.driver)
        place_environment(driver=self.driver)
        self.driver.implicitly_wait(5)
        chat_place_move(self.driver)
        self.driver.implicitly_wait(5)
        chat_place_surrounding_share(self.driver, n=1)
        mylogger.info("分享位置触发")
        time.sleep(2)
        screenShot(driver=self.driver, test_name=test_name)
        self.driver.implicitly_wait(5)
        place_environment_reset(self.driver)

    def test7_place_Service(self):
        """进入 place service 并分享周边兴趣列表位置"""
        test_name = "出行下分享"
        mylogger.debug("%s start" % test_name)
        self.driver.implicitly_wait(5)
        mainChat_element(self.driver)
        place_environment(driver=self.driver)
        self.driver.implicitly_wait(5)
        chat_place_service(self.driver)
        self.driver.implicitly_wait(5)
        chat_place_surrounding_share(self.driver, n=1)
        mylogger.info("分享位置触发")
        time.sleep(2)
        screenShot(driver=self.driver, test_name=test_name)
        self.driver.implicitly_wait(5)
        place_environment_reset(self.driver)

    def test8_place_Nearby(self):
        """进入 place Nearby 页面"""
        test_name = "出行下分享"
        mylogger.debug("%s start" % test_name)
        self.driver.implicitly_wait(5)
        mainChat_element(self.driver)
        place_environment(driver=self.driver)
        self.driver.implicitly_wait(5)
        chat_place_nearby(self.driver)
        self.driver.implicitly_wait(5)
        mylogger.info("进入周边分享界面")
        time.sleep(2)
        screenShot(driver=self.driver, test_name=test_name)
        self.driver.implicitly_wait(5)
        self.driver.press_keycode(4)
        time.sleep(2)
        self.driver.press_keycode(4)
        place_environment_reset(self.driver)

    def test9_place_Favor(self):
        """进入 place service 并分享周边兴趣列表位置"""
        test_name = "出行下分享"
        mylogger.debug("%s start" % test_name)
        self.driver.implicitly_wait(5)
        mainChat_element(self.driver)
        place_environment(driver=self.driver)
        self.driver.implicitly_wait(5)
        chat_place_service(self.driver)
        self.driver.implicitly_wait(5)
        chat_place_surrounding_share(self.driver, n=1)
        mylogger.info("分享位置触发")
        time.sleep(2)
        screenShot(driver=self.driver, test_name=test_name)
        self.driver.implicitly_wait(5)
        place_environment_reset(self.driver)




if __name__ == '__main__':
    unittest.main(verbosity=2)