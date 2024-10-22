"""
登录页面 相关
"""
from comm.config import MyConfig
import os
myconfig = MyConfig()


# 点击个人中心 登录/注册 button
def dL_element(driver):
    driver.find_element_by_id("com.erlinyou.worldlist:id/user_name_tv").click()


# 点击登录页面微信入口
def wX_element(driver):

    driver.find_element_by_id("com.erlinyou.worldlist:id/iv_other_login").click()

# 微信登录页面 输入账号
def wxUser_element(driver, wx_username):
    driver.find_element_by_xpath(
        "//android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.EditText").send_keys(wx_username)


# 微信登录页面 输入密码
def wxPassword_element(driver, wx_password):
    driver.find_element_by_xpath(
        "//android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.EditText").send_keys(wx_password)


# 微信登录页面 点击登录buttton
def wxDl_element(driver):
    driver.find_element_by_id("com.tencent.mm:id/cqc").click()


# 微信登录页面 账号密码登录title 点击
def mobile_title_element(driver):
    driver.find_element_by_android_uiautomator('new UiSelector().textContains("账号密码登录") ').click()
    # driver.find_element_by_id("com.erlinyou.worldlist:id/account_login").click()


# 账号密码登录：输入手机号登陆   mobile_number = "18612463553"
def mobile_user_element(driver):
    adb1 = 'adb shell ime set com.sohu.inputmethod.sogou.xiaomi/.SogouIME'
    adb3 = 'adb shell ime set io.appium.android.ime/.UnicodeIME'
    os.system(adb1)
    print(myconfig.get_mobile_number())
    driver.implicitly_wait(5)
    driver.find_element_by_id("com.erlinyou.worldlist:id/et_username").send_keys(myconfig.get_mobile_number())
    os.system(adb3)


# 账号密码登录 ：输入密码
def mobile_password_element(driver):
    driver.find_element_by_id("com.erlinyou.worldlist:id/et_pwd").send_keys(myconfig.get_mobile_password())


#  账号密码登录，立即登录
def mobile_login_element(driver):
    driver.find_element_by_id("com.erlinyou.worldlist:id/submit").click()


if __name__ == '__main__':

    print(myconfig.get_mobile_number())
    print(type(myconfig.get_mobile_number()))