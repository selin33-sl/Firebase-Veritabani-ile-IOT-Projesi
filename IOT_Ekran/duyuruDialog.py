# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'duyuruDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(813, 574)
        Dialog.setStyleSheet("#Dialog{border-image: url(deneme2.jpg);}")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(178, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 15, -1, 15)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.duyuru_basligi = QtWidgets.QLabel(Dialog)
        self.duyuru_basligi.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(198, 118, 214, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:10px;")
        self.duyuru_basligi.setObjectName("duyuru_basligi")
        self.horizontalLayout.addWidget(self.duyuru_basligi)
        self.duyuru_basligi_yazialani = QtWidgets.QTextEdit(Dialog)
        self.duyuru_basligi_yazialani.setStyleSheet("border-radius:1px;")
        self.duyuru_basligi_yazialani.setObjectName("duyuru_basligi_yazialani")
        self.horizontalLayout.addWidget(self.duyuru_basligi_yazialani)
        self.horizontalLayout.setStretch(0, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(7)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.duyuru_mesaji = QtWidgets.QLabel(Dialog)
        self.duyuru_mesaji.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(198, 118, 214, 255), stop:1 rgba(255, 255, 255, 255));")
        self.duyuru_mesaji.setObjectName("duyuru_mesaji")
        self.horizontalLayout_2.addWidget(self.duyuru_mesaji)
        self.duyuru_mesaji_yazialani = QtWidgets.QTextEdit(Dialog)
        self.duyuru_mesaji_yazialani.setStyleSheet("border-radius:10px;")
        self.duyuru_mesaji_yazialani.setObjectName("duyuru_mesaji_yazialani")
        self.horizontalLayout_2.addWidget(self.duyuru_mesaji_yazialani)
        self.horizontalLayout_2.setStretch(1, 3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 5)
        self.verticalLayout.setStretch(3, 1)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(178, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.duyuru_basligi.setText(_translate("Dialog", "  Duyuru Başlığı :  "))
        self.duyuru_mesaji.setText(_translate("Dialog", "  Duyuru Mesajı :  "))

#import deneme_rc
