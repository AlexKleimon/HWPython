"""
Задание 5.
Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.
Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""
import subprocess
import chardet

yandex = ['ping', 'yandex.ru']
ya_ping = subprocess.Popen(yandex, stdout=subprocess.PIPE)
for line in ya_ping.stdout:
    result = chardet.detect(line)
    print(line.decode(encoding=result['encoding']))

youtube = ['ping', 'youtube.com']
yt_ping = subprocess.Popen(youtube, stdout=subprocess.PIPE)
for line in yt_ping.stdout:
    result = chardet.detect(line)
    print(line.decode(encoding=result['encoding']))
