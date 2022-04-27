from .Human import Human


class Patient(Human):
    def __init__(self, name, surname, second_surname, birhaday_date):
        super().__init__(name=name, surname=surname, second_surname=second_surname)
        self.in_que = False
        self.que_for = '-'
        self.birhaday_date = birhaday_date
        self.diagnos = []
        self.history = []
        self.what_wrong = ''

    def show_info(self):
        if self.diagnos == []:
            return ''.join([self.surname, ' ', self.name, ' ', self.second_surname, f". Дата рождения {self.birhaday_date.strftime('%d.%m.%Y')[:10]}" ,f'{f". В очереди к {self.que_for}" if self.in_que else ""} '])
        return ''.join([self.surname, ' ', self.name, ' ', self.second_surname, f". Дата рождения {self.birhaday_date.strftime('%d.%m.%Y')[:10]}" , f' Диагноз{"ы" if len(self.diagnos) > 1 else ""}: ', ', '.join(self.diagnos), f'{f". В очереди к {self.que_for}" if self.in_que else ""}'])