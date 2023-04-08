"""
3. Задание на закрепление знаний по модулю yaml.
 Написать скрипт, автоматизирующий сохранение данных
 в файле YAML-формата.
Для этого:

Подготовить данные для записи в виде словаря, в котором
первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа —
это целое число с юникод-символом, отсутствующим в кодировке
ASCII(например, €);

Реализовать сохранение данных в файл формата YAML — например,
в файл file.yaml. При этом обеспечить стилизацию файла с помощью
параметра default_flow_style, а также установить возможность работы
с юникодом: allow_unicode = True;

Реализовать считывание данных из созданного файла и проверить,
совпадают ли они с исходными.
"""

import yaml

dict_data = {
    "items": ["PC", "Printer", "Keyboard", "Mouse"],
    "item_quantity": 4,
    "item_price": {
        "PC": "200€-1000€",
        "Printer": "100€-300€",
        "Keyboard": "5€-50€",
        "Mouse": "4€-7€"
    }
}

with open("file.yaml", "w", encoding="UTF-8") as ym_file:
    yaml.dump(dict_data, ym_file, default_flow_style=False,
              allow_unicode=True, sort_keys=False)
with open("file.yaml", encoding="UTF-8") as ym_file:
    data = yaml.load(ym_file, Loader=yaml.FullLoader)
if data == dict_data:
    print(f"Данные совпадают!\nС файла: {data}\nИсходник: {dict_data}")
