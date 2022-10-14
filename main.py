# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 17:34:07 2022

@author: Everton Castro
"""


from sys import argv
from splash_art import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5 import QtGui
import sys

class Inicializa(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__(parent = None)
        super().setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)




if __name__ == "__main__":
    qt = QApplication(argv)
    window = Inicializa() 
    window.show()
    
    exit(qt.exec_())