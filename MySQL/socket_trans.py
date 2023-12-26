import socket
from datawrite import insert_data
import re
from sugar import timer

# 创建 socket 对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定到给定的 IP 地址和端口
server_addr = ('192.168.147.103', 9888)
server_socket.bind(server_addr)

# 开始监听传入的连接请求
server_socket.listen(1)
print(f"正在监听端口： {server_addr}")


@timer
def receive():
    # 接受一个连接
    client_socket, client_address = server_socket.accept()
    print(f"连接到： {client_address}")

    # 从客户端接收数据
    data = client_socket.recv(45)
    receive = data.decode()
    print(f"接收: {receive}")
    match = re.search(r"(\d+\.\d+)", receive)
    if match:
        # 将匹配的字符串转换为浮点数
        temperature = float(match.group(1))
        insert_data(114.0, temperature, 65.6, 2.5)
        print(f'温度为：{temperature}°C')
    else:
        print("没有找到温度数据")

    # 发送数据回客户端
    client_socket.sendall(b"received!")

    # 关闭连接
    client_socket.close()
    print(f"连接已关闭")


# 不要忘记在某个时候关闭服务器 socket
# server_socket.close()

while True:
    receive()