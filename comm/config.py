import os


def read_config_text():
    # path = get_path()
    # f = open(path, encoding='utf-8')
    f = open(r"C:\Users\zhoujialin\PycharmProjects\LT\comm\send_config.txt", encoding='utf-8')
    chat_str3 = f.read()
    f.close()
    return chat_str3


class MyConfig:
    def __init__(self):
        self.chat_str_0 = u"d发斯蒂芬斯蒂芬德生科技付款了的房价快速的减肥肯定是放假快乐的实际付款时代峻峰"
        self.chat_str_1 = u"华为备胎芯华为备胎芯华为备胎芯华为备胎芯华为备胎芯华为备胎芯华为备胎芯华为备胎芯华为备胎芯华为备胎芯华为备胎芯华为备胎芯华为备胎芯华为备胎芯华为备胎芯华为备胎芯华为备胎芯华为备胎芯华为备胎芯华为备胎芯"
        self.chat_str_2 = u"%s" % read_config_text()
        self.mobile_number = u"13231533164"
        self.mobile_password = str(u"5211314")
        self.place_input = [u"北京西站", u"上地五街", u"beijing", u"龙泽苑西区南门", u" 北京市昌平区回龙关西大街111号", u"搜狗", u"奥林匹克公园", u"望京soho"]
        self.home_page_details_input = [u"龙泽苑西区"]

    def get_mobile_number(self):
        return self.mobile_number

    def get_mobile_password(self):
        return self.mobile_password

    def get_place_share_search(self, n):
        """
        对place 页面返回搜索值
        :param
        n = 0 ： 地点
        n = 1 :  街道
        n = 2 :  城市
        n = 3 :  家
        n = 4 :  门牌号
        n = 5 :  搜狗
        n = 6 :  奥林匹克公园
        n = 7 :  公司
        :return: place
        """
        return self.place_input[n]
        # if n == :
        #     # return self.place_share_place
        #     return self.place_input[0]
        # elif n == 2:
        #     return self.place_input[1]
        #     # return self.place_share_street
        #
        # elif n == 3:
        #     return self.place_input[2]
        #     # return self.place_share_city

    def get_chat_str(self, n):
        if n == 0:
            return self.chat_str_0
        elif n == 1:
            return self.chat_str_1
        elif n == 2:
            return self.chat_str_2