"""
 Задание 1. Реализовать дескрипторы для любых двух классов
"""


class Validation:
    def __set__(self, instance, value):
        if type(value) is dict:
            if type(value["wage"]) is int and type(value["bonus"] is int):
                if value["wage"] < 0 or value["bonus"] < 0:
                    raise ValueError("Числовые параметры должны быть "
                                     "больше нуля")
            else:
                raise TypeError("Числовые параметры должны соответствовать"
                                " типу int ")
        if type(value) is str:
            if not value.istitle():
                raise ValueError("Имена должны начинаться с заглавной буквы")
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Worker:
    _income = Validation()
    name = Validation()
    surname = Validation()

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print(f"{self.name} {self.surname} {self.position}")

    def get_total_income(self):
        print(f"Доход: {self._income['wage'] + self._income['bonus']}")

    def __str__(self):
        return (f"З/п: {self._income['wage']}"
                f"\nБонус: {self._income['bonus']}")


a = Position("Иван", "Иванов", "Инженер", 1000, 200)
a.get_full_name()
a.get_total_income()
print(a)


class Valid_Roat:
    def __set__(self, instance, value):
        if type(value) == int:
            if value <= 0:
                raise ValueError("Параметры не могут быть меньше нуля "
                                 "либо равны нулю")
        else:
            raise TypeError("Числовые параметры должны соответствовать"
                            " типу int ")
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Road:
    weight = 25
    thick = 0.05
    _length = Valid_Roat()
    _width = Valid_Roat()

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_road(self):
        return self._length * self._width * self.weight * self.thick


mass_road = Road(20, 5000)
print(f"Результат: {mass_road.mass_road()}")
