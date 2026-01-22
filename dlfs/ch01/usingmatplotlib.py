import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread

# 简单地画出sin函数图像
x = np.arange(0, 6, 0.1)
y = np.sin(x)
# plt.plot(x, y)
# plt.show()

# 同时画出cos函数图像
y_cos = np.cos(x)
plt.plot(x, y, label='sin')
plt.plot(x, y_cos, linestyle='--', label='cos')
plt.xlabel('x')
plt.ylabel('y')
plt.title('sin & cos')
plt.legend()
# plt.show()

# 画出图像
# 注意当前目录和脚本所在目录的区别
# 当前目录：python执行脚本所在的目录
# 脚本目录：与python执行目录无关
import os
# 这个python 执行时目录
# path = os.getcwd()
# print(path)
img = imread(path + "wallhaven.jpg")
plt.imshow(img)
plt.show()