from PyQt5.QtWidgets import QApplication
from AnaEkran_page import anaekran



app=QApplication([])
window=anaekran()
window.show()
app.exec_()
