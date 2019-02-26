# the datetime module

import datetime
import time


# datetime模块提供了操作日期和时间功能
# datetime模块定义了5个类，分别是
# 1.datetime.date：表示日期的类
# 2.datetime.datetime：表示日期时间的类
# 3.datetime.time：表示时间的类
# 4.datetime.timedelta：表示时间间隔，即两个时间点的间隔
# 5.datetime.tzinfo：时区的相关信息


print(datetime.date.today())

birthday = datetime.datetime(1993,10,20,0,0)
print(birthday)

# date对象只能表示日期，不能表示时间
date=datetime.date(1993,10,20)
print(date)

# time对象只能用来表示时间，而不能用来表示日期
time01=datetime.time(10,20,15)
print(time01)


# 手动实例化timedelta时，可以传入的参数有：days, seconds, microseconds, milliseconds, minutes, hours, weeks。
current_time=datetime.datetime.today()
print("current time: ", current_time)
earlier_time=current_time - datetime.timedelta(minutes=12)
print("Earlier time: ", earlier_time)

later_time=current_time + datetime.timedelta(seconds=30)
print("Later time: ", later_time)



