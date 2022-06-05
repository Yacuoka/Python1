# my_list = [1, 2, 3, 4, 5]
# print(my_list)
#
# for i in my_list:
#     print(i**2, end=" ")
#
# for i in range(len(my_list)):
#     my_list[i] += 5
#     print(my_list)


# summa = 0
# a = int(input("Кол-во: "))
# for i in range(a):
#     b = int(input("->"))
#     if b < 0:
#         summa += b
#         print(summa)


# n = list(range(21, 41))
# print(n)
# k = s = 0
# for i in range (len(n)):
#     if n[i] % 2 == 0:
#         k += 1
#     else:
#         s += n[i]
# print(k)
# print(s)


# summa = k = 0
# n = [int(input("->")) for i in range(int(input("n  = ")))]
# for i in range(len(n)):
#     if n[i] != 0:
#         summa += n[i]
#         k += 1
# print(summa / k)


# Срезы - получение какой-то части списка, которая в свою очеред тоже является списком

# s = [1, 4, 3, 4, 5, 8]
# print(s[0])
#
# s = [1, 4, 3, 4, 5, 8]
# print(s[-1])
#
# s = [1, 4, 3, 4, 5, 8]
# print(s[1:4])
#
# s = [1, 4, 3, 4, 5, 8]
# print(s[2:])
#
# s = [1, 4, 3, 4, 5, 8]
# print(s[:4])
#
# s = [1, 4, 3, 4, 5, 8]
# print(s[::])
#
# s = [1, 4, 3, 4, 5, 8]
# print(s[::2])
#
# s = [1, 4, 3, 4, 5, 8]
# print(s[::-1])
#
# s = [1, 4, 3, 4, 5, 8]
# print(s[0:5:1])
#
# s = [1, 4, 3, 4, 5, 8]
# print(s[5:0:-1])
#
# s = [1, 4, 3, 4, 5, 8]
# print(s[5::-1])
#
# s = [1, 4, 3, 4, 5, 8]
# print(s[-2:2:-1])
#
# s = [1, 4, 3, 4, 5, 8]
# print(s[-2:-4:-1])


# s = [1, 2, 3, 4, 5, 6, 7]
# print(s[:])
#
# s = [1, 2, 3, 4, 5, 6, 7]
# print(s[:-1])
#
# s = [1, 2, 3, 4, 5, 6, 7]
# print(s[-1::-1])
#
# s = [1, 2, 3, 4, 5, 6, 7]
# print(s[6::-1])
#
# s = [1, 2, 3, 4, 5, 6, 7]
# print(s[::2])
#
# s = [1, 2, 3, 4, 5, 6, 7]
# print(s[1::2])
#
# s = [1, 2, 3, 4, 5, 6, 7]
# print(s[-1:])
#
# s = [1, 2, 3, 4, 5, 6, 7]
# print(s[3:4])
#
# s = [1, 2, 3, 4, 5, 6, 7]
# print(s[-3:-6:-1])
#
s = [1, 2, 3, 4, 5, 6, 7]
# print(s[4:1:-1])
#
# s = [1, 2, 3, 4, 5, 6, 7]
# print(s[-3:1:-1])

# s = [1, 2, 3, 4, 5, 6, 7]
# s[1:3] = [0, 0, 0, 0]
# s[1:2] = [20]
# s[8] = [20]
# s[9:10] = [20]
# print(s)

#Методы

# s = [1, 2, 3, 4, 5, 6, 7]
# s[1:3] = [0, 0, 0, 0]
# s[1:2] = [20]
# s[8] = [20]
# s.append(99) #добавляет элемент в конец списка
# print(s)

# s1 = []
# s1.extend([1, 2, 3]) #добавляет множество элементов
# print(s1)
# s1.extend('add')
# print(s1)
# s1.append('add')
# print(s1)
# s1.append(['add', 2])
# print(s1)

# l = []
# l.extend(([i**2 for i in range(1, 11)]))
# print("Список квадратов: ", l)
#
# num_array = []
# for i in range(1, 11):
#     num_array.extend[(i**2)]
# print(num_array)

