n = int(input("Введите ширину шоколадки: "))
m = int(input("Введите длину шоколадки: "))
k = int(input("Введите требуемое количество долек: "))
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print("Шоколадку можно разделить на", k, "прямоугольных долек")
else:
    print("Шоколадка не делится...")