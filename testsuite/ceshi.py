import unittest
from comm.usuallymodule import *
from comm.webDriver import *

class Test5(webDriver, unittest.TestCase):
    # def test1_a(self):
    #     """zh 登录"""
    #     zh_login(self=self, driver=self.driver)
    #     self.driver.press_keycode(4)
    #     mylogger.info("返回home page")

    def test2_a_0(self):
        """回家"""
        test_name = "回家"
        mylogger.info("%s" % test_name)
        self.driver.implicitly_wait(10)
        homepage_input_box(self.driver)
        print("输入")
        go_home_number = 0
        self.driver.implicitly_wait(5)
        try:
            homepage_details_go_home_add(self.driver)
            go_home_number = go_home_number
        except:
            homepage_details_go_home_cancel_element(self.driver)
            go_home_number = go_home_number + 1
            print(2)

        if go_home_number == 0:
            mylogger.info("进入添加家的测试用例")
            # go_home_number.click()
            chat_place_search_place(driver=self.driver, n=3)
            mylogger.info('触发输入家的地址成功')
            # 选择查询到的第一个搜索结果
            self.driver.find_element_by_xpath(
                "//android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.view.View").click()
            mylogger.info("选择搜索结果成功")
            homepage_details_go_home_element(self.driver)
            mylogger.info("进入导航页")
        elif go_home_number == 1:
            homepage_details_go_home_element(self.driver)
            mylogger.info("进入导航页，已经设置家")
            check_direct_go_home(driver=self.driver, test_name=test_name)
        self.driver.implicitly_wait(5)
        navigation_details_goto_element(self.driver)
        screenShot(driver=self.driver, test_name="%s+ '路线规划图'" % test_name)
        mylogger.info("开始规划路线")
        self.driver.implicitly_wait(20)
        navigation_details_trip_mode(driver=self.driver, mode=2)
        navigation_details_navigation_element(self.driver)
        mylogger.info("开始导航")
        screenShot(driver=self.driver, test_name="%s+ '导航开始'" % test_name)
        self.driver.press_keycode(4)
        # navigation_details_quit(self.driver)
        time.sleep(1)
        self.driver.press_keycode(4)
        mylogger.info("返回主页面")

    def test2_a_1(self):
        """取消回家并对家重新设置"""
        test_name = "取消回家操作"
        mylogger.info("%s" % test_name)
        self.driver.implicitly_wait(5)
        homepage_input_box(self.driver)
        go_home_number = 0
        self.driver.implicitly_wait(5)
        try:
            homepage_details_go_home_add(self.driver)
            go_home_number = go_home_number
            print(1)
        except Exception as e:
            print(e)
            mylogger.info("当前用户已经设置了回家")
            homepage_details_go_home_cancel_element(self.driver)
            go_home_number = go_home_number + 1
            print(2)

        if go_home_number == 0:
            mylogger.info("进入添加家的测试用例")
            # go_home_number.click()
            chat_place_search_place(driver=self.driver, n=3)
            mylogger.info('触发输入家的地址成功')
            # 选择查询到的第一个搜索结果
            self.driver.find_element_by_xpath(
                "//android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.view.View").click()
            mylogger.info("选择搜索结果成功")
            homepage_details_go_home_element(self.driver)
            mylogger.info("进入导航页")
            self.driver.implicitly_wait(5)
            navigation_details_goto_element(self.driver)
            screenShot(driver=self.driver, test_name="%s+ '路线规划图'" % test_name)
            mylogger.info("开始规划路线")
            self.driver.implicitly_wait(10)
            navigation_details_trip_mode(driver=self.driver, mode=2)
            navigation_details_navigation_element(self.driver)
            mylogger.info("开始导航")
            screenShot(driver=self.driver, test_name="%s+ '导航开始'" % test_name)
        elif go_home_number == 1:
            homepage_details_go_home_cancel_element_1(self.driver)
            mylogger.info("取消回家设置")
            homepage_details_go_home_add(self.driver)
            self.assertTrue(check_cancel_go_home(driver=self.driver, test_name=test_name))
        self.driver.press_keycode(4)
        time.sleep(1)
        self.driver.press_keycode(4)