import random
from time import sleep

# 存储用户信息的字典
users = {}

# 锁定的卡号列表
locked_cards = []

# 当前登录的用户
current_user = None


# 开户功能
def open_account():
    name = input("请输入姓名：")
    id_number = input("请输入身份证号：")
    phone = input("请输入手机号：")
    balance = float(input("请输入预存金额："))
    password = input("请输入密码：")
    card_number = generate_card_number()

    users[card_number] = {
        "name": name,
        "id_number": id_number,
        "phone": phone,
        "balance": balance,
        "password": password
    }

    print("开户成功！您的卡号是：", card_number)


# 查询功能
def inquire():
    card_number = input("请输入卡号：")
    password = input("请输入密码：")

    if card_number in locked_cards:
        print("该卡号已被锁定，请联系银行解锁。")
        return

    user = users.get(card_number)
    if user and user["password"] == password:
        print("您的余额为：", user["balance"])
    else:
        print("卡号或密码错误！")
        if card_number in users:
            if card_number not in locked_cards:
                users[card_number].setdefault("wrong_password_count", 0)
                users[card_number]["wrong_password_count"] += 1
                if users[card_number]["wrong_password_count"] >= 3:
                    locked_cards.append(card_number)
                    print("连续输错密码已达3次，该卡已被锁定。")


# 取款功能
def withdraw():
    card_number = input("请输入卡号：")
    password = input("请输入密码：")

    if card_number in locked_cards:
        print("该卡号已被锁定，请联系银行解锁。")
        return

    user = users.get(card_number)
    if user and user["password"] == password:
        print("您的余额为：", user["balance"])
        amount = float(input("请输入取款金额："))
        if amount > user["balance"] or amount < 0:
            print("取款金额无效！")
        else:
            user["balance"] -= amount
            print("取款成功！")
            print("当前余额为：", user["balance"])
    else:
        print("卡号或密码错误！")
        if card_number in users:
            if card_number not in locked_cards:
                users[card_number].setdefault("wrong_password_count", 0)
                users[card_number]["wrong_password_count"] += 1
                if users[card_number]["wrong_password_count"] >= 3:
                    locked_cards.append(card_number)
                    print("连续输错密码已达3次，该卡已被锁定。")


# 存款功能
def deposit():
    card_number = input("请输入卡号：")
    password = input("请输入密码：")

    if card_number in locked_cards:
        print("该卡号已被锁定，请联系银行解锁。")
        return

    user = users.get(card_number)
    if user and user["password"] == password:
        print("您的余额为：", user["balance"])
        amount = float(input("请输入存款金额："))
        if amount < 0:
            print("存款金额无效！")
        else:
            user["balance"] += amount
            print("存款成功！")
            print("当前余额为：", user["balance"])
    else:
        print("卡号或密码错误！")
        if card_number in users:
            if card_number not in locked_cards:
                users[card_number].setdefault("wrong_password_count", 0)
                users[card_number]["wrong_password_count"] += 1
                if users[card_number]["wrong_password_count"] >= 3:
                    locked_cards.append(card_number)
                    print("连续输错密码已达3次，该卡已被锁定。")


# 转账功能
def transfer():
    from_card_number = input("请输入转出卡号：")
    from_password = input("请输入密码：")

    if from_card_number in locked_cards:
        print("该卡号已被锁定，请联系银行解锁。")
        return

    from_user = users.get(from_card_number)
    if from_user and from_user["password"] == from_password:
        print("您的余额为：", from_user["balance"])
        to_card_number = input("请输入转入卡号：")
        to_user = users.get(to_card_number)

        if to_card_number in locked_cards:
            print("对方卡号已被锁定，无法转账。")
            return

        if not to_user:
            print("转入卡号不存在，无法转账。")
            return

        amount = float(input("请输入转账金额："))
        if amount > from_user["balance"] or amount < 0:
            print("转账金额无效！")
            return

        confirm = input("确认执行转账功能？(Y/N)")
        if confirm.lower() == "y":
            from_user["balance"] -= amount
            to_user["balance"] += amount
            print("转账成功！")
            print("当前余额为：", from_user["balance"])
        else:
            print("已取消转账功能。")
    else:
        print("卡号或密码错误！")
        if from_card_number in users:
            if from_card_number not in locked_cards:
                users[from_card_number].setdefault("wrong_password_count", 0)
                users[from_card_number]["wrong_password_count"] += 1
                if users[from_card_number]["wrong_password_count"] >= 3:
                    locked_cards.append(from_card_number)
                    print("连续输错密码已达3次，该卡已被锁定。")


# 锁定功能
def lock_card():
    card_number = input("请输入卡号：")
    password = input("请输入密码：")

    if card_number in locked_cards:
        print("卡号已被锁定，请联系客服解锁。")
        return

    user = users.get(card_number)
    if user and user["password"] == password:
        locked_cards.append(card_number)
        print("卡号已被锁定。")
    else:
        print("卡号或密码错误！")


# 解锁功能
def unlock_card():
    card_number = input("请输入卡号：")
    password = input("请输入密码：")

    user = users.get(card_number)
    if user and user["password"] == password:
        if card_number in locked_cards:
            locked_cards.remove(card_number)
            print("卡号已解锁。")
        else:
            print("该卡号未被锁定。")
    else:
        print("卡号或密码错误！")


# 生成不重复的6位数字卡号
def generate_card_number():
    card_number = str(random.randint(100000, 999999))
    while card_number in users:
        card_number = str(random.randint(100000, 999999))
    return card_number


# 存盘功能
def save_data():
    with open("bank_data.txt", "w") as file:
        for card_number, user in users.items():
            file.write(
                f"{card_number},{user['name']},{user['id_number']},{user['phone']},{user['balance']},{user['password']}\n")

    with open("locked_cards.txt", "w") as file:
        file.write("\n".join(locked_cards))

    print("数据已保存到本地文件。")

#加载存盘的数据
def load_data():
    global users, locked_cards

    with open("bank_data.txt", "r") as file:
        for line in file:
            card_number, name, id_number, phone, balance, password = line.strip().split(",")
            users[card_number] = {
                "name": name,
                "id_number": id_number,
                "phone": phone,
                "balance": float(balance),
                "password": password
            }

    with open("locked_cards.txt", "r") as file:
        for line in file:
            locked_cards.append(line.strip())


# 退出功能
def login_or_out(option):
    admin_account = "root"
    admin_password = "root"

    account = input("请输入管理员账号：")
    password = input("请输入管理员密码：")

    if account == admin_account and password == admin_password:
        if option == 1:
            load_data()
            print("登录成功！")
            # continue with normal operations
        elif option == 2:
            save_data()
            print("已退出系统。")
            exit()
        else:
            print("无效的选项！请传入1或2。")
    else:
        print("管理员账号或密码错误！")
        if option == 1:
            load_data()
            sleep(1)
            exit()
            # continue with normal operations
        elif option == 2:
            save_data()

# 主程序
login_or_out(1)
while True:
    print("=============== 欢迎使用银行管理系统 ===============")
    print("1. 开户    2. 查询    3. 取款")
    print("4. 存款    5. 转账    6. 锁定 ")
    print("7. 解锁    8. 存盘    9. 退出")
    print("================================================")

    choice = input("请输入您的选择（数字）：")

    if choice == "1":
        open_account()
    elif choice == "2":
        inquire()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        deposit()
    elif choice == "5":
        transfer()
    elif choice == "6":
        lock_card()
    elif choice == "7":
        unlock_card()
    elif choice == "8":
        save_data()
    elif choice == "9":
        login_or_out(2)
    else:
        print("无效的选择！")
