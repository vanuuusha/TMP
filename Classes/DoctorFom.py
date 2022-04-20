from help_elements import create_button, create_label, create_combo_box
from constants import DIAGNISIS
import tkinter as tk
import os
from PIL import Image, ImageTk


class DoctorForm:
    def __init__(self, main, doctor):
        self.doctor = doctor
        self.MainForm = main
        self.MainForm.window.title("Поликлиника (доктор)")
        self.MainForm.create_console('Вы перешли на страницу доктора')
        self.show_main_screen()

    def show_main_screen(self):
        self.MainForm.destroy_all()
        self.MainForm.active_elements['doctor_label'] = create_label(font_color = "#0C8EEC",
                                                                     text="Вы находитесь на панели доктора",
                                                                     position=[400, 40], background = "#b5effb",
        font = "Sedan 14")
        self.MainForm.active_elements['doctor_name_label'] = create_label(font_color = "#0C8EEC",
                                                                          text=f"Имя {self.doctor.name}",
                                                                          position=[20, 250], background = "#b5effb",
        font = "Sedan 14")
        self.MainForm.active_elements['doctor_surname_label'] = create_label(font_color = "#0C8EEC",
                                                                             text=f"Фамилия {self.doctor.surname}",
                                                                             position=[20, 300], background = "#b5effb",
        font = "Sedan 14")
        self.MainForm.active_elements['doctor_second_surname_label'] = create_label(font_color = "#0C8EEC",
                                                                                    text=f"Отчество {self.doctor.second_surname}",
                                                                                    position=[20, 350], background = "#b5effb",
        font = "Sedan 14")
        self.MainForm.active_elements['doctor_prof_label'] = create_label(font_color = "#0C8EEC",
                                                                          text=f"Профессия {self.doctor.profession}",
                                                                          position=[20, 400], background = "#b5effb",
        font = "Sedan 14")
        self.MainForm.active_elements['doctor_exp_label'] = create_label(font_color = "#0C8EEC",
                                                                         text=f"Стаж {self.doctor.experience}",
                                                                         position=[20, 450], background = "#b5effb",
        font = "Sedan 14")
        self.MainForm.active_elements['history'] = create_button(font_color = '#ffffff',
                                                                  text="Показать историю",
                                                                  command=self.show_history,
                                                                  position=[20, 550], background = '#2998E9', width = '25', height = '3', font = "Sedan 12")
        self.show_que_flag = False
        self.MainForm.active_elements['show_que'] = create_button(font_color = '#ffffff',
                                                                  text="Показать очередь",
                                                                  command=self.show_que,
                                                                  position=[20, 700], background = '#2998E9', width = '25', height = '3', font = "Sedan 12")
        self.MainForm.active_elements['delete'] = create_button(font_color='#ffffff', text="Уволиться",
                                                                 command=self.delete_doctor,
                                                                 position=[1000, 625], background='#2998E9', width='25',
                                                                 height='3', font="Sedan 12")
        self.MainForm.active_elements['go_back'] = create_button(font_color = '#ffffff', text="Основной экран",
                                                                 command=self.MainForm.return_to_main_screen,
                                                                 position=[1000, 700], background = '#2998E9', width = '25', height = '3', font = "Sedan 12")

    def delete_doctor(self):
        self.MainForm.doctors.remove(self.doctor)
        self.MainForm.return_to_main_screen()

    def create_diagnosis_combo(self, event):
        self.MainForm.create_console('Добавлена форма выставления диагноза')
        self.MainForm.active_elements['combo_diagons'] = create_combo_box(width = 12, font_color = "#000000",
                                                                          position=[475, 725],
                                                                          values=DIAGNISIS[self.doctor.profession],
                                                                          default=1, font = "Sedan 14")
        self.MainForm.active_elements['submit'] = create_button(font_color = '#ffffff', text="Поставить диагноз",
                                                                 command=self.do_dignos,
                                                                 position=[700, 700], background = '#2998E9', width = '25', height = '3', font = "Sedan 12")

    def return_to_main_screen(self, text):
        self.MainForm.create_console(text)
        self.show_main_screen()

    def return_from_show_history(self):
        self.return_to_main_screen('Возврат на страницу доктора')

    def do_dignos(self):
        patients_fio = [self.MainForm.doctor_ques[self.doctor.profession][patient].get_fio(patient+1) for patient in range(len(self.MainForm.doctor_ques[self.doctor.profession]))]
        now_pationt_fio = self.MainForm.active_elements['combo_chose_doctor'].get()
        need_index = patients_fio.index(now_pationt_fio)
        patient = self.MainForm.doctor_ques[self.doctor.profession][need_index]
        if self.MainForm.active_elements['combo_diagons'].get() not in patient.diagnos:
            patient.diagnos.append(self.MainForm.active_elements['combo_diagons'].get())
            patient.que_for = '-'
            patient.in_que = False
            self.MainForm.doctor_ques[self.doctor.profession].remove(patient)
            self.doctor.make_more_history(f"Пациенту {patient.get_fio()} был поставлен диагноз {self.MainForm.active_elements['combo_diagons'].get()}")
            patient.make_more_history(f"Врачом {self.doctor.get_fio()}({self.doctor.profession}) был поставлен диагноз {self.MainForm.active_elements['combo_diagons'].get()}")
            self.return_to_main_screen('Вы успешно поставили диагноз')
        else:
            self.MainForm.create_console("\nТакой диагноз уже поставлен")

    def show_que(self):
        if not self.show_que_flag:
            self.MainForm.create_console('Добавлена форма просмотра очереди')
            self.MainForm.active_elements['combo_chose_doctor'] = create_combo_box(width = 12, font_color = "#000000",
                                                                                   position=[275, 725],
                                                                                   values=[
                                                                                       self.MainForm.doctor_ques[self.doctor.profession][patient].get_fio(
                                                                                           patient+1) for patient in
                                                                                       range(len(self.MainForm.doctor_ques[self.doctor.profession]))],
                                                                                   default=None,
                                                                                   callback=self.create_diagnosis_combo, font = "Sedan 14")
            self.show_que_flag = True
        else:
            self.MainForm.create_console('Форма просмотра очереди удалена')
            if self.MainForm.active_elements.get('combo_chose_doctor') is not None:
                self.MainForm.active_elements['combo_chose_doctor'].destroy()
                del self.MainForm.active_elements['combo_chose_doctor']
            if self.MainForm.active_elements.get('combo_diagons') is not None:
                self.MainForm.active_elements['combo_diagons'].destroy()
                del self.MainForm.active_elements['combo_diagons']
            if self.MainForm.active_elements.get('submit') is not None:
                self.MainForm.active_elements['submit'].destroy()
                del self.MainForm.active_elements['submit']
            self.show_que_flag = False

    def show_history(self):
        text = self.doctor.show_history()
        if text == "":
            text = 'Истории пока нет'
            self.MainForm.create_console(text)
        else:
            self.MainForm.destroy_all()
            self.MainForm.active_elements['go_back'] = create_button(font_color='#ffffff', text="Назад",
                                                                     command=self.return_from_show_history,
                                                                     position=[1000, 700], background='#2998E9',
                                                                     width='25', height='3', font="Sedan 12")
            self.MainForm.create_big_console(text)

