import unittest
from comm.webDriver import *
from comm.common import *
from page_element.home_page_element import *
from page_element.login_page_element import *
from page_element.message_page_element import *
from page_element.mine_page_element import *
from page_element.mine_leavemap_allmap_element import *
from comm.logging import *
from page.Assertion import check_mobile_login


class ZH_message(webDriver, unittest.TestCase):
    # @unittest.skip('not need')  跳过该跳测试用例
    def test_dl_mobile_number(self):
        """登录手机账号密码"""
        print(self._testMethodName)  # 返回测试用例名称
        test_name = self._testMethodName
        self.driver.implicitly_wait(5)
        mainChat_element(self.driver)
        mylogger.info("进入登录页面成功")
        self.driver.implicitly_wait(5)
        mobile_tile_element(self.driver)
        mylogger.info("切换成账号密码登录")
        self.driver.implicitly_wait(5)
        mobile_user_element(self.driver)
        mylogger.info("输入账号成功")
        mobile_password_element(self.driver)
        mylogger.info("输如密码成功")
        self.driver.implicitly_wait(5)
        mobile_login_element(self.driver)
        mylogger.info("触发登录")
        self.assertEqual(True, check_mobile_login(self.driver, test_name))
        mylogger.info("登录成功")

    def



if __name__ == '__main__':
    unittest.main(verbosity=2)