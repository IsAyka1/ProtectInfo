from crypto import *
from tkinter import *
import sys
from functools import partial

from input_password import *
from reading_file import *

class InputCode:
    def __init__(self, root, users):
        self.root = root
        self.root.geometry('500x400')
        self.root.title("Вход")
        self.users = users


    def draw_widgets(self):

        self.label = Label(self.root, text="Введите парольную фразу", padx=20, pady=10)
        self.label.pack()

        self.password = StringVar()
        self.entry = Entry(self.root, show="*", textvariable=self.password)
        self.entry.pack()

        self.button = Button(self.root, text="Далее", background="#555", foreground="#ccc",
                 padx="20", pady="8", font="16", command=partial(self.check_password, self.password))
        self.button.pack()


    def delete_widgets(self):
        self.label.destroy()
        self.entry.destroy()
        self.button.destroy()

    def check_password(self, password):
        if decrypt(password):
            self.users = read_from_json()
            self.delete_widgets()
            input_pass = InputPassword(self.root, self.users)
            input_pass.draw_widgets()
        else:
            sys.exit()
