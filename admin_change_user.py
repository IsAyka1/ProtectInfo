from functools import partial
from tkinter import *

import create_user
import find_user
import input_password

class AdminChangeUser:
    def __init__(self, root, users, login_value):
        self.root = root
        self.root.title("Список пользователей")
        self.users = users
        self.users_list = list(users.items())
        self.users_list.pop(0)


    def user_next(self):
        if self.id + 1 == len(self.users_list):
            self.id = 0
        else:
            self.id += 1
    def user_before(self):
        if self.id - 1 < 0:
            self.id = 1
        else:
            self.id -= 1
    def user_start(self):
        self.id = 0
    def user_finish(self):
        self.id = len(self.users_list) - 1


    def draw_widgets(self, new_id = 0):
        self.id = new_id

        self.btn_before = Button(self.root, text="<", foreground="#ccc",
                                padx="20", pady="8", font="16",
                                command=self.user_before)
        self.btn_before.grid(column=0, row=0)

        self.btn_next = Button(self.root, text=">", foreground="#ccc",
                               padx="20", pady="8", font="16",
                               command=self.user_next)
        self.btn_next.grid(column=3, row=0)

        self.labellogin = Label(self.root, text="Логин: ", padx=20, pady=10)
        self.labellogin.grid(column=1, row=0)
        self.labellimit = Label(self.root, text="Ограничение на пароль: ", padx=20, pady=10)
        self.labellimit.grid(column=1, row=1)
        self.labelblock = Label(self.root, text="Заблокирован: ", padx=20, pady=10)
        self.labelblock.grid(column=1, row=2)

        self.btn_start = Button(self.root, text="В начало", foreground="#ccc",
                                         padx="20", pady="8", font="16",
                                         command=self.user_start)
        self.btn_start.grid(column=0, row=2)
        self.btn_finish = Button(self.root, text="В конец", foreground="#ccc",
                                padx="20", pady="8", font="16",
                                command=self.user_finish)
        self.btn_finish.grid(column=0, row=2)

        self.labellogin_user = Label(self.root, text=self.users_list[self.id]['login'], padx=20, pady=10)
        self.labellogin_user.grid(column=2, row=0)
        value_is_password_limited = BooleanVar()
        value_is_password_limited.set(self.users_list[self.id]['is_password_limited'])
        self.check_is_password_limited = Checkbutton(self.root, variable=value_is_password_limited, onvalue=1, offvalue=0)
        self.check_is_password_limited.grid(column=2, row=1)
        value_is_blocked = BooleanVar()
        value_is_blocked.set(self.users_list[self.id]['is_blocked'])
        self.check_is_blocked = Checkbutton(self.root, variable=value_is_blocked, onvalue=1,
                                                     offvalue=0)
        self.check_is_blocked.grid(column=2, row=2)

        self.btn_save = Button(self.root, text="Сохранить", background="#555", foreground="#ccc",
                               padx="20", pady="8", font="16",
                               command=partial(self.save, value_is_password_limited, value_is_blocked, self.users_list[self.id]['login']))
        self.btn_save.grid(column=0, row=3)
        self.btn_add = Button(self.root, text="Добавить пользователя", foreground="#ccc",
                              padx="20", pady="8", font="16",
                              command=self.add)
        self.btn_add.grid(column=1, row=3)
        self.btn_find = Button(self.root, text="Найти пользователя", foreground="#ccc",
                               padx="20", pady="8", font="16",
                               command=self.find)
        self.btn_find.grid(column=2, row=3)
        self.btn_back = Button(self.root, text="Назад", foreground="#ccc",
                                         padx="20", pady="8", font="16",
                                         command=self.back)
        self.btn_back.grid(column=2, row=3)


    def delete_widgets(self):
        self.btn_before.destroy()
        self.btn_next.destroy()
        self.labellogin.destroy()
        self.labellimit.destroy()
        self.labelblock.destroy()
        self.btn_start.destroy()
        self.btn_finish.destroy()
        self.labellogin_user.destroy()
        self.check_is_password_limited.destroy()
        self.check_is_blocked.destroy()
        self.btn_save.destroy()
        self.btn_add.destroy()
        self.btn_find.destroy()
        self.btn_back.destroy()


    def save(self, value_is_password_limited, value_is_blocked, login):
        self.delete_widgets()

        self.users_list[login]['is_password_limited'] = value_is_password_limited.get()
        self.users_list[login]['is_blocked'] = value_is_blocked.get()
        value = input_password.InputPassword(self.root, self.users_list)
        value.draw_widgets()

    def add(self):
        self.delete_widgets()

        value = create_user.CreateUser(self.root, self.users)
        value.draw_widgets()

    def find(self):
        self.delete_widgets()

        value = find_user.FindUser(self.root, self.users)
        value.draw_widgets()

    def back(self):
        self.delete_widgets()

        value = input_password.InputPassword(self.root, self.users)
        value.draw_widgets()
