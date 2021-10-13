from functools import partial
from tkinter import *
from tkinter import messagebox

import admin_change_user
import change_password
import input_password
# from main import users_main


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
        self.btn_changePassword = Button(self.root, text="Изменить пароль",
                             padx="20", pady="8", font="16", command=self.change_password)
        self.btn_changePassword.pack()

        self.btn_personalList = Button(self.root, text="Список пользователей",
                             padx="20", pady="8", font="16", command=self.change_users)
        self.btn_personalList.pack()

        self.btn_back = Button(self.root, text="Выход",
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
        if len(self.users['ADMIN']['password']) == 0:
            messagebox.showinfo("Попытка входа", "Необходимо сменить пароль")
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
