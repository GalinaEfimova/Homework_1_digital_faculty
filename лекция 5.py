# # Используется матплотлиб:
# # 1. сценарий
# # 2. командная оболочка IPython
# # 3. Jupyter


# # 1
# # plt.show() - запускается только один раз, все изображается в одном окне, но можно разделить при необходимости
# # создается объект Figure, ищутся все активные объекты фигуры и создается в окнах графика


import matplotlib.pyplot as plt
import numpy as np

# x = np.linspace(0,10,100)

# fig = plt.figure()

# plt.plot(x, np.sin(x))
# plt.plot(x, np.tan(x))

# plt.show() #смотрит на то, что было до запуска. т.е косинус который ниже задан, уже отображаться не будет
# plt.plot(x, np.cos(x))




# # IPython
# # %matplotlib
# # import matplotlib.pyplot as plt
# # plt.plot(...)




# # Jupyter
# # %matplotlib inline - в блокнот добавляется статическая картинка
# # %matplotlib notebook - графики будут интерактивные

# fig.savefig('saved_images.png') # сохраняется картинка

# print(fig.canvas.get_supported_filetypes()) #получение типов файлов и их расшифровка


# два способа вывода графиков
# - MATLAB-подобный стиль. зависит от последовательности строчек кода
# - в ОО(объектно-ориентированный) стиле

# x = np.linspace(0, 10, 100)

# 1
# plt.figure()

# plt.subplot(2, 1, 1)# в верхней части полотно создается
# plt.plot(x, np.sin(x))
# plt.subplot(2, 1, 2)#в нижней части полотно создается
# plt.plot(x, np.cos(x))


# 2
# fig: Figure - контейнер, который содержит объекты(системы координат, метки), ax:Axes - система координат - прямоугольник с метками, делениями и т.д.
# fig = plt.figure()
# ax = plt.axes()

# цвета линий color
# - 'blue'
# - 'rgbcmyk' -> 'rg'
#  - '0.14' - градация серого
# - RRGGBB - 'FF00EE'
# - RGB - (1.0, 0.2, 0.3)
#  - HTML - 'salmon'

# стиль линии linestyle
# - сплошная линия '-' or 'solid'
# - штриховая линия '--' or 'dashed'
#  - штрих-пунктирная '-.' or 'dashdot'
#  - пунктирная линия ':' or 'dotted'

# ax.plot(x, np.sin(x), color = 'blue', linestyle = 'dashed')
# ax.plot(x, np.sin(x-1), color = 'g', linestyle = 'dotted')

# x = np.linspace(0, 10, 100)
# fix, ax = plt.subplots(4)

# ax[0].plot(x, np.sin(x))
# ax[1].plot(x, np.sin(x))
# ax[2].plot(x, np.sin(x))
# ax[3].plot(x, np.sin(x))

# ax[1].set_xlim(-2, 12) #указание ограничений
# ax[1].set_ylim(-1.5, 1.5)

# ax[2].set_xlim(12, -2)
# ax[2].set_ylim(1.5, -1.5)

# ax[3].autoscale(tight=True)

# plt.subplot(3, 1, 1)
# plt.plot(x, np.sin(x))
# plt.title("Синус") 
# plt.xlabel('x') #подпись осей
# plt.ylabel('sin(x)')

# plt.subplot(3, 1, 2)
# plt.plot(x, np.sin(x), '-g', label='sin(x)')
# plt.plot(x, np.cos(x), ':b', label='cos(x)')
# plt.title("Синус и косинус")
# plt.legend() #легенда

# plt.subplot(3, 1, 3)
# plt.plot(x, np.sin(x), '-g', label='sin(x)')
# plt.plot(x, np.cos(x), ':b', label='cos(x)')
# plt.axis('equal') #выравнивание
# plt.legend()

# plt.subplots_adjust(hspace = 0.5)

# x = np.linspace(0, 10, 30)
# plt.plot(x, np.sin(x), 'o', color='green') # o - чисто точками указываться будет
# plt.plot(x, np.sin(x) + 1, '>', color='green') # это всякие другие варианты маркировки чисто по "точкам"
# plt.plot(x, np.sin(x) + 2, '^', color='green') 
# plt.plot(x, np.sin(x) + 3, 's', color='green') 

# x = np.linspace(0, 10, 30)
# plt.plot(x, np.sin(x), '--p', markersize=15, linewidth=4, markerfacecolor='white', markeredgecolor='gray', markeredgewidth=2) #соединяются точки пунктиирной линией

# rng = np.random.default_rng(0)

# colors = rng.random(30)
# sizes = 30 * rng.random(30)
# plt.scatter(x, np.sin(x), marker='o', c=colors, s=sizes)
# plt.colobar() #шкала значение в зависимости от цвета

# Если точек больше 1000, то плот предпочтительнее из-за производительности

# визуализация погрешности
# x = np.linspace(0, 10, 50)
# dy = 0.4
# y = np.sin(x) + dy * np.random.randn(50)
# plt.errorbar(x, y, yerr=dy, fmt='.k')
# plt.fill_between(x, y-dy, y+dy, color='red', alpha=0.4) #альфа - параметр полупрозрачности


# def f(x,y):
#     return np.sin(x) ** 5 + np.cos(20 + x * y) * np.cos(x)

# x = np.linspace(0, 5, 50)
# y = np.linspace(0, 5, 40)
# X, Y = np.meshgrid(x,y)
# Z = f(X,Y)

# # plt.contour(X,Y,Z, color = 'green')
# # plt.contourf(X,Y,Z, cmap='RdGy')

# c=plt.contour(X,Y,Z, color='red')
# plt.clabel(c) #значения на графике показывает
# plt.imshow(Z, extent=[0,5,0,5], cmap='RdGy', interpolation='gaussian', origin='lower', aspect='equal') #аспект показывает соотношение сторон, чтобы они выглядели лушче
# plt.colorbar()


plt.show()


