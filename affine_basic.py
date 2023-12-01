import numpy as np

# 输入长度
line_in = 2
line_out = 3

# 参数转移
if 1 == 1:
    a = line_in
    b = line_out

# 主函数
X = np.random.rand(a)  # 输入
W = np.random.rand(a, b)  # 权重
B = np.random.rand(b)  # 偏置


class Affine:
    def __init__(self):
        self.W = W
        self.B = B
        self.X = X
        self.dW = None
        self.dB = None


Y = np.dot(X, W) + B  # 输出

print(X, W, B)
print(Y)
