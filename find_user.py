from functools import partial
from tkinter import *
from tkinter import messagebox

import admin_change_user


class FindUser:
    def __init__(self, root, users):
        self.root = root
        self.root.title("Поиск пользователя")
        self.users = users

    def draw_widgets(self):
        self.labellogin = Label(self.root, text="Логин", padx=20, pady=10)
        self.labellogin.pack()

        login = StringVar()
        self.entrylogin = Entry(self.root, textvariable=login)
        self.entrylogin.pack()

        self.button = Button(self.root, text="Найти", background="#555", foreground="#ccc",
                             padx="20", pady="8", font="16",
                             command=partial(self.find_user, login))
        self.button.pack()
        self.button_back = Button(self.root, text="Найти", background="#555", foreground="#ccc",
                             padx="20", pady="8", font="16",
                             command=self.back)
        self.button_back.pack()

    def delete_widgets(self):
        self.labellogin.destroy()
        self.entrylogin.destroy()
        self.button.destroy()
        self.button_back.destroy()

    def back(self):
        self.delete_widgets()

        value = admin_change_user.AdminChangeUser(self.root, self.users)
        value.draw_widgets()

    def find_user(self, value_login):
        value = admin_change_user.AdminChangeUser(self.root, self.users)
        try:
            user = self.users[value_login.get()]
            users = list(self.users.values())
            users.pop(0)
            messagebox.showinfo("Поиск пользователя", "Пользователь найден")
            self.delete_widgets()
            value.draw_widgets(users.index(user))
        except KeyError:
            messagebox.showinfo("Поиск пользователя", "Пользователь не найден")
