"""
演示python中input语句获取键盘输入信息
"""
# input默认接受字符串

# print("你是谁？")
# name = input()
# print("只知道了，你的名字是%s" % name)

# name = input("你是谁？\n")
# print("我记得你%s" % name)

# 输入数字类型
num = input("请告诉我你的手机号\n")
print("你的手机号的类型是：", type(num))
# 数据类型转换
num = int(num)
print("你的手机号的类型是：", type(num))
