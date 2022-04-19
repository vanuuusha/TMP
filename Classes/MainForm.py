import tkinter as tk
from help_elements import create_button, create_entry, create_label, create_combo_box
from checker import check_correct_admin_password
from .AdminForm import AdminForm
from .DoctorFom import DoctorForm
from .PatientForm import PatientForm
from constants import DEFAULTKWARGSBUTTON, DEFAULTKWARGSLABEL, DEFAULTKWARGSENTRY, CONSOLETEXT, DEFAULTCOMBOBOX, \
    DOCTOR_PROFESSIONS


class MainForm:
    def __init__(self):
        self.doctors, self.patients = [], []
        self.doctor_ques = {}
        for name_prof in DOCTOR_PROFESSIONS:
            self.doctor_ques[name_prof] = []
        self.active_elements = {}
        self.window = tk.Tk()
        self.window.geometry('1400x1000')
        self.show_main_screen()
        self.create_console(text=CONSOLETEXT)
        self.window.mainloop()

    def create_console(self, text):
        create_label(width=50, **DEFAULTKWARGSLABEL,
                     text=text, position=[600, 300])

    def show_main_screen(self):
        self.window.title("Поликлиника")
        self.active_elements['admin_button'] = create_button(width=30, **DEFAULTKWARGSBUTTON, text="Войти как админ",
                                                             command=self.show_admin_auth, position=[200, 300])
        self.doctor_auth_active = False
        self.now_doctors = []
        self.active_elements['doctor_button'] = create_button(width=30, **DEFAULTKWARGSBUTTON, text="Войти как доктор",
                                                              command=self.show_doctor_auth, position=[200, 400])
        self.patient_auth_active = False
        self.active_elements['patient_button'] = create_button(width=30, **DEFAULTKWARGSBUTTON, text="Войти как пациент",
                                                               command=self.show_patient_auth, position=[200, 500])

    def show_admin_auth(self):
        self.destroy_all()
        self.active_elements['admin_label'] = create_label(width=30, **DEFAULTKWARGSLABEL,
                                                           text="Введите пароль администора", position=[200, 300])
        self.active_elements['admin_entry'] = create_entry(width=30, **DEFAULTKWARGSENTRY, position=[200, 350])
        self.active_elements['success'] = create_button(width=15, **DEFAULTKWARGSBUTTON, text="Выполнить",
                                                        command=self.check_correct_admin_password, position=[200, 500])
        self.active_elements['go_back'] = create_button(width=15, **DEFAULTKWARGSBUTTON, text="Отменить",
                                                        command=self.return_to_main_screen, position=[400, 500])

    def destroy_all(self):
        for elem in self.active_elements:
            self.active_elements[elem].destroy()
        self.active_elements.clear()

    def return_to_main_screen(self):
        self.create_console(CONSOLETEXT + '\tВозврат на основной экран')
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
        values = [self.now_doctors[doctor].get_fio(doctor) for doctor in range(len(self.now_doctors))]
        self.active_elements['combo_doctor_auth_who'].destroy()
        self.active_elements['combo_doctor_auth_who'] = create_combo_box(width=30, **DEFAULTCOMBOBOX,
                                                                         position=[450, 700],
                                                                         values=values, default=None)

    def show_doctor_auth(self):
        if not self.doctor_auth_active:
            self.active_elements['doctor_auth_label'] = create_label(width=30, **DEFAULTKWARGSLABEL,
                                                                     text="Выберите профессию доктора",
                                                                     position=[450, 500])
            self.active_elements['combo_doctor_auth_prof'] = create_combo_box(width=30, **DEFAULTCOMBOBOX,
                                                                              position=[450, 600],
                                                                              values=DOCTOR_PROFESSIONS, default=None,
                                                                              callback=self.create_chose_doctor)
            self.active_elements['doctor_auth_label_2'] = create_label(width=30, **DEFAULTKWARGSLABEL,
                                                                       text="Выберите доктора",
                                                                       position=[450, 650])
            self.active_elements['combo_doctor_auth_who'] = create_combo_box(width=30, **DEFAULTCOMBOBOX,
                                                                             position=[450, 700],
                                                                             values=[doctor.get_fio() for doctor in
                                                                                     self.now_doctors], default=None)
            self.active_elements['doctor_success'] = create_button(width=15, **DEFAULTKWARGSBUTTON, text="Выполнить",
                                                                   command=self.enter_doctor_menu,
                                                                   position=[450, 750])

            self.doctor_auth_active = True
        else:
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
            self.doctor_auth_active = False
            self.now_doctors = []

    def enter_doctor_menu(self):
        doctors_fio = [self.doctors[doctor].get_fio(doctor) for doctor in range(len(self.doctors))]
        if self.active_elements.get('combo_doctor_auth_who').get() != "":
            chose_doctor = self.active_elements.get('combo_doctor_auth_who').get()
            need_index = doctors_fio.index(chose_doctor)
            need_doctor = self.doctors[need_index]
            DoctorForm(self, need_doctor)

    def show_patient_auth(self):
        if not self.patient_auth_active:
            self.active_elements['patient_auth_label'] = create_label(width=30, **DEFAULTKWARGSLABEL,
                                                                      text="Выберите пациента",
                                                                      position=[700, 500])
            self.active_elements['combo_patient_auth'] = create_combo_box(width=30, **DEFAULTCOMBOBOX,
                                                                          position=[700, 600],
                                                                          values=[self.patients[patient].get_fio(patient) for patient in
                                                                                  range(len(self.patients))], default=None)
            self.active_elements['patient_success'] = create_button(width=15, **DEFAULTKWARGSBUTTON, text="Выполнить",
                                                                    command=self.enter_patient_menu,
                                                                    position=[700, 600])
            self.patient_auth_active = True
        else:
            self.active_elements['patient_auth_label'].destroy()
            self.active_elements['combo_patient_auth'].destroy()
            self.active_elements['patient_success'].destroy()
            self.active_elements.pop('patient_auth_label')
            self.active_elements.pop('combo_patient_auth')
            self.active_elements.pop('patient_success')
            self.patient_auth_active = False

    def enter_patient_menu(self):
        patients_fio = [self.patients[doctor].get_fio(doctor) for doctor in range(len(self.patients))]
        if self.active_elements.get('combo_patient_auth').get() != "":
            chose_patient = self.active_elements.get('combo_patient_auth').get()
            need_index = patients_fio.index(chose_patient)
            need_patient = self.patients[need_index]
            PatientForm(self, need_patient)
