from nicegui import ui
if __name__ == '__main__':
    ui.label('你好 nicegui!')
    ui.link('这是百度的链接', 'https://www.baidu.com/')
    ui.button('点我速度！', on_click=lambda: ui.notify('你点我了！'))

    with ui.element('div').classes('p-2 bg-blue-100'):
        ui.label('在颜色框内')

    ui.markdown('This is **Markdown**， <table><tr><td bgcolor=#54FF9F>墨绿色</td></tr></table><font color="#00dd00">浅绿色')

    ui.mermaid('''
    graph LR;
        A --> B;
        A --> C;
        B --> A;
        B --> A;
    ''')

    with ui.button('点我!', on_click=lambda: badge.set_text(int(badge.text) + 1)):
        badge = ui.badge('0', color='green').props('floating')

    toggle1 = ui.toggle([1, 2, 3, 4, 8456], value=1)
    toggle2 = ui.toggle({1: 'A', 2: 'B', 3: 'C',8456: 'ASW'}).bind_value(toggle1, 'value')

    ui.run(port=8012)
