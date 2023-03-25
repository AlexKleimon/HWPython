"""
Задача 20:
В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
ценность. В случае с английским алфавитом очки распределяются так:
A,E,I,O,U,L,N,S,T,R - 1 очко;
D,G - 2 очка;
B,C,M,P - 3 очка;
F,H,V,W,Y - 4 очка;
K - 5 очков;
J,X - 8 очков;
Q,Z - 10 очков;
А русские буквы оцениваются так:
А,В,Е,И,Н,О,Р,С,Т - 1 очко;
Д,К,Л,М,П,У - 2 очка;
Б,Г,Ё,Ь,Я - 3 очка;
Й,Ы - 4 очка;
Ж,З,Х,Ц,Ч - 5 очков;
Ш,Э,Ю - 8 очков;
Ф,Щ,Ъ - 10 очков.
Напишите программу, которая вычисляет стоимость введенного пользователем
слова. Будем считать, что на вход подается только одно слово, которое
содержит либо английские, либо только русские буквы.
Пример:
Слово: ноутбук
Цена: 12
"""


def sum_score(alphabet, word_upp):
    list_keys = list(alphabet.keys())
    score_char = 0
    for char_word in word_upp:
        flag = True
        for count in range(len(list_keys)):
            if flag:
                element_key = list_keys[count]
                for index in range(len(element_key)):
                    if char_word == element_key[index]:
                        score_char += alphabet[element_key]
                        flag = False
                        break
            else:
                break
    return score_char


alphabet_eng = {'AEIOULNSTR': 1, 'DG': 2, 'BCMP': 3, 'FHVWY': 4, 'K': 5,
                'JX': 8, 'QZ': 10}
alphabet_rus = {'АВЕИНОРСТ': 1, 'ДКЛМПУ': 2, 'БГЁЬЯ': 3, 'ЙЫ': 4, 'ЖЗХЦЧ': 5,
                'ШЭЮ': 8, 'ФЩЪ': 10}
language = int(input("Выберите язык -> введите 1 (русский язык) "
                     "или любое другое число (английский): "))
word = input("Введите слово: ").upper()
if language == 1:
    print(sum_score(alphabet_rus, word))
else:
    print(sum_score(alphabet_eng, word))
