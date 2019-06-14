from appium import webdriver
import os
import re
import threading
import time
def startServers(serial, port):
    cmd = 'appium --address 127.0.0.1' + ' --port' + str(port) + ' --bookstrap-port ' + str(port -2000) + '-U' + serial + '--session-override --no-reset'
    os.system(cmd)


class Test:
    def seTUp(self, serial, newPort, systemPort):
        desired_caps = {}
        desired_caps['platformName'] = 'Android',
        desired_caps['platformVersion'] = '8.0',
        desired_caps['deviceName'] = 'Android'
        # 'appPackage': 'com.erlinyou.worldlist',
        # 'appActivity': 'com.erlinyou.map.Erlinyou',
        desired_caps['appPackage'] = 'com.erlinyou.worldlist',
        desired_caps['appActivity'] = 'com.erlinyou.map.Erlinyou',
        desired_caps["systemPort"] = systemPort
        self.driver = webdriver.Remote('http://127.0.0.1:' + str(newPort) + '/wd/hub', desired_caps)
        self.testCase(serial)

    def testCase(self, serial):
        self.tearDown()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    threads = []   # 定义server线程池
    threads1 = []  # 定义driver 线程池
    port = 4723    # 初始化默认端口
    out = os.popen('adb devices')  # 输出设备信息
    a = 0
    for i in out.readlines():
        if 'List of devicces' in i or "adb" in or 'daemon' in i or 'offline' in i or "unauthorized" in i or len(i) < 5:
            pass
        else:
            serial = re.findall('(.*?) device', i)
            newPort  = port + a
            systemPort = port + a + 4000
            test = Test()
            a = a + 1
            serial = re.findall('(.*?) device', i) # 设备序列号
            threads.append(threading.Thread(target=startServers, args=(serial[0], newPort),))
            threads1.append(threading.Thread(target=test.setUp, args= (serial[0], newPort, systemPort,)))

    for t in threads:
        t.start()
    time.sleep(20)
    for i in threads1:
        i.start()