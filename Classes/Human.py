class Human:
    def __init__(self, name, surname, second_surname):
        self.name = name.lower().title()
        self.surname = surname.lower().title()
        self.second_surname = second_surname.lower().title()
        self.history = []

    def show_info(self):
        pass

    def make_more_history(self, new_history):
        self.history.append(new_history)

    def show_history(self):
        return '\n'.join(self.history)

    def get_fio(self, number=None):
        if number is not None:
            return ''.join([self.name,' ', self.surname[0], '. ', self.second_surname[0], '. (', str(number), ')'])
        return ''.join([self.name, ' ', self.surname[0], '. ', self.second_surname[0], '.'])