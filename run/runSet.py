from HTMLTestRunner import HTMLTestRunner
import os, time
import unittest
from comm.common import *


def getSuite():
    """获取执行测试套件"""
    start_dir = os.path.join(os.path.dirname(os.path.dirname(__file__))) + '/testsuite'
    print(start_dir)
    suite = unittest.TestLoader().discover(
        start_dir=start_dir,
        pattern='test*.py',
        top_level_dir=None
    )
    # print(1)
    return suite


def run():
    """测试suite执行"""
    # 获取当前时间戳
    now_time = str_nowTime()
    # 定义报告存放路径
    report_file = str(os.path.dirname(os.path.dirname(__file__)) + '/report/html_result/%sTest Report.html') % now_time
    fp = open(report_file, 'wb')
    # filename = 'F:/ ' + now + 'result.html'
    # 定义测试报告
    runner = HTMLTestRunner(stream=fp, title='test report', description='version-1')
    suite = getSuite()
    runner.run(suite)
    fp.close()  # 关闭报告文件


if __name__ == '__main__':
    run()
