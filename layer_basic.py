import numpy as np


class LayerBasic:
    def __init__(self):
        self.x = None
        self.y = None

    def forward_multiplication(self, x, y):
        self.x = x
        self.y = y
        return x * y
    # 乘法正向传播↑

    def backward_multiplication(self, out):
        dx = self.y * out
        dy = self.x * out
        return dy, dx
    # 乘法反向传播↑

    def forward_add(self, x, y):
        out = x + y
        return out
    # 加法正向传播↑

    def backward_add(self, out):
        return out
    # 加法反向传播↑


class Sigmoid:
    def __init__(self):
        self.out = None

    def forward(self, x):
        out = 1 / (1 + np.exp(-x))
        self.out = out
        return out
    # 前向传播 输入x 输出y  ↑

    def backward(self,dout):
        dx = dout * (1.0-self.out)*self.out
        return dx
    # 前向传播 输入dL/dy 输出y(1-y)*dL/dy  # ↑
    # 即得到其输出的变化率对于输入变化率的影响，即变量反向传播后的输入值变化量

if __name__ == '__main__':
    print("start!")

    apple = 100
    apple_number = 2
    tax = 1.2

    all_price = 1

    # 层init  参数传递
    apple_layer = LayerBasic()
    appletax_layer = LayerBasic()
    test_layer = Sigmoid()

    # 正向传播
    layer1 = apple_layer.forward_multiplication(apple_number, apple)
    layer2 = appletax_layer.forward_multiplication(layer1, tax)
    print(int(layer2))

    # 反向传播
    layer2_1, layer2_2 = appletax_layer.backward_multiplication(all_price)
    print(layer2_1, layer2_2)
    layer1_1, layer1_2 = apple_layer.backward_multiplication(layer2_2)
    print(layer1_1, layer1_2)

    # sigmoid函数正反传播
    out = test_layer.forward(0)
    dout = test_layer.backward(10)
    print(out,dout)

    print("ended!")
