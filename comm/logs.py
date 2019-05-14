import logging.config

import os
import time
from logging.handlers import RotatingFileHandler


class myLog:
    def __init__(self):
        global format1, logPath
        # 日志内容的格式
        format1 = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # # 日志大小和数目
        # backupCount = int(myConfig.getLog('backupCount'))
        # maxBytes = int(myConfig.getLog('maxBytes'))
        # # 日志级别
        # logLevel = int(myConfig.getLog('level'))
        # 文件的日期格式
        rq = time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime(time.time()))
        # log文件的存放路径
        logPath = os.path.dirname(os.getcwd()) + '/report/logs/' + rq + 'logs.text'
        # report文件的存放路径
        # now = time.strftime('%Y-%m-%d_%H_%M_%S')
        # reportPath = os.path.dirname(os.getcwd()) + '/report/logs/' + rq + 'logs.text'

    # 保存日志到文件的函数
    # 日志存放路径
    @staticmethod
    def getLogPath():
        return logPath
    # # 测试报告存放路径
    # @staticmethod
    # def getReportPath():
    #     return reportPath
    @staticmethod
    def logger():
        # 创建一个logger
        logger1 = logging.getLogger()
        logger1.setLevel(logging.DEBUG)
        if not logger1.handlers:
            # 创建一个handler,用于写入文件
            Rthandler = RotatingFileHandler(myLog().getLogPath(), encoding='utf-8')
            # 这里来设置日志的级别
            # CRITICAl    50
            # ERROR    40
            # WARNING    30
            # INFO    20
            # DEBUG    10
            # NOSET    0

            # 定义handler的输出格式
            logFormat = logging.Formatter(format1)
            # 给handler添加formatter
            Rthandler.setFormatter(logFormat)
            logger1.removeHandler(Rthandler)
            # 给logger添加handler
            logger1.addHandler(Rthandler)
        return logger1