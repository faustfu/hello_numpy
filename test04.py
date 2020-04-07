import numpy as np
import matplotlib.pyplot as plt
# ==========================================
# 圓的基本資訊
# 1.圓半徑
r = 2.0
# 2.圓心座標
a, b = (0., 0.)
# ==========================================
# 方法一：引數方程
theta = np.arange(0, 2*np.pi, 0.01)
x = a + r * np.cos(theta)
y = b + r * np.sin(theta)
fig = plt.figure()
axes = fig.add_subplot(111)
axes.plot(x, y)
axes.axis('equal')
plt.title('引數方程')
# ==========================================
# 方法二：標準方程
x = np.arange(a-r, a + r, 0.01)
y = b + np.sqrt(r**2 - (x - a)**2)
fig = plt.figure()
axes = fig.add_subplot(111)
axes.plot(x, y)  # 上半部
axes.plot(x, -y)  # 下半部
plt.axis('equal')
plt.title('標準方程')
# ==========================================
plt.show()
