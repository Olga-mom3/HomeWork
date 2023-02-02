"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""

# u_name = input('Введите имя: '),
# surname = input('Введите фамилию: '),
# birth_date = int(input('Введите год рождения: ')),
# place = input('Введите город проживания: '),
# email = input('Введите e-mail: '),
# phone = input('Введите телефон: ')


u_name = input('Введите Ваше имя - ')
surname = input('Введите Вашу фамилию - ')
year = int(input('Введите год Вашего рождения - '))
place = input('Введите город Вашего проживания - ')
email = input('Введите Ваш e-mail - ')
phone = input('Введите Ваш номер телефона - ')


def personal(arg_1, arg_2, arg_3, arg_4, arg_5, arg_6):
    result = f'{u_name} {surname} {year} года рождения, проживает в городе {place}, ' \
             f'e-mail: {email}, телефон: {phone}'
    return result


print(personal(arg_1=u_name, arg_2=surname, arg_3=year, arg_4=place, arg_5=email, arg_6=phone))
