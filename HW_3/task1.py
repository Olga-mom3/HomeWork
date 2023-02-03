"""
1. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.
Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""
# day = int(input("Введите месяц в виде целого числа от 1 до 12 : "))
# dct={1:'зима',2:'зима', 12:'зима', 3:'весна', 4:'весна', 5:'весна', 6:'лето', 7:'лето',8:'лето',9:'осень',10:'осень',11:'осень'}

seasons_dict = {'Зима': (1, 2, 12),
                'Весна': (3, 4, 5),
                'Лето': (6, 7, 8),
                'Осень': (9, 10, 11)}
seasons_list = ['Зима','Весна','Лето','Осень']

month = int(input('Введите месяц в виде целого числа от 1 до 12 : '))
if 1 <= month <= 12:
    """
 Решение через словарь
    """
for key, value in seasons_dict.items():
    if month in value:
        print(f'результат через словарь: {key}')

    """
  Решение через список
    """
if month == 1 or month == 2 or month == 12:
    print(f'результат через словарь: {seasons_list[0]}')
elif month == 3 or month == 4 or month == 5:
    print(f'результат через словарь: {seasons_list[1]}')
elif month == 6 or month == 7 or month == 8:
    print(f'результат через список: {seasons_list[2]}')
elif month == 9 or month == 10 or month == 11:
    print(f'результат через словарь: {seasons_list[3]}')

else:
    print(f'Ошибка. Нет такого месяца.')
