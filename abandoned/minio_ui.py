from nicegui import ui
from minio import Minio
from minio.error import S3Error
import threading
import time
from queue import Queue
from threading import Thread


# 创建一个队列用于线程间通信
update_queue = Queue()

# MinIO 客户端配置
client = Minio(
    "192.168.147.107:9500",
    access_key="uL0hh3dlU2hq5i6ZKXFj",
    secret_key="mkWiZt5niwgqZkBRz4I8HZGB8p1gI6fMHrcb39OJ",
    secure=False
)


def get_bucket_size(client, bucket_name):
    try:
        objects = client.list_objects(bucket_name)
        total_size = sum(obj.size for obj in objects if obj.size is not None)
        return total_size
    except S3Error as e:
        print("S3 error: ", e)
        return None


def format_size(size_bytes):
    if size_bytes < 1024:
        return f"{size_bytes} bytes"
    elif size_bytes < 1024 ** 2:
        return f"{size_bytes / 1024:.3f} KB"
    elif size_bytes < 1024 ** 3:
        return f"{size_bytes / 1024 ** 2:.3f} MB"
    else:
        return f"{size_bytes / 1024 ** 3:.3f} GB"


def update_bucket_size():
    while True:
        bucket_size = get_bucket_size(client, "usedfor-s-three-test")
        if bucket_size is not None:
            formatted_size = format_size(bucket_size)
            update_queue.put(formatted_size)
        time.sleep(30)  # 更新频率，这里设置为每30秒更新一次



