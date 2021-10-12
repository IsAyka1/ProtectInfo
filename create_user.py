from functools import partial
from tkinter import *
from tkinter import messagebox

import admin_change_user


class CreateUser:
    def __init__(self, root, users):
        self.root = root
        self.root.title("Создание нового пользователя")
        self.users = users

    def __del__(self):
        users_main = self.users

    def draw_widgets(self):
        self.labellogin = Label(self.root, text="Логин", padx=20, pady=10)
        self.labellogin.pack()

        login = StringVar()
        self.entrylogin = Entry(self.root, textvariable=login)
        self.entrylogin.pack()

        self.button = Button(self.root, text="Добавить", background="#555", foreground="#ccc",
                             padx="20", pady="8", font="16",
                             command=partial(self.add_user, login))
        self.button.pack()
        self.button_back = Button(self.root, text="Назад", background="#555", foreground="#ccc",
                             padx="20", pady="8", font="16",
                             command=self.back)
        self.button_back.pack()

    def delete_widgets(self):
        self.users.clear()
        self.labellogin.destroy()
        self.entrylogin.destroy()
        self.button.destroy()
        self.button_back.destroy()

    def back(self):
        tmp = self.users
        self.delete_widgets()

        value = admin_change_user.AdminChangeUser(self.root, tmp)
        value.draw_widgets()

    def add_user(self, value_login):
        self.users[value_login.get()] = {"login": "", "password": "", "is_password_limited": "False", "is_blocked": "False"}
        self.users[value_login.get()]['login'] = value_login.get()

        messagebox.showinfo("Создание нового пользователя", "Пользователь успешно создан")
        tmp = self.users
        self.delete_widgets()
        value = admin_change_user.AdminChangeUser(self.root, tmp)
        value.draw_widgets(len(tmp) - 2)

