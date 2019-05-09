"""
我的页面
"""


# 点击个人中心 登录/注册 button
def dL_element(driver):
    driver.find_element_by_id("user_name_tv").click()


# 点击离线地图
def download_map(driver):
    driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android."
                                 "support.v7.widget.RecyclerView[1]/android.widget.RelativeLayout[1]").click()


# 点击设置按钮
def mine_setting(driver):
    driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView/android.widget.LinearLayout[10]"
                                 "/android.widget.RelativeLayout").click()
