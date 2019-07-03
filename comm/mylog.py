# logging模块支持我们自定义封装一个新日志类
import logging
import os.path
import time
from comm.common import str_nowTime
from comm.common import screenShot


class Logger(object):

    def __init__(self, logger):
        """
        指定保存日志的文件路径，日志级别，调用文件
        将日志存入到指定的文件中
        :param logger:
        """
        # 创建一个logger(记录器)
        # 日志记录的工作主要由Logger对象来完成。在调用getLogger时要提供Logger的名称（注：多次使用相同名称 来调用getLogger，返回的是同一个对象的引用。）
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于写入日志文件
        # rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        rq = str_nowTime()
        # print("this is log %s" % testCase_id)
        log_name = os.path.dirname(os.getcwd()) + '/report/logs/' + rq + 'logs.text'
        # log_name = log_path + rq + '.log'  # 文件名
        # print(log_name)
        # 将日志写入磁盘
        fh = logging.FileHandler(log_name, encoding="utf-8")
        fh.setLevel(logging.INFO)
        fh.setLevel(logging.DEBUG)
        # 创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setLevel(logging.DEBUG)
        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def get_log(self):
        return self.logger


mylogger = Logger(logger="Logger").get_log()
