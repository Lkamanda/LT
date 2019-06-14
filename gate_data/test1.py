# import datetime
# now_time = datetime.datetime.now()
# yes_time = now_time + datetime.timedelta(days=-1)
# start_time = yes_time.strftime('%Y-%m-%d') + " " + "00:00:00"
# print(start_time)

# import subprocess

# returnCode = subprocess.call('adb devices')
# print(type(returnCode))
import os

# b = os.popen('adb devices')
# text2 = b.read()
# print(text2)
# print(type(text2))
# b.close()
# import re
# c = "a82ccd1d	device"
#
# # print(re.split(r'[:,\s]\s*', c)[0])
# print(re.split(r'[\s]\s*', c)[0])


deviceAndroidVersion = list(os.popen('adb shell getprop ro.build.version.release'))
print(deviceAndroidVersion)