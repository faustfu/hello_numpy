import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(20) * 8 - 4

y = np.sin(x)+np.random.rand(20)*0.2

omega = np.polyfit(x, y, 3)  # 一元n次方程式
f = np.poly1d(omega)
print(f)

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Using regression analysis and ployfit')

plt.grid()  # start to draw grid

plt.scatter(x, y, marker='*', c='red')

xx = np.linspace(-4, 4, 100)

plt.plot(xx, f(xx), color='green')

plt.show()
