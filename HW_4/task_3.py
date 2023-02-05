"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
 """

# решение без функции sort()
def my_func(arg_1, arg_2, arg_3):
    if arg_1 < arg_2:
        return arg_2 + arg_3
    elif arg_2 < arg_1:
        return arg_1 + arg_3
    else:
        return arg_1 + arg_2


num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))
num_3 = int(input('Введите третье число: '))

print(f'сумма наибольших двух чисел ( без функции sort): {my_func(num_1, num_2, num_3)}')

# решение с функцией sort()
def my_func(arg_1, arg_2, arg_3):
    if arg_1 < arg_2:
        return arg_2 + arg_3
    elif arg_2 < arg_1:
        return arg_1 + arg_3
    else:
        return arg_1 + arg_2


print(f'сумма наибольших двух чисел ( с функцией sort): {my_func(num_1, num_2, num_3)}')
