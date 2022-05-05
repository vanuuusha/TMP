import tkinter as tk
from help_elements import create_button, create_entry, create_label, create_combo_box
from checker import check_correct_admin_password, fio_checker, experience_checker
from .AdminForm import AdminForm
from .DoctorFom import DoctorForm
from .PatientForm import PatientForm
from constants import CONSOLETEXT,  DOCTOR_PROFESSIONS
import os
import pandas as pd
from .Doctor import Doctor
from .Patient import Patient
import datetime


class MainForm:
    def __init__(self):
        self.doctor_auth_active = None
        self.doctors, self.patients = [], []
        self.doctor_ques = {}
        for name_prof in DOCTOR_PROFESSIONS:
            self.doctor_ques[name_prof] = []
        self.active_elements = {}
        self.window = tk.Tk()
        self.window.geometry('1400x875')

        background = tk.PhotoImage(file=os.path.abspath(os.path.join('background.png')))
        self.__background_label = tk.Label(self.window, image=background)
        self.__background_label.place(x=0, y=0, relwidth=1, relheight=1)

        label_name = tk.PhotoImage(file=os.path.abspath(os.path.join('label.png')))
        self.__secret_label = tk.Label(self.window, image=label_name, background='#70e0fa')
        self.__secret_label.place(x=40, y=40)

        self.show_main_screen()
        self.create_console()
        self.window.mainloop()

    def create_console(self, text=""):
        create_label(font_color='#000000',
                     text=CONSOLETEXT, position=[550, 175], font="Sedan 14", background="#30d3f9")

        label = tk.Label(
            text=text,
            font="Sedan 14",
            foreground='#000000',
            background='#ffffff',
            width=50,
            height=16,
        )
        label.place(x=560, y=225)

    def create_big_console(self, text=""):
        self.active_elements['big_console'] = tk.Label(
            text=text,
            font="Sedan 14",
            foreground='#000000',
            background='#ffffff',
            width=100,
            height=22,
        )
        self.active_elements['big_console'].place(x=150, y=200)

    def show_main_screen(self):
        self.window.title("Поликлиника")
        self.active_elements['chose_what_do'] = create_label(font_color='#000000', text="Выберите действие:", position=[280, 175], background="#30d3f9", font="Sedan 14")
        self.active_elements['admin_button'] = create_button(font_color='#ffffff', text="Войти как админ", command=self.show_admin_auth, position=[240, 425], background='#2998E9', width='25', height='3', font="Sedan 12")
        self.doctor_auth_active = False
        self.now_doctors = []
        self.active_elements['doctor_button'] = create_button(font_color='#ffffff', text="Войти как доктор", command=self.show_doctor_auth, position=[240, 325], background='#2998E9', width='25', height='3', font="Sedan 12")
        self.patient_auth_active = False
        self.active_elements['patient_button'] = create_button(font_color='#ffffff', text="Войти как пациент", command=self.show_patient_auth, position=[240, 225], background='#2998E9', width='25', height='3', font="Sedan 12")
        self.file_flag = False
        self.active_elements['file_button'] = create_button(font_color='#ffffff', text="Работа с файлом",
                                                               command=self.show_file, position=[240, 525],
                                                               background='#2998E9', width='25', height='3',
                                                               font="Sedan 12")
        self.active_elements['get_more_info'] = create_button(font_color='#ffffff', text="Показать информацию",
                                                            command=self.show_more_info, position=[10, 225],
                                                            background='#2998E9', width='20', height='3',
                                                            font="Sedan 12")
    def show_more_info(self):
        self.destroy_all()
        text = ''
        for patient in self.patients:
            if patient.in_que:
                text += f"\nПациент {patient.get_full_fio()} стоит в очереди к врачу-{patient.que_for.lower()}у"
        if text == "":
            text = 'Пациентов в очереди пока нет'
        self.create_big_console(text)
        self.active_elements['go_back_button'] = create_button(font_color='#ffffff', text="назад",
                                                              command=self.return_to_main_screen, position=[1000, 700],
                                                              background='#2998E9', width='20', height='3',
                                                              font="Sedan 12")


    def copy_from_file(self):
        excel_data = pd.read_excel("data.xlsx")
        data = pd.DataFrame(excel_data, columns=['Фамилия доктора', 'Имя доктора', 'Отчество доктора', 'Специализация доктора', 'Стаж доктора', 'Фамилия пациента', 'Имя пациента', 'Отчество пациента', 'Дата рождения пациента'])
        doctor_correct_flag = False
        patient_correct_flag = False
        doctors_info, patient_info = [], []
        if len(data['Фамилия доктора']) == len(data['Имя доктора']) == len(data['Отчество доктора']) == len(data['Специализация доктора']) == len(data['Стаж доктора']):
            for index in range(len(data['Фамилия доктора'])):
                if str(data['Фамилия доктора'][index]) != 'nan':
                    surname, surname_flag = fio_checker(data['Фамилия доктора'][index])
                    name, name_flag = fio_checker(data['Имя доктора'][index])
                    second_surname, second_surname_flag = fio_checker(data['Отчество доктора'][index])
                    specialisation = data['Специализация доктора'][index]
                    experience = data['Стаж доктора'][index]
                    experience, experience_flag = experience_checker(str(experience))
                    if specialisation.lower().title() in DOCTOR_PROFESSIONS:
                        specialisation_flag = True
                    else:
                        specialisation_flag = False
                    if not specialisation_flag:
                        self.create_console(f'В строчке {index + 1} cпециализация врача не может быть установлена')
                    if not experience_flag:
                        self.create_console(f'В строчке {index + 1} стаж врача не введён неверно')
                    if not second_surname_flag:
                        self.create_console(f'В строчке {index + 1} отчество врача введёно неверно')
                    if not surname_flag:
                        self.create_console(f'В строчке {index + 1} фамилия врача введёна неверно')
                    if not name_flag:
                        self.create_console(f'В строчке {index + 1} имя врача введёно неверно')
                    if not specialisation_flag or not experience_flag or not second_surname_flag or not surname_flag or not name_flag:
                        break
                    find_equal = False
                    for doctor in self.doctors:
                        if doctor.name == name and doctor.surname == surname and doctor.second_surname == second_surname and doctor.profession == specialisation and doctor.experience == experience:
                            find_equal = True
                    for doctor in doctors_info:
                        if doctor.name == name and doctor.surname == surname and doctor.second_surname == second_surname and doctor.profession == specialisation and doctor.experience == experience:
                            find_equal = True
                    if not find_equal:
                        doctors_info.append(Doctor(name=name, surname=surname, second_surname=second_surname, profession=specialisation.lower().title(), experience=experience))
            else:
                doctor_correct_flag = True

        else:
            self.create_console('Количество записей про врачей не может быть однозначно установлено!')
        if len(data['Фамилия пациента']) == len(data['Имя пациента']) == len(data['Отчество пациента']) == len(data['Отчество пациента']) == len(data['Дата рождения пациента']):
            for index in range(len(data['Фамилия пациента'])):
                if str(data['Фамилия пациента'][index]) != 'nan':
                    surname, surname_flag = fio_checker(data['Фамилия пациента'][index])
                    name, name_flag = fio_checker(data['Имя пациента'][index])
                    try:
                        bithday_flag = False
                        birhaday_date = str(data['Дата рождения пациента'][index])[:10].split('-')
                        birhaday_date = datetime.datetime.strptime(
                            '.'.join([birhaday_date[2], birhaday_date[1], birhaday_date[0]]), '%d.%m.%Y')
                        if (birhaday_date < datetime.datetime.now() and birhaday_date.year > 1900):
                            bithday_flag = True
                    except:
                        bithday_flag = False
                    second_surname, second_surname_flag = fio_checker(data['Отчество пациента'][index])
                    if not second_surname_flag:
                        self.create_console(f'В строчке {index + 1} отчество пациента введёно неверно')
                    if not surname_flag:
                        self.create_console(f'В строчке {index + 1} фамилия пациента введёна неверно')
                    if not name_flag:
                        self.create_console(f'В строчке {index + 1} имя пациента введёно неверно')
                    if not bithday_flag:
                        self.create_console(f'В строчке {index + 1} дата рождения пациента введёно неверно')
                    if not bithday_flag or not second_surname_flag or not surname_flag or not name_flag:
                        break
                    find_equal = False
                    for patient in self.patients:
                        if patient.name == name and patient.surname == surname and patient.second_surname == second_surname and patient.birhaday_date == birhaday_date:
                            find_equal = True
                    for patient in patient_info:
                        if patient.name == name and patient.surname == surname and patient.second_surname == second_surname and patient.birhaday_date == birhaday_date:
                            find_equal = True
                    if not find_equal:
                        patient_info.append(Patient(name=name, surname=surname, second_surname=second_surname, birhaday_date=birhaday_date))
                else:
                    patient_correct_flag = True
        else:
            self.create_console('Количество записей про пациентов не может быть однозначно установлено!')
        if patient_correct_flag and doctor_correct_flag:
            self.create_console('Записи из файла успешно добавлены')
            self.doctors.extend(doctors_info)
            self.patients.extend(patient_info)
            self.show_file(flag=True)


    def show_file(self, flag=False):
        if not self.file_flag:
            self.create_console('Создана форма работы с файлом')
            self.active_elements['copy_file_btn'] = create_button(font_color='#ffffff', text="Скопировать из файла",
                                                                command=self.copy_from_file, position=[240, 625],
                                                                background='#2998E9', width='25', height='3',
                                                                font="Sedan 12")
            self.file_flag = True
        else:
            if not flag:
                self.create_console('Форма работы с файлом удалена')
            self.active_elements['copy_file_btn'].destroy()
            self.active_elements.pop('copy_file_btn')
            self.file_flag = False


    def show_admin_auth(self):
        self.destroy_all()
        self.create_console('Переход на страницу входа в административную панель')
        self.active_elements['admin_label'] = create_label(font_color="#0C8EEC", text="Вход для\n Администратора", position=[400, 72], background="#b5effb", font="Sedan 16")
        self.active_elements['admin_password_label'] = create_label(font_color="#000000", text="Введите пароль: ", position=[250, 175], background="#57dcf9", font="Sedan 14")
        self.active_elements['admin_entry'] = create_entry(width=25, font="Sedan 14", font_color="#000000", position=[200, 225])
        self.active_elements['success'] = create_button(font_color='#ffffff', text="Выполнить", command=self.check_correct_admin_password, position=[200, 280], background='#2998E9', width='13', height='3', font="Sedan 12")
        self.active_elements['go_back'] = create_button(font_color='#ffffff', text="Отменить", command=self.return_to_main_screen, position=[350, 280],  background='#2998E9', width='13', height='3', font="Sedan 12")

    def destroy_all(self):
        for elem in self.active_elements:
            self.active_elements[elem].destroy()
        self.active_elements.clear()

    def return_to_main_screen(self):
        self.create_console('Возврат на основной экран')
        self.destroy_all()
        self.show_main_screen()

    def check_correct_admin_password(self):
        flag = check_correct_admin_password(self.active_elements['admin_entry'].get())
        if flag:
            self.destroy_all()
            AdminForm(self)
        else:
            self.create_console("Пароль введён неверно")

    def create_chose_doctor(self, event):
        now_prof = self.active_elements['combo_doctor_auth_prof'].get()
        self.now_doctors = []
        for doctor in self.doctors:
            if doctor.profession == now_prof:
                self.now_doctors.append(doctor)
        values = [self.now_doctors[doctor].get_fio(doctor+1) for doctor in range(len(self.now_doctors))]
        self.active_elements['combo_doctor_auth_who'].destroy()
        self.active_elements['combo_doctor_auth_who'] = create_combo_box(width=12, font_color="#000000", position=[875, 140], values=values, default=None, font="Sedan 14")

    def show_doctor_auth(self):
        if not self.doctor_auth_active:
            self.create_console('Создана форма добавления доктора')
            self.active_elements['doctor_label'] = create_label(font_color="#0C8EEC", text="Вход для доктора", position=[20, 140], background="#b5effb", font="Sedan 14")
            self.active_elements['doctor_auth_label'] = create_label(font_color="#0C8EEC", text="Выберите профессию доктора:", position=[200, 140], background="#b5effb", font="Sedan 14")
            self.active_elements['combo_doctor_auth_prof'] = create_combo_box(width=12, font_color="#000000", position=[500, 140], values=DOCTOR_PROFESSIONS, default=None, callback=self.create_chose_doctor, font="Sedan 14")
            self.active_elements['doctor_auth_label_2'] = create_label(font_color="#0C8EEC", text="Выберите доктора", position=[675, 140], background="#b5effb", font="Sedan 14")
            self.active_elements['combo_doctor_auth_who'] = create_combo_box(width=12, font_color="#000000", position=[875, 140], values=[doctor.get_fio() for doctor in self.now_doctors], default=None, font="Sedan 14")
            self.active_elements['doctor_success'] = create_button(font_color='#ffffff', text="Выполнить", command=self.enter_doctor_menu, position=[1050, 140],  background='#2998E9', width='13', height='1', font="Sedan 12")

            self.doctor_auth_active = True
        else:
            self.create_console('Форма добавления доктора удалена')
            self.active_elements['doctor_label'].destroy()
            self.active_elements['doctor_auth_label'].destroy()
            self.active_elements['combo_doctor_auth_prof'].destroy()
            self.active_elements['doctor_auth_label_2'].destroy()
            self.active_elements['combo_doctor_auth_who'].destroy()
            self.active_elements['doctor_success'].destroy()
            self.active_elements.pop('doctor_auth_label')
            self.active_elements.pop('combo_doctor_auth_prof')
            self.active_elements.pop('doctor_auth_label_2')
            self.active_elements.pop('combo_doctor_auth_who')
            self.active_elements.pop('doctor_success')
            self.active_elements.pop('doctor_label')
            self.doctor_auth_active = False
            self.now_doctors = []

    def enter_doctor_menu(self):
        if self.active_elements.get('combo_doctor_auth_who').get() != "":
            doctors_fio = [self.now_doctors[doctor].get_fio(doctor+1) for doctor in range(len(self.now_doctors))]
            need_index = doctors_fio.index(self.active_elements['combo_doctor_auth_who'].get())
            need_doctor = self.now_doctors[need_index]
            DoctorForm(self, need_doctor)
        else:
            self.create_console('Вы не выбрали врача')

    def show_patient_auth(self):
        if not self.patient_auth_active:
            self.create_console('Создана форма добавления пациента')
            self.active_elements['patient_label'] = create_label(font_color="#0C8EEC", text="Вход для пациента", position=[400, 70], background="#b5effb", font="Sedan 14")
            self.active_elements['patient_auth_label'] = create_label(font_color="#0C8EEC", text="Выберите пациента", position=[600, 70], background="#b5effb", font="Sedan 14")
            self.active_elements['combo_patient_auth'] = create_combo_box(width = 12, font_color = "#000000", position=[800, 70], values=[self.patients[patient].get_fio(patient+1) for patient in range(len(self.patients))], default=None, font = "Sedan 14")
            self.active_elements['patient_success'] = create_button(font_color = '#ffffff', text="Выполнить", command=self.enter_patient_menu, position=[1000, 70], background = '#2998E9', width = '13', height = '1', font = "Sedan 12")
            self.patient_auth_active = True
        else:
            self.create_console('Форма добавления пациента удалена')
            self.active_elements['patient_label'].destroy()
            self.active_elements['patient_auth_label'].destroy()
            self.active_elements['combo_patient_auth'].destroy()
            self.active_elements['patient_success'].destroy()
            self.active_elements.pop('patient_label')
            self.active_elements.pop('patient_auth_label')
            self.active_elements.pop('combo_patient_auth')
            self.active_elements.pop('patient_success')
            self.patient_auth_active = False

    def enter_patient_menu(self):
        patients_fio = [self.patients[patient].get_fio(patient+1) for patient in range(len(self.patients))]
        if self.active_elements.get('combo_patient_auth').get() != "":
            chose_patient = self.active_elements.get('combo_patient_auth').get()
            need_index = patients_fio.index(chose_patient)
            need_patient = self.patients[need_index]
            PatientForm(self, need_patient)
        else:
            self.create_console('Вы не выбрали пациента')
