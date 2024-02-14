"""
演示python中关于函数的介绍
"""

# 函数：组织好的，可以重复利用，用来实现特定功能的代码段
# 演示：快速体验函数的开发和应用
# 需求：统计字符串长度，不使用内置函数
str1 = "1234567"
str2 = "987654321"
str3 = "0123456789"


# 自定义函数
# 定义一个计数的变量
j = 0
for i in str1:
    j += 1
print(j)

j = 0
for i in str2:
    j += 1
print(j)

j = 0
for i in str3:
    j += 1
print(j)
# 等效于
print(len(str3))


# 使用函数优化过程
def my_len(date):
    j = 0
    for _ in date:
        j += 1
    print(j)


my_len(str1)
my_len(str2)
my_len(str3)
