"""
Задание 1.
Создать класс TrafficLight (светофор) и определить у него один приватный
атрибут color (цвет) и публичный метод running (запуск). В рамках метода
running реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго
(желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. Для имитации
"горения" каждого цвета испольщуйте ф-цию sleep модуля time Переключение
между режимами должно осуществляться только в указанном порядке
(красный, желтый, зеленый). Проверить работу примера, создав экземпляр и
вызвав описанный метод.
"""
import time


class TrafficLight:
    __color = ["Красный", "Желтый", "Зеленый"]

    def __init__(self, traffic):
        self.traffic = traffic

    def running(self):
        for time_tr in range(1, self.traffic + 1):
            print(f"{time_tr} проход - начало:")
            for el in TrafficLight.__color:
                if "Красный" in el:
                    print(el)
                    time.sleep(7)
                elif "Желтый" in el:
                    print(el)
                    time.sleep(2)
                else:
                    print(el)
                    time.sleep(4)
            print(f"{time_tr} проход - конец.")


light = TrafficLight(3)
light.running()
