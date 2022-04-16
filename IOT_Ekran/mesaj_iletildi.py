# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mesaj_iletildi.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(508, 126)
        Dialog.setStyleSheet("#Dialog{border-image: url(deneme2.jpg);}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 24, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.mesaj_iletildi_bilgisi = QtWidgets.QLabel(Dialog)
        self.mesaj_iletildi_bilgisi.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(94, 181, 159, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"border-radius:15px;\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.mesaj_iletildi_bilgisi.setObjectName("mesaj_iletildi_bilgisi")
        self.horizontalLayout.addWidget(self.mesaj_iletildi_bilgisi)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(20, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.mesaj_iletildi_bilgisi.setText(_translate("Dialog", "  Mesajınız başarıyla iletilmiştir..  "))

#import deneme_rc
