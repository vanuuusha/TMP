from help_elements import create_button, create_label, create_combo_box, create_entry
from constants import DOCTOR_PROFESSIONS


class PatientForm:
    def __init__(self, main, patient):
        self.patient = patient
        self.MainForm = main
        self.MainForm.window.title("Поликлиника (пациент)")
        self.MainForm.create_console('Вы перешли на страницу пациента')
        self.show_main_screen()

    def show_main_screen(self):
        self.MainForm.destroy_all()
        self.MainForm.active_elements['doctor_label'] = create_label(font_color="#000000",
                                                                     text="Вы находитесь на панели пациента",
                                                                     position=[400, 40], background="#b5effb",
                                                                     font="Sedan 14")
        self.MainForm.active_elements['patient_name_label'] = create_label(font_color="#000000",
                                                                           text=f"Имя: {self.patient.name}",
                                                                           position=[20, 250], background="#b5effb",
                                                                           font="Sedan 14")
        self.MainForm.active_elements['patient_surname_label'] = create_label(font_color="#000000",
                                                                              text=f"Фамилия: {self.patient.surname}",
                                                                              position=[20, 300], background="#b5effb",
                                                                              font="Sedan 14")
        self.MainForm.active_elements['patient_second_surname_label'] = create_label(font_color="#000000",
                                                                                     text=f"Отчество: {self.patient.second_surname}",
                                                                                     position=[20, 350],
                                                                                     background="#b5effb",
                                                                                     font="Sedan 14")
        self.MainForm.active_elements['patine_in_que'] = create_label(font_color="#000000",
                                                                      text=f"Очередь: {'Да' if self.patient.in_que else 'Нет'}",
                                                                      position=[20, 400], background="#b5effb",
                                                                      font="Sedan 14")
        self.MainForm.active_elements['patine_for_que'] = create_label(font_color="#000000",
                                                                       text=f"Очередь к: {self.patient.que_for}",
                                                                       position=[20, 450], background="#b5effb",
                                                                       font="Sedan 14")
        self.MainForm.active_elements['patine_diagnos'] = create_label(font_color="#000000",
                                                                       text=f"Диагноз{'ы' if len(self.patient.diagnos) > 1 else ''}: {', '.join(self.patient.diagnos)}{'-' if len(self.patient.diagnos) == 0 else ''}",
                                                                       position=[20, 500], background="#b5effb",
                                                                       font="Sedan 14")
        self.MainForm.active_elements['patine_birthaday'] = create_label(font_color="#000000",
                                                                         text=f"Дата рождения: {self.patient.birhaday_date.strftime('%d.%m.%Y')[:10]}",
                                                                         position=[20, 550], background="#b5effb",
                                                                         font="Sedan 14")
        self.MainForm.active_elements['show_info'] = create_button(font_color='#ffffff', text="Показать историю",
                                                                   command=self.show_info,
                                                                   position=[20, 600], background='#2998E9', width='25',
                                                                   height='3', font="Sedan 12")
        self.queue_flag = False
        self.MainForm.active_elements['queue'] = create_button(font_color='#ffffff', text="Встать в очередь",
                                                               command=self.stay_in_queue,
                                                               position=[20, 700], background='#2998E9', width='25',
                                                               height='3', font="Sedan 12")

        self.MainForm.active_elements['delete'] = create_button(font_color='#ffffff', text="Выписаться",
                                                                command=self.delete_patient,
                                                                position=[1000, 625], background='#2998E9', width='25',
                                                                height='3', font="Sedan 12")

        self.MainForm.active_elements['go_back'] = create_button(font_color='#ffffff', text="Основной экран",
                                                                 command=self.MainForm.return_to_main_screen,
                                                                 position=[1000, 700], background='#2998E9', width='25',
                                                                 height='3', font="Sedan 12")

    def delete_patient(self):
        self.MainForm.patients.remove(self.patient)
        if self.patient.in_que:
            self.MainForm.doctor_ques[self.patient.que_for].remove(self.patient)
        self.MainForm.return_to_main_screen()

    def return_to_main_screen(self, text):
        self.MainForm.create_console(text)
        self.show_main_screen()

    def return_from_show_history(self):
        self.return_to_main_screen('Возврат на страницу пациента')

    def stay_in_queue(self):
        if not self.queue_flag:
            self.MainForm.create_console('Добавлена форма становления в очередь')
            self.MainForm.active_elements['type_doctor'] = create_label(font_color="#000000",
                                                                             text=f"Выберите тип врача",
                                                                             position=[300, 685], background="#b5effb",
                                                                             font="Sedan 14")
            self.MainForm.active_elements['combo_chose_doctor'] = create_combo_box(width=12, font_color="#000000",
                                                                                   position=[300, 725],
                                                                                   values=DOCTOR_PROFESSIONS,
                                                                                   default=None, font="Sedan 14")
            self.MainForm.active_elements['enter_your_bads'] = create_label(font_color="#000000",
                                                                             text=f"Введите жалобу:",
                                                                             position=[520, 685], background="#b5effb",
                                                                             font="Sedan 14")
            self.MainForm.active_elements['enter_your_bads_entry'] = create_entry(width=25, font="Sedan 14", font_color="#000000", position=[500, 725])

            self.MainForm.active_elements['go_to'] = create_button(font_color='#ffffff',
                                                                   text="Встать",
                                                                   command=self.go_to_queue,
                                                                   position=[800, 700], background='#2998E9',
                                                                   width='12', height='3', font="Sedan 12")
            self.queue_flag = True
        else:
            self.MainForm.create_console('Форма становления в очередь удалена')
            self.MainForm.active_elements['combo_chose_doctor'].destroy()
            self.MainForm.active_elements['go_to'].destroy()
            self.MainForm.active_elements['type_doctor'].destroy()
            self.MainForm.active_elements['enter_your_bads'].destroy()
            self.MainForm.active_elements['enter_your_bads_entry'].destroy()
            self.MainForm.active_elements.pop('combo_chose_doctor')
            self.MainForm.active_elements.pop('go_to')
            self.MainForm.active_elements.pop('type_doctor')
            self.MainForm.active_elements.pop('enter_your_bads')
            self.MainForm.active_elements.pop('enter_your_bads_entry')
            self.queue_flag = False

    def go_to_queue(self):
        need_prof = self.MainForm.active_elements['combo_chose_doctor'].get()
        what_wrong = self.MainForm.active_elements['enter_your_bads_entry'].get()
        print(len(what_wrong))
        if need_prof != '':
            if not self.patient.in_que:
                if what_wrong != '' and len(what_wrong) < 50:
                    self.MainForm.doctor_ques[need_prof].append(self.patient)
                    self.stay_in_queue()
                    self.patient.in_que = True
                    self.patient.que_for = need_prof
                    self.return_to_main_screen('Вы успешно встали в очередь')
                    self.patient.what_wrong = what_wrong
                else:
                    self.MainForm.create_console("Вы неверно указали что с вами случилось\n (не более 50 символов)")
            else:
                self.MainForm.create_console("Вы уже стоите в очереди")
        else:
            self.MainForm.create_console("Вы не выбрали специальность врача")

    def show_info(self):
        text = self.patient.show_history()
        if text == "":
            text = 'Истории пока нет'
            self.MainForm.create_console(text)
        else:
            self.MainForm.destroy_all()
            self.MainForm.create_big_console(text)
            self.MainForm.active_elements['go_back'] = create_button(font_color='#ffffff', text="Назад",
                                                                     command=self.return_from_show_history,
                                                                     position=[1000, 700], background='#2998E9',
                                                                     width='25', height='3', font="Sedan 12")
