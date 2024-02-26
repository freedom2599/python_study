from time import sleep

users = {"mqy": "123456", "root": "root", "kali": "kali", "admin": "admin"}
money = 900000

for i in range(3):
    username = input("请输入用户名：")

    if username in users:
        for ii in range(3):
            user_password = input("请输入您的密码：")
            if user_password == users[username]:
                print("登陆成功")
                break

            else:
                if (2 - ii) > 0:
                    print("密码错误,您还有%d次机会" % (2 - ii))
                else:
                    print("密码连续错误3次，用户已被锁定，请联系相关机构")
                    sleep(3)
                    exit()
        break

    else:
        if (2 - i) > 0:
            print("用户名不存在，请重新输入！您还有%d次机会" % (2 - i))
        else:
            print("用户名不存在，已强制踢出")
            sleep(3)
            exit()


def check_balance(boll):  # 余额查询
    if boll:
        print("---------------------余额---------------------")
    print(f"{username}，您好，您的余额剩余：{money}")


def deposit():  # 存款
    print("---------------------存款---------------------")
    global money
    money_in = int(input("请输入存款数（元）："))
    print(f"{username}，您好，您存款{money_in}元成功")
    money += money_in
    check_balance(False)


def withdraw_money():  # 取款
    print("---------------------取款---------------------")
    global money
    money_out = int(input("请输入取款数（元）："))
    if money_out > money:
        print(f"抱歉，{username}，您的余额不足，余额剩余：{money}")
    else:
        print(f"{username}，您好，您取款{money_out}元成功")
        money -= money_out
        check_balance(False)


def main():
    print("---------------------主菜单---------------------")
    print(f"{username}，欢迎来到ATM，请选择操作：")
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    return int(input("请输入您的选择："))


while True:
    fuuc = main()
    if fuuc == 1:
        check_balance(True)
        continue
    elif fuuc == 2:
        deposit()
        continue
    elif fuuc == 3:
        withdraw_money()
    elif fuuc == 4:
        print("退出成功")
        sleep(3)
        break
    else:
        print("选项不存在，请重新输入")
