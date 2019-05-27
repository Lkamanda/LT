from HTMLTestRunner import HTMLTestRunner
import unittest
from comm.common import *
from comm.mylog import *


class runner:
    def getSuite(self):
        """获取执行测试套件"""
        start_dir = os.path.join(os.path.dirname(os.path.dirname(__file__))) + '/testsuite'
        print(start_dir)
        suite = unittest.TestLoader().discover(
            start_dir=start_dir,
            pattern='test*.py',
            top_level_dir=None
        )
        return suite

    def run(self):
        """测试suite执行"""
        # 获取当前时间戳
        now_time = str_nowTime()
        # 定义报告存放路径
        report_file = str(
            os.path.dirname(os.path.dirname(__file__)) + '/report/html_result/%sTest Report.html') % now_time
        fp = open(report_file, 'wb')
        # filename = 'F:/ ' + now + 'result.html'
        # 定义测试报告
        runner1 = HTMLTestRunner(stream=fp, title='test report', description='version-1')
        suite = self.getSuite()
        runner1.run(suite)
        fp.close()  # 关闭报告文件

    def main(self):
        n = 0
        z = 0
        for i in range(1, 2):
            print("运行第%s次" % i)
            try:
                z = z + 1
                self.run()
            except Exception as e:
                print(e)
                n = n + 1
                if n == 2:
                    break
                else:
                    self.run()
        all_run_number = z + n
        print(all_run_number)
        mylogger.info("这次运行执行了%s" % all_run_number)


if __name__ == '__main__':
    runner = runner()
    runner.main()

