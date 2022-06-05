# Условия:
# Задача 1

calc = input('Выберите операцию: \n1 - "r" - применяет унарный минус к операнду \n2 - "+" - сложение \n3 - "-" - вычитание \n4 - "/" - деление \n5 - "*" - умножение \n6 - "%" - деление по модулю (остаток от деления) \n7 - "<" - минимальное из двух чисел \n8 - ">" - максимальное из двух чисел \nВведите цифру: ')
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

if calc == "1":
    print(-num1 if +num1 else num1)
    print(-num2 if +num2 else num2)
if calc == "2":
    print(num1 + num2)
if calc == "3":
    print(num1 - num2)
if calc == "4":
    try:
        print(num1 / num2)
    except ZeroDivisionError:
        print("На ноль делить нельзя!")
if calc == "5":
    print(num1 * num2)
if calc == "6":
    print(num1 % num2)
if calc == "7":
    print(str(num1) + " < " + str(num2) if num1 < num2 else str(num2) + " < " + str(num1) if num1 > num2 else str(num1) + " = " + str(num2))
if calc == "8":
    print(str(num1) + " > " + str(num2) if num1 > num2 else str(num2) + " > " + str(num1) if num1 < num2 else str(num1) + " = " + str(num2))

# Задача 2
print("\n")

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
print("Максимальное значение: ", a if b < a > c else b if a < b > c else c)


# Цикл While:
# Задача 1
print("\n")

am = int(input("Введите количество чисел последовательности: "))
num = float(input("Введите число: "))
min_num = num
max_num = num
sum_num = num
i = 1

while i < am:
    num = float(input("Введите число: "))
    sum_num += num
    if num < min_num:
        min_ch = num
    if num < min_num:
        max_num = num
    i += 1

print("Количество чисел: ", am)
print("Среднее арифметическое: ", sum_num/am)
print("Минимальное число: ", min_num)
print("Максимальное число: ", max_num)


# Задача 2
print("\n")

amount = input("Введите количество символов: ")
i = 0
while type(amount) != int:
    try:
        amount = int(amount)
    except ValueError:
        print("Нельзя вводить строки!")
        amount = input("Введите число: ")
sym = input("Введите тип символов: ")
orient = int(input("Выберите ориентацию символов (1 - вертикальная, 2 - горизонтальная): "))
if orient == 1:
    while i < amount:
        print(sym)
        i += 1
if orient == 2:
    while i < amount:
        print(sym, end=" ")
        i += 1
















