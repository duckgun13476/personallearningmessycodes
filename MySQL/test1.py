import mysql.connector

# 创建数据库连接
conn = mysql.connector.connect(
    host="192.168.147.107",  # 例如 "localhost"
    port="3345",
    user="root",
    password="123456",
    # database="数据库名"
)

# 创建一个cursor对象来执行SQL语句
cursor = conn.cursor()

# SQL语句

sql = "show databases"  # 例如 "SELECT * FROM table_name"

# 执行SQL语句
cursor.execute(sql)

# 获取查询结果
result = cursor.fetchall()

# 打印结果
for row in result:
    print(row)

# 关闭cursor和连接
cursor.close()
conn.close()
