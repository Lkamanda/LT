import subprocess

from time import ctime

import multiprocessing  # 导入多进程模块


def appium_start(host, port):
    bootstrap_port = str(port + 1)

    # /b是不打开cmd命令窗口

    cmd = 'start /b appium -a ' + host + ' -p ' + str(port) + ' -bp ' + str(bootstrap_port)

    print('%s at %s' % (cmd, ctime()))

    # a是追加写入的方式

    # subprocess.Popen(cmd, shell=True, stdout=open('appium_log/' + str(port) + '.log', 'a'), stderr=subprocess.STDOUT)


# 构建appium进程组
appium_process = []

# 加载appium进程

for i in range(2):
    host = '127.0.0.1'

    port = 4723 + 2 * i

    # target指向方法，args指向参数，且必须是一个元组的形式

    appium = multiprocessing.Process(target=appium_start, args=(host, port))

    # 将进程从变量appium加载到进程内

    appium_process.append(appium)

if __name__ == '__main__':

    # 并发启动appium服务，for循环开启多个appium服务，join主进程等待子进程结束

    for appium in appium_process:
        appium.start()

    for appium in appium_process:
        appium.join()
