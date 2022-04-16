from PyQt5.QtWidgets import *
from hosgeldin_sahip import *


class hosgeldin_ekrani(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.kapat.clicked.connect(self.kapat)

    def kapat(self):
        self.close()