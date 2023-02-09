# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UserInterface.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1008, 650)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget#centralwidget{\n"
"background: qlineargradient(spread:pad, x1:0, y1:0.528409, x2:1, y2:0.523, stop:0 rgba(0, 242, 96, 255), stop:1 rgba(5, 117, 230, 255));\n"
"}\n"
"")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.MainPage = QWidget()
        self.MainPage.setObjectName(u"MainPage")
        self.gridLayout_2 = QGridLayout(self.MainPage)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.InputsLayout = QVBoxLayout()
        self.InputsLayout.setSpacing(30)
        self.InputsLayout.setObjectName(u"InputsLayout")
        self.InputsLayout.setContentsMargins(100, -1, 100, 30)
        self.Spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.InputsLayout.addItem(self.Spacer)

        self.DOCXFileLayout = QHBoxLayout()
        self.DOCXFileLayout.setSpacing(0)
        self.DOCXFileLayout.setObjectName(u"DOCXFileLayout")
        self.DOCXFileLabel = QLabel(self.MainPage)
        self.DOCXFileLabel.setObjectName(u"DOCXFileLabel")
        self.DOCXFileLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background: transparent;\n"
"font: 87 14pt \"Segoe UI Black\";")

        self.DOCXFileLayout.addWidget(self.DOCXFileLabel)

        self.DOCXFileButton = QPushButton(self.MainPage)
        self.DOCXFileButton.setObjectName(u"DOCXFileButton")
        self.DOCXFileButton.setMinimumSize(QSize(300, 35))
        self.DOCXFileButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.DOCXFileButton.setStyleSheet(u"QPushButton#DOCXFileButton{\n"
"	border: none;\n"
"	background-color: #fff;\n"
"	border-radius: 10px;\n"
"	color: #000\n"
"}\n"
"QPushButton#DOCXFileButton::hover{\n"
"	background-color: transparent;\n"
"	border: 1px solid #fff;\n"
"	color: #fff;\n"
"}")

        self.DOCXFileLayout.addWidget(self.DOCXFileButton)


        self.InputsLayout.addLayout(self.DOCXFileLayout)

        self.KeywordLayout = QHBoxLayout()
        self.KeywordLayout.setSpacing(0)
        self.KeywordLayout.setObjectName(u"KeywordLayout")
        self.KeywordLabel = QLabel(self.MainPage)
        self.KeywordLabel.setObjectName(u"KeywordLabel")
        self.KeywordLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background: transparent;\n"
"font: 87 14pt \"Segoe UI Black\";")

        self.KeywordLayout.addWidget(self.KeywordLabel)

        self.Keyword = QLineEdit(self.MainPage)
        self.Keyword.setObjectName(u"Keyword")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Keyword.sizePolicy().hasHeightForWidth())
        self.Keyword.setSizePolicy(sizePolicy)
        self.Keyword.setMinimumSize(QSize(300, 35))
        self.Keyword.setMaximumSize(QSize(16777215, 16777215))
        self.Keyword.setStyleSheet(u"border: 1px solid white;\n"
"border-radius: 10px;\n"
"color: white;\n"
"font: 15pt \"Tw Cen MT Condensed Extra Bold\";\n"
"background: transparent;")
        self.Keyword.setAlignment(Qt.AlignCenter)

        self.KeywordLayout.addWidget(self.Keyword)


        self.InputsLayout.addLayout(self.KeywordLayout)

        self.Spacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.InputsLayout.addItem(self.Spacer_2)


        self.gridLayout_2.addLayout(self.InputsLayout, 0, 0, 1, 1)

        self.StartLayout = QHBoxLayout()
        self.StartLayout.setObjectName(u"StartLayout")
        self.StartLayout.setContentsMargins(-1, -1, -1, 40)
        self.Spacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.StartLayout.addItem(self.Spacer_3)

        self.StartButtonLayout = QVBoxLayout()
        self.StartButtonLayout.setObjectName(u"StartButtonLayout")
        self.HowDoesItWorkButton = QPushButton(self.MainPage)
        self.HowDoesItWorkButton.setObjectName(u"HowDoesItWorkButton")
        self.HowDoesItWorkButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.HowDoesItWorkButton.setStyleSheet(u"color: rgb(0, 0, 255);\n"
"font: 9pt \"MS Sans Serif\";\n"
"text-decoration: underline;")

        self.StartButtonLayout.addWidget(self.HowDoesItWorkButton)

        self.StartButton = QPushButton(self.MainPage)
        self.StartButton.setObjectName(u"StartButton")
        self.StartButton.setMinimumSize(QSize(300, 40))
        self.StartButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.StartButton.setStyleSheet(u"QPushButton#StartButton{\n"
"	border: none;\n"
"	background-color: #fff;\n"
"	border-radius: 10px;\n"
"	color: #000\n"
"}\n"
"QPushButton#StartButton::hover{\n"
"	background-color: transparent;\n"
"	border: 1px solid #fff;\n"
"	color: #fff;\n"
"}")

        self.StartButtonLayout.addWidget(self.StartButton)


        self.StartLayout.addLayout(self.StartButtonLayout)

        self.Spacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.StartLayout.addItem(self.Spacer_4)


        self.gridLayout_2.addLayout(self.StartLayout, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.MainPage)
        self.StatusPage = QWidget()
        self.StatusPage.setObjectName(u"StatusPage")
        self.gridLayout_3 = QGridLayout(self.StatusPage)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.Spacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.Spacer_9, 0, 0, 1, 1)

        self.StatusLayout = QVBoxLayout()
        self.StatusLayout.setSpacing(50)
        self.StatusLayout.setObjectName(u"StatusLayout")
        self.StatusLayout.setContentsMargins(-1, -1, -1, 50)
        self.WorkingLabel = QLabel(self.StatusPage)
        self.WorkingLabel.setObjectName(u"WorkingLabel")
        self.WorkingLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background: transparent;\n"
