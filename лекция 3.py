import numpy as np
import pandas as pd

# Pandas -  расширение NumPy (структурированные массивы. Строки и столбцы индексируются метками, а не только числовыми значениями

# Series, DataFrame, Index ("обертки" над NumPy)

## Series

data = pd.Series([0.25, 0.5, 0.75, 1.0])
print(data)
print(type(data))

print(type(data.values))
print(type(data.index))

print(data[0])
print(data[1:3]) # можем обращаться как к срезу или как к индексу


data = pd.Series([0.25, 0.5, 0.75, 1.0], index = ['a', 'b', 'c', 'd'])
print(data)

print(data['a'])
print(data['b':'d'])
print(type(data.index))


data = pd.Series([0.25, 0.5, 0.75, 1.0], index = [1, 10, 7, 'd'])
print(data)

print(data[1])
print(data[10:'d'])

population_dict = {
    'city 1': 1001,
    'city 2': 1002,
    'city 3': 1003,
    'city 4': 1004,
    'city 5': 1005,
}

population = pd.Series(population_dict)
print(population)

print(population['city 4'])
print(population['city 4': 'city 5'])

# Для создания Series  можно использовать
#  - списки или массивы из NumPy
#  - скалярные значения
#  - словари
# 1. Привести различные способы создания объектов типа Series

## DataFrame -  двумерный массив с явно определенными индексами. Последовательность "согласованных" объектов Series

# будет согласование по индексам 
area_dict = {
    'city 1': 9991,
    'city 2': 9992,
    'city 3': 9993,
    'city 4': 9994,
    'city 5': 9995,
}

population = pd.Series(population_dict)
area = pd.Series(area_dict)

print(population)
print(area)

states = pd.DataFrame({
    'population1' : population,
    'area1' : area,
})

print(states)

print(states.values)
print(states.index)
print(states.columns)

print(type(states.values))
print(type(states.index))
print(type(states.columns))

print(states['area1'])

# 2. Привести различные способы создания объектов типа DataFrame
#DateFrame.  Способы создания
# Через объекты Series
# Списки словарей
# Словари объектов Series
# Двумерный массив NumPy
# Структурированный массив NumPy

## Index - способ организации ссылки на данные объектов Series  и DataFrame. Index  - неизменяем (по сути как кортеж), упорядочен, является мультимножеством (в нем могут быть повторяющиеся значения)

ind = pd.Index([2,3,5,7,11])
print(ind[1])
print(ind[::2])

# ind[1] = 5 - ошибка тк неизм

# Index- следует соглашению объекта Set (python) - можно объединять, пересекать и тд

indA = pd.Index([1,2,3,4,5])
indB = pd.Index([2,3,4,5,6])
# пересечение
print(indA.intersection(indB))

# Выборка данных из Series
# Sreries ведет себя как словарь
data = pd.Series([0.25, 0.5, 0.75, 1.0], index = ['a', 'b', 'c', 'd'])

print('a' in data)
print('z' in data)

print(data.keys())

print(list(data.items()))

data['a'] = 100
data['z'] = 1000

print(data)

## как одномерный массив тоже может вести себя Series
data = pd.Series([0.25, 0.5, 0.75, 1.0], index = ['a', 'b', 'c', 'd'])

print(data['a':'c'])
print(data[0:2])
print(data[(data > 0.5) & (data < 1)])
print(data[['a','d']])

# Могут быть ошибки(коллизии) из-за разных типов индексов
# Решение: атрибуты-индексаторы

data = pd.Series([0.25, 0.5, 0.75, 1.0], index = [1, 3, 10, 15])

print(data[1])

# По значениям индексов
print(data.loc[1])
# По номеру в индексе - 0,1,2...
print(data.iloc[1])

# Выборка данных из DataFrame
# как словарь действует

population_dict = {
    'city 1': 1001,
    'city 2': 1002,
    'city 3': 1003,
    'city 4': 1004,
    'city 5': 1005,
}

area_dict = {
    'city 1': 9991,
    'city 2': 9992,
    'city 3': 9993,
    'city 4': 9994,
    'city 5': 9995,
}

pop = pd.Series({
    'city 1': 1001,
    'city 2': 1002,
    'city 3': 1003,
    'city 4': 1004,
    'city 5': 1005,
    })
