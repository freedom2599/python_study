"""
演示python中运算符的相关操作
"""
# 调用math库用于取余取模讲解
import math
# 算数（数学）运算符
print("1 + 1 = ", 1 + 1)
print("2 - 1 = ", 2 - 1)
print("3 * 3 = ", 3 * 3)
print("8 / 2 = ", 8 / 2)
print("9 // 4 = ", 9 // 4)
print("9 % 4 = ", 9 % 4)
print("9 % -4 = ", 9 % -4)
print("2 ** 2 = ", 2 ** 2)
# 赋值运算符
mun = 1 + 2 * 3
print("mun = 1 + 2 * 3 =", mun)
# 复合赋值运算符
# +=
mun = 1
print("mun = ", mun)
mun += 2    # mun = mun + 2
print("mun += 2:", mun)
# -=
mun = 3
print("mun = ", mun)
mun -= 2    # mun = mun - 2
print("mun -= 2:", mun)
# *=
mun = 2
print("mun = ", mun)
mun *= 2    # mun = mun * 2
print("mun *= 2:", mun)
# /=
mun = 4
print("mun = ", mun)
mun /= 2    # mun = mun / 2
print("mun /= 2:", mun)
# //=
mun = 5
print("mun = ", mun)
mun //= 2   # mun = mun // 2
print("mun //= 2:", mun)
# %=
mun = 5
print("mun = ", mun)
mun %= 2    # mun = mun % 2
print("mun %= 2:", mun)
# **=
mun = 2
print("mun = ", mun)
mun **= 2   # mun = mun ** 2
print("mun **= 2:", mun)

# 取余和取模:当两个数均为正数是，取余与取模的结果是一致的，而当两个数一正一负时结果就不一样
# 取余
a = -5
b = 3
print("a = ", a)
print("b = ", b)
# y为余 m为模
c = a / b
print("c = a / b = ", c)
# 取余时，会将 c 向0的方向舍弃掉小数部分，c = -1.67，
c = math.ceil(c)    # 补充：向上取整：math.ceil()；
# 舍弃后 c = -1，则余数计算如下：
y = a - b * c
print("取余时，会将 c 向0的方向舍弃掉小数部分,则c= ", c)
print("y = a - b * c = ", y)

# 取模
a = -5
b = 3
print("a = ", a)
print("b = ", b)
# y为余 m为模
c = a / b
print("c = a / b = ", c)
# 取模时，会将 c 向负无穷的方向取整，c = -1.67，
# 调用math库里的floor函数对c进行向下取整
c = math.floor(c)   # 补充：四舍五入：round()；向下取整：math.floor()
# 向负无穷方向取整后 c = -2：
m = a - b * c
print("取模时，会将 c 向负无穷的方向取整,则c= ", c)
print("m = a - b * c = ", m)
print("也就是：a % b =", a % b, "\n故，python中的%为取模")
