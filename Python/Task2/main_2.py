import matplotlib.pyplot as plt
import argparse

# Создаем парсер аргументов командной строки
parser = argparse.ArgumentParser(description='Построение графика y = f(x) по данным из текстового файла.')
parser.add_argument('input_file', help='Имя входного файла с данными x и f(x).')
parser.add_argument('--xmin', type=float, help='Минимальное значение x для графика.')
parser.add_argument('--xmax', type=float, help='Максимальное значение x для графика.')
parser.add_argument('--xlabel', help='Подпись оси X.')
parser.add_argument('--ylabel', help='Подпись оси Y.')
parser.add_argument('--title', help='Заголовок графика.')
parser.add_argument('--output_file', help='Имя выходного файла (по умолчанию: plot.txt).')

# Парсим аргументы командной строки
args = parser.parse_args()

# Считываем данные из входного файла
with open(args.input_file) as f:
    data = [line.strip().split('    ') for line in f]
x = [float(x) for x, y in data]
y = [float(y) for x, y in data]

# Создаем график
fig, ax = plt.subplots()
ax.plot(x, y)

# Устанавливаем подписи осей и заголовок
if args.xmin and args.xmax:
    ax.set_xlim([args.xmin, args.xmax])
if args.xlabel:
    ax.set_xlabel(args.xlabel)
if args.ylabel:
    ax.set_ylabel(args.ylabel)
if args.title:
    plt.title(args.title)

# Сохраняем график в файл
output_file = args.output_file or 'plot.png'
plt.savefig(output_file)

# Выводим сообщение в консоль
print(f'График сохранен в файл {output_file}')