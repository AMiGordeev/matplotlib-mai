import numpy as np
import matplotlib.pyplot as plt

# Диаметр сферы
diameter = 0.1

# Диапазон частот
frequencies = np.linspace(1e9, 10e9, 100)

# Расчет ЭПР
wavelengths = (3e8 / frequencies) * 1e-9
rcs = (np.pi * diameter*2 / 4) * (1 - (wavelengths / (np.pi * diameter)))*2

# Построение графика
plt.plot(frequencies / 1e9, rcs)
plt.xlabel('Frequency (GHz)')
plt.ylabel('RCS (m^2)')
plt.title('RCS vs. Frequency')
plt.show()