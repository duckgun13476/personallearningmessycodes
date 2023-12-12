from nicegui import ui

if __name__ in {"__main__", "__mp_main__"}:
    with ui.row():
        ui.label("                  ")
        ui.markdown('           <font size="7">**导航页面**</font>')
    ui.separator()
    ui.link('这是百度的链接', 'https://www.baidu.com/')
    ui.button('点我速度！', on_click=lambda: ui.notify('你点我了！'))
    with ui.row():
        with ui.element('div').classes('p-2 bg-blue-100'):
            with ui.link('这是minio的链接', 'http://192.168.147.107:9501/'):
                ui.tooltip('点此以访问minio').classes('bg-black')
        with ui.element('div').classes('p-2 bg-blue-100'):
            with ui.link('这是媒体服务器的链接', 'https://192.168.147.107:8097/'):
                ui.tooltip('点此以访问媒体服务器').classes('bg-black')
        with ui.element('div').classes('p-2 bg-blue-100'):
            with ui.link('服务器管理登录界面', 'https://192.168.147.107:5002/'):
                ui.tooltip('点此以访问DSM').classes('bg-black')
        with ui.expansion('外网无法访问？', icon='work').classes('w-full'):
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
        #####################################################################################
        ui.separator()
        with ui.splitter() as splitter:
            with splitter.before:
                ui.mermaid('''
                graph LR;
                    A --> B;
                    A --> C;
                    B --> A;
                    B --> A;
                ''')
            with splitter.after:
                ui.label('This is some content on the right hand side.').classes('ml-2')

    with ui.tabs().classes('w-full') as tabs:
        one = ui.tab('变量')
        two = ui.tab('？？？')
        three = ui.tab('主题')
    with ui.tab_panels(tabs, value=one).classes('w-full'):
        with ui.tab_panel(one):
            with ui.element('div').classes('p-2 bg-pink-100'):
                ui.label('变量标题')
            toggle1 = ui.toggle([1, 2, 3, 4, 8456], value=1)
            toggle2 = ui.toggle({1: 'A', 2: 'B', 3: 'C', 8456: 'ASW'}).bind_value(toggle1, 'value')

        with ui.tab_panel(two):
            with ui.element('div').classes('p-2 bg-white-100'):
                ui.label('奇怪的地方')
            with ui.button('点我!', on_click=lambda: badge.set_text(int(badge.text) + 1)):
                badge = ui.badge('0', color='green').props('floating')
            with ui.dialog() as dialog1, ui.card():
                ui.label('不知道从哪里出现的小猫，它炸毛了，你应该？')
                ui.button('~抚摸~', on_click=dialog1.close)

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
    ui.run(port=8012)
