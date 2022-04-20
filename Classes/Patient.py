from .Human import Human


class Patient(Human):
    def __init__(self, name, surname, second_surname):
        super().__init__(name=name, surname=surname, second_surname=second_surname)
        self.in_que = False
        self.que_for = '-'
        self.diagnos = []
        self.history = []

    def show_info(self):
        if self.diagnos == []:
            return ''.join([self.surname, ' ', self.name[0], '. ', self.second_surname[0], '.'])
        return ''.join([self.surname, ' ', self.name[0], '. ', self.second_surname[0], f'. Диагноз{"ы" if len(self.diagnos) > 1 else ""}: ', ', '.join(self.diagnos)])