from PyQt5.QtWidgets import *
from yüz_tanıma_alanı import *


class yuztanima_ekran(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)


        self.ui.kapat.clicked.connect(self.ekranikapat)

    def ekranikapat(self):

        self.close()
