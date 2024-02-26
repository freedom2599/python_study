"""
演示python中布尔类型的定义
以及比较运算符的应用
"""
# 定义变量存储布尔类型的数据
bool_1 = True
bool_2 = False
print(f"bool_1变量的内容是:{bool_1}，类型是{type(bool_1)}")
print(f"bool_2变量的内容是:{bool_2}，类型是{type(bool_2)}")

# 比较运算符的使用
# ==,!=,>,<,>=,<=
# 演示进行内容的相等比较
num1 = 10
num2 = 10
print(f"10 == 10 的结果是：{num1 == num2}")

num1 = 10
num2 = 15
print(f"10 != 15 的结果是：{num1 != num2}")

name1 = "mqy"
name2 = "mqy1"
print(f"name1 == name2的结果是：{name1 == name2}")

# 演示大于小于，大于等于，小于等于的比较运算
num1 = 10
num2 = 15

print(f"10 > 15 的结果是：{num1 > num2}")
print(f"10 < 15 的结果是：{num1 < num2}")

num1 = 10
num2 = 10
num3 = 11
print(f"10 >= 10 的结果是：{num1 >= num2}")
print(f"10 <= 10 的结果是：{num1 <= num2}")
print(f"10 >= 11 的结果是：{num1 >= num3}")
print(f"10 <= 11 的结果是：{num1 <= num3}")


