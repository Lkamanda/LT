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

    def test_2(self):
        """通过搜索分享地点"""
        self.driver.implicitly_wait(5)
        mainChat_element(self.driver)
        place_environment(driver=self.driver)
        time.sleep(2)
        self.driver.implicitly_wait(10)
        # 搜索地点
        self.driver.find_element_by_id("com.erlinyou.worldlist:id/search_edit").send_keys(u"辅导费")
        chat_place_search_place(driver=self.driver, place=myconfig.get_place_share_search(n=1))
        mylogger.info("触发：输入框输入")




















if __name__ == '__main__':
    unittest.main(verbosity=2)