"font: 87 14pt \"Segoe UI Black\";")
        self.WorkingLabel.setAlignment(Qt.AlignCenter)

        self.StatusLayout.addWidget(self.WorkingLabel)


        self.gridLayout_3.addLayout(self.StatusLayout, 1, 0, 1, 1)

        self.CopyResultsWithConfirmLayout = QHBoxLayout()
        self.CopyResultsWithConfirmLayout.setObjectName(u"CopyResultsWithConfirmLayout")
        self.Spacer_6 = QSpacerItem(37, 37, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.CopyResultsWithConfirmLayout.addItem(self.Spacer_6)

        self.CopyResultsLayout = QVBoxLayout()
        self.CopyResultsLayout.setObjectName(u"CopyResultsLayout")
        self.CopyReslutsButton = QPushButton(self.StatusPage)
        self.CopyReslutsButton.setObjectName(u"CopyReslutsButton")
        self.CopyReslutsButton.setMinimumSize(QSize(300, 40))
        self.CopyReslutsButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.CopyReslutsButton.setStyleSheet(u"QPushButton#CopyReslutsButton{\n"
"	border: none;\n"
"	background-color: #fff;\n"
"	border-radius: 10px;\n"
"	color: #000\n"
"}\n"
"QPushButton#CopyReslutsButton::hover{\n"
"	background-color: transparent;\n"
"	border: 1px solid #fff;\n"
"	color: #fff;\n"
"}")

        self.CopyResultsLayout.addWidget(self.CopyReslutsButton)

        self.EmailCopiedSuccessfullyLabel = QLabel(self.StatusPage)
        self.EmailCopiedSuccessfullyLabel.setObjectName(u"EmailCopiedSuccessfullyLabel")
        self.EmailCopiedSuccessfullyLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background: transparent;\n"
"font: 87 11pt \"Segoe UI Black\";")
        self.EmailCopiedSuccessfullyLabel.setAlignment(Qt.AlignCenter)

        self.CopyResultsLayout.addWidget(self.EmailCopiedSuccessfullyLabel)


        self.CopyResultsWithConfirmLayout.addLayout(self.CopyResultsLayout)

        self.Spacer_5 = QSpacerItem(37, 37, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.CopyResultsWithConfirmLayout.addItem(self.Spacer_5)


        self.gridLayout_3.addLayout(self.CopyResultsWithConfirmLayout, 2, 0, 1, 1)

        self.Spacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.Spacer_10, 3, 0, 1, 1)

        self.BackToMainPageLayout = QHBoxLayout()
        self.BackToMainPageLayout.setObjectName(u"BackToMainPageLayout")
        self.BackToMainPageLayout.setContentsMargins(-1, -1, -1, 40)
        self.Spacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BackToMainPageLayout.addItem(self.Spacer_7)

        self.BackToMainPageButton = QPushButton(self.StatusPage)
        self.BackToMainPageButton.setObjectName(u"BackToMainPageButton")
        self.BackToMainPageButton.setMinimumSize(QSize(300, 40))
        self.BackToMainPageButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.BackToMainPageButton.setStyleSheet(u"QPushButton#BackToMainPageButton{\n"
"	border: none;\n"
"	background-color: #fff;\n"
"	border-radius: 10px;\n"
"	color: #000\n"
"}\n"
"QPushButton#BackToMainPageButton::hover{\n"
"	background-color: transparent;\n"
"	border: 1px solid #fff;\n"
"	color: #fff;\n"
"}")

        self.BackToMainPageLayout.addWidget(self.BackToMainPageButton)

        self.Spacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BackToMainPageLayout.addItem(self.Spacer_8)


        self.gridLayout_3.addLayout(self.BackToMainPageLayout, 4, 0, 1, 1)

        self.stackedWidget.addWidget(self.StatusPage)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.DOCXFileLabel.setText(QCoreApplication.translate("MainWindow", u"DOCX File :", None))
        self.DOCXFileButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.KeywordLabel.setText(QCoreApplication.translate("MainWindow", u"Keyword :", None))
        self.Keyword.setPlaceholderText(QCoreApplication.translate("MainWindow", u"...", None))
        self.HowDoesItWorkButton.setText(QCoreApplication.translate("MainWindow", u"How does it work ?", None))
        self.StartButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.WorkingLabel.setText(QCoreApplication.translate("MainWindow", u"Working ...", None))
        self.CopyReslutsButton.setText(QCoreApplication.translate("MainWindow", u"Copy Results", None))
        self.EmailCopiedSuccessfullyLabel.setText("")
        self.BackToMainPageButton.setText(QCoreApplication.translate("MainWindow", u"Back", None))
    # retranslateUi

