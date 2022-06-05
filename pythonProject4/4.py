# i = 0
# while i < 3:
#     j = 0
#     while j < 6:
#         print("^", end="")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if i % 2 == 0:
#             print("+", end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1


# i = 0
# while i < 5:
#     j = 0
#     while j < i:
#         print(" ", end="")
#         j += 1
#     print("*")
#     i += 1
#
#
# i = 0
# while i < 5:
#     print(" " * i, "*")
#     i += 1


# for element in collections:
#     print(element)

# for i in 'Hello':
#     print(i)

# j = 1
# for color in 'red', 'orange', 'yellow', 'green', 'blue':
#     print(j, 'color:', color)
#     j +=1

# for i  in 'one', 'two', 1, 20, 0.3:
#     print(i)

# range(start, stop, step)

# for i in range(9):
#     print(i, end=" ")

# for i in range(3, 9):
#     print(i, end=" ")

# for i in range(2, 9, 3):
#     print(i, end=" ")

# for i in range(9, 2, -1):
#     print(i, end=" ")

# num = int(input("Введите целое число: "))
# for i in range(1, num):
#     if num % i == 0:
#         print(i, end=" ")

# num = 1
# for i in range(10, 100):
#     if i % 10 == 0:
#         print(i + num, end=" ")
#         num += 1

# for i in range(10):
#     print(i, end=" ")
#     if i == 5:
#         break
# else:
#     print("\nDone!")

# for i in range(3):
#     print("***")
#     for j in range(2):
#         print("------")

# w = int(input("Введите ширину прямоугольника: "))
# h = int(input("Введите высоту прямоугольника: "))
# for i in range(h):
#     for j in range(w):
#         print("*", end=" ")
#     print()

# w = int(input("Введите ширину прямоугольника: "))
# h = int(input("Введите высоту прямоугольника: "))
# for i in range(h):
#     for j in range(w):
#         if (i == 0 or i == h - 1) or (j == 0 or j == w - 1):
#             print("*", end=" ")
#         else:
#             print(" ", end="")
#     print()


# [результирующее выражение | цикл | опциональные условия]

# print([i * 2 for i in "Hello"])
# print([i ** 2 for i in range(30) if i % 2 == 0])
#
# num = [i ** 2 for i in range(30) if i % 2 == 0]
# print(num)


# num = 15
# s = 0
# for i in range (1, 100):
#     ch = int(input("Введите число от 1 до 100: "))
#     if (ch > num):
#         print("Загаданное число меньше")
#         s += 1
#     if (ch < num):
#         print("Загаданное число больше")
#         s +=1
#     if (ch == 0):
#         print("Вы вышли из игры")
#         break
#     if ch == num:
#         print("Вы угадали число с ", str(s), "раза")
#         break


# Списки

# num = [8, 3, 6, 5, 7]
# print(num[2])
# print(num[-1])
# num[1] = 256
# print(num)
# num[3] += 100
# print(num)
# print("Длина списка: ", len(num))

# s = []
# s = [5,6]
# s = [5] * 6
# print(s)

# b = list("Hello")
# print(b)

# n = list(range(2, 10, 2))
# print(n)
#
# s = list(range(10, 2, -2))
# print(s)

# a = [0 for i in range(5)]
# print(a)

# a = [i ** 2 for i in range(5)]
# print(a)

# n = 5
# a = [i ** 2 for i in range(1, n+1)]
# print(a)

# c = [i * 3 for i in "list"]
# print(c)

# a = [1, 2, 3]
# b = [4, 5]
# c = a + b
# print(c)
#
# d = b * 3

# print(d)


# a = [0] * int(input("Введите количество элементов списка: "))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input("-> "))
# print(a)


a = [input("-> ") for i in range(int(input("Количество элементов: ")))]
print(a)

for i in range(len(a)):
    print(a[i])

print()
for j in a:
    print(j, end=" ")