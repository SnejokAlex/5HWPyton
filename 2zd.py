# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых
# неотрицательных чисел. Из всех арифметических операций допускаются 
# только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
#     4 

def f(n, k):
    if k == 0:
        return n
    return f(n+1,k-1)
n = int(input('Введите первое число'))
k = int(input('введите второе число'))
print(f(n, k))