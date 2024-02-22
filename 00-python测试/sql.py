# 导入pymysql模块以实现对MySQL数据库的连接操作
from pymysql import connect

# 定义数据库连接参数，建立与MySQL服务器的连接
# 主机名设置为本地localhost，端口号为3306（默认MySQL端口）
conn = connect(
    host='localhost',   # 主机名（或ip地址）
    port=3306,  # 端口号
    user='root',    # 数据库用户名
    password='718817mqy'    # 数据库用户密码
)

# 创建游标对象
curse = conn.cursor()
# 选择数据库
conn.select_db('test')
# 执行SQL查询语句
curse.execute('select * from stu')
# 获取所有查询结果
result: tuple = (curse.fetchall())
# 遍历查询结果并打印每一行数据
for row in result:
    print(row)

# 在完成数据库相关操作后，确保关闭数据库连接以释放资源
conn.close()
