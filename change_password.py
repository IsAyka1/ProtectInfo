from functools import partial
from tkinter import *
from tkinter import messagebox

import user_choose
import admin_choose
# from main import users_main


class ChangePassword:
    def __init__(self, root, users, user):
        self.root = root
        self.root.title("Изменение пароля")
        self.user = user
        self.users = users

    def __del__(self):
        users_main = self.users

    def draw_widgets(self):
        self.label_old_password = Label(self.root, text="Старый пароль", padx=20, pady=10)
        self.label_old_password.pack()
        old_password = StringVar()
        self.entry_old_password = Entry(self.root, show="*", textvariable=old_password)
        self.entry_old_password.pack()

        self.label_new_password = Label(self.root, text="Новый пароль", padx=20, pady=10)
        self.label_new_password.pack()
        new_password = StringVar()
        self.entry_new_password = Entry(self.root, show="*", textvariable=new_password)
        self.entry_new_password.pack()

        self.label_new_password2 = Label(self.root, text="Повторите новый пароль", padx=20, pady=10)
        self.label_new_password2.pack()
        new_password2 = StringVar()
        self.entry_new_password2 = Entry(self.root, show="*", textvariable=new_password2)
        self.entry_new_password2.pack()

        self.button_change = Button(self.root, text="Изменить", background="#555", foreground="#ccc",
                                    padx="20", pady="8", font="16",
                                    command=partial(self.change, old_password, new_password,
                                                    new_password2))
        self.button_change.pack()
        self.button_back = Button(self.root, text="Назад", foreground="#ccc",
                                  padx="20", pady="8", font="16",
                                  command=self.draw_widgets)
        self.button_back.pack()

    def delete_widgets(self):
        self.users.clear()
        self.label_old_password.destroy()
        self.entry_old_password.destroy()
        self.label_new_password.destroy()
        self.entry_new_password.destroy()
        self.label_new_password2.destroy()
        self.entry_new_password2.destroy()
        self.button_change.destroy()
        self.button_back.destroy()

    def change(self, old_pass_value, new_pass_value, new_pass_value2):
        if old_pass_value.get() == self.user['password']:
            if new_pass_value.get() == new_pass_value2.get():
                if self.user['is_password_limited'] != 'True':
                    messagebox.showinfo("Изменение пароля", "Пароль успешно изменен")
                    self.users[self.user['login']]['password'] = new_pass_value2.get() #users[self.user['login']][password]!!!!
                    self.back()
                elif self.check_password_limit(new_pass_value.get()):
                    messagebox.showinfo("Изменение пароля", "Пароль успешно изменен")
                    self.users[self.user['login']]['password'] = new_pass_value2.get() #users[self.user['login']][\password]!!!!
                    self.back()
                    return
                else:
                    messagebox.showerror("Изменение пароля", "Новый пароль не удовлетворяет ограничениям:\nДолжны присутствовать буквы, цифры и знаки препинания")
            else:
                messagebox.showerror("Изменение пароля", "Новые пароли не совпадают")
        else:
            messagebox.showerror("Изменение пароля", "Старый пароль введен не верно")


    def back(self):
        if len(self.user['password']) == 0:
            messagebox.showinfo("Смена пароля", 'Нельзя выходить с пустым паролем')
            return
        if self.user['is_password_limited'] == 'True':
            if self.check_password_limit(self.user['password']):
                messagebox.showinfo("Смена пароля", 'Необходимо сменить пароль учитывая ограничения')
                return
        tmp = self.users
        self.delete_widgets()
        if self.user['login'] == 'ADMIN':
            value = admin_choose.AdminChoose(self.root, tmp)
            return
        else:
            value = user_choose.UserChoose(self.root, tmp, self.user)
            return


    def check_password_limit(self, password):
        letters = {'letters': 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
         'digit': '1234567890',
         'sign': """!\#$%&'()*+-/:;<,=.>?@[]^_`{|}~"""}
        check = {'letters': False, 'digit': False, 'sign': False}

        for let in password:
            for key in check.keys():
                if let in letters[key]:
                    check[key] = True
        return check['letters'] and check['digit'] and check['sign']
