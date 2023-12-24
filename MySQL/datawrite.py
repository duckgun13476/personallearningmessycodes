import mysql.connector


def insert_data(preasure, temperature, wet, wave):
    try:
        # 创建数据库连接
        conn = mysql.connector.connect(
            host="192.168.147.107",
            port="3345",
            user="root",
            password="123456",
            database="tempdata"
        )

        # 创建一个cursor对象来执行SQL语句
        cursor = conn.cursor()

        # 准备SQL插入语句
        sql = """
        INSERT INTO datasavelist (preasure, temperature, wet, wave)
        VALUES (%s, %s, %s, %s)
        """

        # 执行SQL语句
        cursor.execute(sql, (preasure, temperature, wet, wave))

        # 提交到数据库执行
        conn.commit()

        # 插入成功消息
        print("数据成功插入")

    except mysql.connector.Error as err:
        # 返回错误消息
        print(f"错误: {err}")

    finally:
        # 关闭cursor和连接
        if conn.is_connected():
            cursor.close()
            conn.close()


# 调用函数示例
if __name__ == '__main__':
    insert_data(114.0, 27.5, 65.6, 2.5)
