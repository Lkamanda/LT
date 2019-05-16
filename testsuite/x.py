"""
微信用户的登录和退出
"""
import unittest
from comm.webDriver import *
from comm.usuallymodule import *


class WX(webDriver, unittest.TestCase):

    # @unittest.skip('not need')
    def test_1(self):
        """微信登录"""
        print("test_1")
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
        print("test_2")
        logout(self=self, driver=self.driver)


if __name__ == '__main__':
    unittest.main(verbosity=2)