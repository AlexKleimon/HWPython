"""
2. Задание на закрепление знаний по модулю json. Есть файл orders
в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий
его заполнение данными.

Для этого:
Создать функцию write_order_to_json(), в которую передается
5 параметров — товар (item), количество (quantity), цена (price),
покупатель (buyer), дата (date). Функция должна предусматривать запись
данных в виде словаря в файл orders.json. При записи данных указать
величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json()
с передачей в нее значений каждого параметра.

ПРОШУ ВАС НЕ УДАЛЯТЬ ИСХОДНЫЙ JSON-ФАЙЛ
ПРИМЕР ТОГО, ЧТО ДОЛЖНО ПОЛУЧИТЬСЯ

{
    "orders": []
}

вам нужно подгрузить JSON-объект
и достучаться до списка, который и нужно пополнять
а потом сохранять все в файл
"""
import json


def write_order_to_json(dc_js):
    with open("orders.json") as js_file:
        data = json.load(js_file)
    temp = list(data["orders"])
    temp.append(dc_js)
    data["orders"] = temp
    with open("orders.json", "w") as js_file:
        json.dump(data, js_file, ensure_ascii=False, indent=4)


def dict_json(*args):
    list_key = ["item", "quantity", "price", "buyer", "date"]
    dict_data = dict()
    index = 0
    for key in list_key:
        dict_data[key] = args[index]
        index += 1
    return dict_data


item = input("Введите товар: ")
price = input("Введите цену: ")
write_order_to_json(dict_json(item, "1", price, "Petrov P.P.", "11.12.23"))
