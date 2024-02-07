# Python学习笔记

## [基本语句](https://github.com/freedom2599/python_study/tree/master/01-%E5%9F%BA%E6%9C%AC%E8%AF%AD%E5%8F%A5)

### [字面量](https://github.com/freedom2599/python_study/blob/master/01-%E5%9F%BA%E6%9C%AC%E8%AF%AD%E5%8F%A5/01-%E5%AD%97%E9%9D%A2%E9%87%8F.py)

```python
# 整数

int_a = 66

# 浮点数（小数）

float_b = 66.6

# 字符串（文本）

str_c = "mqy"

# 打印整数

print(int_a)

# 打印浮点数

print(float_b)

# 打印字符串

print(str_c)
```

### [注释](https://github.com/freedom2599/python_study/blob/master/01-%E5%9F%BA%E6%9C%AC%E8%AF%AD%E5%8F%A5/02-%E6%B3%A8%E9%87%8A.py)

```python
# 
单行注释

"""
多行注释
"""
```

### [变量](https://github.com/freedom2599/python_study/blob/master/01-%E5%9F%BA%E6%9C%AC%E8%AF%AD%E5%8F%A5/03-%E5%8F%98%E9%87%8F.py)

```python
# 定义一个变量money，值为50

money = 50

# 通过print语句进行打印

print("钱包还有", money, "元")

# 买了可乐花费5元

cole = 5

# 通过print语句进行打印

print("买可乐花费", cole, "元，剩余", money - cole, "元")
```

### [数据类型](https://github.com/freedom2599/python_study/blob/master/01-%E5%9F%BA%E6%9C%AC%E8%AF%AD%E5%8F%A5/04-%E6%95%B0%E6%8D%AE%E7%B1%BB%E5%9E%8B.py)

```python
# 方式1：使用print直接输出类型信息

print("方式1")
print("name数据类型为", type("mqy"))
print("age数据类型为", type(24))
print("num数据类型为", type(66.5))

# 方式2：使用变量存储type（）语句的结果

print("方式2")
name_type = type("mqy")
age_type = type(24)
num_type = type(66.5)
print("name数据类型为", name_type)
print("age数据类型为", age_type)
print("num数据类型为", num_type)

# 方式3：使用type（）语句，查看变量中存储的数据类型信息

print("方式3")
name = "mqy"
age = 24
num = 66.5
print("name数据类型为", type(name))
print("age数据类型为", type(age))
print("num数据类型为", type(num))
```

### [数据类型转换](https://github.com/freedom2599/python_study/blob/master/01-%E5%9F%BA%E6%9C%AC%E8%AF%AD%E5%8F%A5/05-%E6%95%B0%E6%8D%AE%E7%B1%BB%E5%9E%8B%E8%BD%AC%E6%8D%A2.py)

```python
# 将数字类型(整数和浮点数)转换为字符串

int_str = str(24)
float_str = str(24.6)
print("int_str的值为", int_str, "数据类型为：", type(int_str))
print("float_str的值为", float_str, "数据类型为：", type(float_str))

# 将字符串转换为数字(整数和浮点数)

str_int = int("24")
str_float = float("24.6")
print("str_int的值为", str_int, "数据类型为：", type(str_int))
print("str_float的值为", str_float, "数据类型为：", type(str_float))

# 整数类型和浮点数互转

int_float = float(24)
float_int = int(24.6)
print("int_float的值为", int_float, "数据类型为：", type(int_float))
print("float_int的值为", float_int, "数据类型为：", type(float_int))

# 非数字字符串无法转为数字类型,eg: str_int_ValueError = int("mqy")
```

### [标识符](https://github.com/freedom2599/python_study/blob/master/01-%E5%9F%BA%E6%9C%AC%E8%AF%AD%E5%8F%A5/06-%E6%A0%87%E8%AF%86%E7%AC%A6.py)

```python
# 规则1.命名标识符只允许出现英文、中文、数字、下划线

# 注意！不推荐使用中文！！；数字不可以开头

# 举例

a = "英文"
例 = "中文（不推荐）"
_ = "下划线"

# 组合

a_1 = '字母下划线数字组合'

# 错误示例： 6 = "禁止数字"

# 规则2.大小写敏感

Admin = "用户1"
admin = "用户2"
print(Admin)
print(admin)

# 规则3.不可使用关键字

# False Ture None and as assert break class continue def del elif else

# except finally for form global if import in is lambda nonlocal not or

# pass raise return try while with yield

# 变量命名规范
```

