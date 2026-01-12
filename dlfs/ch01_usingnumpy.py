import numpy as np

# 构造 numpy 数组
x = np.array([1.0, 2.0, 3.0])
print(f"numpy 数组：{x}")
print(f"numpy 数组类型：type(x)")
print()

# 使用 numpy 进行算数运算
x = np.array([1.0, 2.0, 3.0])
y = np.array([2.0, 3.0, 4.0])
print(f"numpy 数组：{x}")
print(f"numpy 数组：{y}")
print(f"对应位加法运算：{x + y}") 
print(f"对应位减法运算：{x - y}") 
print(f"对应位相乘运算（不是矩阵乘法）：{x * y}") 
print(f"对应位除法运算：{x / y}") 
print(f"广播运算：{x / 2.0}") 
print()

# 构造 numpy 矩阵
x = np.array([[1.0, 2.0], [3.0, 4.0]])
print(f"numpy 构造矩阵（二维数组）： {x}")
print(f"numpy 矩阵的形状：{x.shape}")
print(f"numpy 矩阵元素的类型：{x.dtype}")
print()

# 使用 numpy 矩阵进行运算
x = np.array([[1.0, 2.0], [3.0, 4.0]])
y = np.array([[2.0, 3.0], [4.0, 5.0]])
print(f"numpy 矩阵：{x}")
print(f"numpy 矩阵：{y}")
print(f"矩阵加法 x + y：{x + y}")
print(f"矩阵乘法 x * y：{x * y}")
print(f"矩阵广播 x * 4：{x * 4}")
print()

# 广播运算，高维的多个低维元素依次与同样shape的低维元素进行算术等运算
x = np.array([[1.0, 2.0], [3.0, 4.0]])
y = np.array([11.0, 12.0])
print(f"numpy 二维数组：{x}")
print(f"numpy 一维数组：{y}")
print(f"x 和 y 的广播运算：{x + y}")