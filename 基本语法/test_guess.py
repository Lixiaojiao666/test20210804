import random


print("这是一个猜数字游戏\n数字范围是0到100\n你有三次机会猜数字\n规则介绍完了\n那我们开始吧！")

computer_number = random.randint(0,100)
print(computer_number)
i=1
while i <=3:
    print('第' + str(i) + '次机会：')
    i += 1
    person_number = int(input('请输入你的数字：'))
    if person_number == computer_number:
        print('好厉害，你竟然猜对啦')
        break
    elif person_number < computer_number:
        print('你猜小了哦，还有'+str(3-i+1)+'次机会，试试大点的数字吧')
    elif person_number >computer_number:
        print('你猜大了哦,还有'+str(3-i+1)+'次机会，试试小点的数字吧')
else:
    print('三次机会已经耗尽。。。\n拜拜')
