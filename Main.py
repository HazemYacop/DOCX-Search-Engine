import docx
import pandas
import _ctypes
import threading
from PySide2.QtWidgets import QApplication
from Functions import Package, UserInterface


class Main:
    def __init__(self):
        super().__init__()
        # Re-translating UI
        self.UserInterface = UserInterface()
        self.UserInterface.stackedWidget.setCurrentIndex(0)

        # Button(s) Functions(s)
        self.UserInterface.StartButton.clicked.connect(lambda: [self.required_data(), threading.Thread(target=self.main).start(), self.UserInterface.stackedWidget.setCurrentIndex(1), self.UserInterface.transition([self.UserInterface.stackedWidget]), self.UserInterface.WorkingLabel.setText("Working ..."), self.UserInterface.BackToMainPageButton.setDisabled(True), self.UserInterface.CopyReslutsButton.setDisabled(True), self.UserInterface.EmailCopiedSuccessfullyLabel.setText("")])
        self.UserInterface.DOCXFileButton.clicked.connect(lambda: self.UserInterface.DOCXFileButton.setText(Package.ask_for_file()))
        self.UserInterface.CopyReslutsButton.clicked.connect(lambda: [pandas.DataFrame(self.results).to_clipboard(index=False, header=False), self.UserInterface.EmailCopiedSuccessfullyLabel.setText("Copied !")])
        self.UserInterface.BackToMainPageButton.clicked.connect(lambda: [self.UserInterface.stackedWidget.setCurrentIndex(0), self.UserInterface.transition([self.UserInterface.stackedWidget])])
        self.UserInterface.HowDoesItWorkButton.clicked.connect(lambda: Package.help())

    def main(self):
        try:
            # Converting DOCX file to a string
            docx_text = []
            for paragraph in docx.Document(self.docx_file).paragraphs:
                docx_text.append(paragraph.text)

            self.results = Package.search(self.keyword, '\n'.join(docx_text))  # Searches for keyword

            # Re-translating UI
            self.UserInterface.WorkingLabel.setText(f"Program finished\nResults : {len(self.results)}")
            self.UserInterface.CopyReslutsButton.setDisabled(False)
            self.UserInterface.BackToMainPageButton.setDisabled(False)

        except Exception as e:
            print(e)
            self.UserInterface.WorkingLabel.setText("Error Occurred, Take a screenshot of the CMD (Black Screen) and Contact : +201150169348")
            self.UserInterface.BackToMainPageButton.setDisabled(False)

    def required_data(self):
        self.docx_file = self.UserInterface.DOCXFileButton.text()
        self.keyword = self.UserInterface.Keyword.text()


if __name__ == '__main__':
    app = QApplication()
    main = Main()
    app.exec_()
