import os
import webbrowser
import tkinter as tk
from tkinter import filedialog
from PySide2.QtWidgets import *
from UserInterface import Ui_MainWindow as design
from PySide2.QtCore import QParallelAnimationGroup, QPropertyAnimation, QEasingCurve, QPoint


class Package:
    @staticmethod
    def load_txt(user_interface, name):
        try:
            with open(f'{os.path.expanduser("~")}\AppData\Local\DOCX Search Engine\{name}.txt', 'r+',
                      encoding="utf-8") as file:
                try:
                    user_interface.setText(str(file.read()))
                except AttributeError:
                    user_interface.setPlainText(str(file.read()))
        except FileNotFoundError:
            pass

    @staticmethod
    def save_txt(name, value):
        with open(f'{os.path.expanduser("~")}\AppData\Local\DOCX Search Engine\{name}.txt', 'w+',
                  encoding="utf-8") as file:
            file.writelines(str(value))

    @staticmethod
    def ask_for_file():
        root = tk.Tk()
        root.withdraw()
        root.attributes('-topmost', True)
        file = filedialog.askopenfilename()
        if file != "":
            return file.replace('/', '\\')
        else:
            return "..."

    @staticmethod
    def search(keyword, docx_text):
        special_characters = [
            "۞",
            "ɸ"
        ]

        # Searching For Keyword
        results = []
        if " " in keyword:
            index = 0
            while index < len(docx_text):
                if docx_text[index:index + len(keyword)] == keyword:
                    first_index = index
                    while ' ' != docx_text[first_index]:
                        first_index -= 1

                    last_index = index + len(keyword) - 1
                    while ' ' != docx_text[last_index]:
                        last_index += 1

                    # Remove special characters and delete empty space
                    for character in special_characters:
                        if docx_text[first_index:last_index].replace(character, "").strip() not in results:
                            results.append(docx_text[first_index:last_index].replace(character, "").strip())

                index += 1
            return results

        else:
            for word in docx_text.split():
                if keyword in word:
                    for character in special_characters:
                        if word.replace(character, "").strip() not in results:
                            results.append(word.replace(character, "").strip())
            return results

    @staticmethod
    def help():
        print("This will be available in the future")
        # webbrowser.open('https://stackoverflow.com/questions/4302027/how-to-open-a-url-in-python')


class UserInterface(QMainWindow, design):
    def __init__(self):
        super(UserInterface, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("DOCX Search Engine")
        self.show()

    def transition(self, ui_element):
        self.anim_group = QParallelAnimationGroup()

        for element in ui_element:
            self.element = element
            x = self.element.x()
            y = self.element.y()
            element.move(x - 50, y)

        for element in ui_element:
            effect = QGraphicsOpacityEffect(element)
            self.element = element
            x = self.element.x()
            y = self.element.y()
            self.element.setGraphicsEffect(effect)
            self.anim_1 = QPropertyAnimation(effect, b"opacity")
            self.anim_1.setStartValue(0)
            self.anim_1.setEndValue(1)
            self.anim_1.setDuration(300)
            self.child = element
            self.anim = QPropertyAnimation(self.child, b"pos")
            self.anim.setEasingCurve(QEasingCurve.InOutCubic)
            self.anim.setEndValue(QPoint(x + 50, y))
            self.anim.setDuration(300)
            self.anim_group.addAnimation(self.anim_1)
            self.anim_group.addAnimation(self.anim)

        self.anim_group.start()
