# How to generate a random timestamp

# datetime.timedelta()
# random.randint()
# datetime.sfrftime()

import random,datetime

endTime = datetime.datetime.today()
startTime = endTime - datetime.timedelta(seconds=30)

print('end time: ', endTime)
print('start time: ', startTime)

# 生成一个随机时间，并将其写入到文件中
# 注意换行

f=open('/home/nathan/time.log','a')

for i in range(1000):
    eventTime = startTime + datetime.timedelta(seconds=(random.randint(1, 30)))
    print(eventTime.strftime('%d/%b/%Y:%H:%M:%S'))
    f.write(str(eventTime) +'\n')