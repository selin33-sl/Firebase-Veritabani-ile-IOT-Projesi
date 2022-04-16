# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mesaj.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1055, 620)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#centralwidget{\n"
"border-image: url(deneme2.jpg);}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.bilgi = QtWidgets.QLabel(self.centralwidget)
        self.bilgi.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";\n"
"background-color: qlineargradient(spread:pad, x1:0.507463, y1:0.79, x2:0.507, y2:0.0511364, stop:0 rgba(108, 190, 167, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"border-radius:15px;")
        self.bilgi.setObjectName("bilgi")
        self.verticalLayout.addWidget(self.bilgi)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(15, -1, 15, -1)
        self.horizontalLayout_5.setSpacing(15)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, 15, -1, 15)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Ad_Soyad = QtWidgets.QLabel(self.centralwidget)
        self.Ad_Soyad.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"\n"
"border-radius:10px;\n"
"background-color: rgb(230, 255, 251);\n"
"")
        self.Ad_Soyad.setObjectName("Ad_Soyad")
        self.horizontalLayout.addWidget(self.Ad_Soyad)
        self.ad_soyad_yazialani = QtWidgets.QLineEdit(self.centralwidget)
        self.ad_soyad_yazialani.setStyleSheet("border-radius:5px;\n"
"background-color: rgb(230, 255, 251);")
        self.ad_soyad_yazialani.setObjectName("ad_soyad_yazialani")
        self.horizontalLayout.addWidget(self.ad_soyad_yazialani)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 8)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Telefon_Label = QtWidgets.QLabel(self.centralwidget)
        self.Telefon_Label.setStyleSheet("background-color: rgb(230, 255, 251);\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"border-radius:10px;\n"
"")
        self.Telefon_Label.setObjectName("Telefon_Label")
        self.horizontalLayout_2.addWidget(self.Telefon_Label)
        self.Telefon_yazialani = QtWidgets.QLineEdit(self.centralwidget)
        self.Telefon_yazialani.setStyleSheet("border-radius:5px;\n"
"background-color: rgb(230, 255, 251);")
        self.Telefon_yazialani.setObjectName("Telefon_yazialani")
        self.horizontalLayout_2.addWidget(self.Telefon_yazialani)
        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 8)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Eposta_Label = QtWidgets.QLabel(self.centralwidget)
        self.Eposta_Label.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(230, 255, 251);\n"
"\n"
"border-radius:10px;")
        self.Eposta_Label.setObjectName("Eposta_Label")
        self.horizontalLayout_3.addWidget(self.Eposta_Label)
        self.eposta_yazialani = QtWidgets.QLineEdit(self.centralwidget)
        self.eposta_yazialani.setStyleSheet("border-radius:5px;\n"
"background-color: rgb(230, 255, 251);")
        self.eposta_yazialani.setObjectName("eposta_yazialani")
        self.horizontalLayout_3.addWidget(self.eposta_yazialani)
        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 8)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Mesajiniz_Label = QtWidgets.QLabel(self.centralwidget)
        self.Mesajiniz_Label.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(230, 255, 251);\n"
"border-radius:10px;\n"
"")
        self.Mesajiniz_Label.setObjectName("Mesajiniz_Label")
        self.horizontalLayout_4.addWidget(self.Mesajiniz_Label)
        self.mesaj_yazialani = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mesaj_yazialani.sizePolicy().hasHeightForWidth())
        self.mesaj_yazialani.setSizePolicy(sizePolicy)
        self.mesaj_yazialani.setStyleSheet("border-radius:5px;\n"
"background-color: rgb(230, 255, 251);\n"
"\n"
"\n"
"\n"
"")
        self.mesaj_yazialani.setObjectName("mesaj_yazialani")
        self.horizontalLayout_4.addWidget(self.mesaj_yazialani)
        self.horizontalLayout_4.setStretch(0, 2)
        self.horizontalLayout_4.setStretch(1, 8)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.bilgi_yazialani = QtWidgets.QLabel(self.centralwidget)
        self.bilgi_yazialani.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(239, 255, 251);\n"
"\n"
"border-radius:10px;")
        self.bilgi_yazialani.setObjectName("bilgi_yazialani")
        self.horizontalLayout_6.addWidget(self.bilgi_yazialani)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem2)
        self.sayac = QtWidgets.QLabel(self.centralwidget)
        self.sayac.setObjectName("sayac")
        self.horizontalLayout_9.addWidget(self.sayac)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Iptal = QtWidgets.QPushButton(self.centralwidget)
        self.Iptal.setStyleSheet("font: 75 15pt \"MS Shell Dlg 2\";\n"
"background-color: qlineargradient(spread:pad, x1:0.536701, y1:0.796, x2:0.512438, y2:0, stop:0 rgba(0, 102, 139, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"border-radius:15px;")
        self.Iptal.setObjectName("Iptal")
        self.verticalLayout_3.addWidget(self.Iptal)
        self.Temizle = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Temizle.sizePolicy().hasHeightForWidth())
        self.Temizle.setSizePolicy(sizePolicy)
        self.Temizle.setMinimumSize(QtCore.QSize(0, 0))
        self.Temizle.setStyleSheet("font: 75 15pt \"MS Shell Dlg 2\";\n"
"background-color: qlineargradient(spread:pad, x1:0.502, y1:0.716227, x2:0.522388, y2:0.051, stop:0 rgba(145, 103, 128, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"border-radius:15px;")
        self.Temizle.setObjectName("Temizle")
        self.verticalLayout_3.addWidget(self.Temizle)
        self.Gonder = QtWidgets.QPushButton(self.centralwidget)
        self.Gonder.setStyleSheet("font: 75 15pt \"MS Shell Dlg 2\";\n"
"background-color: qlineargradient(spread:pad, x1:0.507463, y1:0.79, x2:0.507, y2:0.0511364, stop:0 rgba(108, 190, 167, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:15px;")
        self.Gonder.setObjectName("Gonder")
        self.verticalLayout_3.addWidget(self.Gonder)
        self.verticalLayout_3.setStretch(0, 10)
        self.verticalLayout_3.setStretch(1, 10)
        self.verticalLayout_3.setStretch(2, 10)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        self.horizontalLayout_5.setStretch(0, 7)
        self.horizontalLayout_5.setStretch(1, 2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.klavye = QtWidgets.QTextEdit(self.centralwidget)
        self.klavye.setStyleSheet("border-radius:10px;\n"
"border-radius:15px;")
        self.klavye.setObjectName("klavye")
        self.verticalLayout_4.addWidget(self.klavye)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1044, 26))
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
        self.bilgi.setText(_translate("MainWindow", "     Lütfen aşağıdaki tüm alanları eksiksiz doldurarak, mesajınızı bırakın. "))
        self.Ad_Soyad.setText(_translate("MainWindow", "   Ad/Soyad:"))
        self.Telefon_Label.setText(_translate("MainWindow", "   Telefon:"))
        self.Eposta_Label.setText(_translate("MainWindow", "   E-posta:"))
        self.Mesajiniz_Label.setText(_translate("MainWindow", "  Mesajınız:"))
        self.bilgi_yazialani.setText(_translate("MainWindow", "                           "))
        self.sayac.setText(_translate("MainWindow", "             "))
        self.Iptal.setText(_translate("MainWindow", "İptal"))
        self.Temizle.setText(_translate("MainWindow", "Temizle"))
        self.Gonder.setText(_translate("MainWindow", "Gönder"))

