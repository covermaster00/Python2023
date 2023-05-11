def exponentiation(number, degree):
    if (degree != 1):
        return (number * exponentiation(number, degree - 1))
    else:
        return (number)
number = int(input("Число: "))
degree = int(input("Степень: "))
print(number, "^", degree, "=", exponentiation(number, degree))