### [运算符](https://github.com/freedom2599/python_study/blob/master/01-%E5%9F%BA%E6%9C%AC%E8%AF%AD%E5%8F%A5/07-%E8%BF%90%E7%AE%97%E7%AC%A6.py)

```python
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

# 调用math库用于取余取模讲解

import math

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
```

### 字符串

#### [字符串的定义法](https://github.com/freedom2599/python_study/blob/master/01-%E5%9F%BA%E6%9C%AC%E8%AF%AD%E5%8F%A5/08-%E5%AD%97%E7%AC%A6%E4%B8%B2-01-%E5%AD%97%E7%AC%A6%E4%B8%B2%E7%9A%84%E5%AE%9A%E4%B9%89%E6%B3%95.py)

```python
# 单引号定义法

name_1 = '张三'
print(name_1)

# 双引号定义法

name_2 = "张三"
print(name_2)

# 三引号定义法,与多行注释写法一样，同样支持换行操作，使用变量接收就是字符串，不接收就可作为多行注释

# 单行会提示，W292 no newline at end of file

name_3 = """
我叫
张三
"""
print(name_3)

# 字符串的嵌套

# 单引号定义法，可以内含双引号

name_12 = '我叫"张三"'
print("单引号定义法，可以内含双引号：", name_12)

# 双引号定义法，可以内含单引号

name_21 = "我叫'张三'"
print("双引号定义法，可以内含单引号：", name_21)

# 使用转义字符（\）来将引号解除效用，变成普通字符串

name_4 = "我叫\"张三\""
print("使用转义字符\\来将引号解除效用:", name_4)
```

#### [字符串的拼接](https://github.com/freedom2599/python_study/blob/master/01-%E5%9F%BA%E6%9C%AC%E8%AF%AD%E5%8F%A5/08-%E5%AD%97%E7%AC%A6%E4%B8%B2-02-%E5%AD%97%E7%AC%A6%E4%B8%B2%E7%9A%84%E6%8B%BC%E6%8E%A5.py)

```python
# 字符串字面量之间的拼接

print("390566" + "161")

# 字符串字面量和字符串变量的拼接（字符串没有办法通过加号和整数、浮点数等其他类型进行拼接）

qq = "3905666161"
name = "mqy"
print("我是：" + name + "我的QQ号是：" + qq)
```

#### [字符串格式化](https://github.com/freedom2599/python_study/blob/master/01-%E5%9F%BA%E6%9C%AC%E8%AF%AD%E5%8F%A5/08-%E5%AD%97%E7%AC%A6%E4%B8%B2-03-%E5%AD%97%E7%AC%A6%E4%B8%B2%E6%A0%BC%E5%BC%8F%E5%8C%96.py)

```python
# 通过占位的形式，完成拼接

name = "mqy"
message = "我的名字是%s" % name
print(message)

# 通过占位的形式，完成数字和字符串的拼接

qq = 390566161
level = 70
message = "我的QQ号是%s,QQ等级是%s" % (qq, level)
print(message)

# 通过占位的形式，完成字符串、整数、浮点数，三种不同类型变量的占位

name = "mqy"
age = 24
birthday = 8.17
message = "我是%s，我今年%d岁，我的生日是%.2f" % (name, age, birthday)
print(message)
```

####  [字符串格式化的精度控制](https://github.com/freedom2599/python_study/blob/master/01-%E5%9F%BA%E6%9C%AC%E8%AF%AD%E5%8F%A5/08-%E5%AD%97%E7%AC%A6%E4%B8%B2-04-%E5%AD%97%E7%AC%A6%E4%B8%B2%E6%A0%BC%E5%BC%8F%E5%8C%96%E7%9A%84%E7%B2%BE%E5%BA%A6%E6%8E%A7%E5%88%B6.py)

```python
# 我们可以使用辅助符号"m.n"来控制数据的宽度和精度

# m,控制宽度，要求是数字（很少使用），设置宽度小于数字自身时，不生效

# n，控制小数点精度，要求是数字，会进行小数的四舍五入

num1 = 11
num2 = 12.345
print("数字11宽度限制5，结果是：%5d" % num1)
print("数字11宽度限制1，结果是：%1d" % num1)
print("数字12.345宽度限制7，小数精度2，结果是：%7.2f" % num2)
print("数字12.345宽度不限制，小数精度2，结果是：%.2f" % num2)
```

#### [字符串格式化方式2](https://github.com/freedom2599/python_study/blob/master/01-%E5%9F%BA%E6%9C%AC%E8%AF%AD%E5%8F%A5/08-%E5%AD%97%E7%AC%A6%E4%B8%B2-05-%E5%AD%97%E7%AC%A6%E4%B8%B2%E6%A0%BC%E5%BC%8F%E5%8C%962.py)

