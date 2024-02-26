"""
演示python中关于函数的嵌套调用的介绍
"""


# 定义函数func_a
def func_a():
    print('h')


# 定义函数func_b，调用func_a
def func_b():
    # 调用func_a
    func_a()
    print("i")


func_b()
