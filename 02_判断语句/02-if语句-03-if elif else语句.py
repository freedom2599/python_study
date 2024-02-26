"""
演示python中关于判断语句：if elif else语句
"""
age = int(input("请输入你的年龄"))
if age >= 18:
    print("请购买门票！")
elif age <= 6:
    print("请在父母陪同下游玩！")
else:
    print("您无需购买门票")
print("祝你游玩愉快")
