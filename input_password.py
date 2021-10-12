from functools import partial
from tkinter import messagebox
from tkinter import *

import admin_choose
import user_choose

last_login = None
count = 3


class InputPassword:
    def __init__(self, root, users):
        self.root = root
        self.root.title("Авторизация")
        self.users = users

    def draw_widgets(self):
        self.labellogin = Label(self.root, text="Логин", padx=20, pady=10)
        self.labellogin.pack()

        login = StringVar()
        self.entrylogin = Entry(self.root, textvariable=login)
        self.entrylogin.pack()

        self.labelpassword = Label(self.root, text="Пароль", padx=20, pady=10)
        self.labelpassword.pack()

        password = StringVar()
        self.entrypassword = Entry(self.root, show="*", textvariable=password)
        self.entrypassword.pack()

        self.button = Button(self.root, text="Войти", background="#555", foreground="#ccc",
                             padx="20", pady="8", font="16", command=partial(self.check_user_data, login, password))
        self.button.pack()

    def delete_widgets(self):
        self.labelpassword.destroy()
        self.entrypassword.destroy()
        self.labellogin.destroy()
        self.entrylogin.destroy()
        self.button.destroy()

    def check_user_data(self, login_value, password_value):
        global last_login, count

        try:
            tmp = login_value.get()
            user = self.users[tmp]
        except KeyError:
            messagebox.showinfo("Попытка входа", "Логин не верный")
            return

        if self.users[login_value.get()]['password'] == password_value.get():
            count = 3
            last_login = None
            if login_value.get() == 'ADMIN':
                self.delete_widgets()
                main_page = admin_choose.AdminChoose(self.root, self.users)
                return
            else:
                self.delete_widgets()
                if self.users[login_value.get()]['is_blocked']:
                    messagebox.showerror("Попытка входа", "Вход заблокирован администратором")
                    sys.exit()
                main_page = user_choose.UserChoose(self.root, self.users, login_value.get())
                return
        elif last_login != login_value.get():
            last_login = login_value.get()
            count = 3
        if count > 1:
            count -= 1
        else:
            messagebox.showerror("Попытка входа", "Пароль не верный\nПопытки входа закончились")
            sys.exit()
        messagebox.showinfo("Попытка входа", "Пароль не верный\nОсталось попыток: " + str(count))