from help_elements import create_button, create_entry, create_label, create_combo_box
from constants import DEFAULTKWARGSBUTTON, DEFAULTKWARGSLABEL, DEFAULTKWARGSENTRY, CONSOLETEXT, DOCTOR_PROFESSIONS, \
    DEFAULTCOMBOBOX, MAXEXPERIENCE, MAXLENNAME

class PatientForm:
    def __init__(self, main, patient):
        self.patient = patient
        self.MainForm = main
        self.MainForm.window.title("Поликлиника (пациент)")
        self.show_main_screen()

    def show_main_screen(self):
        self.MainForm.destroy_all()
        self.MainForm.active_elements['patient_label'] = create_label(width=60, **DEFAULTKWARGSLABEL,
                                                                    text="Вы находитесь в панели пациента",
                                                                    position=[100, 100])
        self.MainForm.active_elements['patient_name_label'] = create_label(width=60, **DEFAULTKWARGSLABEL,
                                                                     text=f"Имя: {self.patient.name}",
                                                                     position=[100, 150])
        self.MainForm.active_elements['patient_surname_label'] = create_label(width=60, **DEFAULTKWARGSLABEL,
                                                                          text=f"Фамилия: {self.patient.surname}",
                                                                          position=[100, 200])
        self.MainForm.active_elements['patient_second_surname_label'] = create_label(width=60, **DEFAULTKWARGSLABEL,
                                                                             text=f"Отчество: {self.patient.second_surname}",
                                                                             position=[100, 250])
        self.MainForm.active_elements['patine_in_que'] = create_label(width=60, **DEFAULTKWARGSLABEL,
                                                                                     text=f"Очередь: {'Да' if self.patient.in_que else 'Нет'}",
                                                                                     position=[100, 300])
        self.MainForm.active_elements['patine_for_que'] = create_label(width=60, **DEFAULTKWARGSLABEL,
                                                                      text=f"Очередь к: {self.patient.que_for}",
                                                                      position=[100, 350])
        self.MainForm.active_elements['patine_diagnos'] = create_label(width=60, **DEFAULTKWARGSLABEL,
                                                                       text=f"Диагноз: {', '.join(self.patient.diagnos)}",
                                                                       position=[100, 400])
        self.MainForm.active_elements['show_info'] = create_button(width=15, **DEFAULTKWARGSBUTTON, text="Показать историю",
                                                               command=self.show_info,
                                                               position=[100, 450])
        self.queue_flag = False
        self.MainForm.active_elements['queue'] = create_button(width=15, **DEFAULTKWARGSBUTTON, text="Встать в очередь",
                                                                 command=self.stay_in_queue,
                                                                 position=[100, 550])

        self.MainForm.active_elements['go_back'] = create_button(width=15, **DEFAULTKWARGSBUTTON, text="Основной экран",
                                                                 command=self.MainForm.return_to_main_screen,
                                                                 position=[400, 650])

    def stay_in_queue(self):
        if not self.queue_flag:
            self.MainForm.active_elements['combo_chose_doctor'] = create_combo_box(width=30, **DEFAULTCOMBOBOX,
                                                                             position=[300, 400],
                                                                             values=DOCTOR_PROFESSIONS, default=None)
            self.MainForm.active_elements['go_to'] = create_button(width=15, **DEFAULTKWARGSBUTTON,
                                                                     text="Встать",
                                                                     command=self.go_to_queue,
                                                                     position=[300, 550])
            self.queue_flag = True
        else:
            self.MainForm.active_elements['combo_chose_doctor'].destroy()
            self.MainForm.active_elements['go_to'].destroy()
            self.MainForm.active_elements.pop('combo_chose_doctor')
            self.MainForm.active_elements.pop('go_to')
            self.queue_flag = False

    def go_to_queue(self):
        need_prof = self.MainForm.active_elements['combo_chose_doctor'].get()
        if need_prof != '':
            if not self.patient.in_que:
                for doctor in self.MainForm.doctors:
                    if doctor.profession == need_prof:
                        self.MainForm.doctor_ques[doctor.profession].append(self.patient)
                self.stay_in_queue()
                self.patient.in_que = True
                self.patient.que_for = need_prof
                self.show_main_screen()
            else:
                self.MainForm.create_console(CONSOLETEXT + "\tВы уже стоите в очереди")

    def show_info(self):
        text = CONSOLETEXT + self.patient.show_history()
        self.MainForm.create_console(text)

