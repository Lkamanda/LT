"""
在message下对place模块下功能进行测试
"""
import unittest
from comm.usuallymodule import *
from comm.webDriver import *


class Message_zh(webDriver, unittest.TestCase):

    def test_1(self):
        """zh login """
        zh_login(self=self, driver=self.driver)

    def test_2(self):
        """通过搜索分享地点"""
        place_environment(driver=self.driver)
        time.sleep(2)
        # 搜索地点
        chat_place_search_place(driver=self.driver, place=myconfig.get_place_share_search(n=1))
        time.sleep(4)



















if __name__ == '__main__':
    unittest.main(verbosity=2)