import pymysql
from collections import OrderedDict
from connect_mysql.time import get_start_time, get_end_time

D = OrderedDict()
select_list = ["360", "Baidu", "HUAWEI", "Mi", "OPPO", "Tencent", "VIVO", "WDJ", "App Store"]


def get_D():
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
        print(type(D))
        # for key in D:
        #     print(key, D[key])
        return D

    except Exception as e:
        print(e)


if __name__ == '__main__':
    x1, y1, z1, x2, y2, z2 = eval(input("start_time 和 end_time 格式如（2019,6,19,2019,6,20）："))
    start_time = get_start_time(x1, y1, z1)
    end_time = get_end_time(x2, y2, z2)
    get_D()