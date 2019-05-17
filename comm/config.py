class MyConfig:
    def __init__(self):
        self.chat_str = u"d发斯蒂芬斯蒂芬德生科技付款了的房价快速的减肥肯定是放假快乐的实际付款时代峻峰"
        self.mobile_number = "13231533164"
        self.mobile_password = "5211314"
        self.place_share_place = "北京西站"
        self.place_share_street = "上地五街"
        self.place_share_city = "beijing"

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
            return self.place_share_place

        elif n == 2:
            return self.place_share_street

        elif n == 3:
            return self.place_share_city

    def get_chat_str(self, n):
        if n == 1:
            return self.chat_str



