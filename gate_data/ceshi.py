from selenium import webdriver
import pytesseract as pt
from PIL import Image
import time
import datetime
import requests
# import tesserocr
# img_address = "http://static.jingcailvtu.org:9081/stats-admin/imageServlet"
#
#
# r = requests.get(img_address)
# with open('./03.png', 'wb') as f:
#     f.write(r.content)
#     print(1)
#
# image = Image.open("03.png")
# result = tesserocr.image_to_text(image)
# print(result)
#
# #image = Image.open("YM_01.png")
# # 调用pytessreact,把图片转换成文字
#
# driver.find_element_by_name("randomCode").send_keys(result)

def yesterday():
    now_time = datetime.datetime.now()
    yes_time = now_time + datetime.timedelta(days=-1)
    start_time = yes_time.strftime('%Y-%m-%d') + " " + "00:00:00"
    print(start_time)
    return start_time


driver = webdriver.Chrome()
driver.get("http://static.jingcailvtu.org:9081/stats-admin/framework")
driver.implicitly_wait(5)
pass_word = "zhoujialin"
driver.find_element_by_id("username").send_keys(pass_word)
driver.implicitly_wait(5)
driver.find_element_by_id("password").send_keys(pass_word)
driver.implicitly_wait(5)
time.sleep(10)
# driver.find_element_by_xpath('//*[@id="loginForm"]/div[4]/input').click()
# 启动记录
driver.implicitly_wait(10)
driver.find_element_by_xpath('//*[@id="_easyui_tree_3"]/span[3]').click()
select_list = ['360', 'baidu', 'huawei', 'mi', 'oppo', 'tencent', 'vivo', 'WDJ', 'appstore']
result_list = []
result = 0
start_time = yesterday()
end_time = time.strftime('%Y-%m-%d') + " " + "00:00:00"

for i in select_list:
    if i != 'appstore':
        # 下载渠道
        time.sleep(4)
        driver.find_element_by_xpath("//*[@id='RecordStarttb']/div[1]/span[2]/input").send_keys(i)
        #driver.find_element_by_name('rstartAppchannel').send_keys(i)
        #
        # driver.find_element_by_name("rstartPlatform").click()
        # start_time
        driver.implicitly_wait(5)
        ele_start = driver.find_element_by_xpath('//*[@id="RecordStarttb"]/div[1]/span[4]/span[2]/input[1]')
        ele_start.clear()
        driver.implicitly_wait(5)
        ele_start.send_keys(start_time)
        driver.implicitly_wait(5)
        ele_end = driver.find_element_by_xpath('//*[@id="RecordStarttb"]/div[1]/span[4]/span[4]/input[1]')
        ele_end.clear()
        driver.implicitly_wait(5)
        ele_end.send_keys(end_time)
        driver.implicitly_wait(5)
        driver.find_element_by_xpath('//*[@id="RecordStarttb"]/div[2]/span[2]/a[1]/span/span').click()

    else:
        pass
for i in result_list:
    result = result + i
last_dict = zip(select_list, result_list)

