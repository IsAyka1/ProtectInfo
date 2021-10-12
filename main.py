from tkinter import *
from input_code import *
from reading_file import *

users = {}

class MainClass():
    def __del__(self):
        write_to_json(users)

def main():
    mainClass = MainClass()
    code = InputCode(Tk(), users)
    code.draw_widgets()

    code.root.mainloop()


if __name__ == '__main__':
    main()


