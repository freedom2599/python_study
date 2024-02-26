"""
演示python中关于循环语句：
for循环的嵌套应用
"""

# 利用for循环嵌套，坚持表白100天，每天先送十朵花，再去表白
i = 1
for i in range(1, 101):
    print(f"今天是第{i}天")
    for j in range(1, 11):
        print(f"送出第{j}朵玫瑰")
    print("小刘我喜欢你")
print(f"第{i}天表白成功")

# 利用for加while循环
for i in range(1,101):
    print(f"今天是第{i}天")
    j = 1
    while j <= 10:
        print(f"送出第{j}朵玫瑰")
        j += 1
    print("小刘我喜欢你")
