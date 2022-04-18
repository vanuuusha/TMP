from .Human import Human


class Patient(Human):
    def __init__(self, name, surname, age):
        super().__init__(name=name, surname=surname, age=age)