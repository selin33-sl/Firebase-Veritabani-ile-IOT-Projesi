# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kullanıcı_bilgileri.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1055, 620)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#centralwidget{\n"
"border-image: url(deneme2.jpg);}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, 15, -1, 15)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(0, 15, 0, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.kullanici_bilgileri = QtWidgets.QLabel(self.centralwidget)
        self.kullanici_bilgileri.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.513, y1:0.284, x2:0.552239, y2:1, stop:0 rgba(82, 139, 158, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 17pt \"MS Shell Dlg 2\";\n"
"\n"
"border-radius:15px;")
        self.kullanici_bilgileri.setObjectName("kullanici_bilgileri")
        self.horizontalLayout_3.addWidget(self.kullanici_bilgileri)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.kullanici_adi = QtWidgets.QLabel(self.centralwidget)
        self.kullanici_adi.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"background-color: qlineargradient(spread:pad, x1:0.513, y1:0.284, x2:0.552239, y2:1, stop:0 rgba(82, 139, 158, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:10px;")
        self.kullanici_adi.setObjectName("kullanici_adi")
        self.horizontalLayout.addWidget(self.kullanici_adi)
        self.kullaniciadi_yazialani = QtWidgets.QLineEdit(self.centralwidget)
        self.kullaniciadi_yazialani.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"border-radius:5px;")
        self.kullaniciadi_yazialani.setObjectName("kullaniciadi_yazialani")
        self.horizontalLayout.addWidget(self.kullaniciadi_yazialani)
        spacerItem2 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 6)
        self.horizontalLayout.setStretch(2, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.sifre = QtWidgets.QLabel(self.centralwidget)
        self.sifre.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"background-color: qlineargradient(spread:pad, x1:0.513, y1:0.284, x2:0.552239, y2:1, stop:0 rgba(82, 139, 158, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:10px;")
        self.sifre.setObjectName("sifre")
        self.horizontalLayout_2.addWidget(self.sifre)
        self.sifre_yazialani = QtWidgets.QLineEdit(self.centralwidget)
        self.sifre_yazialani.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"border-radius:5px;")
        self.sifre_yazialani.setObjectName("sifre_yazialani")
        self.horizontalLayout_2.addWidget(self.sifre_yazialani)
        spacerItem3 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 6)
        self.horizontalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(15, -1, 15, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem4 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName("verticalLayout")
        self.bilgi_yazialani = QtWidgets.QLabel(self.centralwidget)
        self.bilgi_yazialani.setStyleSheet("\n"
"\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.bilgi_yazialani.setText("")
        self.bilgi_yazialani.setObjectName("bilgi_yazialani")
        self.verticalLayout.addWidget(self.bilgi_yazialani)
        self.Temizle = QtWidgets.QPushButton(self.centralwidget)
        self.Temizle.setStyleSheet("font: 75 15pt \"MS Shell Dlg 2\";\n"
"background-color: qlineargradient(spread:pad, x1:0.478, y1:0.00568182, x2:0.527363, y2:0.994, stop:0 rgba(127, 10, 52, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:10px;")
        self.Temizle.setObjectName("Temizle")
        self.verticalLayout.addWidget(self.Temizle)
        self.Onayla = QtWidgets.QPushButton(self.centralwidget)
        self.Onayla.setStyleSheet("border-radius:10px;\n"
"font: 75 15pt \"MS Shell Dlg 2\";\n"
"background-color: qlineargradient(spread:pad, x1:0.498, y1:0.0227273, x2:0.512, y2:0.972, stop:0 rgba(128, 84, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.Onayla.setObjectName("Onayla")
        self.verticalLayout.addWidget(self.Onayla)
        self.iptal = QtWidgets.QPushButton(self.centralwidget)
        self.iptal.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.512, y1:0.153409, x2:0.527, y2:0.976955, stop:0 rgba(124, 60, 130, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 15pt \"MS Shell Dlg 2\";\n"
"border-radius:10px;")
        self.iptal.setObjectName("iptal")
        self.verticalLayout.addWidget(self.iptal)
        self.verticalLayout.setStretch(0, 3)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.setStretch(1, 4)
        self.verticalLayout_2.setStretch(2, 4)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.klavye = QtWidgets.QTextEdit(self.centralwidget)
        self.klavye.setObjectName("klavye")
        self.verticalLayout_3.addWidget(self.klavye)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 967, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.kullanici_bilgileri.setText(_translate("MainWindow", "  Kullanıcı Bilgileri  "))
        self.kullanici_adi.setText(_translate("MainWindow", "  Kullanıcı Adı:"))
        self.sifre.setText(_translate("MainWindow", "  Şifre:"))
        self.Temizle.setText(_translate("MainWindow", "                  Temizle                 "))
        self.Onayla.setText(_translate("MainWindow", "             Onayla              "))
        self.iptal.setText(_translate("MainWindow", "İptal  "))

#import deneme_rc
