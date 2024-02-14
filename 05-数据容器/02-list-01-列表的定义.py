"""
演示python中关于列表的定义
"""
"""
基本语法：
字面量：
[元素1, 元素2, 元素3, 元素4, ...]

定义变量：
变量名称 = [元素1, 元素2, 元素3, 元素4, ...]

定义空列表
变量名称 = []
变量名称 = list()
"""
# 定义一个列表list
name_list = ["小刘", "小孟", 520, True]
print(name_list)
print(type(name_list))

# 定义一个嵌套的列表
list_list = [[1, 2, 3, 4], [5, 6, 7, 8]]
print(list_list)
print(type(list_list[1]))
