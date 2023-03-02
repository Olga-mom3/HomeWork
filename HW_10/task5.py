"""
Задание 5.
Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.
Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import subprocess
import chardet

ARGS = ['yandex.ru', 'youtube.ru']

for ping_el in ARGS:
    PING = subprocess.Popen(['ping', ping_el], stdout=subprocess.PIPE)
    for line in PING.stdout:
        result = chardet.detect(line)
        line = line.decode(result['encoding'])
        print(line)
