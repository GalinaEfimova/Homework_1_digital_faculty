import numpy as np
import sys
import array

# ОТВЕТЫ НА ВОПРОСЫ К ЛЕКЦИИ 1

## 1. Какие еще существуют коды типов?

'''
«c» — символ (char);
«b» — подписанный символ (signed char); 
«B» — неподписанный символ (unsigned char); 
«u» — символ Unicode (unicode character); 
«h» — подписанный короткий символ (signed short int); 
«H» — неподписанный короткий символ (unsigned short int); 
«l» — подписанный длинный символ (signed long int); 1
«L» — неподписанный длинный символ (unsigned long long); 
«f» — число с плавающей точкой (float); 
«d» — двойное число с плавающей точкой (double float)
'''

## 2. Напишите код, подобный приведенному выше, но с другим типом

a1 = array.array('f', [1.07,2,3])
print(sys.getsizeof(a1))
print(type(a1))
print(a1)

## 3. Напишите код для создания массива с 5 значениями, располагающимися через равные интервалы в диапазоне от 0 до 1

a = np.linspace(0,1,5)
print(a)

## 4. Напишите код для создания массива с 5 равномерно распределенными случайными значениями в диапазоне от 0 до 1

b = np.random.uniform(0,1,5)
print(b)

## 5. Напишите код для создания массива с 5 нормально распределенными случайными значениями с мат. ожиданием = 0 и дисперсией 1

c = np.random.normal(loc=0, scale=1, size=5)
print(c)

## 6. Напишите код для создания массива с 5 случайнвми целыми числами в от [0, 10)

d = np.random.randint(0, 10, size = 5)
print(d)

## 7. Написать код для создания срезов массива 3 на 4
## - первые две строки и три столбца
## - первые три строки и второй столбец
## - все строки и столбцы в обратном порядке
## - второй столбец
## - третья строка

array =  np.arange(1,13).reshape(3,4)
print(array)
slice1 = array[:2, :3]
slice2 = array[:3, 1:2]
slice3 = array[::-1, ::-1]
slice4 = array[:, 1]
slice5 = array[2, :]
print(slice1)
print(slice2)
print(slice3)
print(slice4)
print(slice5)

## 8. Продемонстрируйте, как сделать срез-копию

copy_slice = array[:3, :3].copy()
# Таким образом при изменении:
copy_slice[0,1] = 1200
print(copy_slice)
print(array) # Исходный массив не изменился - это копия

## 9. Продемонстрируйте использование newaxis для получения вектора-столбца и вектора-строки

vector = np.array([1, 2, 3])

row_vector = vector[np.newaxis, :] 
print("Вектор-строка:")
print(row_vector)
print(row_vector.shape)

column_vector = vector[:, np.newaxis]
print("Вектор-столбец:")
print(column_vector)
print(column_vector.shape)

## 10. Разберитесь, как работает метод dstack

x = np.array([1,2,3])
y = np.array([4,5,6])
r1 = np.dstack([x,y])
print(r1)

## 11. Разберитесь, как работают методы split, vsplit, hsplit, dsplit

arr = np.array([0, 1, 2, 3, 4, 5])
split_arrays = np.split(arr, 3)  
print(split_arrays)

arr = np.array([[1, 2], [3, 4], [5, 6]])
vsplit_arrays = np.vsplit(arr, 3)
print(vsplit_arrays)

arr = np.array([[1, 2, 3], [4, 5, 6]])
hsplit_arrays = np.hsplit(arr, 3)
print(hsplit_arrays)

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
dsplit_arrays = np.dsplit(arr, 2)
print(dsplit_arrays)

## 12. Привести пример использования всех универсальных функций, которые я привел

# 1. Сложение (+)
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(np.add(a, b))  

# 2. Вычитание (-)
print(np.subtract(a, b))

# 3. Деление (/)
print(np.divide(a, b))  

# 4. Целочисленное деление (//)
print(np.floor_divide(a, b))  

# 5. Умножение (*)
print(np.multiply(a, b))  

# 6. Возведение в степень (**)
print(np.power(a, 2))  

# 7. Остаток от деления (%)
print(np.mod(a, b))  

# 8. Абсолютное значение (abs)
c = np.array([-1, -2, -3])
print(np.abs(c))  

# 9. Синус (sin)
angles = np.array([0, np.pi/2, np.pi])  
print(np.sin(angles))  

# 10. Косинус (cos)
print(np.cos(angles))  

# 11. Экспонента (exp)
print(np.exp(a))  

# 12. Логарифм (log)
print(np.log(a))  
