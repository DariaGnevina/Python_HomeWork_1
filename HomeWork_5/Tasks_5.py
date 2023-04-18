# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B
# с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8 



def function(a,b):
    if b == 0:
        return 1
    else:
        return a * function(a, b -1)
x = int(input("Введите число А:"))
y = int(input("Введите число B:"))
print(function(x,y))


# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
#     4 

def summa(a,b):
    if a == 0:
        return b
    return summa(a - 1, b + 1)
x = int(input("Введите число А:"))
y = int(input("Введите число B:"))
print(summa(x,y))

# Задача про палиндром (провер с пом рекурсии)

def palindrome(a):
    if len(a) <= 1:
       return print('Это палиндром')
    elif a[0] == a[-1]:
       palindrome(a[1:-1])
    else:
      return print('Это НЕ палиндром')


a = input("Введите текст: ")
palindrome(a)