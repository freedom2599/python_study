"""
演示python中关于判断语句：判断语句的嵌套
"""
age = int(input("请输入你的年龄：\n"))
if age <= 18:
    print("你无需购买门票！")
    if age <= 6:
        print("请在父母陪同下游玩！")
elif age > 55:
    print("您的年龄过大")
    exit()
else:
    print("请您购买门票")
print("祝你游玩愉快")
