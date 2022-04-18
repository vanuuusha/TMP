import tkinter as tk
from checker import fio_checker, age_checker
from Classes.Doctor import Doctor
from Classes.Patient import Patient

console_text = "Результат ваших действий: "
CONSTFORBIGBUTTONS = 22
CONSTFORDEFAULTBUTTONS = 17
CONSTFORMINIBUTTONS = 8


class Form:
    def __init__(self): # тут объявляются необходимые переменные и константы и создается окно
        self.what_show = 0
        self.doctors, self.patients, self.elements = [], [], {}
        self.font = "Arial 14"
        self.font_color = "black"

        self.window = tk.Tk()
        self.add_console(console_text)
        self.window.title('Поликлиника')
        self.window.geometry("1400x900")
        self.show()

    def add_new_console(self, text):
        self.console.destroy()
        self.add_console(text)

    def add_console(self, text):
        self.console = tk.Label(
            self.window,
            text=text,
            foreground=self.font_color,
            font=self.font,
        )
        self.console.place(x=600, y=100)

    def destroy_all(self): # удаляет все текущие элементы
        for elem in self.elements.keys():
            self.elements[elem].destroy()
        self.elements = {}

    def show(self): # выбирает что положить в окно
        self.destroy_all()
        if self.what_show == 0:
            self.show_start_menu()
        elif self.what_show == 1:
            self.show_add_doctor_menu()
        elif self.what_show == 2:
            self.show_add_patient_menu()
        self.window.mainloop()

    def go_main(self):
        self.add_new_console(console_text + "Возвращение на главный экран")
        self.what_show = 0
        self.show()

    def show_add_patient_menu(self): # меню при добавлении пациента
        self.add_label('Имя нового пациента: ', position=[100, 100])
        self.add_entry(position=[100, 150])
        self.add_label('Фамилия нового Пациента: ', position=[100, 200])
        self.add_entry(position=[100, 250])
        self.add_label('Дата рождения нового Пациента (через точки): ', position=[100, 300])
        self.add_entry(position=[100, 350])
        self.add_button("Добавить", self.check_correct_patient, position=[100, 400], width=CONSTFORDEFAULTBUTTONS)
        self.add_button("Отменить", self.go_main, position=[350, 400], width=CONSTFORDEFAULTBUTTONS)

    def show_add_doctor_menu(self): # меню при добавлении доктора
        self.add_label('Имя нового врача: ', position=[100, 100])
        self.add_entry(position=[100, 150])
        self.add_label('Фамилия нового врача: ', position=[100, 200])
        self.add_entry(position=[100, 250])
        self.add_label('Дата рождения нового врача (через точки): ', position=[100, 300])
        self.add_entry(position=[100, 350])
        self.add_button("Добавить", self.check_correct_doctor, position=[100, 400], width=CONSTFORDEFAULTBUTTONS)
        self.add_button("Отменить", self.go_main, position=[350, 400], width=CONSTFORDEFAULTBUTTONS)

    def show_start_menu(self): # картинка стартового меню
        self.add_label(f'В поликлинике работает: {len(self.doctors)} врачей', position=[100, 100])
        self.add_label(f'За поликлиникой закреплено : {len(self.patients)} пациентов', position=[100, 150])
        self.add_button('Добавить врача', self.add_doctor, position=[100, 225], width=CONSTFORDEFAULTBUTTONS)
        self.add_button('Показать всех врачей', self.show_all_doctors, position=[350, 225], width=CONSTFORBIGBUTTONS)
        self.add_button('Добавить пациента', self.add_patient, position=[100, 300], width=CONSTFORDEFAULTBUTTONS)
        self.add_button('Показать всех пациентов', self.show_all_pations, position=[350, 300], width=CONSTFORBIGBUTTONS)
        self.show_more_info_from_flag = False
        self.add_button('Оцифровать архив', self.show_more_info_from, position=[100, 375], width=CONSTFORDEFAULTBUTTONS)

    def packer(self, vidget, name, position): # добавляет элемент в массив с текущими элементами на форме и отображает его
        count = 1
        start_name = name
        while name in self.elements.keys():
            count += 1
            name = ''.join([start_name, str(count)])
        self.elements[name] = vidget
        vidget.place(x=position[0], y=position[1])

    def add_entry(self, position): # добавить поле ввода
        entry = tk.Entry(
            self.window,
            foreground=self.font_color,
            font=self.font,
        )
        self.packer(entry, 'entry', position)

    def add_label(self, text, position): # добавить надпись
        label = tk.Label(
            self.window,
            text=text,
            height=2,
            foreground=self.font_color,
            font=self.font,
        )
        self.packer(label, 'label', position)

    def add_button(self, text, command, position, width): # добавить кнопку
        button = tk.Button(
            self.window,
            text=text,
            background="blue",
            foreground=self.font_color,
            font=self.font,
            width=width,
            height=2,
            command=command,
        )
        self.packer(button, 'button', position)

    def add_patient(self): # вызывается при нажатии на кнопку добавить пациента
        self.add_new_console(console_text + "Переход на страницу добавления пациента")
        self.what_show = 2
        self.show()

    def add_doctor(self): # вызывается при нажатии на кнопку добавить доктора
        self.add_new_console(console_text + "Переход на страницу добавления доктора")
        self.what_show = 1
        self.show()

    def check_correct_doctor(self): # Вызывается при нажатии на кнопку выполнить в меню доктора
        name, name_flag = fio_checker(self.elements.get('entry').get())
        surname, surname_flag = fio_checker(self.elements.get('entry2').get())
        age_flag = age_checker(self.elements.get('entry3').get(), 8395)
        age = self.elements.get('entry3').get()
        text = ""
        if not name_flag:
            text = "Имя доктора введено некорректно, повторите попытку"
        if not surname_flag:
            text = "Фамилия доктора введена некорректно, повторите попытку"
        if not age_flag:
            text = "Дата рождения доктора введена неверно\nУчтите что доктором можно стать только если " \
                                  "родился хотя бы 23 года назад "
        if name_flag and surname_flag and age_flag:
            self.doctors.append(Doctor(name, surname, age))
            self.what_show = 0
            self.add_new_console(console_text + "Доктор успешно добавлен")
            self.show()
        else:
            self.add_new_console(console_text + text)

    def check_correct_patient(self): # Вызывается при нажатии на кнопку выполнить в меню пациента
        name, name_flag = fio_checker(self.elements.get('entry').get())
        surname, surname_flag = fio_checker(self.elements.get('entry2').get())
        age_flag = age_checker(self.elements.get('entry3').get(), 0)
        age = self.elements.get('entry3').get()
        text = ""
        if not name_flag:
            text = "Имя пациента введено некорректно, повторите попытку"
        if not surname_flag:
            text = "Фамилия пациента введена некорректно, повторите попытку"
        if not age_flag:
            text = "Дата рождения пациента введена неверно"
        if name_flag and surname_flag and age_flag:
            self.patients.append(Patient(name, surname, age))
            self.what_show = 0
            self.add_new_console(console_text + "Пациент успешно добавлен")
            self.show()
        else:
            self.add_new_console(console_text + text)

    def show_all_doctors(self): # показывает всех докторов
        text = console_text
        count = 1
        for elem in self.doctors:
            text = '\n\t'.join([text, ''.join([str(count), ') ФИ: ', elem.surname, ' ', elem.name, ' Возраст: ', elem.age])])
            count += 1
        if text == console_text:
            text += "\n\tВрачей пока нет"
        self.add_new_console(text)

    def show_all_pations(self): # показывает всех пациентов
        text = console_text
        count = 1
        for elem in self.patients:
            text = '\n\t'.join([text, ''.join([str(count), ') ФИ: ', elem.surname, ' ', elem.name, ' Возраст: ', elem.age])])
            count += 1
        if text == console_text:
            text += "\n\tПациентов пока нет"
        self.add_new_console(text)

    def show_more_info_from(self): # взять информацию из файлов
        if not self.show_more_info_from_flag:
            self.add_button('Excel', self.get_from_excel, position=[350, 375],
                            width=CONSTFORMINIBUTTONS)
            self.add_button('.txt', self.get_from_txt, position=[505, 375],
                            width=CONSTFORMINIBUTTONS)
            self.show_more_info_from_flag = True
        else:
            self.elements['button6'].destroy()
            self.elements['button7'].destroy()
            self.elements.pop('button6')
            self.elements.pop('button7')
            self.show_more_info_from_flag = False

    def get_from_excel(self):
        pass

    def get_from_txt(self):
        pass



