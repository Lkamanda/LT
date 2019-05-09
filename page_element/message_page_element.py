"""
消息页面元素事件
"""


# 聊天title
def chatTitle_element(driver):
    driver.find_element_by_id("com.erlinyou.worldlist:id/textview_tab_chat").click()


#  联系人 title
def contacts_element(driver):
    driver.find_element_by_text("联系人").click()


# 通知 title
def notice_element(driver):
    driver.find_element_by_text("通知")


# 聊天下第一个窗口
def first_chat_element(driver):
    driver.find_element_by_id("//android.widget.ListView/android.widget.RelativeLayout[1]").click()


# img_more  加号button
def chat_img_more_element(driver):
    driver.find_element_id("com.erlinyou.worldlist:id/img_more").click()


# 表情
def chat_expression_element(driver):
    driver.find_element_by_id("com.erlinyou.worldlist:id/img_exp").click()


# 聊天输入框 输入
def chat_sendkeys_element(driver, send_str):
    driver.find_element_by_id("com.erlinyou.worldlist:id/rlEdit").sendkey(send_str)


# 发送消息button 点击
def chat_send_all_elment(driver):
    driver.find_element_by_id("	com.erlinyou.worldlist:id/btnSend").click()


# 