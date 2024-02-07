# 调入随机数
import random
# 调入书面
from time import sleep

# 获取范围1-100的随机数
num = random.randint(1,100)
# 定义一个变量，记录共猜测了多少次
time = 0

# 通过一个布尔类型的变量。做循环是否继续的标志
flag = True

# while循环，flag为True，继续循环，反之跳出循环
while flag:
    # 输入猜测的数字
    guess_num=input("请输入您猜测的数字（1-100）：")

    # 利用try——except语句，对输入的数据进行检测
    try:
        # 尝试利用int函数将输入的数据转为整数
        guess_num = int(guess_num)
    # 如果报错，则进行打印
    except ValueError:
            print("输入有误，请重新输入")
            continue
        # if函数判断输入的数字是否在1-100内
    if guess_num not in [1,100]:
        print("请输入1-100内的数字！")
    else:
        # 次数加1
        time += 1
        if guess_num == num:
            print("猜中了")
            print("一共猜测了%d次"% time)
            # 强制睡眠1秒
            sleep(1)
            # 设置为False，就是终止循环的条件
            flag = False
        else:
            if guess_num > num:
                print("哇，这也太大了吧！")

            else:
                print("猜的有些小了！")



