# day = int(input("Введите день недели (цифрами): "))
# if 1 <= day <=5:  #(day >= 1) and (day <= 5):
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("Понедельник")
#     if day == 2:
#         print("Вторник")
#     if day == 3:
#         print("Среда")
#     if day == 4:
#         print("Четверг")
#     if day == 5:
#         print("Пятница")
# elif 6 <= day == 7:
#     print("Выходной день - ", end="")
#     if day == 6:
#         print("Суббота")
#     if day == 7:
#         print("Воскресенье")
# else:
#     print("Такого дня недели нет!")


# Способ 1

# month = int(input("Введите номер месяца: "))
# if 3 <= month <= 5:
#     print("Весна")
#     if month == 3:
#         print("Март")
#     if month == 4:
#         print("Апрель")
#     if month == 5:
#         print("Май")
# elif 6 <= month <= 8:
#     print("Лето")
#     if month == 6:
#         print("Июнь")
#     if month == 7:
#         print("Июль")
#     if month == 8:
#         print("Август")
# elif 9 <= month <= 11:
#     print("Осень")
#     if month == 9:
#         print("Сентябрь")
#     if month == 10:
#         print("Октябрь")
#     if month == 11:
#         print("Ноябрь")
# elif 12 == month or 1 <= month <= 2:
#     print("Зима")
#     if month == 12:
#         print("Декабрь")
#     if month == 1:
#         print("Январь")
#     if month == 2:
#         print("Февраль")
# else:
#     print("Такого месяца не существует!")


# Способ 2

# month = int(input("Введите номер месяца: "))
# if 1 <= month <= 12:
#     if month == 1 or month == 2 or month == 12:
#         print("Зима")
#     elif 3 <= month <= 5:
#         print("Весна")
#     elif 6 <= month <= 8:
#         print("Лето")
#     elif 9 <= month <= 11:
#         print("Осень")
# else:
#     print("Ошибка ввода данных")


# a, b = 10, 20
# minim = a if a < b else b #слева - истина, справа - ложь
# print(minim)

# a, b = 10, 20
# print("a = b" if a == b else "a < b" if a < b else "b < a")

# a, b = 2, 3
# print("Делить на ноль нельзя" if b == 0 else a/b)


#Перехват (обработка) исключений

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print((n / m))
# except ValueError:
#     print("Нельзя вводить строки!")
# except ZeroDivisionError:
#     print("Нельзя делить на 0!")

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print((n / m))
# except (ValueError, ZeroDivisionError):
#     print("Нельзя вводить строки!")
#     print("Нельзя делить на 0!")

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print((n / m))
# except ValueError:
#     print("Нельзя вводить строки!")
# except ZeroDivisionError:
#     print("Нельзя делить на 0!")
# else:
#     print("Всё нормально. Вы ввели числа", n, "и", m)
# finally:
#     print("Конец программы")


# a = input("Введите первое число: ")
# b = input("Введите второе число: ")
#
# try:
#     a = int(a)
#     b = int(b)
# except ValueError:
#     a = str(a)
#     b = str(b)
# finally:
#     print(a + b)


#Циклы

# i = 0
# while i < 5:
#     print(i)
#     i += 1

# i = 10
# while i > 0:
#     print(i)
#     i -= 1

# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print(i)
#     i += 1
#
# i = 0
# while i <= 20:
#     print(i)
#     i += 2

# star = int(input("Введите количество символов: "))
# i = 0
# while i < star:
#     print("*")
#     i += 1

# star = int(input("Введите количество символов: "))
# i = 0
# while i < star:
#     print("*", end=" ")
#     i += 1


# n = input("Введите целое число")
#
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое!")
#         n = input("Введите целое число: ")
# if n % 2 == 0:
#     print("Чётное")
# else:
#     print("Не чётное")


# n = int(input("Введите начало диапазона"))
# m = int(input("Введите конец диапазона"))
# sum = 0
#
# while n < m:
#     if n % 2 != 0:
#         sum += n
#     n += 1
# print("Сумма нечётных чисел: ", sum)


# i = 0;
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен")

# while True:
#     n = int(input("Введите положительное число"))
#     if not n > 0:
#         break

# a = 0
# while True:
#     n = int(input("Введите число: "))
#     a =+ n
#     if n == 0:
#         print("Результат: ", sum)
#         break


# i = 0
# while i < 10:
#     print(i)
#     i += 1
# else:
#     print("Цикл окончен, i =", i)

#
# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# else:
#     print("Цикл окончен, i =", i)


# i = 1
# while i < 5:
#     print("Внешний цикл ", i)
#     j = 1
#     while j < 4:
#         print("Внутренний цикл ", j)
#         j += 1
#     i += 1


i = 1
while i < 10:
    j = 1
    while j < 10:
        print(i, "*", j, "=", i*j, "\t\t", end="\n")
        j += 1
    print()
    i += 1


















