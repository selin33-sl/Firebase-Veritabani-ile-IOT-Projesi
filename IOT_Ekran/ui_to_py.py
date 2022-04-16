from PyQt5 import uic

with open('mesaj.py', 'w', encoding="utf-8") as fout:
    uic.compileUi('mesaj.ui', fout)