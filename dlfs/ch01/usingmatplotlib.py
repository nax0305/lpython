import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as imread

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
img = imread("wallhaven.jpg")
plt.imshow(img)
plt.show()