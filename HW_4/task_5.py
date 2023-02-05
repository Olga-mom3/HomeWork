"""
5. Сделайте профилирование кода любого или любых выполненных заданий
с помощью модуля timeit, опишите результат
"""

from timeit import timeit

num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))
num_3 = int(input('Введите третье число: '))

def my_func(arg_1, arg_2, arg_3):
    lst = list()
    lst.append(arg_1)
    lst.append(arg_2)
    lst.append(arg_3)
    lst.sort()
    return lst[1] + lst[2]


print(f"Сумма наибольших двух аргументов - {my_func(num_1, num_2, num_3)}")
print(timeit('my_func', globals=globals(), number=100000))

def my_func_1(arg_1, arg_2, arg_3):
    if arg_1 < arg_2:
        return arg_2 + arg_3
    elif arg_2 < arg_1:
        return arg_1 + arg_3
    else:
        return arg_1 + arg_2

print(f'сумма наибольших двух чисел: {my_func_1(num_1, num_2, num_3)}')
print(timeit('my_func_1', globals=globals(), number=100000))

"""
В первом случае 
0.0027772430000001513
Во втором случае
0.0025855290000000863

Со встроенной функцией .sort работает немного медленнее
"""
