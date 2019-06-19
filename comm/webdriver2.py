# from appium import webdriver
#
# from comm.common import *
#
#
# def get_webdrver(z):
#
#     global driver
#     port = 4723
#     mobile_config, device_count = get_android_devices()
#     print(mobile_config, device_count)
#     desired_caps = {'platformName': 'Android',     # 手机类型
#                     'platformVersion': mobile_config[0][1],   # 被测试手机，   baa822b7
#                     'deviceName': mobile_config[0][0],     # baa822b7  a82ccd1d Q8JNNNGUOF8L4PON   设备名称， adb devices
#                     'appPackage': 'com.erlinyou.worldlist',
#                     'appActivity': 'com.erlinyou.map.Erlinyou',
#                     'unicodeKeyboard': True,     # appium 传输中使用自己的输入法，可以传输中文
#                     'resetKeyboard': True,      # 程序结束时重置原来的输入法
#                     'noReset': True,       # 如果app存在则不重新安装
#                     # 'autoGrantPermissions': 'True'
#                     # 'app': r"C:\Users\zhoujialin\PycharmProjects\aut_LT\LT\apps\boobuz.apk"
#                     # desired_caps['autoGrantPermissions'] = 'True'
#                     }
#     time.sleep(3)
#     try:
#         if z == 0:
#             driver = webdriver.Remote("http://127.0.0.1:" + str(port) + '/wd/hub', desired_caps)
#             return
#             # driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
#         # myLog.logger().info('driver加载成功 %s', cls.driver)
#     except Exception as e:
#         # myLog.logger().info('driver加载失败 %s', e)
#         print(e)

from run.runSet import runner
