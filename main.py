# 这是一个示例 Python 脚本。
# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
from sugar import *


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


@timer
def hello():
    print(f"hello,world!")


@memoize
@timer
@debug
def hello_n():
    for i in range(0, 10):
        hello()


@timer
def sum_1():
    i = 13
    for j in range(0, 8000000):
        i = i + 10


@timer
@memoize
def sum_2():
    i = 13
    for j in range(0, 8000000):
        i = i + 10


# 按装订区域中的绿色按钮以运行脚本。

if __name__ == '__main__':
    print_hi('PyCharm')

    sum_1()
    sum_2()
