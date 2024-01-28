# 调用math库用于175行的取余取模讲解
import math


# """
# python学习笔记
# """
# print(
#     """
# 演示python中字面量的相关操作
# """
# )
# # 整数
# int_a = 66
# # 浮点数（小数）
# float_b = 66.6
# # 字符串（文本）
# str_c = "mqy"
# # 打印整数
# print(int_a)
# # 打印浮点数
# print(float_b)
# # 打印字符串
# print(str_c)
#
# print(
#     """
# 演示python中注释的相关操作
# """
# )
# # 单行注释
# """
# 多行注释
# """
#
# print(
#     """
# 演示python中变量的相关操作
# """
# )
# # 定义一个变量money，值为50
# money = 50
# # 通过print语句进行打印
# print("钱包还有", money, "元")
# # 买了可乐花费5元
# cole = 5
# # 通过print语句进行打印
# print("买可乐花费", cole, "元，剩余", money - cole, "元")
#
# print(
#     """
# 演示python中数据类型的相关操作
# """
# )
# # 方式1：使用print直接输出类型信息
# print("方式1")
# print("name数据类型为", type("mqy"))
# print("age数据类型为", type(24))
# print("num数据类型为", type(66.5))
# # 方式2：使用变量存储type（）语句的结果
# print("方式2")
# name_type = type("mqy")
# age_type = type(24)
# num_type = type(66.5)
# print("name数据类型为", name_type)
# print("age数据类型为", age_type)
# print("num数据类型为", num_type)
# # 方式3：使用type（）语句，查看变量中存储的数据类型信息
# print("方式3")
# name = "mqy"
# age = 24
# num = 66.5
# print("name数据类型为", type(name))
# print("age数据类型为", type(age))
# print("num数据类型为", type(num))
#
#
# print(
#     """
# 演示python中数据类型转换的相关操作
# """
# )
# # 将数字类型(整数和浮点数)转换为字符串
# int_str = str(24)
# float_str = str(24.6)
# print("int_str的值为", int_str, "数据类型为：", type(int_str))
# print("float_str的值为", float_str, "数据类型为：", type(float_str))
# # 将字符串转换为数字(整数和浮点数)
# str_int = int("24")
# str_float = float("24.6")
# print("str_int的值为", str_int, "数据类型为：", type(str_int))
# print("str_float的值为", str_float, "数据类型为：", type(str_float))
# # 整数类型和浮点数互转
# int_float = float(24)
# float_int = int(24.6)
# print("int_float的值为", int_float, "数据类型为：", type(int_float))
# print("float_int的值为", float_int, "数据类型为：", type(float_int))
# # 非数字字符串无法转为数字类型,eg: str_int_ValueError = int("mqy")
#
# """
# 演示python中标识符的相关操作
# """
# # 规则1.命名标识符只允许出现英文、中文、数字、下划线
# # 注意！不推荐使用中文！！；数字不可以开头
# # 举例
# a = "英文"
# 例 = "中文（不推荐）"
# _ = "下划线"
# # 组合
# a_1 = '字母下划线数字组合'
# # 错误示例： 6 = "禁止数字"
# # 规则2.大小写敏感
# Admin = "用户1"
# admin = "用户2"
# print(Admin)
# print(admin)
# # 规则3.不可使用关键字
# # False Ture None and as assert break class continue def del elif else
# # except finally for form global if import in is lambda nonlocal not or
# # pass raise return try while with yield
# # 变量命名规范
#
# """
# 演示python中运算符的相关操作
# """
# # 算数（数学）运算符
# print("1 + 1 = ", 1 + 1)
# print("2 - 1 = ", 2 - 1)
# print("3 * 3 = ", 3 * 3)
# print("8 / 2 = ", 8 / 2)
# print("9 // 4 = ", 9 // 4)
# print("9 % 4 = ", 9 % 4)
# print("9 % -4 = ", 9 % -4)
# print("2 ** 2 = ", 2 ** 2)
# # 赋值运算符
# mun = 1 + 2 * 3
# print("mun = 1 + 2 * 3 =", mun)
# # 复合赋值运算符
# # +=
# mun = 1
# print("mun = ", mun)
# mun += 2 # mun = mun + 2
# print("mun += 2:", mun)
# # -=
# mun = 3
# print("mun = ", mun)
# mun -= 2 # mun = mun - 2
# print("mun -= 2:", mun)
# # *=
# mun = 2
# print("mun = ", mun)
# mun *= 2 # mun = mun * 2
# print("mun *= 2:", mun)
# # /=
# mun = 4
# print("mun = ", mun)
# mun /= 2 # mun = mun / 2
# print("mun /= 2:", mun)
# # //=
# mun = 5
# print("mun = ", mun)
# mun //= 2 # mun = mun // 2
# print("mun //= 2:", mun)
# # %=
# mun = 5
# print("mun = ", mun)
# mun %= 2 # mun = mun % 2
# print("mun %= 2:", mun)
# # **=
# mun = 2
# print("mun = ", mun)
# mun **= 2 # mun = mun ** 2
# print("mun **= 2:", mun)
#
# # 取余和取模:当两个数均为正数是，取余与取模的结果是一致的，而当两个数一正一负时结果就不一样
# # 取余
# a = -5
# b = 3
# print("a = ", a)
# print("b = ", b)
# # y为余 m为模
# c = a / b
# print("c = a / b = ", c)
# # 取余时，会将 c 向0的方向舍弃掉小数部分，c = -1.67，
# c = math.ceil(c)    # 补充：向上取整：math.ceil()；
# # 舍弃后 c = -1，则余数计算如下：
# y = a - b * c
# print("取余时，会将 c 向0的方向舍弃掉小数部分,则c= ", c)
# print("y = a - b * c = ", y)
#
# # 取模
# a = -5
# b = 3
# print("a = ", a)
# print("b = ", b)
# # y为余 m为模
# c = a / b
# print("c = a / b = ", c)
# # 取模时，会将 c 向负无穷的方向取整，c = -1.67，
# # 调用math库里的floor函数对c进行向下取整
# c = math.floor(c)   # 补充：四舍五入：round()；向下取整：math.floor()
# # 向负无穷方向取整后 c = -2：
# m = a - b * c
# print("取模时，会将 c 向负无穷的方向取整,则c= ", c)
# print("m = a - b * c = ", m)
# print("也就是：a % b =", a % b,"\n故，python中的%为取模")
