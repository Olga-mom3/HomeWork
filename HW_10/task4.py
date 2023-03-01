"""
Задание 4.
Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).
Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

words = ['разработка', 'администрирование', 'protocol', 'standard']

for word in words:
    str_bytes = word.encode('utf-8')
    bytes_str = str_bytes.decode('utf-8')
    print(f'Слово: "{word}" перевод в байты - {str_bytes}')
    print(f'из байтов в строку - {bytes_str}')
    print()