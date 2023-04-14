"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт,
осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt,
info_3.txt и формирующий новый «отчетный» файл в формате CSV.

Для этого:

Создать функцию get_data(), в которой в цикле осуществляется перебор файлов
с данными, их открытие и считывание данных. В этой функции из считанных данных
необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список. Должно
получиться четыре списка — например, os_prod_list, os_name_list,
os_code_list, os_type_list. В этой же функции создать главный список
для хранения данных отчета — например, main_data — и поместить в него
названия столбцов отчета в виде списка: «Изготовитель системы»,
«Название ОС», «Код продукта», «Тип системы». Значения для этих
столбцов также оформить в виде списка и поместить в файл main_data
(также для каждого файла);

Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(),
а также сохранение подготовленных данных в соответствующий CSV-файл;

Пример того, что должно получиться:

Изготовитель системы,Название ОС,Код продукта,Тип системы

1,LENOVO,Windows 7,00971-OEM-1982661-00231,x64-based

2,ACER,Windows 10,00971-OEM-1982661-00231,x64-based

3,DELL,Windows 8.1,00971-OEM-1982661-00231,x86-based

Обязательно проверьте, что у вас получается примерно то же самое.

ПРОШУ ВАС НЕ УДАЛЯТЬ СЛУЖЕБНЫЕ ФАЙЛЫ TXT И ИТОГОВЫЙ ФАЙЛ CSV!!!
"""
import csv
import re


def get_data():
    ls_name_file = ["info_1.txt", "info_2.txt", "info_3.txt"]
    number_ls = ["1", "2", "3"]
    main_data = [[
        'Изготовитель системы',
        'Название ОС',
        'Код продукта',
        'Тип системы'
    ]]
    os_prod_list = list()
    os_name_list = list()
    os_code_list = list()
    os_type_list = list()
    pattern_product = re.compile(r"Изготовитель системы:\s*(\S+)")
    pattern_name = re.compile(r"Название ОС:\s*(\S+\s+\S+\s+\S+)")
    pattern_code = re.compile(r"Код продукта:\s*(\S+)")
    pattern_type = re.compile(r"Тип системы:\s*(\S*)")
    for name in ls_name_file:
        with open(name) as txt_file:
            data = txt_file.read()
        os_prod_list.append(pattern_product.findall(data)[0])
        os_name_list.append(pattern_name.findall(data)[0])
        os_code_list.append(pattern_code.findall(data)[0])
        os_type_list.append(pattern_type.findall(data)[0])
    zip_obj = zip(
        number_ls, os_prod_list, os_name_list, os_code_list, os_type_list)
    for element in list(zip_obj):
        main_data.append(list(element))
    return main_data


def rite_to_csv():
    data = get_data()
    with open("test.csv", "w", encoding='utf-8') as csv_file:
        wr_csv = csv.writer(csv_file, delimiter=",")
        for text in data:
            wr_csv.writerow(text)


rite_to_csv()
