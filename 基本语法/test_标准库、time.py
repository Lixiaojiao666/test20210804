import time

print(time.asctime())
print(time.time())
print(time.localtime())
print(time.strftime("%Y-%m-%d %H-%M-%S", time.localtime()))

#获取两天前的时间
now = time.time()
two_day_ago = now - 60*60*24*2
print(time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(two_day_ago)))

#获取两天后的时间
now1 = time.time()
two_day_later = now1 + 60*60*24*2
print(time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(two_day_later)))
