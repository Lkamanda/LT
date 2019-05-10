"""
消息页面元素事件
"""
from comm.config import MyConfig


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
    # driver.find_element_by_xpath("//android.widget.ListView/android.widget.RelativeLayout[1]").click()
    # driver.find_element_by_android_uiautomator('new UiSelector().text("WE")').click()
    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.ListView/android.widget.RelativeLayout[1]").click()


# img_more  加号button
def chat_img_more_element(driver):
    driver.find_element_by_id("com.erlinyou.worldlist:id/img_more").click()


# 表情
def chat_expression_element(driver):
    driver.find_element_by_id("com.erlinyou.worldlist:id/img_exp").click()


# 聊天输入框 输入
def chat_sendkeys_element(driver):
    send_str = MyConfig().get_send_str()
    # print(send_str)
    driver.find_element_by_id("com.erlinyou.worldlist:id/et_msg").click()
    print(1)
    driver.implicitly_wait(1)
    # driver.find_element_by_xpath("//android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]").send_keys("1235435345")
    print('pass')


# 发送消息button 点击
def chat_send_all_elment(driver):
    driver.find_element_by_id("com.erlinyou.worldlist:id/btnSend").click()


# 调用相册
def chat_add_photo_album(driver):
    driver.find_element_by_xpath("//android.support.v4.view.ViewPager/android.widget.GridView/android.widget.LinearLayout[1]/android.widget.ImageView").click()


# 任选相册位置
def chat_add_photo_album_n(driver, n):
    """
    :param driver:
    :param n: 第几张图片
    """
    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget."
                                 "FrameLayout/android.widget.RelativeLayout/android.widget.GridView/android.widget."
                                 "RelativeLayout[%s]/android.widget.RelativeLayout/android.widget.Button" % n).click()


def chat_add_photo_send(driver):
    """相册发送按钮"""
    driver.find_element_by_id("com.erlinyou.worldlist:id/ok_button").click()


def chat_add_photo_preview(driver):
    """相册预览按钮"""
    driver.find_element_by_id("preview").click()


def chat_add_photo_preview_send(driver):
    """相册预览后的发送按钮"""
    driver.find_element_by_id("com.erlinyou.worldlist:id/btn_send").click()
