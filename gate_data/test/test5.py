import subprocess

from time import ctime


def appium_start(host, port):
    bootstrap_port = str(port + 1)

    # /b表示不打开cmd命令窗口，-p表示指定appium端口，-bp表示指定appium和设备通信的端口

    cmd = 'start /b appium -a ' + host + ' -p ' + str(port) + ' -bp ' + str(bootstrap_port)

    print('%s at %s' % (cmd, ctime()))

    # a是追加写入的方式

    # subprocess.Popen(cmd, shell=True, stdout=open('appium_log/' + str(port) + '.log', 'a'), stderr=subprocess.STDOUT)


if __name__ == '__main__':

    host = '127.0.0.1'

    port = 4723

    for i in range(2):
        port = 4723 + 2 * i

        appium_start(host, port)
