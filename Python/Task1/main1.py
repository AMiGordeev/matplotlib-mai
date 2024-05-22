import os
import numpy as np
import matplotlib.pyplot as plt

# Задаем константу A
A = 10

# Задаем интервал и шаг дискретизации
x_min = -5.12
x_max = 5.12
num_points = 1000
step = (x_max - x_min) / (num_points - 1)

# Создаем массив значений x
x = np.linspace(x_min, x_max, num_points)

# Вычисляем значения функции y
y = A + x**2 - A * np.cos(2 * np.pi * x)

# Создаем директорию results, если ее нет
if not os.path.exists("results"):
    os.mkdir("results")

# Сохраняем результаты в текстовый файл
with open("results/data.txt", "w") as f:
    for i in range(len(x)):
        f.write(f"{x[i]:.4f}   {y[i]:.4f}n")

# Строим график функции
plt.plot(x, y)
plt.title("График функции y = A + x^2 - A cos(2π x)")
plt.xlabel("x")
plt.ylabel("y")
plt.show()