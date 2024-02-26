"""
演示tuple元组的定义和操作
"""

# 定义元组
tuple_1 = (1, "Hello", True)
tuple_2 = ()
tuple_3 = tuple()
print(f"tuple_1的类型是：{type(tuple_1)}, 内容是：{tuple_1}")
print(f"tuple_2的类型是：{type(tuple_2)}, 内容是：{tuple_2}")
print(f"tuple_3的类型是：{type(tuple_3)}, 内容是：{tuple_3}")

# 定义单个元素的元素
tuple_4 = ("hello", )
print(f"tuple_4的类型是：{type(tuple_4)}, tuple_4的内容是：{tuple_4}")
# 元组的嵌套
tuple_5 = ((1, 2, 3), (4, 5, 6))
print(f"tuple_5的类型是：{type(tuple_5)}, 内容是：{tuple_5}")

# 下标索引去取出内容
num = tuple_5[1][2]
print(f"从嵌套元组中取出的数据是：{num}")

# 元组的操作：index查找方法
tuple_6 = ("小梦", "小孟", "Python")
index = tuple_6.index("小孟")
print(f"在元组tuple_6中查找小孟，的下标是：{index}")
# 元组的操作：count统计方法
tuple_7 = ("小梦", "小孟", "小梦", "小梦", "python")
num = tuple_7.count("小孟")
print(f"在元组tuple_7中统计小孟的数量有：{num}个")
# 元组的操作：len函数统计元组元素数量
tuple_8 = ("小梦", "小孟", "小梦", "小梦", "python")
num = len(tuple_8)
print(f"tuple_8元组中的元素有：{num}个")
# 元组的遍历：while
index = 0
while index < len(tuple_8):
    print(f"元组的元素有：{tuple_8[index]}")
    # 至关重要
    index += 1

# 元组的遍历：for
for element in tuple_8:
    print(f"元组的元素有：{element}")

# 修改元组内容
# tuple_8[0] = "小孟"

# 定义一个元组
tuple_9 = (1, 2, ["小孟", "小刘"])
print(f"tuple_9的内容是：{tuple_9}")
tuple_9[2][0] = "freedom"
tuple_9[2][1] = "python"
print(f"tuple_9的内容是：{tuple_9}")