# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

bushes_number = int(input("Введите количестве кустов: "))
array = list()
for i in range(bushes_number):
    berry = int(input("Количество ягод на кусту №" + str(i+1) + ": "))
    array.append(berry)

berries_count = list()
for i in range(len(array) - 1):
    berries_count.append(array[i - 1] + array[i] + array[i + 1])
berries_count.append(array[-2] + array[-1] + array[0])
print(max(berries_count))