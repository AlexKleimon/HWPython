"""
Задание 2. Реализовать метакласс. позволяющий создавать всегда один и тот
же объект класса (см. урок)
"""


class Singleton(type):
    inst_cls = None

    def __call__(cls):
        if cls.inst_cls is None:
            cls.inst_cls = super().__call__()
            return cls.inst_cls
        else:
            return cls.inst_cls


class TestSingleton(metaclass=Singleton):
    pass


cls_1 = TestSingleton()
cls_2 = TestSingleton()
cls_3 = TestSingleton()
cls_4 = TestSingleton()
print(f"cls_1 and cls_2: {cls_1 is cls_2}\n"
      f"cls_1 and cls_3: {cls_1 is cls_3}\n"
      f"cls_1 and cls_4: {cls_1 is cls_4}\n"
      f"cls_2 and cls_3: {cls_2 is cls_3}\n"
      f"cls_2 and cls_4: {cls_2 is cls_4}\n"
      f"cls_3 and cls_4: {cls_3 is cls_4}")
