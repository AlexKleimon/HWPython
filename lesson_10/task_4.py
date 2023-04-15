"""
Задание 4.
Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).
Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""
words = ["разработка", "администрирование", "protocol", "standard"]
for word in words:
    b_word = word.encode('utf-8')
    print(f"\n{word} -> {b_word}")
    s_word = b_word.decode('utf-8')
    print(f"{b_word} -> {s_word}")
