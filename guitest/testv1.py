from nicegui import ui
weather='天气如下： \n日期：2023/12/15 星期五 多云 无持续风向微风 温度：22℃~28℃ 东北风3~4级 \n日期：2023/12/16 星期六 多云 东北风3~4级 温度：19℃~28℃ 东北风3~4级 \n日期：2023/12/17 星期日 多云 东北风3~4级 温度：19℃~24℃ 无持续风向微风 \n日期：2023/12/18 星期一 多云 东风3~4级 温度：22℃~26℃ 无持续风向微风 \n日期：2023/12/19 星期二 多云 东风3~4级 温度：22℃~27℃ 东北风3~4级 \n日期：2023/12/20 星期三 多云 东北风3~4级 温度：17℃~25℃ 北风3~4级 \n日期：2023/12/21 星期四 多云 东北风3~4级 温度：18℃~23℃ 东北风4~5级'

print(weather)
weather_info = weather.replace("\n", "<br>")
ui.html(f'{weather_info}')

ui.run(port=2323)
#日期：2023/12/15 星期五 多云 无持续风向微风 温度：22℃~28℃ 东北风3~4级
#————————————————————————————————————————————————————————————————