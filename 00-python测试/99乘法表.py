# 利用while循环嵌套
i = 1
while i <= 9:
    ii = 1
    while ii <= i:
        print(f"{ii}x{i}={i*ii}\t", end="")
        ii += 1
    i += 1
    print()

# 利用for循环嵌套
for i in range(1, 10):
    for j in range(1, i+1):
        print(f"{j}x{i}={j*i}\t", end="")
    print()
