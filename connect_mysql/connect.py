import pymysql

try:
    db=pymysql.connect(
        host='cn-master.cgl0jlkt5nez.rds.cn-north-1.amazonaws.com.cn',
        user='jialin',
        password='jialin',
        db='stats',
        port=3306
                        )
    coursor = db.cursor()
    sql = 'select * from t_record_start limit 10'
    a = coursor.execute(sql)
    print(a)
    for r in a:
        print(r.total)
    db.close()

except Exception as e:
    print(e)
