from .Human import Human


class Doctor(Human):
    def __init__(self, name, surname, second_surname, profession, experience):
        super().__init__(name=name, surname=surname, second_surname=second_surname)
        self.profession = profession
        self.experience = experience

    def show_info(self):
        return ''.join([self.surname, ' ', self.name, ' ', self.second_surname, '. Специальность: ', self.profession, ', Стаж: ', str(self.experience), f' {"лет" if self.experience >= 5 else "года"}'])


