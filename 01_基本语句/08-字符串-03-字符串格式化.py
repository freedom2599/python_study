"""
 演示python中字符串格式化的相关操作
"""
# 通过占位的形式，完成拼接
name = "mqy"
message = "我的名字是%s" % name
print(message)

# 通过占位的形式，完成数字和字符串的拼接
qq = 390566161
level = 70
message = "我的QQ号是%s,QQ等级是%s" % (qq, level)
print(message)

# 通过占位的形式，完成字符串、整数、浮点数，三种不同类型变量的占位
name = "mqy"
age = 24
birthday = 8.17
message = "我是%s，我今年%d岁，我的生日是%.2f" % (name, age, birthday)
print(message)
