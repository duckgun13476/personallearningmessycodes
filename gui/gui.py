from nicegui import ui
import threading
import time
from bin.minio_read import read_bucket_size
from bin.weather_read import get__weather


##################################################################################################################
#  参数更新
def read_bucket_size_f():  # 更新minio的文件大小
    while True:
        bucket_size, bucket_name = read_bucket_size()
        if bucket_size is not None:
            bucket_size_show.set_text(f"存储桶已使用： {bucket_size} ")  # 这里放指令
            bucket_name_show.set_text(f"存储桶名：{bucket_name}")
        time.sleep(3)  # 更新频率，这里设置为每3秒更新一次


def update_weather():  # 更新今日天气
    while True:
        time.sleep(7200)  # 更新频率，这里设置为每2h更新一次
        weather_str_out = get__weather()
        weather_info = weather_str_out.replace("\n", "<br>")
        if weather_info is not None:
            weather_label_1.set_content(f"{weather_info}")  # 这里放指令


###################################################################################################################
#  主界面
if __name__ in {"__main__", "__mp_main__"}:
    with ui.row():
        ui.label("                  ")
        ui.markdown('           <font size="7">**导航页面**</font>')
    ui.separator()

    with ui.element('div').classes('p-2 bg-pink-100'):
        bucket_name_show = ui.tooltip('正在读取存储桶名称...').classes('bg-purple')
        bucket_size_show = ui.label('正在读取数据：')
        threading.Thread(target=read_bucket_size_f, daemon=True).start()  # bucket_size_show的参数更新

    with ui.row():
        with ui.element('div').classes('p-2 bg-red-100'):
            with ui.link('这是minio的链接', 'http://192.168.147.107:9501/'):
                ui.tooltip('点此以访问minio').classes('bg-black')
        with ui.element('div').classes('p-2 bg-yellow-100'):
            with ui.link('这是媒体服务器的链接', 'https://192.168.147.107:8097/'):
                ui.tooltip('点此以访问媒体服务器').classes('bg-black')
        with ui.element('div').classes('p-2 bg-blue-100'):
            with ui.link('服务器管理登录界面', 'https://192.168.147.107:5002/'):
                ui.tooltip('点此以访问DSM').classes('bg-black')
        with ui.element('div').classes('p-2 bg-blue-100'):
            with ui.link('百度', 'https://www.baidu.com/'):
                ui.tooltip('点此以访问百度').classes('bg-black')
        with ui.element('div').classes('p-2 bg-yellow-100'):
            with ui.link('github', 'https://github.com/'):
                ui.tooltip('点此以访问github').classes('bg-black')
        with ui.element('div').classes('p-2 bg-purple-100'):
            with ui.link('google翻译', 'https://translate.google.com/'):
                ui.tooltip('点此以访问google翻译').classes('bg-black')
        with ui.element('div').classes('p-2 bg-blue-100'):
            with ui.link('ipinfo', 'https://ipinfo.io/'):
                ui.tooltip('点此以访问ipinfo').classes('bg-black')
        with ui.element('div').classes('p-2 bg-orange-100'):
            with ui.link('YouTube', 'https: // www.youtube.com /'):
                ui.tooltip('点此以访问YouTube').classes('bg-black')
        with ui.element('div').classes('p-2 bg-yellow-100'):
            with ui.link('牛津词典', 'https://oalecd10.cp.com.cn/'):
                ui.tooltip('点此以访问牛津词典').classes('bg-black')
        with ui.element('div').classes('p-2 bg-blue-100'):
            with ui.link('merriam', 'https://www.merriam-webster.com/'):
                ui.tooltip('点此以访问merriam').classes('bg-black')
        with ui.element('div').classes('p-2 bg-pink-100'):
            with ui.link('IP2world', 'https://www.ip2world.com/'):
                ui.tooltip('点此以访问IP2world').classes('bg-black')
    with ui.row():
        with ui.element('div').classes('p-2 bg-orange-100'):
            with ui.link('X', 'https://twitter.com/'):
                ui.tooltip('点此以访问X').classes('bg-black')
        with ui.element('div').classes('p-2 bg-red-100'):
            with ui.link('netflix', 'https://www.netflix.com/'):
                ui.tooltip('点此以访问netflix').classes('bg-black')
        with ui.element('div').classes('p-2 bg-blue-100'):
            with ui.link('网易见外工作台', 'https://jianwai.youdao.com/'):
                ui.tooltip('点此以访问网易见外工作台').classes('bg-black')
        with ui.element('div').classes('p-2 bg-red-100'):
            with ui.link('易贝', 'https://www.ebay.com/'):
                ui.tooltip('点此以访问易贝').classes('bg-black')
        with ui.element('div').classes('p-2 bg-pink-100'):
            with ui.link('openai(ChatGPT)', 'https://openai.com/'):
                ui.tooltip('点此以访问openai').classes('bg-black')
        with ui.element('div').classes('p-2 bg-blue-100'):
            with ui.link('paypal', 'https://www.paypal.com/'):
                ui.tooltip('点此以访问paypal').classes('bg-black')
        with ui.element('div').classes('p-2 bg-blue-100'):
            with ui.link('欧易)', 'https://www.okx.com/'):
                ui.tooltip('点此以访问欧易').classes('bg-black')
        with ui.element('div').classes('p-2 bg-green-100'):
            with ui.link('nobepay', 'https://www.nobepay.com/'):
                ui.tooltip('点此以访问nobepay').classes('bg-black')
        with ui.element('div').classes('p-2 bg-purple-100'):
            with ui.link('cloudflare', 'https://www.cloudflare.com/'):
                ui.tooltip('点此以访问cloudflare').classes('bg-black')

        with ui.expansion('外网无法访问？', icon='work').classes('w-full'):
            ui.label('外网访问链接')
            with ui.row():
                with ui.element('div').classes('p-2 bg-blue-100'):
                    with ui.link('这是媒体服务器的链接', 'https://aichangeworld.tech:1801/'):
                        ui.tooltip('点此以访问媒体服务器').classes('bg-black')
                with ui.element('div').classes('p-2 bg-blue-100'):
                    with ui.link('服务器管理登录界面', 'https://aichangeworld.tech:1800/'):
                        ui.tooltip('点此以访问DSM').classes('bg-black')
        #########################################################################################################
        ui.separator()
        with ui.row():
            with ui.element('div').classes('p-2 bg-pink-100'):
                ui.tooltip('这里会更新服务器所在地的天气哦').classes('bg-blue')
                weather_label_1 = ui.html('加载天气数据中...<br'
                                          '>|————————————————————————————————————————————————————————————————<br'
                                          '>|————————————————————————————————————————————————————————————————<br'
                                          '>|————————————————————————————————————————————————————————————————<br'
                                          '>|————————————————————————————————————————————————————————————————<br'
                                          '>|————————————————————————————————————————————————————————————————<br'
                                          '>|————————————————————————————————————————————————————————————————<br'
                                          '>|————————————————————————————————————————————————————————————————')

                threading.Thread(target=update_weather, daemon=True).start()
            with ui.mermaid('''
            graph LR;
                A --> B;C --> D;
                A --> C;E --> B;
                B --> A;C --> F;
                B --> C;A --> E;
                C --> A;C --> B;
            '''):
                ui.tooltip('这只是个简单的图表').classes('bg-blue')

    ui.separator()
    with ui.tabs().classes('w-full') as tabs:
        one = ui.tab('变量')
        two = ui.tab('？？？')
        three = ui.tab('主题')
    with ui.tab_panels(tabs, value=one).classes('w-full'):
        with ui.tab_panel(one):
            with ui.element('div').classes('p-2 bg-pink-100'):
                ui.label('变量标题')
            toggle1 = ui.toggle([1, 2, 3, 4, 8456], value=1)
            toggle2 = ui.toggle({1: 'A', 2: 'B', 3: 'C', 4: 'line', 8456: 'ASW'}).bind_value(toggle1, 'value')

        with ui.tab_panel(two):
            with ui.element('div').classes('p-2 bg-white-100'):
                ui.label('奇怪的地方')
            pa = 0


            def click_res():
                global pa
                badge.set_text(f'{pa}')
                pa = pa + 1


            with ui.dialog() as dialog2, ui.card():
                ui.label('~~~~~~~喵喵~~~！')
                ui.button('关闭', on_click=dialog2.close)

            with ui.dialog() as dialog3, ui.card():
                ui.label('~~~~~~~┗|｀O′|┛ 嗷！！！！！~~~~~！')
                ui.button('关闭', on_click=dialog3.close)

            with ui.button('点我!', on_click=lambda: click_res()):
                badge = ui.badge(f'{pa}', color='green').props('floating')

            with ui.dialog() as dialog1, ui.card():
                ui.label('不知道从哪里出现的小猫，它炸毛了，你应该？')
                with ui.row():
                    with ui.button('~抚摸~', on_click=dialog2.open):
                        ui.tooltip('摸摸~').classes('bg-green')
                    with ui.button('踢一脚', on_click=dialog3.open):
                        ui.tooltip('这可能不是个好选择').classes('bg-red')
                    ui.button('悄悄离开~', on_click=dialog1.close)

            with ui.button('看看这是什么？', on_click=dialog1.open):
                ui.tooltip('请不要点它').classes('bg-red')

        with ui.tab_panel(three):
            with ui.row():
                dark = ui.dark_mode()
                with ui.element('div').classes('p-2 bg-blue-100'):
                    ui.label('选择模式')
                ui.button('Dark', on_click=dark.enable)
                ui.button('Light', on_click=dark.disable)
            with ui.row():
                def set_background(color: str) -> None:
                    ui.query('body').style(f'background-color: {color}')


                with ui.element('div').classes('p-2 bg-blue-100'):
                    ui.label('背景')
                ui.button('浅蓝色', on_click=lambda: set_background('#ddeeff'))
                ui.button('浅橙色', on_click=lambda: set_background('#ffeedd'))
            with ui.row():
                with ui.element('div').classes('p-2 bg-blue-100'):
                    ui.label("ui颜色")
                ui.button('Default', on_click=lambda: ui.colors())
                ui.button('Gray', on_click=lambda: ui.colors(primary='#555'))
    with ui.row():
        with ui.button(icon='thumb_up', color='pink', on_click=lambda: ui.notify('感谢支持！', close_button='关闭')):
            ui.tooltip('我喜欢这个页面').classes('bg-green')
        with ui.button(icon='thumb_down', color='white',
                       on_click=lambda: ui.notify('我会努力的！', close_button='关闭')):
            ui.tooltip('我不喜欢这个页面').classes('bg-red')
    with ui.label('这里已经到底啦！'):
        ui.tooltip('~~喵~~').classes('bg-purple')

    # 启动 GUI
    ui.run(port=8012)
