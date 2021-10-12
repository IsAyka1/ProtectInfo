from functools import partial
from tkinter import *
from tkinter import messagebox

import change_password
import input_password


class UserChoose:
    def __init__(self, root, users, login):
        self.root = root
        self.root.title("Главная страница пользователя")
        self.users = users
        self.login = login

        if self.check_need_change_password():
            self.change_password(self.users[self.login])
        else:
            self.draw_widgets()

    def check_need_change_password(self):
        if len(self.users[self.login]['password']) == 0 or self.users[self.login]['is_password_limited']:
            return True
        return False

    def draw_widgets(self):
        self.btn_changePassword = Button(self.root, text="Изменить пароль", foreground="#ccc",
                                         padx="20", pady="8", font="16",
                                         command=partial(self.change_password, self.users[self.login]))
        self.btn_changePassword.pack()

        self.btn_info = Button(self.root, text="О программе", foreground="#ccc",
                                       padx="20", pady="8", font="16", command=self.info)
        self.btn_info.pack()

        self.btn_back = Button(self.root, text="Выход", foreground="#ccc",
                               padx="20", pady="8", font="16", command=self.back)
        self.btn_back.pack()

    def delete_widgets(self):
        self.btn_changePassword.destroy()
        self.btn_info.destroy()
        self.btn_back.destroy()

    def change_password(self):
        self.delete_widgets()

        value = change_password.ChangePassword(self.root, self.users[self.login])
        value.draw_widgets()

    def info(self):
        messagebox.showinfo("О программе", "Автор: Исланова А.М. ИДБ-18-02\nЗадание: Наличие букв, цифр и знаков препинания")

    def back(self):
        self.delete_widgets()

        value = input_password.InputPassword(self.root, self.users)
        value.draw_widgets()