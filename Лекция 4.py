import numpy as np
import pandas as pd


'''#  Если размерность данных > 2, то используют иерархическую индексацию (мультииндекс). В один индекс включается несколько уровней.

index = [
    ('city 1', 2010),
    ('city 1', 2020),
    ('city 2', 2010),
    ('city 2', 2020),
    ('city 3', 2010),
    ('city 3', 2020),
    ]

population = [
    101,
    201,
    102,
    202,
    103,
    203,
]
pop = pd.Series(population, index = index)

print(pop)
print(pop[ [i for i in pop.index if i[1] == 2020] ])

# MultiIndex

index = pd.MultiIndex.from_tuples(index)

pop = pop.reindex(index)
print(pop)

print(pop[:, 2020])

# Из Series в DataFrame и наоборот

pop_df = pop.unstack()
print(pop_df)

print(pop_df.stack())

index = [
    ('city 1', 2010, 1),
    ('city 1', 2010, 2),
    
    ('city 1', 2020, 1),
    ('city 1', 2020, 2),
    
    ('city 2', 2010, 1),
    ('city 2', 2010, 2),
    
    ('city 2', 2020, 1),
    ('city 2', 2020, 2),
    
    ('city 3', 2010, 1),
    ('city 3', 2010, 2),
    
    ('city 3', 2020, 1),
    ('city 3', 2020, 2),
    ]

population = [
    101,
    1010,
    201,
    2010,
    102,
    1020,
    202,
    2020,
    103,
    1030,
    203,
    2030,
]

pop = pd.Series(population, index = index)
print(pop)

index = pd.MultiIndex.from_tuples(index)

pop = pop.reindex(index)
print(pop)

print(pop[:, 2010])
print(pop[:,:,2])

pop_df = pop.unstack()

print(pop_df)
print(pop_df.stack())

index = [
    ('city 1', 2010),
    ('city 1', 2010),
    
    ('city 1', 2020),
    ('city 1', 2020),
    
    ('city 2', 2010),
    ('city 2', 2010),
    
    ('city 2', 2020),
    ('city 2', 2020),
    
    ('city 3', 2010),
    ('city 3', 2010),
    
    ('city 3', 2020),
    ('city 3', 2020),
    ]

population = [
    101,
    201,
    102,
    202,
    103,
    203,
]

pop = pd.Series(population, index = index)
pop_df = pd.DataFrame(
    {
        'total': pop,
        'something': [
            10,
            11,
            12,
            13,
            14,
            15,
            ]
    }
)

print(pop_df)

print(pop_df['something'])

##pop_df1 = pop_df.loc???['city 1', 'something']
##pop_df1 = pop_df.loc???[['city 1','city 3'], ['total', 'something']]
##pop_df1 = pop_df.loc???[['city 1','city 3'], 'something']]
##print(pop_df_1)

# 1. Разобраться, как использовать мультииндексные ключи в данном примере
'''
### Как можно создавать мультииндексы
## - список массивов, задающих значение индекса на каждом уровне

i1 = pd.MultiIndex.from_arrays(
    [
        ['a', 'a','b', 'b'],
        [1,2,1,2]
    ]
)
print(i1)

# - список кортежей, задающих значение индекса в каждой точке

i2 = pd.MultiIndex.from_tuples(
    [
        ('a',1),
        ('a',2),
        ('b',1),
        ('b',2),
    ]
)
print(i2)

# Декартово произведение обычных индексов
i3 = pd.MultiIndex.from_product(
    [
        ['a','b'],
        [1,2],
        ])
print(i3)
# Описание внутреннего представления : levels - список списков, codes - список спиков меток

i4 = pd.MultiIndex(
    levels = [
        ['a','b', 'c'],
        [1,2],
    ],
    codes = [
        [0,0,1,1,2,2], # a a b b c c
        [0,1,0,1,0,1], # 1 2 1 2 1 2
    ]
)
print(i4)
# Уровням можно задавать названия

data = {
    ('city 1', 2010) : 100,
    ('city 1', 2020) : 200,
    ('city 2', 2010) : 1001,
    ('city 2', 2020) : 2001,
    
}
s = pd.Series(data)
print(s)

s.index.names = ['city', 'year']
print(s)

index = pd.MultiIndex.from_product(
    [
        ['city 1','city 2'],
        [2010,2020],
        ],
    names = ['city', 'year']
    )
print(index)

