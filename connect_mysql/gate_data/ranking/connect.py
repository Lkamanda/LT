import pymysql
from collections import OrderedDict
from connect_mysql.gate_data.ranking.time import *
from connect_mysql.gate_data.ranking.python_config import *
from connect_mysql.gate_data.ranking.send_messsage import *
D = OrderedDict()
select_list = ["360", "Baidu", "HUAWEI", "Mi", "OPPO", "Tencent", "VIVO", "WDJ", "App Store"]

month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
              "October", "November", "December"]


def get_text_data_last(value):
    """获取数字的最后一位"""
    return list(map(int, str(value)))[-1]


def get_serial_number(value):
    if value == 1:
        serial = 'st'
        return serial
    elif value == 2:
        serial = 'nd'
        return serial
    elif value == 3:
        serial = "rd"
        return serial
    elif value in [0, 4, 5, 6, 7, 8, 9]:
        serial = "th"
        return serial


def get_D(start_time, end_time):
    global all_number
    all_number = 0
    try:
        db = pymysql.connect(
            host='cn-master.cgl0jlkt5nez.rds.cn-north-1.amazonaws.com.cn',
            user='jialin',
            password='jialin',
            db='stats',
            port=3306
                            )
        coursor = db.cursor()
        for i in select_list:
            global sql
            print(i)
            if i == "App Store":
                sql = 'select * from t_record_start where rstart_appChannel="{0}" and rstart_type="1"' \
                      ' and rstart_platform="2" and rstart_clientCreateDate between "{1}" and ' \
                      '"{2}"'.format(i, start_time, end_time)
            else:
                sql = 'select * from t_record_start where rstart_appChannel="{0}" and rstart_type="1"' \
                      ' and rstart_platform="1" and rstart_clientCreateDate between "{1}" and ' \
                      '"{2}"'.format(i, start_time, end_time)
            a = coursor.execute(sql)
            # a 为查询到数据数量

            D[i] = a
            print(a)
            # 打印出每一条查询结果
            for y in range(a):
                result = coursor.fetchone()
                print(result)
            all_number = all_number + D[i]
        D["all_number"] = all_number
        db.close()
        print(D)
        # for key in D:
        #     print(key, D[key])
        return D
    except Exception as e:
        print(e)


def run():
    x1, y1, z1, x2, y2, z2 = eval(input("start_time 和 end_time 格式如（2019,6,19,2019,6,20）："))
    text_month = month_list[int(y1)-1]                           # 日期 ： 月
    text_day = int(z1)
    text_last_one = get_text_data_last(value=text_day)           # 日期 ： 日 最后一位数字
    serial_number = get_serial_number(text_last_one)             # 日期序号： 1st, 2nd, 3rd others th
    start_time, s = get_start_time(x1, y1, z1)
    end_time = get_end_time(x2, y2, z2)
    week_day = get_week_day(date=s)
    print(week_day)
    D = get_D(start_time=start_time, end_time=end_time)
    print(type(D['360']))
    content = generator_only_text_content(content=read_config(config=get_config(week_day)),
                                          text_month=text_month,
                                          text_day=text_day,
                                          serial_number=serial_number,
                                          D=D
                                          )

    send_content(driver=connect_app(), content=content)


def get_week_day(date):
    week_day_dict = {
        0: '星期一',
        1: '星期二',
        2: '星期三',
        3: '星期四',
        4: '星期五',
        5: '星期六',
        6: '星期天',
    }

    day = date.weekday()
    return week_day_dict[day]


# print(get_week_day(datetime.datetime(x1, y1, z1, 00, 00, 00)))

if __name__ == '__main__':
    run()
    # x=0
    # z = get_text_data_last(x)
    # serial_number = get_serial_number(z)
    # print(serial_number)





