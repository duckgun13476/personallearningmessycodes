import numpy as np


class Relu:
    def __init__(self):
        self.mask = None

    def forward(self, x_1):
        self.mask = (x_1 <= 0)
        se2_out = x_1.copy()
        se2_out[self.mask] = 0
        return se2_out

    def backward(self, dout_1):
        dout_1[self.mask] = 0
        dx_1 = dout_1
        return dx_1


# 创建实例
relu = Relu()

# 模拟一些输入数据
x = np.array([-1, 0, 1, 2])
print(x)
# 前向传播
out = relu.forward(x)
print("Forward:", out)

# 模拟上游梯度
dout = np.array([1, 2, 3, 4])

# 反向传播
dx = relu.backward(dout)
print("Backward:", dx)
