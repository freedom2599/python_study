"""
python学习笔记
"""
print(
    """
演示python中字面量的相关操作
"""
)
# 整数
66
# 浮点数（小数）
66.6
# 字符串（文本）
"mqy"
# 打印整数
print(66)
# 打印浮点数
print(66.6)
# 打印字符串
print("mqy")

print(
    """
演示python中注释的相关操作
"""
)
# 单行注释
"""
多行注释
"""

print(
    """
演示python中变量的相关操作
"""
)
# 定义一个变量money，值为50
money = 50
# 通过print语句进行打印
print("钱包还有", money, "元")
# 买了可乐花费5元
cole = 5
# 通过print语句进行打印
print("买可乐花费", cole, "元，剩余", money - cole, "元")

print(
    """
演示python中数据类型的相关操作
"""
)
# 方式1：使用print直接输出类型信息
print("方式1")
print("name数据类型为", type("mqy"))
print("age数据类型为", type(24))
print("num数据类型为", type(66.5))
# 方式2：使用变量存储type（）语句的结果
print("方式2")
name_type = type("mqy")
age_type = type(24)
num_type = type(66.5)
print("name数据类型为", name_type)
print("age数据类型为", age_type)
print("num数据类型为", num_type)
# 方式3：使用type（）语句，查看变量中存储的数据类型信息
print("方式3")
name = "mqy"
age = 24
num = 66.5
print("name数据类型为", type(name))
print("age数据类型为", type(age))
print("num数据类型为", type(num))


print(
    """
演示python中数据类型转换的相关操作
"""
)
# 将数字类型(整数和浮点数)转换为字符串
int_str = str(24)
float_str = str(24.6)
print("int_str的值为", int_str, "数据类型为：", type(int_str))
print("float_str的值为", float_str, "数据类型为：", type(float_str))
# 将字符串转换为数字(整数和浮点数)
str_int = int("24")
str_float = float("24.6")
print("str_int的值为", str_int, "数据类型为：", type(str_int))
print("str_float的值为", str_float, "数据类型为：", type(str_float))
# 整数类型和浮点数互转
int_float = float(24)
float_int = int(24.6)
print("int_float的值为", int_float, "数据类型为：", type(int_float))
print("float_int的值为", float_int, "数据类型为：", type(float_int))
# 非数字字符串无法转为数字类型,eg: str_int_ValueError = int("mqy")
