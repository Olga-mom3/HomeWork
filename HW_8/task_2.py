"""
2) Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
with open ('file.txt', 'r', encoding='utf-8') as data:
    content = data.readlines()
    print(f'В файле строк - {len(content)} ')
    i = 0
    for el in content:
        i += 1
        print(f'В {i} строке слов - {len(el.split())}')
