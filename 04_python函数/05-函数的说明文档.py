"""
演示python中关于函数说明文档的介绍
"""


# 定义函数，两数相加
def add(a, b):
    """
    add函数接受两个参数进行相加
    :param a: 形参a表示相加的其中那个一个参数
    :param b: 形参b表示相加的其中那个一个参数
    :return: 返回值是两数相加的结果
    """
    result = a + b
    print(f"两数相加的结果是{result}")
    return result


add(5, 6)
