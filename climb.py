import urllib.request
import re

def get_quotes(url):
    # 发送HTTP请求获取页面内容
    response = urllib.request.urlopen(url)
    html_content = response.read().decode('utf-8')

    # 使用正则表达式提取名言信息
    pattern = r'<span class="text" itemprop="text">(.*?)</span>\
    .*?<small class="author" itemprop="author">(.*?)</small>'
    search = r'value="AAH" data-aid="34"> (.*?)', '<input'
    pattern1 = r'<input type="checkbox" value="ANX" data-aid="64">(.*?)</label>'
    pattern2 = r'<label>(.*?)</label>'
    matches = re.findall(pattern, html_content, re.DOTALL)
    matches_1 = re.findall(pattern1, html_content, re.DOTALL)
    matches_2 = re.findall(pattern2,html_content,re.DOTALL)
    tre = str(matches_2)
    matches_3 = re.findall(search, tre , re.DOTALL)
    # 打印名言信息
    for match in matches:
        quote = match[0]
        author = match[1]
        print(f'名言: {quote}\n作者: {author}\n')


url = 'https://weather.cma.cn/'
get_quotes(url)
