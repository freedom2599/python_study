"""
演示python中数据类型转换的相关操作
"""

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
