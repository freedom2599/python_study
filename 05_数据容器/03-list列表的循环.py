"""
演示使用while和for循环遍历列表
"""
mylist = ["小梦", "小孟", "小梦", "小梦", "python"]


def list_while_func():
    """
    使用while循环遍历列表的演示函数
    :return: None
    """
    # 循环控制变量：通过下标索引来控制，默认0
    i = 0
    while i < len(mylist):
        print(mylist[i])
        # 每一次循环将下标加1
        i += 1


def list_for_func():
    """
    使用for循环遍历列表的演示函数
    :return:
    """
    for i in mylist:
        print(i)


list_while_func()
list_for_func()
