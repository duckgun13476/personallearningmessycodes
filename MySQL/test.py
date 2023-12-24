import pymysql

# 此代码用于测试sql数据能否正常工作
host = '192.168.147.107'  # 或者远程服务器的 IP 地址
port = 3345
user = 'root'
password = '123456'  # 您在 docker run 命令中设置的密码
db = 'mysql'  # 使用默认的系统数据库进行测试

try:
    connection = pymysql.connect(host=host, port=port, user=user, password=password, db=db)
    print("数据库连接成功")
except Exception as e:
    print(f"数据库连接失败: {e}")
# finally:
# if connection:
#  connection.close()
