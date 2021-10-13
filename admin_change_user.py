from functools import partial
from tkinter import *

import create_user
import find_user
import admin_choose

class AdminChangeUser:
    def __init__(self, root, users):
        self.root = root
        self.root.geometry('650x400')
        self.root.title("Список пользователей")
        self.users = users
        self.users_list = list(users.values())
        self.users_list.pop(0)


    def user_next(self):
        self.delete_widgets()
        if self.id + 1 == len(self.users_list):
            self.id = 0
        else:
            self.id += 1
        self.draw_widgets(self.id)
    def user_before(self):
        self.delete_widgets()
        if self.id - 1 < 0:
            self.id = 0
        else:
            self.id -= 1
        self.draw_widgets(self.id)
    def user_start(self):
        self.delete_widgets()
        self.id = 0
        self.draw_widgets(self.id)
    def user_finish(self):
        self.delete_widgets()
        self.id = len(self.users_list) - 1
        self.draw_widgets(self.id)


    def draw_widgets(self, new_id = 0):
        self.id = new_id

        self.btn_before = Button(self.root, text="<",
                                padx="20", pady="8", font="16",
                                command=self.user_before)
        self.btn_before.grid(column=0, row=0)

        self.labellogin = Label(self.root, text="Логин: ", padx=20, pady=10)
        self.labellogin.grid(column=1, row=0)
        self.labellimit = Label(self.root, text="Ограничение на пароль: ", padx=20, pady=10)
        self.labellimit.grid(column=1, row=1)
        self.labelblock = Label(self.root, text="Заблокирован: ", padx=20, pady=10)
        self.labelblock.grid(column=1, row=2)

        self.btn_start = Button(self.root, text="В начало",
                                         padx="20", pady="8", font="16",
                                         command=self.user_start)
        self.btn_start.grid(column=0, row=2)
        self.btn_finish = Button(self.root, text="В конец",
                                padx="20", pady="8", font="16",
                                command=self.user_finish)
        self.btn_finish.grid(column=3, row=2)

        text_login = StringVar()
        text_login.set('')
        value_is_password_limited = BooleanVar()
        value_is_password_limited.set(False)
        value_is_blocked = BooleanVar()
        value_is_blocked.set(False)
        if len(self.users_list) != 0:
            text_login.set(self.users_list[self.id]['login'])
            value_is_password_limited.set(self.users_list[self.id]['is_password_limited'] == 'True')
            value_is_blocked.set(self.users_list[self.id]['is_blocked'] == 'True')
        else:
            self.id = -1

        self.labellogin_user = Label(self.root, text=text_login.get(), padx=20, pady=10)
        self.labellogin_user.grid(column=2, row=0)
        self.check_is_password_limited = Checkbutton(self.root, variable=value_is_password_limited, onvalue=1, offvalue=0)
        self.check_is_password_limited.grid(column=2, row=1)
        self.check_is_blocked = Checkbutton(self.root, variable=value_is_blocked, onvalue=1,
                                                     offvalue=0)
        self.check_is_blocked.grid(column=2, row=2)

        self.btn_next = Button(self.root, text=">",
                               padx="20", pady="8", font="16",
                               command=self.user_next)
        self.btn_next.grid(column=3, row=0)

        self.btn_save = Button(self.root, text="Сохранить", background="#555", foreground="#ccc",
                               padx="20", pady="8", font="16",
                               command=partial(self.save, value_is_password_limited, value_is_blocked, text_login, self.id))
        self.btn_save.grid(column=0, row=3)
        self.btn_add = Button(self.root, text="Добавить пользователя",
                              padx="20", pady="8", font="16",
                              command=self.add)
        self.btn_add.grid(column=1, row=3)
        self.btn_find = Button(self.root, text="Найти пользователя",
                               padx="20", pady="8", font="16",
                               command=self.find)
        self.btn_find.grid(column=2, row=3)
        self.btn_back = Button(self.root, text="Назад",
                                         padx="20", pady="8", font="16",
                                         command=self.back)
        self.btn_back.grid(column=3, row=3)


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


    def save(self, value_is_password_limited, value_is_blocked, value_login, id = -1):
        if id != -1:
            self.users_list[id]['is_password_limited'] = str(value_is_password_limited.get())
            self.users_list[id]['is_blocked'] = str(value_is_blocked.get())
            self.users[value_login.get()]['is_password_limited'] = str(value_is_password_limited.get())
            self.users[value_login.get()]['is_blocked'] = str(value_is_blocked.get())

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

        value = admin_choose.AdminChoose(self.root, self.users)
