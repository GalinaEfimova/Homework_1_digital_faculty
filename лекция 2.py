import numpy as np
import matplotlib.pyplot as plt
# Суммирование значений в массиве и другие агрегатные функции

# rng = np.random.default_rng(1) #значения от 0 до 1
# s = rng.random(50) # cлучайные нормально распределенные
# print(s)
# print(sum(s))
# print(np.sum(s)) # считает быстрее и может считать двумерные массивы

# a = np.array([
#     [1,2,3,4,5],
#     [6,7,8,9,10]
# ])
# # print(np.sum(a)) # также можно применять другие функции, например min
# # print(np.sum(a, axis=0)) #axis задает измерение в котором будут свернуты строки а не колонки. [7 9 11 13 15]
# # print(np.sum(a, axis=1)) # [15 40]

# print(np.min(a))
# print(np.min(a, axis=0))
# print(a.min())
# print(a.min(1))
# # NaN = Not a number
# print(np.nanmin(a))
# print(np.nanmin(a, axis=0)) #это все об одном и том же, но с нан безопасные версии для запуска таких функций, когда в данных могут быть None



# Транслирование(broadcasting)
# эта штука описывает набор правил, которые позволяют осуществлять бинарные операции с массивами разных форм и размеров
# a = np.array([0,1,2])
# b = np.array([5,5,5])
# print(a + b) # [5 6 7]
# print(a + 5) # [5 6 7] 5 транслируется в массив похожий на b т.е она подстраивается под размер массива а

# a = np.array([[0,1,2],[3,4,5]])
# print(a+5)
# a = np.array([0,1,2])
# b = np.array([[0],[1],[2]]) 
# print(a+b) # [[0 1 2]
#              #[1 2 3]
#              #[2 3 4]]
# Правила
# 1. если размерности массивов отличаются, то форма массива с меньшей размерностью дополняеься 1 с левой стороны
# 2. если формы массивов не совпадают в каком-то измерении, то если у массива форма = 1, то он растягивается до соответствия формы 2-го массива
# 3. если после применения этих правил в каком-либо измерении размеры отличаются и ни один из них не равен 1, то тогда мы не можем сделать транслирование и не можем их сложить -> ошибка
# a = np.array([[0,1,2],[3,4,5]])
# b = np.array([5])
# print(a.ndim, a.shape) # 1е возвращает количество измерений массива (тут 2), 2е размер(форма) массива (тут (2, 3))
# print(b.ndim, b.shape) # 1. 1   2. (1,)
# a        (2,3)
# b(1,) -> (1,1)
#print(a+b)

# a = np.ones((2,3))
# b = np.arange(3)
# print(a)
# print(b)
# print(a.ndim, a.shape)
# print(b.ndim, b.shape)

# # (2,3)   (2,3)    (2,3)
# # (3,) -> (1,3) -> (2,3)
# c = a + b
# print(c, c.shape)


# a = np.arange(3).reshape((3,1))
# b = np.arange(3)
# print(a)
# print(b)
# print(a.ndim, a.shape)
# print(b.ndim, b.shape)

# # (3,1)   (3,1) -> (3,3)
# # (3,) -> (1,3) -> (3,3)
# c = a + b
# print(c, c.shape)


# a = np.ones((3,2))
# b = np.arange(3)

# 2 (3,2)   (3,2)    (3,2) ---> error
# 1 (3,) -> (1,3) -> (3,3) ---> error

## 01 что надо изменить в последнем примере чтобы он заработал без ошибок?

# X = np.array([
#     [1,2,3,4,5,6,7,8,9],
#     [9,8,7,6,5,4,3,2,1]
# ])

# Xmean0 = X.mean(0) # среднее значение в 0 строке (т.е каждый элемент заменяется на среднее значение всех чисел в этой строке)
# print(Xmean0)

# Xcenter0 = X - Xmean0
# print(Xcenter0)
# Xmean1 = X.mean(1)
# print(Xmean1)
# Xmean1 = Xmean1[:, np.newaxis]
# Xcenter1 = X - Xmean1
# print(Xcenter1)

# x = np.linspace(0, 5, 50)
# y = np.linspace(0, 5, 50)[:, np.newaxis]

# z = np.sin(x)**3 + np.cos(20 + y*x) * np.sin(y)
# print(z.shape)

# plt.imshow(z)
# plt.colorbar() #цветом отображается как бы высота
# plt.show()

# x = np.array([1,2,3,4,5])
# y = np.array([[1,2,3,4,5],[6,7,8,9,10]])
# print(x < 3) # [ True  True False False False]
# print(np.less(x,3)) # то же самое 

# print(np.sum(x < 3)) # количество элементов (вывод 2)
# print(np.sum(y > 4, axis=0)) # [1 1 1 1 2]
# print(np.sum(y > 4, axis=1)) # [1 5]
# print(np.sum(y > 4)) # 6

# & | ^ -
## 02 Пример для у. Вычислить количество элементов (по обоим размерностям), значения которых больше 3 и меньше 9


# Маски - булевы массивы
# x = np.array([1,2,3,4,5])
# y = print(x < 3)

# print(x[x < 3])
# print(bin(42 & 59)) # побитовая операция



# векторизация индекса
# x = np.array([1,2,3,4,5,6,7,8,9])
# index = [1,5,7]
# print(x[index])
# index = [[1,5,7],[2,4,8]]
# print(x[index])
# форма результата отражает форму массива индекса, а не форму исходного массива (в данном случае исходный это х)
# x = np.arange(12).reshape((3,4))

# print(x)
# print(x[2])
# print(x[2, [2,0,1]])
# print(x[1:, [2,0,1]])

# x = np.arange(10)
# i = np.array([2,1,8,4])
# print(x)
# x[i] = 999
# print(x)


# # cортировка массивов
# x = [3,2,6,9,2,4,1,5,7,3]
# print(sorted(x))
# print(np.sort(x)) # быстрее на больших объемах


# структурированные массивы
data = np.zeros(4, dtype = {
    'names':(
        'name', 'age'
    ),
    'formats':(
        'U10', 'i4'
    )
})
# print(data.dtype) #[('name', '<U10'), ('age', '<i4')]     < - говорит об обратном порядке байт, > - прямой порядок байт
name = ['name1', 'name2', 'name3', 'name4']
age = [10, 20, 30, 40]

data['name'] = name
data['age'] = age

# print(data)

# print(data['age'] > 20) # [False False  True  True]
# print(data[data['age'] > 20]['name']) # ['name3' 'name4'] (а без ['name'] выведется просто нужный кортеж)


# массивы записей
data_rec = data.view(np.recarray)
print(data_rec) #[('name1', 10) ('name2', 20) ('name3', 30) ('name4', 40)]
print(data_rec[0]) #('name1', 10)
print(data_rec[-1].name) # name4
