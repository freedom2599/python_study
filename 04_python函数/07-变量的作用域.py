"""
演示python中关于变量的作用域的介绍
"""
"""
局部变量：
定义在函数体内部的变量，即旨在函数体内部生效
作用：在函数内部，临时保存数据，当函数调用完成后，立即销毁局部变量

全局变量：
在函数体内外都能生效的变量

"""


# # 演示局部变量
# def a():
#     b = 4
#     print(b)
#
#
# a()
# # 出了函数体，局部变量无法使用
# print(b)
#
# # 演示全局变量
# num = 1
#
#
# def test_c():
#     print(f"test_c:{num}")
#
#
# test_c()
# print(num)
#
# # 在函数内部修改全局变量，无法修改
# num = 1
#
#
# def test_c():
#     num = 2     # 局部变量
#     print(f"test_c:{num}")
#
#
# test_c()
# print(num)

# 通过global关键字，在函数体内声明变量为全局变量
num = 1


def test_a():
    print(f"test_a:{num}")


def test_c():
    global num  # 设置内部定义的变量为全局变量
    num = 2
    print(f"test_c:{num}")


test_a()
test_c()
print(num)
