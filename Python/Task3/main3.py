import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Определяем функцию
def f(x1, x2):
    return -0.0001 * (np.abs(np.sin(x1) * np.sin(x2) * np.exp(100 - np.sqrt(x1**2 + x2**2) / np.pi)) + 1) + 0.1

# Создаем сетку точек для построения поверхности
x1 = np.linspace(-2.0, 2.0, 50)
x2 = np.linspace(-2.0, 2.0, 50)
X1, X2 = np.meshgrid(x1, x2)
Z = f(X1, X2)

# Создаем фигуру с четырьмя осями
fig = plt.figure(figsize=(12, 8))
ax1 = fig.add_subplot(2, 2, 1, projection='3d')
ax2 = fig.add_subplot(2, 2, 2, projection='3d')
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)

# Построение изометрического вида поверхности
ax1.plot_surface(X1, X2, Z, cmap='jet')
ax1.set_xlabel('x1')
ax1.set_ylabel('x2')
ax1.set_zlabel('f(x1, x2)')
ax1.view_init(30, 45)

# Построение вида сверху поверхности
ax2.plot_surface(X1, X2, Z, cmap='jet')
ax2.set_xlabel('x1')
ax2.set_ylabel('x2')
ax2.set_zlabel('f(x1, x2)')
ax2.view_init(90, 0)

# Построение графика функции y = f(x1) при фиксированном x2
x10 = 1.3491
y = f(x1, x10)
ax3.plot(x1, y)
ax3.set_xlabel('x1')
ax3.set_ylabel('f(x1, x20)')

# Построение графика функции y = f(x2) при фиксированном x1
x20 = 1.3491
y = f(x10, x2)
ax4.plot(x2, y)
ax4.set_xlabel('x2')
ax4.set_ylabel('f(x10, x2)')

plt.show()