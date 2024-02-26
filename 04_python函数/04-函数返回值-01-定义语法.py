"""
演示python中关于函数返回值的定义语法的介绍
"""
"""
语法格式
def 函数(参数):
    函数体
    return 返回值
    
    
变量 = 函数(参数)
"""


# 定义函数，两数相加
def add(a, b):
    result = a + b
    # 通过返回值，将相加的结果返回给调用者
    return result


# 函数的返回值，通过变量来接收
r = add(1, 2)
print(r)
