a = int(input ("Введите сумму загаданных чисел: "))
b = int(input ("Введите произведение загаданных чисел: "))
digits = []
for i in range(a + b):
    if i == (a * i - b) ** 0.5:
        digits.append(i)
if len(digits) == 2:
    print("Вы загали числа:", *digits)
else: 
    print("Вы загали числа:", digits + digits)