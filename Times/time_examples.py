# Python time

# two modules, time and calendar

import time, calendar

current_time=time.time()
print(current_time)


# get a time tuple

localtime=time.localtime(time.time())
print(localtime)


# formatted time

print(time.asctime(localtime))

# time.strftime(), convert time.localtime() to a specific format
# time.localtime()
# timne.strftime()
# %Y-%m-%d %H:%M:%S

print(time.strftime("%Y-%m-%d %U %w", time.localtime()))


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





