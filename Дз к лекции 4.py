
# 1. Разобраться как использовать мультииндексные ключи в данном примере
index = [
     ('city_1', 2010),
     ('city_1', 2020),
     ('city_2', 2010),
     ('city_2', 2020),
     ('city_3', 2010),
     ('city_3', 2020),
 ]
import numpy as np
import pandas as pd
population = [
     101,
     201,
     102,
     202,
     103,
     203,
 ]
pop = pd.Series(population, index = pd.MultiIndex.from_tuples(index))
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

pop_df_1 = pop_df.loc['city_1', 'something']
pop_df_2 = pop_df.loc[['city_1', 'city_3'], ['total', 'something']]
pop_df_3 = pop_df.loc[['city_1', 'city_3'], 'something']

print(pop_df_1)
print(pop_df_2)
print(pop_df_3)

# 2. Из получившихся данных выбрать данные по 
# - 2020 году (для всех столбцов)
# - job_1 (для всех строк)
# - для city_1 и job_2 

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
rng = np.random.default_rng(1)

data = rng.random((4,6))
print(data)

data_df = pd.DataFrame(data, index = index, columns = columns)
print(data_df)

data_2020 = data_df.xs(2020, level = 'year')
print("\n2020 год для всех столбцов:")
print(data_2020)

data_job1 = data_df.xs('job 1', level='job', axis=1)
print("\njob 1 для всех строк:")
print(data_job1)

data_city1_job2 = data_df.loc['city 1', (slice(None), 'job 2')]
print("\nдля city_1 и job_2:")
print(data_city1_job2)


# 3. Взять за основу DataFrame со следующей структурой
# Выполнить запрос на получение следующих данных
# - все данные по person_1 и person_3
# - все данные по первому городу и первым двум person-ам (с использование срезов)
#
# Приведите пример (самостоятельно) с использованием pd.IndexSlice

index = pd.MultiIndex.from_product(
     [
         ['city_1', 'city_2'],
         [2010, 2020]
     ],
     names=['city', 'year']
 )
columns = pd.MultiIndex.from_product(
     [
         ['person_1', 'person_2', 'person_3'],
         ['job_1', 'job_2']
     ],
     names=['worker', 'job']
 )
rng = np.random.default_rng(1)
data = rng.random((4, 6))
data_df = pd.DataFrame(data, index=index, columns=columns)
print(data_df)

data_person1_3 = data_df.loc[:, ['person_1', 'person_3']]
print("\nДанные по person_1 и person_3:")
print(data_person1_3)

data_city1_person1_2 = data_df.loc['city_1', 'person_1':'person_2']
print("\nДанные по city_1 и person_1, person_2:")
print(data_city1_person1_2)

index = pd.MultiIndex.from_product(
    [['Cat', 'Dog', 'Hamster'], [2019, 2020, 2021]],
    names=['Pet', 'Year']
)
columns = pd.MultiIndex.from_product(
    [['length', 'height'], ['meter', 'centimeter']],
    names=['parameter', 'units']
)
rng = np.random.default_rng(42)
data = rng.integers(50, 500, size=(9, 4))
df = pd.DataFrame(data, index=index, columns=columns)
print(df)
idx = pd.IndexSlice
df_s = df.loc[idx[['Cat', 'Hamster'], [2020, 2021]], :]
print("\nДанные по Cat и Hamster за 2020 и 2021 годы:")
print(df_s)




#4. Привести пример использования inner и outer джойнов для Series (данные примера скорее всего нужно изменить)
ser1 = pd.Series(['a', 'b', 'c'], index=[1,2,3])
ser2 = pd.Series(['b', 'c', 'f'], index=[2,3,4])
print(ser1)
print(ser2)
outer_join = pd.concat([ser1, ser2], axis=1, join='outer')
print("\nOuter join:")
print(outer_join)

inner_join = pd.concat([ser1, ser2], axis=1, join='inner')
print("\nInner join:")
print(inner_join)
