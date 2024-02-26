"""
演示面向对象：继承的基础语法
"""


# 演示单继承
class Phone:
    IMEI = None     # 序列号
    producer = "freedom"     # 厂商

    @staticmethod
    def call_by_4g():
        print("4g通话")


class Phone2022(Phone):
    face_id = "10001"       # 面部识别ID

    @staticmethod
    def call_by_5g():
        print("2022年新功能：5g通话")


phone = Phone2022()
print(phone.producer)
phone.call_by_4g()
phone.call_by_5g()


# 演示多继承
class NFCReader:
    nfc_type = "第五代"
    producer = "XM"

    @staticmethod
    def read_card():
        print("NFC读卡")

    @staticmethod
    def write_card():
        print("NFC写卡")


class RemoteControl:
    rc_type = "红外遥控"

    @staticmethod
    def control():
        print("红外遥控开启了")


class MyPhone(Phone, NFCReader, RemoteControl):
    pass


phone = MyPhone()
phone.call_by_4g()
phone.read_card()
phone.write_card()
phone.control()

print(phone.producer)
