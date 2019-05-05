import os, time, unittest
from LT.comm.webDriver import *
from LT.comm.pageElement import *
from LT.comm.common import *


class LT(webDriver, unittest.TestCase):
    def test_1(self):
        """微信登录"""
        # print(self._testMethodName) 返回测试用例名称
        test_name = self._testMethodName
        self.driver.implicitly_wait(5)
        userAvatar(self.driver)
        self.driver.implicitly_wait(5)
        dL(self.driver)
        self.driver.implicitly_wait(5)
        wX(self.driver)
        self.driver.implicitly_wait(5)
        wxUser(self.driver, wx_username='1599200510')
        self.driver.implicitly_wait(5)
        wxPassword(self.driver, wx_password='5211314zxy.')
        self.driver.implicitly_wait(5)
        wxDl(self.driver)
        time.sleep(5)
        screenShot(self.driver, test_name)


if __name__ == '__main__':
    unittest.main(verbosity=2)