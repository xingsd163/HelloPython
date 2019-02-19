# Python time

# two modules, time and calendar
# Python time strftime() 函数接收以时间元组，并返回以可读字符串表示的当地时间，格式由参数format决定。
# Python time sleep() 函数推迟调用线程的运行，可通过参数secs指秒数，表示进程挂起的时间。
# Python time asctime() 函数接受时间元组并返回一个可读的形式为"Tue Dec 11 18:07:14 2008"（2008年12月11日 周二18时07分14秒）的24个字符的字符串。
# Python time localtime() 函数类似gmtime()，作用是格式化时间戳为本地的时间。 如果sec参数未输入，则以当前时间为转换标准。 DST (Daylight Savings Time) flag (-1, 0 or 1) 是否是夏令时。
# Python time gmtime() 函数将一个时间戳转换为UTC时区（0时区）的struct_time，可选的参数sec表示从1970-1-1以来的秒数。其默认值为time.time()，函数返回time.struct_time类型的对象。（struct_time是在time模块中定义的表示时间的对象）。

import time, calendar

current_time=time.time()
print("Get Unix time: " + str(current_time))


# get a time tuple

localtime=time.localtime(time.time())
print("Time in tuple format: " + str(localtime))

print("time.localtime: " +str(time.localtime()))


# formatted time in readable format

print("ASCTIME: " + time.asctime(localtime))
print("ASCTIME: " + time.asctime())
print("ASCTIME: " + time.asctime(time.localtime(time.time())))

# time.strftime(), convert time.localtime() to a specific format
# time.localtime()
# timne.strftime()
# %Y-%m-%d %H:%M:%S

print(time.strftime("%Y-%m-%d %U %w", time.localtime()))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))

# calendar


print("-------------"
)


# time.sleep()

print("Start: ",time.ctime())
time.sleep(1)
print("Middle:", time.ctime())
time.sleep(3)
print("End: ", time.ctime())

str="Do you like me, if you like me, please let me know"

strs=str.split(" ")
for i in strs:
    print(i)
    time.sleep(0.5)





