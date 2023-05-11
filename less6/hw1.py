# Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки

size = int(input('Введите количество элементов прогрессии: '))
progression = [0]*size
progression[0] = int(input('Введите первый элемент: '))
difference = int(input('Введите разность: '))
print (progression[0], end=' ')
for i in range(1,size):
    progression[i] = progression[i-1] + difference
    print (progression[i], end=' ')