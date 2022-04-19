from .Human import Human


class Patient(Human):
    def __init__(self, name, surname, second_surname):
        super().__init__(name=name, surname=surname, second_surname=second_surname)
        self.in_que = False
        self.que_for = '-'
        self.diagnos = []
        self.history = []



    def show_info(self):
        return ''.join([self.surname, ' ', self.name[0], '. ', self.second_surname[0]])
