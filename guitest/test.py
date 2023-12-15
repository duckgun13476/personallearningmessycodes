from nicegui import ui
import threading
import time
from minio_read import read_bucket_size
from weather_read import get__weather

bucket_size = 0
bucket_size_1 = 0


def line_1():
    global bucket_size
    while True:
        bucket_size, bucket_name = read_bucket_size()
        if bucket_size is not None:
            size_label.set_text(f"存储桶：{bucket_name} 已使用： {bucket_size} ")  # 这里放指令
        time.sleep(1)  # 更新频率，这里设置为每30秒更新一次


def update_weather():
    while True:
        time.sleep(18000)  # 更新频率，这里设置为每5h更新一次
        weather_str_out = get__weather()
        weather_info = weather_str_out.replace("\n", "<br>")
        if weather_info is not None:
            weather_label_1.set_content(f"{weather_info}")  # 这里放指令


# 创建 GUI
with ui.element('div').classes('p-2 bg-pink-100'):
    size_label = ui.label('加载数据中...')
    threading.Thread(target=line_1, daemon=True).start()

weather_label_1 = ui.html('加载天气数据中...<br><br><br><br><br><br><br>')
threading.Thread(target=update_weather, daemon=True).start()
ui.run(port=8013)
