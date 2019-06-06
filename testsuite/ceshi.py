from selenium import webdriver
import pytesseract as pt
from PIL import Image
import time
import requests

driver = webdriver.Chrome()

driver.get("http://static.jingcailvtu.org:9081/stats-admin/framework")
driver.implicitly_wait(5)
pass_word = "zhoujialin"
driver.find_element_by_id("username").send_keys(pass_word)
driver.implicitly_wait(5)
driver.find_element_by_id("password").send_keys(pass_word)
driver.implicitly_wait(5)


img_address = "http://static.jingcailvtu.org:9081/stats-admin/imageServlet"


r = requests.get(img_address)
with open('./03.png', 'wb') as f:
    f.write(r.content)
    print(1)

image = Image.open("03.png")
#image = Image.open("YM_01.png")
# 调用pytessreact,把图片转换成文字
time.sleep(4)
text = pt.image_to_string(image)
print(text)

driver.find_element_by_name("randomCode").send_keys(text)