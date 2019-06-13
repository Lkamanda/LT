import datetime
now_time = datetime.datetime.now()
yes_time = now_time + datetime.timedelta(days=-1)
start_time = yes_time.strftime('%Y-%m-%d') + " " + "00:00:00"
print(start_time)