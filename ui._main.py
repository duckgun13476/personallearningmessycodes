from nicegui import ui
from random import random

chart = ui.highchart({
    'title': False,
    'chart': {'type': 'bar'},
    'xAxis': {'categories': ['A', 'B']},
    'series': [
        {'name': 'Alpha', 'data': [0.1, 0.2]},
        {'name': 'Beta', 'data': [0.3, 0.4]},
    ],
}).classes('w-full h-64')


def update():
    chart.options['series'][0]['data'][0] = random()
    chart.update()


with ui.row():
    ui.button('Update', on_click=update)
    ui.button('点我速度！', on_click=lambda: ui.notify('你点我了！'))
##################################################################################
with ui.row():
    toggle1 = ui.toggle([1, 2, 3, 4, 8456], value=1)
    toggle2 = ui.toggle({1: 'A', 2: 'B', 3: 'C', 8456: 'ASW'}).bind_value(toggle1, 'value')
    ui.spinner('dots', size='lg', color='red')
#####################################################################################
with ui.row():
    checkbox = ui.checkbox('check me')
    ui.label('Check!').bind_visibility_from(checkbox, 'value')
###############################################################################
with ui.row():
    switch = ui.switch('switch me')
    ui.label('Switch!').bind_visibility_from(switch, 'value')

ui.input(label='Text', placeholder='start typing',
         on_change=lambda e: result.set_text('you typed: ' + e.value),
         validation={'Input too long': lambda value: len(value) < 20})
result = ui.label()


ui.run(port=7564)
