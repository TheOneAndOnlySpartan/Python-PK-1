from tkinter import *
from tkinter import Tk, filedialog

class Deleter:
    def __init__(self):
        self.width = 400
        self.height = 300
        self.root = Tk()
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()

        self.path = ""

    def main(self):
        x = (self.screen_width / 2) - (self.width / 2)
        y = (self.screen_height / 2) - (self.height / 2)

        self.root.title = "Удалятор комментариев"
        self.root.geometry("%dx%d+%d+%d" % (self.width, self.height, x, y))

        Button(self.root, text="Открыть файл", command=self.ask_for_file).pack()

        self.root.mainloop()

    def ask_for_file(self):
        self.path = filedialog.askopenfilename(
            initialdir="/",
            title="выберите питоновский файл",
            filetype=(("Файлы Python", "*.py"), ("Текстовые файлы", "*.txt"), ("Все файлы", "*.*"))
        )

        if self.path:
            Label(self.root, text=self.path).pack()
            self.make_tests()

    def make_tests(self):
        have_comments: bool = False

        with open(self.path, "r") as file:
            for thing in file.readlines():
                if thing.startswith("#"):
                    have_comments = True
                    Label(self.root, text="Файл имеет комментарии").pack()
                    Button(self.root, text="Удалить комментарии", command=self.delete_comments).pack()
                    return

    def delete_comments(self):
        original_content = ""
        edited_content = ""

        with open(self.path, "r", encoding="utf-8") as file:
            for string in file.readlines():
                original_content += string

        with open(self.path, "r", encoding="utf-8") as file:
            for string in file.readlines():
                if not string.startswith("#"):
                    edited_content += string

        with open(self.path, "w", encoding="utf-8") as file:
            file.write(edited_content)

        Label(self.root, text="Сделано!").pack()


if __name__ == '__main__':
    app = Deleter().main()