# s = [1, 2, 3, 4, 5, 6, 7]
# s.insert(1,100) # добавляет элемент в список в заданную позицию (первый параметр) и с указанным значением (второй параметр)
# print(s)


# s2 = []
# n = int(input("n  = "))
# for i in range(n):
#     x = int(input("->"))
#     s2.append(x)
# print(s2)


# l = []
# a = int(input("Кол-во элементов списка: "))
# for i in range(a):
#      x = int(input("Введите число кратное 3: "))
#      if x % 3 == 0:
#         l.append(x)
#      else:
#         print(x, "не делится на 3 без остатка")
# print(l)

#Вывести (не)пересекающиеся элементы

# a = [5, 9, 2, 1, 4, 3, 2]
# b = [4, 2, 1, 3, 7, 2]
# c = []
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)


a = [1, 2, 3]
b = [11, 22, 33]
c = []
i = 0
while i < len(a):
    c.append(a[i])
    c.append(b[i])
    i += 1
print(c)

s[7:] = []
print(s)
s.remove(2) #удалить элемент из списка с заданным значением. Если элементов несколько, то удалится первый
print(s)
#
# s[3:5] = []
# print(s)
#
# last = s.pop() #возвращает элемент на указанные позиции, удаляя его из списка
# print(last)
# print(s)
#
# second = s.pop(-2)
# print(second)
# print(s)

# s.clear() #удаляет из списка все значения
# print(s)

# del s[:]
# print(s)

# del s[1]
# print(s)


# l = [int(input("->")) for i in range(int(input("Количество элементов: "))) ]
# k = int(input("Введите индекс k: "))
# l.pop(k)
# print(l)

# s.extend(([3, 1, 20, 3, 4, 50, 3]))
# print(s)
# num = s.count(3) #считает количество значений x в списке
# print(num)
#
# ind = s.index(20) #показывает индекс (первого) элемента
# print(ind)
#
# indx = s.index(20, 3, -1) #значение, начало, конец
# print(indx)
#
# s_copy = s.copy()
# print(s)
# print(s_copy)
#
# a = [1, 2, 3]
# b = a
# print(a)
# print(b)
# a.append(20)
# print(a)
# print(b)
#
# s.append(120)
# print(s)
# print(s_copy)
#
# s. reverse() #реверс элементов списка
# print(s)
#
# s.sort() #сортирует список
# print(s)

# sorted_s = sorted(s)
# print(sorted_s)
# print(s)

# s.sort(reverse=True) #сортировка в порядке убывания
# print(s)
#
# sorted_s = sorted(s, reverse=True)
# print(sorted_s)
# print(s)
#
# n = ["Виталий", "Сергей", "Александр", "Екатерина", "Анна"]
# n.sort(key=len)
# print(n)
#
# n = ["Виталий", "Сергей", "Александр", "Екатерина", "Анна"]
# n.sort(key=len, reverse=True)
# print(n)


# l = [int(input("->")) for i in range(int(input("Введите элементы списка: "))) ]
# k = int(input("Введите элемент: "))
# l.pop(k)
# l.sort(reverse=True)
# print(l)


# import random
# print(random.random())

# from random import random, randint, randrange
# print(random()) #от 0 до 1
# print(randint(0, 9)) #второе значение включается в диапазон
# print(randrange(0, 10, 2)) #start, stop, step


import random as r
print(r.randint(0, 5))
print(r.randint(0, 5))

city = ["Москва", "Новосибирск", "Воронеж", "Сочи", "Екатеринбург"]
print(r.choice(city))


# s = [55, 66, 77, 88, 99]
# print(r.choice(s))

s = [55, 66, 77, 88, 99]
print(r.sample(s, 3))

s1 = [55, 66, 77, 88, 99, 33, 111]
print(r.sample(s1, 5))
print(r.choices(s1, k=5))
r.shuffle(s1)
print(s1)

print(round(r.uniform(10.5, 25.5), 2))

mas = [r.randint(0, 100) for i in range(10)]
print(mas)