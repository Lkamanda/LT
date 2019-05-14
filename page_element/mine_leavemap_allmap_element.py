"""
# 我的页面下离线地图，全部地图页面 element
"""

# 全部地图页面返回我的页面
def allmap_back_element(driver):
    driver.find_element_by_id("com.erlinyou.worldlist:id/btnBack").click()
