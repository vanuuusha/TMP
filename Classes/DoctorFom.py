from help_elements import create_button, create_entry, create_label, create_combo_box
from constants import DEFAULTKWARGSBUTTON, DEFAULTKWARGSLABEL, DEFAULTKWARGSENTRY, CONSOLETEXT, DOCTOR_PROFESSIONS, \
    DEFAULTCOMBOBOX, MAXEXPERIENCE, MAXLENNAME, DIAGNISIS


class DoctorForm:
    def __init__(self, main, doctor):
        self.doctor = doctor
        self.MainForm = main
        self.MainForm.window.title("Поликлиника (доктор)")
        self.show_main_screen()

    def show_main_screen(self):
        self.MainForm.destroy_all()
        self.MainForm.active_elements['doctor_label'] = create_label(width=60, **DEFAULTKWARGSLABEL,
                                                                     text="Вы находитесь в панели доктора",
                                                                     position=[100, 100])
        self.MainForm.active_elements['doctor_name_label'] = create_label(width=60, **DEFAULTKWARGSLABEL,
                                                                          text=f"Имя {self.doctor.name}",
                                                                          position=[100, 150])
        self.MainForm.active_elements['doctor_surname_label'] = create_label(width=60, **DEFAULTKWARGSLABEL,
                                                                             text=f"Фамилия {self.doctor.surname}",
                                                                             position=[100, 200])
        self.MainForm.active_elements['doctor_second_surname_label'] = create_label(width=60, **DEFAULTKWARGSLABEL,
                                                                                    text=f"Отчество {self.doctor.second_surname}",
                                                                                    position=[100, 250])
        self.MainForm.active_elements['doctor_prof_label'] = create_label(width=60, **DEFAULTKWARGSLABEL,
                                                                          text=f"Профессия {self.doctor.profession}",
                                                                          position=[100, 300])
        self.MainForm.active_elements['doctor_exp_label'] = create_label(width=60, **DEFAULTKWARGSLABEL,
                                                                         text=f"Стаж {self.doctor.experience}",
                                                                         position=[100, 350])
        self.MainForm.active_elements['history'] = create_button(width=15, **DEFAULTKWARGSBUTTON,
                                                                  text="Показать историю",
                                                                  command=self.show_history,
                                                                  position=[100, 400])
        self.show_que_flag = False
        self.MainForm.active_elements['show_que'] = create_button(width=15, **DEFAULTKWARGSBUTTON,
                                                                  text="Показать очередь",
                                                                  command=self.show_que,
                                                                  position=[100, 450])
        self.MainForm.active_elements['go_back'] = create_button(width=15, **DEFAULTKWARGSBUTTON, text="Основной экран",
                                                                 command=self.MainForm.return_to_main_screen,
                                                                 position=[400, 500])

    def create_diagnosis_combo(self, event):
        self.MainForm.active_elements['combo_diagons'] = create_combo_box(width=30, **DEFAULTCOMBOBOX,
                                                                          position=[200, 600],
                                                                          values=DIAGNISIS[self.doctor.profession],
                                                                          default=1)
        self.MainForm.active_elements['submit'] = create_button(width=15, **DEFAULTKWARGSBUTTON, text="Поставить диагноз",
                                                                 command=self.do_dignos,
                                                                 position=[300, 600])

    def do_dignos(self):
        patients_fio = [self.MainForm.doctor_ques[self.doctor.profession][patient].get_fio(patient) for patient in range(len(self.MainForm.doctor_ques[self.doctor.profession]))]
        now_pationt_fio = self.MainForm.active_elements['combo_chose_doctor'].get()
        need_index = patients_fio.index(now_pationt_fio)
        patient = self.MainForm.doctor_ques[self.doctor.profession][need_index]
        if self.MainForm.active_elements['combo_diagons'].get() not in patient.diagnos:
            patient.diagnos.append(self.MainForm.active_elements['combo_diagons'].get())
            patient.que_for = '-'
            patient.in_que = False
            self.MainForm.doctor_ques[self.doctor.profession].remove(patient)
            self.doctor.make_more_history(f"Пациенту {patient.get_fio()} был поставлен диагноз {self.MainForm.active_elements['combo_diagons'].get()}")
            patient.make_more_history(f"Врачом {self.doctor.get_fio()} был поставлен диагноз {self.MainForm.active_elements['combo_diagons'].get()}")
            self.show_main_screen()
        else:
            self.MainForm.create_console(CONSOLETEXT+"\nТакой диагноз уже поставлен")

    def show_que(self):
        if not self.show_que_flag:
            self.MainForm.active_elements['combo_chose_doctor'] = create_combo_box(width=30, **DEFAULTCOMBOBOX,
                                                                                   position=[100, 600],
                                                                                   values=[
                                                                                       self.MainForm.doctor_ques[self.doctor.profession][patient].get_fio(
                                                                                           patient) for patient in
                                                                                       range(len(self.MainForm.doctor_ques[self.doctor.profession]))],
                                                                                   default=None,
                                                                                   callback=self.create_diagnosis_combo)
            self.show_que_flag = True
        else:
            self.MainForm.active_elements['combo_chose_doctor'].destroy()
            self.MainForm.active_elements['combo_diagons'].destoy()
            self.MainForm.active_elements['submit'].destroy()
            del self.MainForm.active_elements['combo_chose_doctor']
            del self.MainForm.active_elements['combo_diagons']
            del self.MainForm.active_elements['submit']
            self.show_que_flag = False

    def show_history(self):
        text = CONSOLETEXT + self.doctor.show_history()
        self.MainForm.create_console(text)
