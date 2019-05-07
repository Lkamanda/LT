"""
我的页面
"""


# 点击个人中心 登录/注册 button
def dL(driver):
    driver.find_element_by_id("user_name_tv").click()
