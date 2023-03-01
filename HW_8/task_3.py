"""
3) Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
eng = ["One", "Two", "Three", "Four", "Five"]
rus = ["один", "два", "три", "четыре", "пять"]

with open('file_task_3.txt', 'r', encoding='utf-8') as file:
    data = file.read()
    print(data)
    for i, word in enumerate(eng):
        if word in data:
            data = data.replace(word, rus[i])
    print(data)
with open('file_task_3end.txt', 'w', encoding='utf-8') as file:
    file.write(data)
