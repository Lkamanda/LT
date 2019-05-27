def userAvatar_element(driver):
    """点击首页用户头像"""
    driver.find_element_by_id('user_avatar_img').click()


def mainChat_element(driver):
    """主页消息入口 main_chat  id"""
    driver.find_element_by_id("chat_img").click()



