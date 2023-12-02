import numpy as np

# 输入长度

Input = np.random.rand(5)  # 输入

line_in = Input.shape[0]
line_out = 4

# 参数转移
if 1 == 1:
    a = line_in
    b = line_out

# 主函数
X = Input  # 输入
W = np.random.rand(b, a)  # 权重
B = np.random.rand(b)  # 偏置


class Affine:
    def __init__(self, W, B):
        self.W = W
        self.B = B
        self.X = None
        self.dW = None
        self.dB = None

    def forward(self, X):
        self.X = X
        out = np.dot(self.W, X) + self.B
        return out

    def backward(self, dout):
        dX = np.dot(self.W.T, dout)
        # self.dW = np.dot(self.X.T, dout)
        self.dB = np.sum(dout, axis=0)
        return dX


if __name__ == '__main__':
    # Y = np.dot(X, W) + B  # 输出
    afln = Affine(W, B)
    print(np.around(X, 3))

    X1 = afln.forward(X)

    XZ = np.random.rand(b)
    X2 = afln.backward(XZ)

    print(np.around(X1, 3))  # 保留三位小数
    print(np.around(XZ, 3))
    print(np.around(X2, 3))
    # print(X, W, B)
