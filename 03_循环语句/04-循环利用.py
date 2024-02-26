"""
公司准备10000元奖金，一共20个员工，绩点1-10，
绩点小于5，不发放奖金，大于等于5，发放奖金1000元，奖金发放完则不再发放
"""


import random

money = 10000
for i in range(1, 21):
    num = random.randint(1, 10)
    if money >= 1000:
        if num < 5:
            print(f"员工{i},绩点{num},绩点小于5，不发放工资，下一位")
            continue
        money -= 1000
        print(f"员工{i},绩点{num}，发放工资1000元，公司账户余额{money}")
    else:
        print("工资发完了，下个月再领取吧")
        break


"""
公司准备10000元奖金，一共20个员工，绩点1-10，
绩点小于5，不发放奖金，大于等于5的员工平分奖金，奖金发放完则不再发放
"""


num = 0
money = 10000
for i in range(1, 21):
    num1 = random.randint(1, 10)
    if num1 >= 5:
        print(f"员工{i},绩点{num1},满足条件")
        num += 1
        continue
    print(f"员工{i},绩点{num1}")
money2 = money//num
print(f"奖金共有{money}元，此次绩点5以上的共有{num}人，每人发放{money2}元，剩余金额{money-num*money2}元")
