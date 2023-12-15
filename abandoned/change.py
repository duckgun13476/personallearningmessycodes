from minio import Minio
from minio.error import S3Error
from nicegui import ui
from minio import Minio
from minio.error import S3Error
import threading
import time


#  已弃用


def get_bucket_size(client, bucket_name):
    try:
        objects = client.list_objects(bucket_name)
        total_size = sum(obj.size for obj in objects if obj.size is not None)
        return total_size
    except S3Error as e:
        print("S3 error: ", e)


# 创建 MinIO 客户端实例
client = Minio(
    "192.168.147.107:9500",  # 替换为您的 MinIO 服务器地址
    access_key="uL0hh3dlU2hq5i6ZKXFj",  # 替换为您的 access key
    secret_key="mkWiZt5niwgqZkBRz4I8HZGB8p1gI6fMHrcb39OJ",  # 替换为您的 secret key
    secure=False  # 设置为 True 如果是 HTTPS，否则设置为 False
)

# 获取 bucket 的容量
bucket_name = "usedfor-s-three-test"  # 替换为您要查询的 bucket 名称
bucket_size = get_bucket_size(client, bucket_name)

if bucket_size is not None:
    print(f"Bucket '{bucket_name}' size: {bucket_size} bytes")
# 2340899
bucket_size = 0
bucket_size_1 = 0


def update_bucket_size():
    global bucket_size
    while True:
        bucket_size = bucket_size + 1
        if bucket_size is not None:
            size_label.set_text(f"Bucket Size: {bucket_size} bytes")
        time.sleep(3)  # 更新频率，这里设置为每30秒更新一次


def update_bucket_size_1():
    global bucket_size_1
    while True:
        bucket_size_1 = bucket_size_1 + 1
        if bucket_size is not None:
            size_label_1.set_text(f"Bucket Size_2: {bucket_size_1} bytes")
        time.sleep(0.5)  # 更新频率，这里设置为每0.5秒更新一次


# 创建 GUI
size_label = ui.label('Loading bucket size...')
threading.Thread(target=update_bucket_size, daemon=True).start()
size_label_1 = ui.label('Loading bucket size...')
threading.Thread(target=update_bucket_size_1, daemon=True).start()

ui.label('外网访问链接')
with ui.row():
    with ui.element('div').classes('p-2 bg-blue-100'):
        with ui.link('这是百度的链接', 'https://www.baidu.com/'):
            ui.tooltip('点此以访问百度').classes('bg-black')
    with ui.element('div').classes('p-2 bg-blue-100'):
        with ui.link('这是媒体服务器的链接', 'https://aichangeworld.tech:1801/'):
            ui.tooltip('点此以访问媒体服务器').classes('bg-black')
    with ui.element('div').classes('p-2 bg-blue-100'):
        with ui.link('服务器管理登录界面', 'https://aichangeworld.tech:1800/'):
            ui.tooltip('点此以访问DSM').classes('bg-black')
# 启动 GUI
ui.run(port=7882)
