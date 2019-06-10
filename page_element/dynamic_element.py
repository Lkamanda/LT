from page.element_error import element_error


def create_new_dynamic_element(driver):
    """新建动态按钮"""
    try:
        driver.find_element_by_id("com.erlinyou.worldlist:id/imageview_sead_moment").click()
    except Exception as e:
        element_error(driver, e)


def dynamic_input_box(driver):
    """新建动态输入框"""
    n = u"这是一条新动态"
    try:
        driver.find_element_by_id("com.erlinyou.worldlist:id/text_edit").send_keys(n)
    except Exception as e:
        element_error(driver, e)


def dynamic_camera_element(driver):
    """新建动态 打开相册"""
    try:
        driver.find_element_by_id("com.erlinyou.worldlist:id/imageview_camera").click()
    except Exception as e:
        element_error(driver, e)


def dynamic_send_element(driver):
    """发布动态 按钮"""
    try:
        driver.find_element_by_id("com.erlinyou.worldlist:id/send_btn").click()
    except Exception as e:
        element_error(driver, e)


def dynamic_check_box_public_element(driver):
    """ 公开"""
    try:
        driver.find_element_by_id("com.erlinyou.worldlist:id/checkbox_public").click()
    except Exception as e:
        element_error(driver, e)


def dynamic_check_box_friends(driver):
    """仅朋友可见"""
    try:
        driver.find_element_by_id("com.erlinyou.worldlist:id/checkbox_friends").click()
    except Exception as e:
        element_error(driver, e)


def dynamic_check_box_specific(driver):
    """部分朋友可见"""
    try:
        driver.find_element_by_id("com.erlinyou.worldlist:id/checkbox_specific_friends").click()
    except Exception as e:
        element_error(driver, e)


def dynamic_travel_shot(driver):
    """发布为旅拍"""
    try:
        driver.find_element_by_id("com.erlinyou.worldlist:id/imageview_switch").click()
    except Exception as e:
        element_error(driver, e)


def dynamic_choice_picture(driver, n):
    """
    选取第几张图片
    :param driver:self.driver
    :param n: n = 1 拍照   n = 2 录像 n > 3 相册里的图片
    """
    try:
        driver.find_element_by_xpath("//android.widget.RelativeLayout/android.widget.GridView/"
                                     "android.widget.RelativeLayout[%s]/android.widget.ImageView" % n).click()
    except Exception as e:
        element_error(driver, e)


def dynamic_take_picture_taking(driver):
    """摄像机拍照按钮"""
    try:
        driver.find_element_by_id("com.erlinyou.worldlist:id/btn_shutter_camera").click()
    except Exception as e:
        element_error(driver, e)


def dynamic_take_picture_ok(driver):
    """确定拍照保留到动态里"""
    try:
        driver.find_element_by_id("com.erlinyou.worldlist:id/img_done").click()
    except Exception as e:
        element_error(driver, e)


def dynamic_recoding_picture(driver):
    """录制视频 """
    try:
        driver.find_element_by_id("com.erlinyou.worldlist:id/btn_shutter_record").click()
    except Exception as e:
        element_error(driver, e)
