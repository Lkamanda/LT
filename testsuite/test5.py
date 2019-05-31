import unittest
from comm.usuallymodule import *
from comm.webDriver import *


#  """移动地图，旋转地图，2D、3D切换"""
class Test5(webDriver, unittest.TestCase):
    def test1_a(self):
        """zh 登录"""
        zh_login(self=self, driver=self.driver)
        self.driver.press_keycode(4)
        mylogger.info("返回home page")

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

    def test3_a(self):
        # 未完成
        """旋转地图"""
        test_name = "旋转地图"
        mylogger.info("%s" % test_name)
        time.sleep(3)
        homepage_location_element(self.driver)
        mylogger.info("触发旋转")
        screenShot(self.driver, test_name)
        homepage_location_element(self.driver)
        screenShot(self.driver, test_name)

    def test3_a_1(self):
        """2D和3D之间的切换"""
        test_name = "2D和3D之间的切换"
        mylogger.info("%s" % test_name)
        time.sleep(2)
        homepage_amplification_element(self.driver)
        time.sleep(2)
        homepage_amplification_element(self.driver)
        time.sleep(2)
        homepage_amplification_element(self.driver)
        homepage_2d_3d(self.driver)
        mylogger.info("切换成了3d")
        time.sleep(4)
        screenShot(driver=self.driver, test_name="%s+'3d截图'" % test_name)
        homepage_2d_3d(self.driver)
        screenShot(driver=self.driver, test_name="%s+'2d截图'" % test_name)

    def test4_a_1(self):
        """进入漫游模式"""
        test_name = "进入漫游模式"
        mylogger.info("%s" % test_name)
        self.driver.implicitly_wait(5)
        homepage_roam_element(self.driver)
        roam_page_look_more_element(self.driver)
        self.driver.implicitly_wait(5)
        roam_page_choice_ldmark(driver=self.driver, n=6)
        screenShot(driver=self.driver, test_name="漫游截图")
        time.sleep(2)
        roam_page_goto_element(self.driver)
        navigation_details_navigation_element(self.driver)
        self.driver.implicitly_wait(5)
        navigation_details_quit(self.driver)
        self.driver.press_keycode(4)
        time.sleep(1)
        self.driver.press_keycode(4)
        mylogger.info("返回主页面")

    def test5_a_1(self):
        """搜索街道，计算路径，导航回家"""
        test_name = "搜索街道，计算路径，导航回家"
        mylogger.debug("%s" % test_name)
        self.driver.implicitly_wait(10)
        homepage_input_box(self.driver)
        chat_place_search_place(driver=self.driver, n=1)
        chat_place_choice_All(driver=self.driver, n=1)
        navigation_details_goto_element(self.driver)
        mylogger.info("进入路线规划")
        time.sleep(2)
        screenShot(driver=self.driver, test_name="%s+'路线导航'" % test_name)
        navigation_details_navigation_element(self.driver)
        time.sleep(4)
        self.driver.press_keycode(4)
        time.sleep(1)
        self.driver.press_keycode(4)
        mylogger.info("返回主页面")

    def test5_a_2(self):
        """搜索地点，计算路径，导航回家"""
        test_name = "搜索地点，计算路径，导航回家"
        mylogger.debug("%s" % test_name)
        self.driver.implicitly_wait(10)
        homepage_input_box(self.driver)
        chat_place_search_place(driver=self.driver, n=0)
        chat_place_choice_All(driver=self.driver, n=1)
        navigation_details_goto_element(self.driver)
        mylogger.info("进入路线规划")
        time.sleep(2)
        screenShot(driver=self.driver, test_name="%s+'路线导航'" % test_name)
        navigation_details_trip_mode(driver=self.driver, mode=2)
        navigation_details_navigation_element(self.driver)
        time.sleep(4)
        self.driver.press_keycode(4)
        time.sleep(1)
        self.driver.press_keycode(4)
        mylogger.info("返回主页面")

    def test5_a_3(self):
        """搜索门牌号，计算路径，导航回家"""
        test_name = "搜索街道，计算路径，导航回家"
        mylogger.debug("%s" % test_name)
        self.driver.implicitly_wait(10)
        homepage_input_box(self.driver)
        chat_place_search_place(driver=self.driver, n=4)
        chat_place_choice_All(driver=self.driver, n=1)
        navigation_details_goto_element(self.driver)
        mylogger.info("进入路线规划")
        time.sleep(2)
        screenShot(driver=self.driver, test_name="%s+'路线导航'" % test_name)
        navigation_details_navigation_element(self.driver)
        time.sleep(4)
        self.driver.press_keycode(4)
        time.sleep(1)
        self.driver.press_keycode(4)
        mylogger.info("返回主页面")

    def test6_a_1(self):
        """汽车、步行、自行车导航模式"""
        mode_list = [2, 3, 4, 5, 6]
        for i in mode_list:
            test_name_list = ["0", "1", "汽车", "公交", "地铁", "步行", "自行车"]
            test_name = test_name_list[i]
            mylogger.debug("%s" % test_name)
            self.driver.implicitly_wait(10)
            homepage_input_box(self.driver)
            self.driver.implicitly_wait(10)
            chat_place_search_place(driver=self.driver, n=5)
            self.driver.implicitly_wait(10)
            chat_place_choice_All(driver=self.driver, n=1)
            self.driver.implicitly_wait(10)
            navigation_details_goto_element(self.driver)
            mylogger.info("进入路线规划")
            screenShot(driver=self.driver, test_name="%s+'路线规划'" % test_name)
            self.driver.implicitly_wait(10)
            navigation_details_trip_mode(driver=self.driver, mode=i)
            if i == 2 or i == 5 or i == 6:
                self.driver.implicitly_wait(10)
                navigation_details_navigation_element(self.driver)
                time.sleep(2)
            elif i == 3:
                time.sleep(2)
                screenShot(driver=self.driver, test_name="公交路线图")
            elif i == 4:
                mylogger.info("进入地铁路线图")
                time.sleep(2)
                screenShot(driver=self.driver, test_name="地铁路线图")
                # 地铁mode下导航
                self.driver.implicitly_wait(5)
                self.driver.find_element_by_id("com.erlinyou.worldlist:id/detail_iconbutton_container").click()
                mylogger.info("进入地铁导航详情")
                self.driver.find_element_by_id("com.erlinyou.worldlist:id/exit_img").click()
            self.driver.press_keycode(4)
            time.sleep(1)
            self.driver.press_keycode(4)
            mylogger.info("返回主页面")

    def test7_a_1(self):
        """添加历史记录，并对历史记录校验"""
        test_name = "添加历史记录，并对历史记录校验"
        mylogger.debug("%s" % test_name)
        self.driver.implicitly_wait(10)
        homepage_input_box(self.driver)
        self.driver.implicitly_wait(10)
        chat_place_search_place(driver=self.driver, n=6)
        self.driver.implicitly_wait(10)
        self.driver.press_keycode(4)
        self.driver.press_keycode(4)
        self.driver.implicitly_wait(5)
        homepage_input_box(self.driver)
        






