class Human:
    def __init__(self, name, surname, age):
        self.name = name.lower().title()
        self.surname = surname.lower().title()
        self.age = age