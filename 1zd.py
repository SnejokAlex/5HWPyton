# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 
def f(n, k):
    if k == 0:
        return 1
    return n * f(n, k - 1)
n = int(input('Введите число, которое хотите возвести в степень'))
k = int(input('введите в какую степень хотите возвести чесло'))
print(f(n, k))