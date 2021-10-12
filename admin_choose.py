from functools import partial
from tkinter import *

import admin_change_user
import change_password
import input_password


class AdminChoose:
    def __init__(self, root, users):
        self.root = root
        self.root.title("Главная страница администратора")
        self.users = users

        if len(self.users['ADMIN']['password']) == 0:
            self.change_password()
        else:
            self.draw_widgets()


    def draw_widgets(self):
        self.btn_changePassword = Button(self.root, text="Изменить пароль", foreground="#ccc",
                             padx="20", pady="8", font="16", command=partial(self.change_password, self.users['ADMIN']))
        self.btn_changePassword.pack()

        self.btn_personalList = Button(self.root, text="Список пользователей", foreground="#ccc",
                             padx="20", pady="8", font="16", command=self.change_users)
        self.btn_personalList.pack()

        self.btn_back = Button(self.root, text="Выход", foreground="#ccc",
                             padx="20", pady="8", font="16", command=self.back)
        self.btn_back.pack()


    def delete_widgets(self):
        self.btn_changePassword.destroy()
        self.btn_personalList.destroy()
        self.btn_back.destroy()

    def change_password(self):
        try:
            self.delete_widgets()
        except AttributeError:
            pass
        value = change_password.ChangePassword(self.root, self.users, self.users['ADMIN'])
        value.draw_widgets()

    def change_users(self):
        self.delete_widgets()

        value = admin_change_user.AdminChangeUser(self.root, self.users)
        value.draw_widgets()

    def back(self):
        self.delete_widgets()

        value = input_password.InputPassword(self.root, self.users)
        value.draw_widgets()