area = pd.Series({
      'city 1': 9991,
    'city 2': 9992,
    'city 3': 9993,
    'city 4': 9994,
    'city 5': 9995,
    })
data =  pd.DataFrame({'area1': area, 'pop1':pop, 'pop': pop})

print(data)

print(data['area1'])
print(data.area1)

# Возникает ошибка в данном случае
print(data.pop1 is data['pop1'])
print(data.pop is data['pop'])


data['new'] = data['area1']
data['new1'] = data['area1']/data['pop1']

print(data)

# Двумерный массив NumPy
data =  pd.DataFrame({'area1': area, 'pop1':pop, 'pop': pop})

print(data)

print(data.values)

print(data.T) # транспонирование

print(data['area1']) # обращение к столбцу по индексу

print(data.values[0:3]) # обращение к строке по индексу

# атрибуты-индексаторы
print(data.iloc[:3, 1:2])
print(data.loc[:'city 3', 'pop1' : 'pop'])
print(data.loc[data['pop']> 1002, ['area1', 'pop']])

data.iloc[0,2] = 999999

print(data)

rng = np.random.default_rng()
s = pd.Series(rng.integers(0,10,4))
print(s)
print(np.exp(s))

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
data =  pd.DataFrame({'area1': area, 'pop1':pop})

print(data)

# NaN - not a number

# 3. Объедините два объекта Series с неодинаковыми множествами ключей (индексов) так, чтобы вместо NaN было установлено значение 1

dfA = pd.DataFrame(rng.integers(0,10, (2,2)), columns = ['a','b'])

dfB = pd.DataFrame(rng.integers(0,10, (3,3)), columns = ['a','b', 'c'])

print(dfA)
print(dfB)

print(dfA + dfB)

rng = np.random.default_rng(1)

A = rng.integers(0, 10, (3,4))
print(A)

print(A[0])

print(A - A[0])

df = pd.DataFrame(A, columns = ['a', 'b', 'c', 'd'])
print(df)

print(df.iloc[0])

print(df - df.iloc[0]) # получили то же самое

print(df.iloc[0, ::2])

print(df - df.iloc[0, ::2])

# 4. Переписать пример с транслированием для DataFrame так, чтобы вычитание происходило не по строкам, а по столбцам

# NaN - not a number
# NA - значения (отсутствующие): NaN, null, 99999

# Pandas - два способа хранения отсутствующего значения
# индикаторы NaN, None
# второй способ - null
# None - объект (накладные расходы). Не работает с sum, min
val1 = np.array([1,2,3])
print(val1.sum())

"""val1 = np.array([1, None ,2,3])
print(val1.sum()) - не будет работать"""

val1 = np.array([1,np.nan,2,3])
print(val1)
print(val1.sum())
print(np.sum(val1))
print(np.nansum(val1))

x = pd.Series(range(10), dtype=int)
print(x)

x[0] = None
x[1] = np.nan

print(x)

x1 = pd.Series(['a','b','c'])

x1[0] = None # при замене объект остается объектом
x1[1] = np.nan
print(x1)


x2 = pd.Series([1,2,3, np.nan, None, pd.NA])
print(x2)

x3 = pd.Series([1,2,3, np.nan, None, pd.NA], dtype = 'Int32') # привели всё к одному типу - not avalible элементы тоже стали одинаковыми
print(x3)

print(x3.isnull())
print(x3[x3.isnull()])
print(x3[x3.notnull()])

print(x3.dropna()) # 'дропнет' not avaliable-элементы

df = pd.DataFrame(
    [
        [1,2,3, np.nan, None, pd.NA],
        [1,2,3, None,5,6],
        [1,np.nan,3,4,np.nan,6],
    ]
)
print(df)
print(df.dropna())
print('ddddd')
print(df.dropna(axis=0))
print(df.dropna(axis=1))

# how
# all - отбрасыв, если отсут все значения (NA)
# any - хоть одно значение
# thres = x, остается, если присутствует МИНИМУМ ч НЕПУСТЫХ значений
print(df.dropna(axis=1, how='all'))
print(df.dropna(axis=1, how='any'))
print(df.dropna(axis=1, thresh=2))

# 5 На примере объектов DataFrame продемонстрировать использование методов ffill() и bfill()
