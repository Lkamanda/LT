"""发送动态"""
import unittest
from comm.usuallymodule import *
from comm.webDriver import *


class Test6(webDriver, unittest.TestCase):
    def test_a_0(self):
        """zh 登录"""
        zh_login(self=self, driver=self.driver)
        self.driver.press_keycode(4)
        mylogger.info("返回home page")

    def test_a_1(self):
        """发送动态 图片和视频 不发送位置 ，仅部分好友可见"""
        test_name = "发送动态 图片和视频 不发送位置 ，仅部分好友可见"
        mylogger.debug(test_name)
        self.driver.implicitly_wait(5)
        dynamic(self.driver)
        mylogger.info("进入动态界面")
        self.driver.implicitly_wait(5)
        create_new_dynamic_element(self.driver)
        dynamic_input_box(self.driver)
        self.driver.implicitly_wait(5)
        dynamic_camera_element(self.driver)
        self.driver.implicitly_wait(5)
        dynamic_choice_method(driver=self.driver, n=1)
        mylogger.info("启动照相机")
        dynamic_take_picture_taking(self.driver)
        self.driver.implicitly_wait(5)
        dynamic_take_picture_ok(self.driver)
        self.driver.implicitly_wait(5)
        self.driver.press_keycode(4)
        mylogger.info("添加拍摄照片完成")
        dynamic_camera_element(self.driver)
        dynamic_choice_method(driver=self.driver, n=2)
        dynamic_recoding_picture(self.driver)
        ele = self.driver.find_element_by_id("com.erlinyou.worldlist:id/btn_shutter_record")
        action = TouchAction(self.driver)
        action.long_press(el=ele, duration=10000).wait(10000).perform()
        dynamic_recoding_picture(self.driver)
        self.driver.implicitly_wait(5)
        dynamic_take_picture_ok(self.driver)
        self.driver.press_keycode(4)
        dynamic_camera_element(self.driver)
        self.driver.implicitly_wait(5)
        dynamic_choice_picture(driver=self.driver, n=5)
        self.driver.implicitly_wait(5)
        chat_add_photo_send(self.driver)
        mylogger.info("动态视频和图片添加完成")
        dynamic_check_box_specific(self.driver)
        mylogger.info("发布动态设置为部分可见")
        dynamic_choice_who_look(self.driver, n=2)
        dynamic_send_element(self.driver)
        dynamic_delete_place(self.driver)
        self.driver.implicitly_wait(5)
        dynamic_send_element(self.driver)
        mylogger.info('进入校验流程')
        self.driver.implicitly_wait(5)
        dynamic_friend_title(self.driver)
        self.assertEqual(True, check_create_dynamic_just_friend_see(self.driver))
        mylogger.info('当前账号出现该动态，进入切换账号')
        # 如验证该功能应登录允许账号，和不允许账号去检验新建动态在各自账号是否出现
        self.driver.implicitly_wait(5)
        self.driver.press_keycode(4)
        allmap_back_element(self.driver)
        logout(self=self, driver=self.driver)
        # 进入登录
        self.driver.implicitly_wait(5)
        dL_element(self.driver)
        mylogger.info('点击注册/登录 进入登录页面')
        self.driver.implicitly_wait(5)
        wX_element(self.driver)
        mylogger.info('点击微信图标进行登录')
        self.assertEqual(True, check_wx_login(self.driver, test_name))
        mylogger.info('微信登录成功')
        # self.driver.keyevent('BACK')
        allmap_back_element(self.driver)
        mylogger.info("return my page success")
        allmap_back_element(self.driver)
        mylogger.info("return home page success")
        dynamic(self.driver)
        dynamic_friend_title(self.driver)
        self.assertEqual(True, check_create_dynamic_just_friend_see(self.driver))
        mylogger.info("验证通过，进入环境退出")
        self.driver.press_keycode(4)
        time.sleep(2)
        self.driver.press_keycode(4)

    def test_b_1(self):
        """点赞 对第一条动态进行点赞"""
        test_name = "点赞"
        mylogger.debug(test_name)
        self.driver.implicitly_wait(5)
        dynamic(self.driver)
        # 获取好友列表平第一条动态点赞数
        self.driver.implicitly_wait(5)
        dynamic_friend_title(self.driver)
        mylogger.info("获取好友列表平第一条动态点赞数")
        # 获取动态页点赞数
        self.driver.implicitly_wait(10)
        give_like_number = dynamic_get_give_like_number(driver=self.driver, n=1)
        mylogger.info(give_like_number)
        # 获取动态页浏览数
        # Browse_number = dynamic_get_browser_number(driver=self.driver, n=1)
        dynamic_friend_first_dynamic(self.driver, n=1)
        mylogger.info('进入动态详情页')
        self.driver.implicitly_wait(5)
        give_details_give_like_number = dynamic_details_get_give_like_number(self.driver)
        mylogger.info(give_details_give_like_number)
        self.assertEqual(give_like_number, give_details_give_like_number)
        mylogger.info("动态页和动态详情页点赞数显示一致")
        dynamic_give_like_element(self.driver)
        mylogger.info("对该动态进行点赞操作")
        # 进行评论
        self.driver.implicitly_wait(5)
        dynamic_comments_element(self.driver)
        mylogger.info("进入点评界面")
        dynamic_comments_input_box(self.driver)
        dynamic_send_element(self.driver)
        mylogger.info("返回动态详情页")
        swipeUp(driver=self.driver, t=5000)
        self.driver.implicitly_wait(5)
        self.assertEqual(True, check_comments_successful(self.driver))
        self.driver.press_keycode(4)
        time.sleep(3)
        self.driver.press_keycode(4)
        # self.driver.implicitly_wait(5)
        # dynamic_details_get_give_like_number(self.driver)
        # # 动态详情 点赞后 点赞数
        # dynamic_details_Thumb_up_after_number = dynamic_details_get_give_like_number(self.driver)
        # mylogger.info("点赞后的点赞数:%s" % dynamic_details_Thumb_up_after_number)
        # self.driver.press_keycode(4)
        # self.driver.implicitly_wait(5)
        # swipeDown(driver=self.driver, t=5000)
        # dynamic_get_give_like_number(driver=self.driver, n=1)

    def test_c_1(self):
        """发送表情"""
        test_name = "发送表情"
        mylogger.info(test_name)
        self.driver.implicitly_wait(5)
        mainChat_element(self.driver)
        self.driver.implicitly_wait(5)
        first_chat_element(self.driver)
        self.driver.implicitly_wait(5)
        chat_emoji_element(self.driver)
        self.driver.implicitly_wait(5)
        chat_emoji(driver=self.driver, n=1)
        self.driver.implicitly_wait(5)
        chat_emoji(driver=self.driver, n=2)
        self.driver.implicitly_wait(5)
        # chat_send_all_element(self.driver)
        self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("发送")').click()
        time.sleep(3)
        screenShot(driver=self.driver, test_name=test_name)
        self.driver.press_keycode(4)
        time.sleep(2)
        self.driver.press_keycode(4)

    def test_c_2(self):
        """发送动态表情"""
        test_name = "发送动态表情"
        mylogger.info(test_name)
        self.driver.implicitly_wait(5)
        mainChat_element(self.driver)
        self.driver.implicitly_wait(5)
        first_chat_element(self.driver)
        self.driver.implicitly_wait(5)
        chat_emoji_element(self.driver)
        chat_type_emoji(self.driver, n=2)
        self.driver.implicitly_wait(5)
        chat_moving_emoji(driver=self.driver, n=1)
        self.driver.implicitly_wait(5)
        time.sleep(3)
        screenShot(driver=self.driver, test_name=test_name)
        self.driver.press_keycode(4)
        time.sleep(2)
        self.driver.press_keycode(4)

    def test_c_3(self):
        """撤回，下拉刷新，看是否还显示撤回的消息"""
        test_name = "撤回，下拉刷新，看是否还显示撤回的消息"
        mylogger.debug(test_name)
        chat_str = u"撤回测试"
        self.driver.implicitly_wait(5)
        mainChat_element(self.driver)
        self.driver.implicitly_wait(5)
        first_chat_element(self.driver)
        self.driver.implicitly_wait(5)
        chat_send_keys_element(driver=self.driver, chat_str=chat_str)
        self.driver.implicitly_wait(5)
        chat_send_all_element(self.driver)
        self.driver.implicitly_wait(5)
        ele = self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("撤回测试")')
        action = TouchAction(self.driver)
        action.long_press(el=ele, duration=2000).wait(1000).perform()
        mylogger.info("触发长按")
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("撤回")').click()
        time.sleep(3)
        self.driver.press_keycode(4)
        first_chat_element(self.driver)
        self.driver.implicitly_wait(5)
        self.assertEqual(True, check_withdrawn(self.driver))
        mylogger.info('撤销消息成功')
        self.driver.press_keycode(4)
        time.sleep(4)
        self.driver.press_keycode(4)
        time.sleep(2)
        self.driver.press_keycode(4)

    def test_d_4(self):
        logout(self, self.driver)














