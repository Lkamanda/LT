"""
微信用户的登录和退出
"""
import unittest
from comm.webDriver import *
from page_element.home_page_element import *
from page_element.login_page_element import *
from page_element.mine_leavemap_allmap_element import *
from page_element.mine_page_element import *
from page.Assertion import *
from comm.logging import Logger
from comm.common import *


class WX(webDriver, unittest.TestCase):

    # @unittest.skip('not need')
    def test_1(self):
        """微信登录"""
        # 返回测试用例名称
        test_name = self._testMethodName
        print(self._testMethodName)
        self.driver.implicitly_wait(5)
        userAvatar_element(self.driver)
        mylogger.info("进入我的页面")
        self.driver.implicitly_wait(5)
        dL_element(self.driver)
        mylogger.info('点击注册/登录 进入登录页面')
        self.driver.implicitly_wait(5)
        wX_element(self.driver)
        mylogger.info('点击微信图标进行登录')
        # mylogger.info('点击微信图标登录微信')
        # self.driver.implicitly_wait(5)
        # wxUser(self.driver, wx_username='1599200510')
        # self.driver.implicitly_wait(5)
        # wxPassword(self.driver, wx_password='5211314zxy.')
        # self.driver.implicitly_wait(5)
        # wxDl(self.driver)
        # self.driver.find_element_by_name("我的").click()
        # 检查页面是否存在
        self.assertEqual(True, check_wx_login(self.driver, test_name))
        mylogger.info('微信登录成功')
        # self.driver.keyevent('BACK')
        allmap_back_element(self.driver)
        mylogger.info("return my page success")
        allmap_back_element(self.driver)
        mylogger.info("return home page success")

    def test_2(self):
        """当前用户退出"""
        # 测试账号被访问数必须不为0
        test_name = "当前用户退出"
        self.driver.implicitly_wait(3)
        userAvatar_element(self.driver)
        mylogger.info("get into mine home page")
        swipeUp(driver=self.driver, t=1000)
        mylogger.info("向上滑动屏幕")
        self.driver.implicitly_wait(4)
        mine_setting(self.driver)
        self.driver.find_element_by_id("com.erlinyou.worldlist:id/btn_logout").click()
        mylogger.info("触发退出登录按钮")
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("android:id/button1").click()
        mylogger.info("确认退出登录退出")
        allmap_back_element(self.driver)
        mylogger.info("返回我的页面")
        self.assertEqual(True, check_wx_logout(driver=self.driver, test_name=test_name))
        mylogger.info("登录退出成功")


if __name__ == '__main__':
    unittest.main(verbosity=2)