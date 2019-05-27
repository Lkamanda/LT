class MyConfig:
    def __init__(self):
        self.chat_str_1 = u"d发斯蒂芬斯蒂芬德生科技付款了的房价快速的减肥肯定是放假快乐的实际付款时代峻峰"
        self.chat_str_2 = u"华为备胎芯华为备胎芯华为备胎芯华为备胎芯华为备胎芯华为备胎芯华为备胎芯华为备胎芯华为备胎芯华为备胎芯华为备胎芯华为备胎芯华为备胎芯华为备胎芯华为备胎芯华为备胎芯华为备胎芯华为备胎芯华为备胎芯华为备胎芯"
        self.mobile_number = u"13231533164"
        self.mobile_password = u"5211314"
        self.place_input = [u"北京西站",  u"上地五街", u"beijing"]
        self.home_page_details_input = [u"龙泽苑西区"]

    # def get_send_str(self):
    #     return self.send_str

    def get_mobile_number(self):
        return self.mobile_number

    def get_mobile_password(self):
        return self.mobile_password

    def get_place_share_search(self, n):
        """
        对place 页面返回搜索值
        :param
        n = 1 ： 地点
        n = 2 :  街道
        n = 3 :  城市

        :return: place
        """

        if n == 1:
            # return self.place_share_place
            return self.place_input[0]
        elif n == 2:
            return self.place_input[1]
            # return self.place_share_street

        elif n == 3:
            return self.place_input[2]
            # return self.place_share_city

    def get_chat_str(self, n):
        if n == 1:
            return self.chat_str_2

    def get_homepage_input(self, n):
        """
        主页详情页面的输入内容
        :param n:
        :return:
        """
        if n == 1:
            return self.home_page_details_input[0]