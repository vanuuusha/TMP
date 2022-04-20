import tkinter as tk
from help_elements import create_button, create_entry, create_label, create_combo_box
from checker import check_correct_admin_password
from .AdminForm import AdminForm
from .DoctorFom import DoctorForm
from .PatientForm import PatientForm
from constants import CONSOLETEXT,  DOCTOR_PROFESSIONS
import os


class MainForm:
    def __init__(self):
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
        create_label(font_color='#ffffff',
                     text=CONSOLETEXT, position=[560, 250], font="Sedan 14", background="#30d3f9")

        label = tk.Label(
            text=text,
            font="Sedan 14",
            foreground='#000000',
            background='#ffffff',
            width=50,
            height=12,
        )
        label.place(x=560, y=300)

    def create_big_console(self, text=""):
        self.active_elements['big_console_label'] = create_label(font_color='#ffffff',
                     text=CONSOLETEXT, position=[150, 150], font="Sedan 14", background="#30d3f9")

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
        self.active_elements['chose_what_do'] = create_label(font_color='#ffffff', text="Выберите действие:", position=[280, 250], background="#30d3f9", font="Sedan 14")
        self.active_elements['admin_button'] = create_button(font_color='#ffffff', text="Войти как админ", command=self.show_admin_auth, position=[240, 500], background='#2998E9', width='25', height='3', font="Sedan 12")
        self.doctor_auth_active = False
        self.now_doctors = []
        self.active_elements['doctor_button'] = create_button(font_color='#ffffff', text="Войти как доктор", command=self.show_doctor_auth, position=[240, 400], background='#2998E9', width='25', height='3', font="Sedan 12")
        self.patient_auth_active = False
        self.active_elements['patient_button'] = create_button(font_color='#ffffff', text="Войти как пациент", command=self.show_patient_auth, position=[240, 300], background='#2998E9', width='25', height='3', font="Sedan 12")

    def show_admin_auth(self):
        self.destroy_all()
        self.create_console('Переход на страницу входа в административную панель')
        self.active_elements['admin_label'] = create_label(font_color="#0C8EEC", text="Вход для\n Администратора", position=[400, 72], background="#b5effb", font="Sedan 16")
        self.active_elements['admin_password_label'] = create_label(font_color="#ffffff", text="Введите пароль: ", position=[250, 250], background="#57dcf9", font="Sedan 14")
        self.active_elements['admin_entry'] = create_entry(width=25, font="Sedan 14", font_color="#000000", position=[200, 290])
        self.active_elements['success'] = create_button(font_color='#ffffff', text="Выполнить", command=self.check_correct_admin_password, position=[200, 350], background='#2998E9', width='13', height='3', font="Sedan 12")
        self.active_elements['go_back'] = create_button(font_color='#ffffff', text="Отменить", command=self.return_to_main_screen, position=[350, 350],  background='#2998E9', width='13', height='3', font="Sedan 12")

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
            self.create_console(CONSOLETEXT + "\tПароль введён неверно")

    def create_chose_doctor(self, event):
        now_prof = self.active_elements['combo_doctor_auth_prof'].get()
        self.now_doctors = []
        for doctor in self.doctors:
            if doctor.profession == now_prof:
                self.now_doctors.append(doctor)
        values = [self.now_doctors[doctor].get_fio(doctor+1) for doctor in range(len(self.now_doctors))]
        self.active_elements['combo_doctor_auth_who'].destroy()
        self.active_elements['combo_doctor_auth_who'] = create_combo_box(width=12, font_color="#000000", position=[875, 150], values=values, default=None, font="Sedan 14")

    def show_doctor_auth(self):
        if not self.doctor_auth_active:
            self.create_console('Создана форма добавления доктора')
            self.active_elements['doctor_label'] = create_label(font_color="#0C8EEC", text="Вход для доктора", position=[20, 150], background="#b5effb", font="Sedan 14")
            self.active_elements['doctor_auth_label'] = create_label(font_color="#0C8EEC", text="Выберите профессию доктора:", position=[200, 150], background="#b5effb", font="Sedan 14")
            self.active_elements['combo_doctor_auth_prof'] = create_combo_box(width=12, font_color="#000000", position=[500, 150], values=DOCTOR_PROFESSIONS, default=None, callback=self.create_chose_doctor, font="Sedan 14")
            self.active_elements['doctor_auth_label_2'] = create_label(font_color="#0C8EEC", text="Выберите доктора", position=[675, 150], background="#b5effb", font="Sedan 14")
            self.active_elements['combo_doctor_auth_who'] = create_combo_box(width=12, font_color="#000000", position=[875, 150], values=[doctor.get_fio() for doctor in self.now_doctors], default=None, font="Sedan 14")
            self.active_elements['doctor_success'] = create_button(font_color='#ffffff', text="Выполнить", command=self.enter_doctor_menu, position=[1050, 150],  background='#2998E9', width='13', height='1', font="Sedan 12")

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
            self.active_elements['patient_label'] = create_label(font_color="#0C8EEC", text="Вход для пациента", position=[400, 40], background="#b5effb", font="Sedan 14")
            self.active_elements['patient_auth_label'] = create_label(font_color="#0C8EEC", text="Выберите пациента", position=[600, 40], background="#b5effb", font="Sedan 14")
            self.active_elements['combo_patient_auth'] = create_combo_box(width = 12, font_color = "#000000", position=[800, 40], values=[self.patients[patient].get_fio(patient+1) for patient in range(len(self.patients))], default=None, font = "Sedan 14")
            self.active_elements['patient_success'] = create_button(font_color = '#ffffff', text="Выполнить", command=self.enter_patient_menu, position=[1000, 40], background = '#2998E9', width = '13', height = '1', font = "Sedan 12")
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
