# 点击首页用户头像
def userAvatar_element(driver):
    driver.find_element_by_id('user_avatar_img').click()


# 主页消息入口 main_chat  id
def mainChat_element(driver):
    driver.find_element_by_id("chat_img").click()


# 点击主页漫游页面
def roam_element(driver):
    driver.find_element_by_xpath("//android.widget.LinearLayout/android.widget.LinearLayout"
                                 "/android.widget.ImageView").click()


