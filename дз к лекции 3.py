import numpy as np
import pandas as pd

# 1. Привести различные способы создания объектов типа Series

# Из списка
n_list = pd.Series([10, 20, 30, 40])
print(n_list)

# Из массива NumPy
array = np.array([1, 2, 3, 4, 5])
n_array = pd.Series(array)
print(n_array)

# Скалярное значение
from_scalar = pd.Series(5, index=['a', 'b', 'c', 'd'])
print(from_scalar)

# Из словаря
data = {'a': 90, 'b': 80, 'c': 70}
from_dict = pd.Series(data)
print(from_dict)

# 2. Привести различные способы создания объектов типа DataFrame

# Через объекты Series
s1 = pd.Series([1, 2, 3], name = 'a')
s2 = pd.Series([4, 5, 6], name = 'b')
from_series = pd.DataFrame({s1.name: s1, s2.name: s2})
print(from_series)

# Через список словарей
data = [
    {'name': 'Anasteisha', 'age': 25, 'city': 'New York'},
    {'name': 'Sergey', 'age': 30, 'city': 'Los Angeles'},
    {'name': 'Ivan', 'age': 19, 'city': 'Chicago'}
]
from_list_of_dicts = pd.DataFrame(data)
print(from_list_of_dicts)

# Через словарь объектов Series
s1 = pd.Series([90, 80, 70], index=['row1', 'row2', 'row3'])
s2 = pd.Series([60, 50, 40], index=['row1', 'row2', 'row3'])
from_dict_of_series = pd.DataFrame({'A': s1, 'B': s2})
print(from_dict_of_series)

# Через двумерный массив NumPy
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
from_numpy = pd.DataFrame(array, columns=['Col1', 'Col2', 'Col3'], index=['Row1', 'Row2', 'Row3'])
print(from_numpy)

# Через структурированный массив NumPy
structured_array = np.array(
    [('Tom', 16, 'Moscow'), ('Kate', 56, 'Tbilisi'), ('Denis', 25, 'Orsck')],
    dtype=[('name', 'U10'), ('age', 'i4'), ('city', 'U15')]
)
from_structured_array = pd.DataFrame(structured_array)
print(from_structured_array)

# 3. Объедините два объекта Series с неодинаковыми множествами ключей (индексов) так, чтобы вместо NaN было установлено значение 1

pop = pd.Series({
    'city 1': 1001,
    'city 2': 1002,
    'city 3': 1003,
    'city 41': 1004,
    'city 52': 1005,
})

area = pd.Series({
    'city 1': 9991,
    'city 2': 9992,
    'city 3': 9993,
    'city 42': 9994,
    'city 50': 9995,
})

data = pd.DataFrame({'area1': area, 'pop1': pop}).fillna(1)

print(data)

# 4. Переписать пример с транслированием для DataFrame так, чтобы вычитание происходило не по строкам, а по столбцам

data = pd.DataFrame({
    'A': [10, 20, 30],
    'B': [40, 50, 60],
    'C': [70, 80, 90]
})

subtract_series = pd.Series([5, 10, 15], index=['A', 'B', 'C'])
result = data.subtract(subtract_series, axis=1)
print(result)

# 5 На примере объектов DataFrame продемонстрировать использование методов ffill() и bfill()

data = pd.DataFrame({
    'A': [1, None, 3, None, 5],
    'B': [None, 2, None, 4, None],
    'C': [25, None, None, 50, None]
})

print(data)

# ffill()
ffill_result = data.ffill()

print(ffill_result)

# bfill()
bfill_result = data.bfill()

print(bfill_result)
