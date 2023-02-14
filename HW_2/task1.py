"""
Задание 1.
Спортсмен занимается ежедневными пробежками.
В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня,
на который результат спортсмена составит не менее b километров.
Программа должна принимать значения параметров a и b
и выводить одно натуральное число — номер дня.
Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22
Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
"""
start_km = float(input('Укажите километраж первого дня: '))
finish_km = float(input('Укажите желаемый километраж: '))
day = 1
print(f'{day}-ый день: {start_km:.2f}')
while start_km < finish_km:
    start_km *= 1.1
    day += 1
    print(f'{day}-ый день: {start_km:.2f} ')
print(f'Ответ: на {day}-ый день спортсмен достиг результата — не менее {finish_km:.0f} км')