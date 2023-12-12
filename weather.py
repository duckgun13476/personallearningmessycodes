import urllib.request
import re
from sugar import *


@timer
def get_html(url):
    # 发送HTTP请求获取页面内容
    response = urllib.request.urlopen(url)
    html_content_1 = response.read().decode('utf-8')
    return html_content_1


def handle_weather(html_content_2):
    date = r' 7天天气预报（(.*?)发布）(.*?)<table class="hour-table" id="hourTable_0" style="">'
    matches = re.findall(date, html_content_2, re.DOTALL)

    date1 = (r'星期(.*?)\n         <br>(.*?)\n        </div> \n        <div class="day-item dayicon">\n         (.*?)\n '
             r'       </div> \n        <div class="day-item">\n         (.*?)\n        </div> \n        <div '
             r'class="day-item">\n         (.*?)\n        </div> \n        <div class="day-item">\n         (.*?)\n  '
             r'      </div> \n        <div class="day-item bardiv">\n         (.*?)\n          <div class="high">\n  '
             r'         (.*?)\n          </div>\n          <div class="low">\n           (.*?)\n          </div>\n   '
             r'      </div>\n        </div> \n        <div class="day-item nighticon">\n         (.*?)\n        '
             r'</div> \n        <div class="day-item">\n         (.*?)\n        </div> \n        <div '
             r'class="day-item">\n         (.*?)\n        </div> \n        <div class="day-item">\n         (.*?)\n  '
             r'      </div> \n       </div> \n')
    matches1 = re.findall(date1, str(matches[0][1]), re.DOTALL)
    print(f'天气如下：')
    for match in matches1:
        day = match[0]
        date = match[1]
        weather = match[3]
        wind = match[4]
        wave = match[5]
        high_temp = match[7]
        low_temp = match[8]
        unknown = match[11]
        wave_speed = match[12]
        print(
            f"日期：2023/{date}  星期{day}  {weather} {wind}{wave}     温度：{low_temp}~{high_temp} {unknown}{wave_speed}")


url = 'https://weather.cma.cn/web/weather/59948.html'
html_content = get_html(url)
handle_weather(html_content)
try:
    a = a + 1
except :
    print(f"error")
