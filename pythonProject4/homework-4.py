# Задание 1

reverse = 0
num = int(input("Введите число: "))
i = num
while i > 0:
    reverse = reverse * 10 + i % 10
    i = i // 10
print(num)
print(reverse)
print("Палиндром" if num == reverse else "Не палиндром")

print()
# Задание 2

num1 = int(input("Начало диапазона: "))
num2 = int(input("Конец диапазона: ", ))
for i in range(num1, num2 + 1):
    if i % 2 != 0:
        print(i, end=" ")

print("\n")
# Задание 3

i = 8
while i > 0:
    print("*" * i, " ")
    i -= 1

print()
# Задание 4

h = 9
w = 1
for i in range(h):
    for j in range(w):
        print("*" * i)





