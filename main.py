from tkinter import *

import input_code
import reading_file

users = {}

class MainClass():
    def __del__(self):
        reading_file.write_to_json(users)

def main():
    mainClass = MainClass()
    code = input_code.InputCode(Tk(), users)
    code.draw_widgets()

    code.root.mainloop()


if __name__ == '__main__':
    main()


