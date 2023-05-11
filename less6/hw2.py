# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random
source_array = [random.randint(-50, 50) for i in range(random.randint(10,20))]
print ("Массив: ", *source_array)
max = int(input("Введите максимальное значение диапазона: "))
min = int(input("Введите минимальное значение диапазона: "))
array = []
if max>=min:
   for i in range(len(source_array)):
      if max>=source_array[i] and min<=source_array[i]:
          array.append(i)
   print("Кол-во элементов:", len(array), "Индексы:",array)