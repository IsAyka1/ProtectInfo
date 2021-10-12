from tkinter import *

import input_code
import reading_file


class MainClass:
    def __init__(self, users):
        self.users = users

    def __del__(self):
        if len(self.users):
            reading_file.write_to_json(self.users)


def main():
    users = {}
    main_class = MainClass(users)
    code = input_code.InputCode(Tk(), users)
    code.draw_widgets()

    code.root.mainloop()


if __name__ == '__main__':
    main()


