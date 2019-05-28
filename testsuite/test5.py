import unittest
from comm.usuallymodule import *
from comm.webDriver import *


#  """移动地图，旋转地图，2D、3D切换"""
class Test5(webDriver, unittest.TestCase):
    # def test1(self):
    #     """zh 登录"""
    #     zh_login(self=self, driver=self.driver)
    #     self.driver.press_keycode(4)
    #     mylogger.info("返回home page")

    def test2(self):
        """回家"""
        test_name = "回家"
        mylogger.info("%s" % test_name)
        self.driver.implicitly_wait(5)
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

        if go_home_number == 0:
            mylogger.info("进入添加家的测试用例")
            # go_home_number.click()
            chat_place_search_place(driver=self.driver, n=3)
            mylogger.info('触发输入家的地址成功')
            # 选择查询到的第一个搜索结果
            self.driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.view.View").click()
            mylogger.info("选择搜索结果成功")
            homepage_details_go_home_element(self.driver)
            mylogger.info("进入导航页")