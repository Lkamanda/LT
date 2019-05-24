"""
消息页面元素事件
"""

from comm.usuallymodule import mylogger
from page.element_error import element_error


def message_back_element(driver):
    """消息页面返回home_page按钮"""
    try:
        driver.find_element_by_id("com.erlinyou.worldlist:id/imageview_search").click()
    except Exception as e:
        element_error(driver, e)


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
    driver.find_element_by_xpath("//android.widget.LinearLayout/android.widget.ListView"
                                 "/android.widget.RelativeLayout[1]").click()


# img_more  加号button
def chat_img_more_element(driver):
    driver.find_element_by_id("com.erlinyou.worldlist:id/img_more").click()


# 表情
def chat_expression_element(driver):
    driver.find_element_by_id("com.erlinyou.worldlist:id/img_exp").click()


def chat_send_keys_element(driver, chat_str):
    """
    聊天输入框 输入
    :param driver: self.driver
    :param chat_str: 输入的字符
    :return:
    """
    driver.find_element_by_id("et_msg").send_keys(chat_str)


# 发送消息button 点击
def chat_send_all_element(driver):
    try:
        driver.find_element_by_id("com.erlinyou.worldlist:id/btnSend").click()
    except:
        mylogger.debug("发送button定位失败")


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


def chat_add_all(driver, n):
    """
    对加号下的各个接口调用
    :param driver:
    :param n:
    n = 1 :相册
    n = 2 : 拍摄
    n = 3 : 语音聊天
    n = 4 : 视频聊天
    n = 5 : 位置分享
    n = 6 : 联系人
    n = 7 : 地点
    n = 8 : 分享软件
    """
    driver.find_element_by_xpath("//android.support.v4.view.ViewPager/android.widget.GridView/android.widget.LinearLayout[%s]/android.widget.ImageView" % n).click()


def chat_add_sendfile(driver):
    """发送文件按钮触发"""
    # 进入加号下调用左滑
    driver.find_element_by_xpath("//android.support.v4.view.ViewPager/android.widget.GridView/android.widget.LinearLayout/android.widget.ImageView").click()


# def chat_take_picture_getback(driver):
#     """拍照下返回"""
#     #driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ImageView").click()
#     driver.find_element_by_id("com.erlinyou.worldlist:id/focusImageView").click()

    # driver.find_element_by_id("com.erlinyou.worldlist:id/btnBack").click()

def chat_take_picture_start(driver):
    """拍照启动"""
    driver.find_element_by_id("com.erlinyou.worldlist:id/btn_shutter_camera").click()


def chat_take_picture_album(driver):
    """从相册中选择"""
    # driver.find_element_by_xpath("//android.widget.FrameLayout/android.widget.ImageView").click()
    driver.find_element_by_id("com.erlinyou.worldlist:id/btn_thumbnail").click()


def chat_take_picture_videotape(driver):
    """照片切换视频按钮"""
    driver.find_element_by_id("com.erlinyou.worldlist:id/btn_switch_mode").click()


def chat_take_picture_sure(driver, n):
    """
    拍照的取消和确定button
    :param driver:
    :param n:
    n : 1 取消
    n : 2 确定
    """
    driver.find_element_by_xpath("//android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ImageView[%s]" % n).click()


def chat_location_share_get_back(driver):
    """位置分享 返回聊天按钮"""
    driver.find_element_by_id("com.erlinyou.worldlist:id/chat").click()


def chat_location_share_stop(driver):
    """位置分享 结束"""
    driver.find_element_by_id("stop").click()


def chat_location_contact_share_search(driver, n):
    """联系人分享 查询button"""
    driver.find_element_by_id("com.erlinyou.worldlist:id/edit_search").send_keys(n)


def chat_contacts_share(driver, n):
    """
    联系人分享 发送名片 button
    :param driver:
    :param n: 选择名片列表下第几个
    """
    driver.find_element_by_xpath("//android.widget.LinearLayout[%s]/android.widget.LinearLayout"
                                 "/android.widget.LinearLayout/android.widget.TextView" % n).click()


def chat_send_file_type(driver, n):
    """
    message 发送文件选择类型
    :param driver: self.driver
    :param n:
    n = 1 :本地视频
    n = 2: 本地音乐
    n = 3 : 文件管理
    n = 4 : wps office
    n = 5 : 相册
    n = 6 : 进入录音机
    n = 7 : 音乐


    """
    try:
        driver.find_element_by_xpath("//android.widget.GridView/android.widget.LinearLayout[%s]" % n).click()
    except Exception as e:
        element_error(driver, e)


def chat_send_file_choice_folder(driver, x, y, z):
    """
    文件管理:下选择具体的文件夹 ， 仅支持首页
    :param driver:
    :param x: 第1层第几个文件夹
    :param y: 第2层第几个文件夹
    :param z: 第3层第几个文件
    :return:
    """
    driver.find_element_by_xpath("//android.widget.ListView/android.widget.FrameLayout[%s]" % x).click()
    driver.find_element_by_xpath("//android.widget.ListView/android.widget.FrameLayout[%s]" % y).click()
    driver.find_element_by_xpath("//android.widget.ListView/android.widget.FrameLayout[%s]" % z).click()
    # 点击确定按钮
    driver.find_element_by_xpath("//android.widget.LinearLayout/android.widget.Button[1]").click()
    mylogger.info("确定发送")