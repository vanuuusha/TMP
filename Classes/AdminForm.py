from help_elements import create_button, create_entry, create_label, create_combo_box
from constants import DEFAULTKWARGSBUTTON, DEFAULTKWARGSLABEL, DEFAULTKWARGSENTRY, CONSOLETEXT, DOCTOR_PROFESSIONS, \
    DEFAULTCOMBOBOX, MAXEXPERIENCE, MAXLENNAME, DIAGNISISLIST
from checker import fio_checker, experience_checker
from .Doctor import Doctor
from .Patient import Patient


class AdminForm:
    def __init__(self, main):
        self.MainForm = main
        self.MainForm.window.title("Поликлиника (администратор)")
        self.MainForm.create_console(CONSOLETEXT + '\tПереход на панель администратора')
        self.show_main_screen()

    def show_main_screen(self):
        self.MainForm.active_elements['admin_label'] = create_label(width=60, **DEFAULTKWARGSLABEL,
                                                                    text="Вы находитесь в панели администратора, что делать с поликлиникой?",
                                                                    position=[100, 100])
        self.MainForm.active_elements['doctor_help_label'] = create_label(width=60, **DEFAULTKWARGSLABEL,
                                                                          text=f"В поликлинике сейчас {str(len(self.MainForm.doctors))} докторов",
                                                                          position=[100, 600])
        self.MainForm.active_elements['pationt_help_label'] = create_label(width=60, **DEFAULTKWARGSLABEL,
                                                                           text=f"В поликлинике сейчас {str(len(self.MainForm.patients))} пациентов",
                                                                           position=[100, 700])
        self.MainForm.active_elements['add_doctor'] = create_button(width=15, **DEFAULTKWARGSBUTTON,
                                                                    text="Добавить доктора",
                                                                    command=self.add_doctor,
                                                                    position=[400, 200])
        self.MainForm.active_elements['add_patient'] = create_button(width=15, **DEFAULTKWARGSBUTTON,
                                                                     text="Добавить пациента",
                                                                     command=self.add_patient,
                                                                     position=[400, 300])
        self.MainForm.active_elements['find_diagnos_label'] = create_label(width=60, **DEFAULTKWARGSLABEL,
                                                                           text=f"Поиск по диагнозу",
                                                                           position=[450, 650])
        self.MainForm.active_elements['find_diagnos_combo'] = create_combo_box(width=30, **DEFAULTCOMBOBOX,
                                                                         position=[450, 700],
                                                                         values=DIAGNISISLIST, default=None,
                                                                               callback=self.show_find)
        self.MainForm.active_elements['show_doctors'] = create_button(width=15, **DEFAULTKWARGSBUTTON,
                                                                    text="Показать докторов",
                                                                    command=self.show_all_doctors,
                                                                    position=[200, 200])
        self.MainForm.active_elements['show_pationts'] = create_button(width=15, **DEFAULTKWARGSBUTTON,
                                                                     text="Показать пациентов",
                                                                     command=self.show_all_patients,
                                                                     position=[200, 300])
        self.MainForm.active_elements['go_back'] = create_button(width=15, **DEFAULTKWARGSBUTTON, text="Основной экран",
                                                                 command=self.MainForm.return_to_main_screen,
                                                                 position=[400, 500])

    def show_find(self, event):
        text = ""
        for patient in self.MainForm.patients:
            if self.MainForm.active_elements['find_diagnos_combo'].get() in patient.diagnos:
                text += f'\n{patient.get_fio()}'
        self.MainForm.create_console(CONSOLETEXT+text)

    def return_to_admin_screen(self):
        self.MainForm.create_console(CONSOLETEXT + '\tВозврат в панель администратора')
        self.MainForm.destroy_all()
        self.show_main_screen()

    def add_patient(self):
        self.MainForm.destroy_all()
        self.MainForm.create_console(CONSOLETEXT + '\tПереход на страницу добавления пациента')
        self.MainForm.active_elements['patient_name'] = create_label(width=60, **DEFAULTKWARGSLABEL,
                                                                     text="Имя пациента", position=[100, 100])
        self.MainForm.active_elements['patient_name_entry'] = create_entry(width=30, **DEFAULTKWARGSENTRY,
                                                                           position=[100, 200])
        self.MainForm.active_elements['patient_surname'] = create_label(width=60, **DEFAULTKWARGSLABEL,
                                                                        text="Фамилия пациента", position=[100, 300])
        self.MainForm.active_elements['patient_surname_entry'] = create_entry(width=50, **DEFAULTKWARGSENTRY,
                                                                              position=[100, 400])
        self.MainForm.active_elements['patient_second_surname'] = create_label(width=30, **DEFAULTKWARGSLABEL,
                                                                               text="Отчество пациента",
                                                                               position=[100, 500])
        self.MainForm.active_elements['patient_second_surname_entry'] = create_entry(width=30, **DEFAULTKWARGSENTRY,
                                                                                     position=[100, 600])

        self.MainForm.active_elements['go_back'] = create_button(width=15, **DEFAULTKWARGSBUTTON, text="Отменить",
                                                                 command=self.return_to_admin_screen,
                                                                 position=[100, 700])
        self.MainForm.active_elements['complete'] = create_button(width=15, **DEFAULTKWARGSBUTTON, text="Выполнить",
                                                                  command=self.add_new_pationt, position=[300, 700])

    def add_doctor(self):
        self.MainForm.destroy_all()
        self.MainForm.create_console(CONSOLETEXT + '\tПереход на страницу добавления доктора')
        self.MainForm.active_elements['doctor_name'] = create_label(width=60, **DEFAULTKWARGSLABEL,
                                                                    text="Имя доктора", position=[100, 100])
        self.MainForm.active_elements['doctor_name_entry'] = create_entry(width=30, **DEFAULTKWARGSENTRY,
                                                                          position=[100, 200])
        self.MainForm.active_elements['doctor_surname'] = create_label(width=60, **DEFAULTKWARGSLABEL,
                                                                       text="Фамилия доктора", position=[100, 300])
        self.MainForm.active_elements['doctor_surname_entry'] = create_entry(width=50, **DEFAULTKWARGSENTRY,
                                                                             position=[100, 400])
        self.MainForm.active_elements['doctor_second_surname'] = create_label(width=30, **DEFAULTKWARGSLABEL,
                                                                              text="Отчество доктора",
                                                                              position=[100, 500])
        self.MainForm.active_elements['doctor_second_surname_entry'] = create_entry(width=30, **DEFAULTKWARGSENTRY,
                                                                                    position=[100, 600])
        self.MainForm.active_elements['doctor_prof'] = create_label(width=30, **DEFAULTKWARGSLABEL,
                                                                    text="Специализация доктора", position=[450, 500])
        self.MainForm.active_elements['doctor_prof_entry'] = create_combo_box(width=30, **DEFAULTCOMBOBOX,
                                                                              position=[450, 600],
                                                                              values=DOCTOR_PROFESSIONS)
        self.MainForm.active_elements['doctor_experience'] = create_label(width=30, **DEFAULTKWARGSLABEL,
                                                                          text="Стаж доктора", position=[750, 500])
        self.MainForm.active_elements['doctor_experience_entry'] = create_entry(width=30, **DEFAULTKWARGSENTRY,
                                                                                position=[750, 600])
        self.MainForm.active_elements['go_back'] = create_button(width=15, **DEFAULTKWARGSBUTTON, text="Отменить",
                                                                 command=self.return_to_admin_screen,
                                                                 position=[100, 700])
        self.MainForm.active_elements['complete'] = create_button(width=15, **DEFAULTKWARGSBUTTON, text="Выполнить",
                                                                  command=self.add_new_doctor, position=[300, 700])

    def add_new_doctor(self):
        name, name_flag = fio_checker(self.MainForm.active_elements['doctor_name_entry'].get())
        surname, surname_flag = fio_checker(self.MainForm.active_elements['doctor_surname_entry'].get())
        second_surname, second_surname_flag = fio_checker(
            self.MainForm.active_elements['doctor_second_surname_entry'].get())
        experience, experience_flag = experience_checker(self.MainForm.active_elements['doctor_experience_entry'].get())
        if not name_flag:
            self.MainForm.create_console(
                CONSOLETEXT + f"\tИмя введено неверно, учтите что длина имени не может превышать {MAXLENNAME} символов")
        if not surname_flag:
            self.MainForm.create_console(
                CONSOLETEXT + f"\tФамилия введена неверно, учтите что длина фамилии не может превышать {MAXLENNAME} символов")
        if not second_surname_flag:
            self.MainForm.create_console(
                CONSOLETEXT + f"\tОтчество введено неверно, учтите что длина отчества не может превышать {MAXLENNAME} символов")
        if not experience_flag:
            self.MainForm.create_console(
                CONSOLETEXT + f"\tСтаж введен неверно, учтите что стаж не может превышать {MAXEXPERIENCE} лет")
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
                CONSOLETEXT + f"\tИмя введено неверно, учтите что длина имени не может превышать {MAXLENNAME} символов")
        if not surname_flag:
            self.MainForm.create_console(
                CONSOLETEXT + f"\tФамилия введена неверно, учтите что длина фамилии не может превышать {MAXLENNAME} символов")
        if not second_surname_flag:
            self.MainForm.create_console(
                CONSOLETEXT + f"\tОтчество введено неверно, учтите что длина отчества не может превышать {MAXLENNAME} символов")
        if name_flag and surname_flag and second_surname_flag:
            self.MainForm.patients.append(Patient(name=name, surname=surname, second_surname=second_surname))
            self.return_to_admin_screen()

    def show_all_doctors(self):
        text = CONSOLETEXT
        for doctor in self.MainForm.doctors:
            text = ''.join([text, '\n', doctor.show_info()])
        if text == CONSOLETEXT:
            text += "\n Докторов пока нет"
        self.MainForm.create_console(text)

    def show_all_patients(self):
        text = CONSOLETEXT
        for pationt in self.MainForm.patients:
            text = ''.join([text, '\n', pationt.show_info()])
        if text == CONSOLETEXT:
            text += "\n Пациентов пока нет"
        self.MainForm.create_console(text)
