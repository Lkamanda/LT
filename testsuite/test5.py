import unittest
from comm.usuallymodule import *
from comm.webDriver import *


#  """移动地图，旋转地图，2D、3D切换"""
class Test5(webDriver, unittest.TestCase):
    # def test1_a(self):
    #     """zh 登录"""
    #     zh_login(self=self, driver=self.driver)
    #     self.driver.press_keycode(4)
    #     mylogger.info("返回home page")

    # def test2_a(self):
    #     """回家"""
    #     test_name = "回家"
    #     mylogger.info("%s" % test_name)
    #     self.driver.implicitly_wait(5)
    #     homepage_input_box(self.driver)
    #     print("输入")
    #     go_home_number = 0
    #     self.driver.implicitly_wait(5)
    #     try:
    #         homepage_details_go_home_add(self.driver)
    #         go_home_number = go_home_number
    #     except:
    #         homepage_details_go_home_cancel_element(self.driver)
    #         go_home_number = go_home_number + 1
    #         print(2)
    #
    #     if go_home_number == 0:
    #         mylogger.info("进入添加家的测试用例")
    #         # go_home_number.click()
    #         chat_place_search_place(driver=self.driver, n=3)
    #         mylogger.info('触发输入家的地址成功')
    #         # 选择查询到的第一个搜索结果
    #         self.driver.find_element_by_xpath(
    #             "//android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.view.View").click()
    #         mylogger.info("选择搜索结果成功")
    #         homepage_details_go_home_element(self.driver)
    #         mylogger.info("进入导航页")
    #     elif go_home_number == 1:
    #         homepage_details_go_home_element(self.driver)
    #         mylogger.info("进入导航页，已经设置家")
    #         check_direct_go_home(driver=self.driver, test_name=test_name)
    #     self.driver.implicitly_wait(5)
    #     navigation_details_goto_element(self.driver)
    #     screenShot(driver=self.driver, test_name="%s+ '路线规划图'" % test_name)
    #     mylogger.info("开始规划路线")
    #     time.sleep(3)
    #     navigation_details_navigation_element(self.driver)
    #     mylogger.info("开始导航")
    #     screenShot(driver=self.driver, test_name="%s+ '导航开始'" % test_name)
    #     self.driver.press_keycode(4)
    #     # navigation_details_quit(self.driver)
    #     time.sleep(1)
    #     self.driver.press_keycode(4)
    #
    # def test3_a(self):
    #     # 未完成
    #     """旋转地图"""
    #     test_name = "旋转地图"
    #     mylogger.info("%s" % test_name)
    #     time.sleep(3)
    #     homepage_location_element(self.driver)
    #     mylogger.info("触发旋转")
    #     screenShot(self.driver, test_name)
    #     homepage_location_element(self.driver)
    #     screenShot(self.driver, test_name)
    #
    # def test3_a_1(self):
    #     """2D和3D之间的切换"""
    #     test_name = "2D和3D之间的切换"
    #     mylogger.info("%s" % test_name)
    #     time.sleep(2)
    #     homepage_amplification_element(self.driver)
    #     time.sleep(2)
    #     homepage_amplification_element(self.driver)
    #     time.sleep(2)
    #     homepage_amplification_element(self.driver)
    #     homepage_2d_3d(self.driver)
    #     mylogger.info("切换成了3d")
    #     time.sleep(4)
    #     screenShot(driver=self.driver, test_name="%s+'3d截图'" % test_name)
    #     homepage_2d_3d(self.driver)
    #     screenShot(driver=self.driver, test_name="%s+'2d截图'" % test_name)

    def test4_a_1(self):
        """进入漫游模式"""
        test_name = "进入漫游模式"
        mylogger.info("%s" % test_name)
        self.driver.implicitly_wait(5)
        homepage_roam_element(self.driver)
        
        roam_page_look_more_element(self.driver)
        roam_page_choice_ldmark(driver=self.driver, n=6)
        screenShot(driver=self.driver, test_name="漫游截图")
        time.sleep(4)
        roam_page_goto_element(self.driver)






