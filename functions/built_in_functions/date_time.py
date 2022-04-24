'''
@author = xiaolin.wang
@description:

'''
import time
from datetime import datetime
print(datetime.now())
print(datetime.time(datetime.now()))
print(datetime.date(datetime.now()))
dt = datetime(2015, 4, 19, 12, 20, 30)
print(dt)
'''
    datetime/timestamp 相互转换
        timestamp() 转换为时间戳
        utcfromtimestamp()  时间戳转换为utc-0的日期
        fromtimestamp()  时间戳转换为当前日期
'''
date_time = datetime.now()
print(date_time.timestamp())
print(datetime.utcfromtimestamp(time.time()))
print(datetime.fromtimestamp(time.time()))

'''
    str/datetime 转换
'''
print(datetime.strptime('2022-04-14 15:23:30', '%Y-%m-%d %H:%M:%S'))
date_time = datetime.now()
time_stamps = time.time()
print(date_time.strftime('%Y-%m-%d %H:%M:%S'))
print(datetime.fromtimestamp(time_stamps).strftime('%Y-%m-%d %H:%M:%S'))
print(date_time.isoweekday())
print(date_time.isocalendar())
print(date_time.utcnow())


'''
    时间加减
    timedelta()  时间加减
    days=0, 
    seconds=0, 
    microseconds=0,
    milliseconds=0, 
    minutes=0, 
    hours=0, 
    weeks=0
'''
from datetime import timedelta
from datetime import timezone
tz_utc_8 = timezone(timedelta(hours=8))
now = datetime.now(tz=tz_utc_8)
print(now)
print(now + timedelta(hours=10))
print(now + timedelta(days=3))
print(now + timedelta(days=-10))

utc_td = datetime.utcnow().replace(tzinfo=timezone.utc)
bj_td = utc_td.astimezone(timezone(timedelta(hours=8)))
print(bj_td)
if __name__ == "__main__":
    pass
