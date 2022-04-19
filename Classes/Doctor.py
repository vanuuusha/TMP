from .Human import Human
from constants import DOCTOR_PROFESSIONS


class Doctor(Human):
    def __init__(self, name, surname, second_surname, profession, experience):
        super().__init__(name=name, surname=surname, second_surname=second_surname)
        self.profession = profession
        self.experience = experience

    def show_info(self):
        return ''.join([self.surname, ' ', self.name[0], '. ', self.second_surname[0], '. Специальность: ', self.profession])