import random


def say_hi():
    print('你好，请配合测量体温！')


def main(t):
    if t > 37.5:
        print("您的体温是%.1f度，需要隔离" % t)
    else:
        print("您的体温是%.1f，体温正常，欢迎光临" % t)


x = random.uniform(36.5, 40)
say_hi()
main(x)
