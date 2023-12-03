import numpy as np


def double_1(x):
    y = 2 * x
    return y


class LayerBasic:
    def __init__(self):
        self.x = None
        self.y = None
        self.out = None

    def forward_multiplication(self, x, y):
        self.x = x
        self.y = y
        return x * y

    # 乘法正向传播↑

    def backward_multiplication(self, out_2):
        dx = self.y * out_2
        dy = self.x * out_2
        return dy, dx

    # 乘法反向传播↑

    def forward_add(self, x, y):
        self.x = x
        self.y = y
        se3_out = self.x + self.y
        return se3_out

    # 加法正向传播↑

    def backward_add(self, out_3):
        self.out = out_3
        return self.out
    # 加法反向传播↑


class Affine:
    def __init__(self, W, B):
        self.W = W
        self.B = B
        self.X = None
        self.dW = None
        self.dB = None

    def forward(self, X):
        self.X = X
        out_4 = np.dot(self.W, X) + self.B
        return out_4

    def backward(self, dout_1):
        dx = np.dot(self.W.T, dout_1)
        # self.dW = np.dot(self.X.T, dout)
        self.dB = np.sum(dout_1, axis=0)
        return dx


class Relu:
    def __init__(self):
        self.mask = None

    def forward(self, x):
        self.mask = (x <= 0)
        se2_out = x.copy()
        se2_out[self.mask] = 0
        return se2_out

    def backward(self, dout_5):
        dout_5[self.mask] = 0
        dx = dout_5
        return dx


class Sigmoid:
    def __init__(self):
        self.out = None

    def forward(self, x):
        se1_out = 1 / (1 + np.exp(-x))
        self.out = se1_out
        return se1_out

    # 前向传播 输入x 输出y  ↑

    def backward(self, dout_6):
        dx = dout_6 * (1.0 - self.out) * self.out
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
    print(out, dout)

    # Rulu层正反传播
    XR = np.array([-1, -2, 0, 3, 4])
    print(XR)
    Rulu_1 = Relu()
    out = Rulu_1.forward(XR)
    dout = Rulu_1.backward(XR)
    print(out, dout)
    print("ended!")
