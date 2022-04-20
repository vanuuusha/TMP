from help_elements import create_button, create_entry, create_label, create_combo_box
from constants import CONSOLETEXT, DOCTOR_PROFESSIONS, MAXEXPERIENCE, MAXLENNAME, DIAGNISISLIST
from checker import fio_checker, experience_checker
from .Doctor import Doctor
from .Patient import Patient


class AdminForm:
    def __init__(self, main):
        self.MainForm = main
        self.MainForm.window.title("Поликлиника (администратор)")
        self.MainForm.create_console('Переход на панель администратора')
        self.show_main_screen()

    def show_main_screen(self):
        self.MainForm.active_elements['admin_label'] = create_label(font_color = "#0C8EEC", text="Вы находитесь в панели администратора, что делать с поликлиникой?", position=[400, 40], background="#b5effb", font="Sedan 14")
        self.MainForm.active_elements['doctor_help_label'] = create_label(font_color = "#0C8EEC",
                                                                          text=f"В поликлинике сейчас {str(len(self.MainForm.doctors))} докторов",
                                                                          position=[400, 80], background="#b5effb", font="Sedan 14")
        self.MainForm.active_elements['pationt_help_label'] = create_label(font_color = "#0C8EEC",
                                                                           text=f"В поликлинике сейчас {str(len(self.MainForm.patients))} пациентов",
                                                                           position=[400, 120], background="#b5effb", font="Sedan 14")
        self.MainForm.active_elements['chose_what_do'] = create_label(font_color="#000000",
                                                                           text=f"Выберите действие:",
                                                                           position=[300, 250], background="#b5effb",
                                                                           font="Sedan 14")
        self.MainForm.active_elements['add_doctor'] = create_button(font_color = '#ffffff',
                                                                    text="Добавить доктора",
                                                                    command=self.add_doctor,
                                                                    position=[275, 300], background = '#2998E9', width = '25', height = '3', font = "Sedan 12")
        self.MainForm.active_elements['add_patient'] = create_button(font_color = '#ffffff',
                                                                     text="Добавить пациента",
                                                                     command=self.add_patient,
                                                                     position=[275, 400], background = '#2998E9', width = '25', height = '3', font = "Sedan 12")
        self.MainForm.active_elements['find_diagnos_label'] = create_label(font_color = "#0C8EEC",
                                                                           text=f"Поиск по диагнозу",
                                                                           position=[800, 100], background="#b5effb", font="Sedan 14")
        self.MainForm.active_elements['find_diagnos_combo'] = create_combo_box(width = 12, font_color = "#000000",
                                                                         position=[800, 150],
                                                                         values=DIAGNISISLIST, default=None,
                                                                               callback=self.show_find, font = "Sedan 14")
        self.MainForm.active_elements['show_doctors'] = create_button(font_color = '#ffffff',
                                                                    text="Показать докторов",
                                                                    command=self.show_all_doctors,
                                                                    position=[275, 500], background = '#2998E9', width = '25', height = '3', font = "Sedan 12")
        self.MainForm.active_elements['show_pationts'] = create_button(font_color = '#ffffff',
                                                                     text="Показать пациентов",
                                                                     command=self.show_all_patients,
                                                                     position=[275, 600], background = '#2998E9', width = '25', height = '3', font = "Sedan 12")
        self.MainForm.active_elements['go_back'] = create_button(font_color = '#ffffff', text="Вернуться на основной экран",
                                                                 command=self.MainForm.return_to_main_screen,
                                                                 position=[1000, 700], background = '#2998E9', width = '25', height = '3', font = "Sedan 12")

    def show_find(self, event):
        text = f"Люди с {self.MainForm.active_elements.get('find_diagnos_combo').get()}:"
        for patient in self.MainForm.patients:
            if self.MainForm.active_elements['find_diagnos_combo'].get() in patient.diagnos:
                text += f'\n{patient.get_fio()}'
        if text == f"Люди с {self.MainForm.active_elements.get('find_diagnos_combo').get()}:":
            text += "\nПо вашему запросу никого не найдено"
        self.MainForm.create_console(text)

    def return_to_admin_screen(self):
        self.MainForm.create_console('Возврат в панель администратора')
        self.MainForm.destroy_all()
        self.show_main_screen()

    def add_patient(self):
        self.MainForm.destroy_all()
        self.MainForm.create_console('Переход на страницу добавления пациента')
        self.MainForm.active_elements['patient_label'] = create_label(font_color="#0C8EEC",
                                                                    text="Страница добавления пациента",
                                                                    position=[400, 40], background="#b5effb",
                                                                    font="Sedan 14")
        self.MainForm.active_elements['patient_name'] = create_label(font_color="#000000",
                                                                     text="Имя пациента", position=[325, 350], background="#b5effb",
                                                                        font="Sedan 14")
        self.MainForm.active_elements['patient_name_entry'] = create_entry(width=25, font = "Sedan 14",
                                                                           position=[250, 400], font_color = "#000000")
        self.MainForm.active_elements['patient_surname'] = create_label(font_color="#000000",
                                                                        text="Фамилия пациента", position=[325, 250], background="#b5effb",
                                                                        font="Sedan 14")
        self.MainForm.active_elements['patient_surname_entry'] = create_entry(width=25, font = "Sedan 14",
                                                                              position=[250, 300], font_color = "#000000")
        self.MainForm.active_elements['patient_second_surname'] = create_label(font_color="#000000",
                                                                               text="Отчество пациента",
                                                                               position=[325, 450], background="#b5effb",
                                                                            font="Sedan 14")
        self.MainForm.active_elements['patient_second_surname_entry'] = create_entry(width=25, font = "Sedan 14",
                                                                                     position=[250, 500], font_color = "#000000")

        self.MainForm.active_elements['go_back'] = create_button(font_color = '#ffffff', text="Назад",
                                                                 command=self.return_to_admin_screen,
                                                                 position = [1000, 700], background = '#2998E9', width = '25', height = '3', font = "Sedan 12")
        self.MainForm.active_elements['complete'] = create_button(font_color = '#ffffff', text="Выполнить",
                                                                  command=self.add_new_pationt, position=[325, 550], background = '#2998E9', width =12, height = '3', font = "Sedan 12")

    def add_doctor(self):
        self.MainForm.destroy_all()
        self.MainForm.create_console('Переход на страницу добавления доктора')
        self.MainForm.active_elements['doctor_label'] = create_label(font_color="#0C8EEC",
                                                                      text="Страница добавления доктора",
                                                                      position=[400, 40], background="#b5effb",
                                                                      font="Sedan 14")
        self.MainForm.active_elements['doctor_name'] = create_label(font_color="#000000",
                                                                    text="Имя доктора", position=[325, 350], background="#b5effb",
                                                                        font="Sedan 14")
        self.MainForm.active_elements['doctor_name_entry'] = create_entry(width=25, font = "Sedan 14",
                                                                           position=[250, 400], font_color = "#000000")
        self.MainForm.active_elements['doctor_surname'] = create_label(font_color="#000000",
                                                                       text="Фамилия доктора", position=[325, 250], background="#b5effb",
                                                                        font="Sedan 14")
        self.MainForm.active_elements['doctor_surname_entry'] = create_entry(width=25, font = "Sedan 14",
                                                                              position=[250, 300], font_color = "#000000")
        self.MainForm.active_elements['doctor_second_surname'] = create_label(font_color="#000000",
                                                                              text="Отчество доктора", position = [325, 450], background = "#b5effb",
                                              font = "Sedan 14")
        self.MainForm.active_elements['doctor_second_surname_entry'] = create_entry(width=25, font = "Sedan 14",
                                                                                     position=[250, 500], font_color = "#000000")
        self.MainForm.active_elements['doctor_prof'] = create_label(font_color="#000000",
                                                                    text="Специализация доктора", position=[325, 550], background="#b5effb",
                                                                            font="Sedan 14")

        self.MainForm.active_elements['doctor_prof_entry'] = create_combo_box(width = 25, font_color = "#000000",
                                                                              position=[250, 600],
                                                                              values=DOCTOR_PROFESSIONS, font = "Sedan 14", default = None)
        self.MainForm.active_elements['doctor_experience'] = create_label(font_color="#000000",
                                                                          text="Стаж доктора", position=[325, 650], background="#b5effb",
                                                                            font="Sedan 14")
        self.MainForm.active_elements['doctor_experience_entry'] = create_entry(width=25, font = "Sedan 14",
                                                                                     position=[250, 700], font_color = "#000000")
        self.MainForm.active_elements['go_back'] = create_button(font_color = '#ffffff', text="Назад",
                                                                 command=self.return_to_admin_screen,
                                                                 position = [1000, 700], background = '#2998E9', width = '25', height = '3', font = "Sedan 12")
        self.MainForm.active_elements['complete'] = create_button(font_color = '#ffffff', text="Выполнить",
                                                                  command=self.add_new_doctor, position=[300, 750], background = '#2998E9', width =12, height = '3', font = "Sedan 12")

    def add_new_doctor(self):
        name, name_flag = fio_checker(self.MainForm.active_elements['doctor_name_entry'].get())
        surname, surname_flag = fio_checker(self.MainForm.active_elements['doctor_surname_entry'].get())
        second_surname, second_surname_flag = fio_checker(
            self.MainForm.active_elements['doctor_second_surname_entry'].get())
        experience, experience_flag = experience_checker(self.MainForm.active_elements['doctor_experience_entry'].get())
        if not name_flag:
            self.MainForm.create_console(
                f"Имя введено неверно\n Учтите что длина имени не может превышать {MAXLENNAME} символов")
        if not surname_flag:
            self.MainForm.create_console(
                f"Фамилия введена неверно\n Учтите что длина фамилии не может превышать {MAXLENNAME} символов")
        if not second_surname_flag:
            self.MainForm.create_console(
                f"Отчество введено неверно\n Учтите что длина отчества не может превышать {MAXLENNAME} символов")
        if not experience_flag:
            self.MainForm.create_console(
                f"Стаж введен неверно\n Учтите что стаж не может превышать {MAXEXPERIENCE} лет")
        if name_flag and surname_flag and second_surname_flag and experience_flag:
            self.MainForm.doctors.append(
                Doctor(name=name, surname=surname, second_surname=second_surname, experience=experience,
                       profession=self.MainForm.active_elements['doctor_prof_entry'].get()))
            self.return_to_admin_screen()

    def add_new_pationt(self):
        name, name_flag = fio_checker(self.MainForm.active_elements['patient_name_entry'].get())
        surname, surname_flag = fio_checker(self.MainForm.active_elements['patient_surname_entry'].get())
        second_surname, second_surname_flag = fio_checker(
            self.MainForm.active_elements['patient_second_surname_entry'].get())
        if not name_flag:
            self.MainForm.create_console(
                f"Имя введено неверно\n Учтите что длина имени не может превышать {MAXLENNAME} символов")
        if not surname_flag:
            self.MainForm.create_console(
                f"Фамилия введена неверно\n Учтите что длина фамилии не может превышать {MAXLENNAME} символов")
        if not second_surname_flag:
            self.MainForm.create_console(
                f"Отчество введено неверно\n Учтите что длина отчества не может превышать {MAXLENNAME} символов")
        if name_flag and surname_flag and second_surname_flag:
            self.MainForm.patients.append(Patient(name=name, surname=surname, second_surname=second_surname))
            self.return_to_admin_screen()

    def show_all_doctors(self):
        self.MainForm.destroy_all()
        self.MainForm.active_elements['go_back'] = create_button(font_color='#ffffff', text="Назад",
                                                                 command=self.return_to_admin_screen,
                                                                 position=[1000, 700], background='#2998E9', width='25',
                                                                 height='3', font="Sedan 12")

        text = ""
        count = 1
        for doctor in self.MainForm.doctors:
            text = ''.join([text, f'\n{count}) ', doctor.show_info()])
            count += 1
        if text == "":
            text += "Докторов пока нет"
        self.MainForm.create_big_console(text)

    def show_all_patients(self):
        text = ""
        self.MainForm.destroy_all()
        self.MainForm.active_elements['go_back'] = create_button(font_color='#ffffff', text="Назад",
                                                                 command=self.return_to_admin_screen,
                                                                 position=[1000, 700], background='#2998E9', width='25',
                                                                 height='3', font="Sedan 12")
        count = 1
        for pationt in self.MainForm.patients:
            text = ''.join([text, f'\n{count}) ', pationt.show_info()])
            count += 1
        if text == "":
            text += "\n Пациентов пока нет"
        self.MainForm.create_big_console(text)
