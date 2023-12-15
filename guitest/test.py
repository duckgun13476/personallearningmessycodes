from nicegui import ui
import threading
import time
from minio_read import read_bucket_size

bucket_size = 0
bucket_size_1 = 0


def line_1():
    global bucket_size
    while True:
        bucket_size, bucket_name = read_bucket_size()
        if bucket_size is not None:
            size_label.set_text(f"存储桶：{bucket_name} 已使用： {bucket_size} ")  # 这里放指令
        time.sleep(1)  # 更新频率，这里设置为每30秒更新一次


def update_bucket_size_1():
    global bucket_size_1
    while True:
        bucket_size_1 = bucket_size_1 + 1
        if bucket_size is not None:
            size_label_1.set_text(f"线程2: {bucket_size_1} bytes")  # 这里放指令
        time.sleep(0.5)  # 更新频率，这里设置为每0.5秒更新一次


# 创建 GUI
size_label = ui.label('加载数据中...')
threading.Thread(target=line_1, daemon=True).start()
size_label_1 = ui.label('加载数据中...')
threading.Thread(target=update_bucket_size_1, daemon=True).start()
ui.run(port=8013)
