import time
import datetime
# from datetime import datetime, timedelta
#
# print( datetime.today().date())
# day =  datetime.today().date()
# ts = int(time.mktime(time.strptime(str(day), '%Y-%m-%d')))
# print(ts)

#
# def get_start_time():
#     today = datetime.date.today()
#     tomorrow = today + datetime.timedelta(days=-1)
#     print(tomorrow)
#     dt = str(tomorrow) + ' ' + '00:00:00'
#     ts = int(time.mktime(time.strptime(dt, "%Y-%m-%d %H:%M:%S"))) * 1000
#     print(ts)
#     return ts
#
#
# def get_end_time():
#     dt = time.strftime('%Y-%m-%d') + ' ' + '00:00:00'
#     print(dt)
#     #
#     # dt = '2019-06-20 00:00:00'
#     ts = int(time.mktime(time.strptime(dt, "%Y-%m-%d %H:%M:%S"))) * 1000
#     print(ts)
#     return ts


def get_start_time(x1, y1, z1):
    # s = datetime.datetime(2019, 06, 20, 00, 00, 00)
    s = datetime.datetime(x1, y1, z1, 00, 00, 00)
    print(s)
    start_time = int(time.mktime(s.timetuple())) * 1000
    print(start_time)
    return start_time, s


def get_end_time(x2, y2, z2):
    s = datetime.datetime(x2, y2, z2, 00, 00, 00)
    # print(s)
    end_time = int(time.mktime(s.timetuple())) * 1000
    print(end_time)
    return end_time


# if __name__ == '__main__':
#
#     # get_start_time(x1=2019, y1=6, z1=19)
#     # # get_end_time()
#
#     # x1, y1, z1, x2, y2, z2 = input()
#     # a,b =input("")
#     # print(a,b)
#
#     # n, m, c = eval(input("4th enter:"))
#     # print(n,m,c)
#     #
#     # x1, y1, z1, x2, y2, z2 = eval(input("start_time 和 end_time 格式如（·）："))
#     x1 = int(2019)
#     y1 = int(6)
#     z1 = int(23)
#     get_start_time(x1=x1, y1=y1, z1=z1)
