from PyQt5.QtWidgets import *
from iletisim_bilgileri import Ui_Dialog

class iletisimbilgileri(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)


