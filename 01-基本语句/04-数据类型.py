"""
演示python中数据类型的相关操作
"""

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