columns = pd.MultiIndex.from_product(
    [
        ['person 1','person 2', 'person 3'],
        ['job 1', 'job 2'],
        ],
    names = ['worker', 'job']
    )
rng = np.random.default_rng(1)

data = rng.random((4,6))
print(data)

data_df = pd.DataFrame(data, index = index, columns = columns)
print(data_df)

# Из получившихся данных выбрать данные по
# - 2020 году (для всех столбцов)
# по job 1 (для всех строк)
# для city 1 и job 2

# Индексация и срезы (по мультииндексу)

data = {
    ('city 1', 2010) : 100,
    ('city 1', 2020) : 200,
    ('city 2', 2010) : 1001,
    ('city 2', 2020) : 2001,
    ('city 3', 2010) : 10001,
    ('city 3', 2020) : 20001,
    
}

s = pd.Series(data)
s.index.names = ['city', 'year']
print(s['city 1', 2010])
print(s['city 1'])

print(s.loc['city 1' : 'city 2'])

print(s[s> 2000])

print(s[['city 1','city 3']])

# 3. Взять за основу DataFrame со следующей структурой
index = pd.MultiIndex.from_product(
    [
        ['city 1','city 2'],
        [2010,2020],
        ],
    names = ['city', 'year']
    )
columns = pd.MultiIndex.from_product(
    [
        ['person 1','person 2', 'person 3'],
        ['job 1', 'job 2'],
        ],
    names = ['worker', 'job']
    )
# выполнить запрос на получение следующих данных
# - все данные по person 1  и person 3
# - все данные по первому городу и первым двум person-ам (с использованием срезов)

# Приведите пример с использованием pd.IndexSlice

# Перегруппировка мультииндексов - машина ожидает, что индексы - отсортированы, иначе - ошибка

rng = np.random.default_rng(1)

index = pd.MultiIndex.from_product(
    [
        ['a', 'b', 'c'],
        [1,2]
        ]
    )
data = pd.Series(rng.random(6), index = index)
data.index.names = ['char','int']

print(data)

data = data.sort_index()

print(data)
print(data['a':'b'])

index = [
    ('city 1', 2010, 1),
    ('city 1', 2010, 2),
    
    ('city 1', 2020, 1),
    ('city 1', 2020, 2),
    
    ('city 2', 2010, 1),
    ('city 2', 2010, 2),
    
    ('city 2', 2020, 1),
    ('city 2', 2020, 2),
    
    ('city 3', 2010, 1),
    ('city 3', 2010, 2),
    
    ('city 3', 2020, 1),
    ('city 3', 2020, 2),
    ]
population = [
    101,
    1010,
    201,
    2010,
    102,
    1020,
    202,
    2020,
    103,
    1030,
    203,
    2030,
]

pop = pd.Series(population, index = index)
print(pop)

i = pd.MultiIndex.from_tuples(index)

pop = pop.reindex(i)

print(pop)
print(pop.unstack()) # переводит в DataFrame
print(pop.unstack(level = 0))
print(pop.unstack(level = 1))
print(pop.unstack(level = 2))

# NumPy Конкатенация
x = [1,2,3]
y = [4,5,6]
z = [7,8,9]

print(np.concatenate([x,y,z])) # склейка в 1 строку

x = [[1,2,3]]
y = [[4,5,6]]
z = [[7,8,9]]

print(np.concatenate([x,y,z])) # склейка по строчкам
print(np.concatenate([x,y,z], axis = 1))
print(np.concatenate([x,y,z], axis = 0))

# Pandas - concat

ser1 = pd.Series(['a','b','c'], index = [1,2,3])
ser2 = pd.Series(['d','e','f'], index = [4,5,6])

print(pd.concat([ser1,ser2]))

ser1 = pd.Series(['a','b','c'], index = [1,2,3])
ser2 = pd.Series(['d','e','f'], index = [1,2,6])

print(pd.concat([ser1,ser2], verify_integrity=False))
print(pd.concat([ser1,ser2], ignore_index=True))
print(pd.concat([ser1,ser2], keys =['x','y'])) # позвол. создать самим  мультииндексы? тут уникальность индексов уже несущественна


ser1 = pd.Series(['a','b','c'], index = [1,2,3])
ser2 = pd.Series(['b','c','f'], index = [4,5,6])

print(pd.concat([ser1,ser2], join='outer'))
print(pd.concat([ser1,ser2], join='inner'))

# 4. привести пример использования inner и outer джойнов для Series (на данных предыдущего примера)

