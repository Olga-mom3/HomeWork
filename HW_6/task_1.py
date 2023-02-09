"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""

from sys import argv

name_script, time, rate, bonus = argv

print("Этот скрипт называется : ", name_script)
print("Отработанное время (в часах) : ", time)
print("Ставка в час (руб): ", rate)
print("Премия (руб) : ", bonus)

salary = float(time) * float(rate) + float(bonus)
print(f'Зарплата сотрудника = {salary:.2f} руб')







#
# try:
#     name = str(name)
#     time = int(time)
#     hourly_rate = int(hourly_rate)
#     bonus = int(bonus)
#
#     print(
#         f'заработная плата сотрудника {name} = {time * hourly_rate + bonus / 100}')
# except:
#     print('Ошибка в данных')

