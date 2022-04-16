from PyQt5.QtWidgets import *
from mesaj_iletildi import Ui_Dialog


class mesajiletimi(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)


