"""
登录页面
"""


# 点击个人中心 登录/注册 button
def dL(driver):
    driver.find_element_by_id("user_name_tv").click()


# 点击登录页面微信入口
def wX(driver):
    driver.find_element_by_id("iv_other_login").click()


# 微信登录页面 输入账号
def wxUser(driver, wx_username):
    driver.find_element_by_xpath(
        "//android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.EditText").send_keys(wx_username)


# 微信登录页面 输入密码
def wxPassword(driver, wx_password):
    driver.find_element_by_xpath(
        "//android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.EditText").send_keys(wx_password)


# 微信登录页面 点击登录buttton
def wxDl(driver):
    driver.find_element_by_id("com.tencent.mm:id/cqc").click()
