from PyQt5.QtWidgets import *
from duyuruDialog import Ui_Dialog

class duyuru(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)

