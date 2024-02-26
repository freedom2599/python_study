"""
演示数据容器字典的定义
"""

# 定义字典
my_dict1 = {"刘一飞": 99, "小孟": 88, "小刘": 77}
# 定义空字典
my_dict2 = {}
my_dict3 = dict()
print(f"字典1的内容是：{my_dict1}, 类型：{type(my_dict1)}")
print(f"字典2的内容是：{my_dict2}, 类型：{type(my_dict2)}")
print(f"字典3的内容是：{my_dict3}, 类型：{type(my_dict3)}")

# 定义重复Key的字典
my_dict1 = {"刘一飞": 99, "刘一飞": 88, "小刘": 77}
print(f"重复key的字典的内容是：{my_dict1}")

# 从字典中基于Key获取Value
my_dict1 = {"刘一飞": 99, "小孟": 88, "小刘": 77}
score = my_dict1["刘一飞"]
print(f"刘一飞的考试分数是：{score}")
score = my_dict1["小孟"]
print(f"小孟的考试分数是：{score}")
# 定义嵌套字典
stu_score_dict = {
    "小刘": {
        "语文": 77,
        "数学": 66,
        "英语": 33
    }, "刘一飞": {
        "语文": 88,
        "数学": 86,
        "英语": 55
    }, "小孟": {
        "语文": 99,
        "数学": 96,
        "英语": 66
    }
}
print(f"学生的考试信息是：{stu_score_dict}")

# 从嵌套字典中获取数据
# 看一下小孟的语文信息
score = stu_score_dict["小孟"]["语文"]
print(f"小孟的语文分数是：{score}")
score = stu_score_dict["小孟"]["英语"]
print(f"小孟的英语分数是：{score}")
