from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from tüm_duyurular import Ui_MainWindow
from duyuruDialog_page import duyuru
import threading

class tümduyurularekran(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)


        self.ui.kapat.clicked.connect(self.ekranikapat)

        self.duyuruDialog_page=duyuru()


    def ekranikapat(self):

        self.close()

