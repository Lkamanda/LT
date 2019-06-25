def read_config(config):
    """获取text文本内容"""
    global text_path
    if config == "only_data":
        text_path = "only_data_text"
    elif config == "all_data":
        text_path = "all_data_text"
    f = open(text_path, encoding='utf-8')
    text_content = f.read()
    # print(text_content)
    f.close()
    return text_content


def generator_only_text_content(content, text_month, text_day, serial_number, D):
    """
    对text中文本，使用替换的方式，将获取得方式传入文本，并返回
    :param content: 读取text的内容
    :param text_month: 英文月份
    :param text_day: 日期：日
    :param serial_number: 日后的序号
    :param D: 获取得数据字典
    :return: 自动化发送需要的文本内容
    """
    content = content.replace("%text_day", str(text_day))
    content = content.replace("%text_month", str(text_month))
    content = content.replace("%serial_number", str(serial_number))
    content = content.replace("%D['360']", str(D['360']))
    content = content.replace("%D['Baidu']", str(D['Baidu']))
    content = content.replace("%D['HUAWEI']", str(D['HUAWEI']))
    content = content.replace("%D['Mi']", str(D['Mi']))
    content = content.replace("%D['OPPO']", str(D['OPPO']))
    content = content.replace("%D['Tencent']", str(D['Tencent']))
    content = content.replace("%D['VIVO']", str(D['VIVO']))
    content = content.replace("%D['WDJ']", str(D['WDJ']))
    content = content.replace("%D['App Store']", str(D['App Store']))
    content = content.replace("%D['all_number']", str(D['all_number']))
    print(content)
    return content


def get_config(week_day):
    """通过判断当前日期来返回不同配置"""
    if week_day in ["星期五", "星期六"]:
        config = "only_data"
        print(config)
        return config
    else:
        config = "all_data"
        print(config)
        return config


if __name__ == '__main__':
    read_config(config="all_data")
