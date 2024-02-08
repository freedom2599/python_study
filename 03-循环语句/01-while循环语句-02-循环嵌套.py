"""
演示python中关于循环语句：
while循环语句的循环嵌套
"""

# 定义外层循环的控制变量
i = 1
while i < 10:

    # 定义内层循环的控制变量
    ii = 1
    while ii <= i:
        # 内层循环的print语句，不要换行，通过\t制表符进行对齐
        print(f"{ii} X {i} = {ii * i}\t", end="")
        ii += 1

    i += 1
    print()     # print空内容，就相当于输出一个换行
