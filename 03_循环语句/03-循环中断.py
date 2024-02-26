"""
演示python中关于循环中断的应用:break和continue
"""

# 演示循环中断语句 continue
for i in range(1, 6):
    print("111")
    continue
    print("222")
print("333")

# 演示 continue的嵌套使用:中断所在循环的当次执行，直接进入下一次
for i in range(1, 6):
    print("111")
    for j in range(1, 6):
        print("222")
        continue
        print("333")
    print("444")

# 演示循环中断语句 break
for i in range(1, 6):
    print("111")
    break
    print("222")
print("333")

# 演示 break的嵌套使用：直接结束所在循环
for i in range(1, 6):
    print("111")
    for j in range(1, 6):
        print("222")
        break
        print("333")
    print("444")
