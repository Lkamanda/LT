class Public_element():
    # def __init__(self):
    #     self.user_avatar = "user_avatar_img"
    user_avatar = "user_avatar_img"
    dl="user_name_tv"
    wx ="iv_other_login"
    wx_user= xpath("//android.widget.LinearLayout[1]/android.widget.EditText")
    wx_password = ("//android.widget.LinearLayout[2]/android.widget.EditText")
    wx_dl="com.tencent.mm:id/ch7"
def get_user_avatar():
    return Public_element.user_avatar