```python
# 展示第二种字符串格式化的方法：f"{占位}"

name = "mqy"
age = 24
birthday = 8.17
print(f"我是{name}，我今年{age}岁，我的生日是{birthday}" )
```

#### [表达式格式化](https://github.com/freedom2599/python_study/blob/master/01-%E5%9F%BA%E6%9C%AC%E8%AF%AD%E5%8F%A5/08-%E5%AD%97%E7%AC%A6%E4%B8%B2-06-%E8%A1%A8%E8%BE%BE%E5%BC%8F%E6%A0%BC%E5%BC%8F%E5%8C%96.py)

```python
print('1 * 1的结果是%d' % (1 * 1))
print(f'1 * 2的结果是{1 * 2}')
print('字符串在python中的类型名是：%s' % type("字符串"))
print(f'字符串在python中的类型名是：{type("字符串")}')
```

### [数据输入](https://github.com/freedom2599/python_study/blob/master/01-%E5%9F%BA%E6%9C%AC%E8%AF%AD%E5%8F%A5/09-%E6%95%B0%E6%8D%AE%E8%BE%93%E5%85%A5.py)

input语句获取键盘输入信息

```python
# input默认接受字符串

# print("你是谁？")

# name = input()

# print("只知道了，你的名字是%s" % name)

# name = input("你是谁？\n")

# print("我记得你%s" % name)

# 输入数字类型

num = input("请告诉我你的手机号\n")
print("你的手机号的类型是：", type(num))

# 数据类型转换

num = int(num)
print("你的手机号的类型是：", type(num))
```

## [判断语句](https://github.com/freedom2599/python_study/tree/master/02-%E5%88%A4%E6%96%AD%E8%AF%AD%E5%8F%A5)

### [布尔类型和比较运算符](https://github.com/freedom2599/python_study/blob/master/02-%E5%88%A4%E6%96%AD%E8%AF%AD%E5%8F%A5/01-%E5%B8%83%E5%B0%94%E7%B1%BB%E5%9E%8B%E5%92%8C%E6%AF%94%E8%BE%83%E8%BF%90%E7%AE%97%E7%AC%A6.py)

python常用的6种值

 ```
  
 - 数字（Number）
 	- 整数（int）
 		 - 如：1、-1等
 	- 浮点数（float）
          - 如：13.14、-131.4等.
 	- 复数（complex）
          - 如：4+3j，以j结尾表示复数
 	- 布尔（bool）
          - 表示现实生活中的逻辑，即真和假 True表示真 Flase表示假 True的本质上是一个数字记作1，False记作0
 - 字符串（String）
 	- 描述文本的一种数据类型
          - 由任意数量的字符组成
 - 列表（List）
 	- 有序的可变序列
          - python中使用最为频繁的数据类型，可有序记录一堆数据
 - 元组（Tuple）
 	- 有序的不可变序列
          - 可有序记录一堆不可变的python数据集合
 - 集合（Set）
 	- 无序不重复集合
          - 可无序记录一堆不重复的python数据集合
 - 字典（Dictionary）
 	- 无序key-value集合
          - 可无序记录一堆key-value型的python数据集合
 ```

​      

演示python中布尔类型的定义以及比较运算符的应用

```python
# 定义变量存储布尔类型的数据
bool_1 = True
bool_2 = False
print(f"bool_1变量的内容是:{bool_1}，类型是{type(bool_1)}")
print(f"bool_2变量的内容是:{bool_2}，类型是{type(bool_2)}")

# 比较运算符的使用
# ==,!=,>,<,>=,<=
# 演示进行内容的相等比较
num1 = 10
num2 = 10
print(f"10 == 10 的结果是：{num1 == num2}")

num1 = 10
num2 = 15
print(f"10 != 15 的结果是：{num1 != num2}")

name1 = "mqy"
name2 = "mqy1"
print(f"name1 == name2的结果是：{name1 == name2}")

# 演示大于小于，大于等于，小于等于的比较运算
num1 = 10
num2 = 15

print(f"10 > 15 的结果是：{num1 > num2}")
print(f"10 < 15 的结果是：{num1 < num2}")

num1 = 10
num2 = 10
num3 = 11
print(f"10 >= 10 的结果是：{num1 >= num2}")
print(f"10 <= 10 的结果是：{num1 <= num2}")
print(f"10 >= 11 的结果是：{num1 >= num3}")
print(f"10 <= 11 的结果是：{num1 <= num3}")
```
