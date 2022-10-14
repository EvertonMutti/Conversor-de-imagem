# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Splash_Intro.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Splash_Intro(object):
    def setupUi(self, Splash_Intro):
        Splash_Intro.setObjectName("Splash_Intro")
        Splash_Intro.resize(501, 530)
        self.centralwidget = QtWidgets.QWidget(Splash_Intro)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 501, 531))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-image: url(:/Intro/Conversor.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(50, 440, 411, 23))
        self.progressBar.setStyleSheet("QProgressBar {\n"
"text-align:center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.119, x2:0.943182, y2:0, stop:0 rgba(255, 92, 92, 255), stop:0.166 rgba(255, 192, 66, 255), stop:0.333 rgba(101, 255, 127, 255), stop:0.5 rgba(0, 255, 255, 255), stop:0.666 rgba(46, 222, 225, 255), stop:0.833 rgba(31, 132, 226, 255), stop:1 rgba(163, 82, 255, 255));\n"
"}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        Splash_Intro.setCentralWidget(self.centralwidget)

        self.retranslateUi(Splash_Intro)
        QtCore.QMetaObject.connectSlotsByName(Splash_Intro)

    def retranslateUi(self, Splash_Intro):
        _translate = QtCore.QCoreApplication.translate
        Splash_Intro.setWindowTitle(_translate("Splash_Intro", "MainWindow"))

import Ui.Intro
