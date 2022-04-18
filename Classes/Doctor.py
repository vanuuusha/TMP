from .Human import Human


class Doctor(Human):
    def __init__(self, name, surname, age):
        super().__init__(name=name, surname=surname, age=age)