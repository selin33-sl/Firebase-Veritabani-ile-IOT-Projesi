# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AnaEkran.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1055, 620)
        MainWindow.setStyleSheet("font: 75 9pt \"MS Shell Dlg 2\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#centralwidget{\n"
"\n"
"border-image: url(deneme2.jpg);}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(50, -1, 50, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.Kullanici_adi = QtWidgets.QLabel(self.centralwidget)
        self.Kullanici_adi.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";\n"
"background-color: qlineargradient(spread:pad, x1:0.527, y1:0.880591, x2:0.497, y2:0.0454545, stop:0 rgba(55, 110, 130, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:15px;\n"
"")
        self.Kullanici_adi.setObjectName("Kullanici_adi")
        self.horizontalLayout.addWidget(self.Kullanici_adi)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, -1, 0, 0)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(0, 10, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Ders_programi = QtWidgets.QTableWidget(self.centralwidget)
        self.Ders_programi.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Ders_programi.sizePolicy().hasHeightForWidth())
        self.Ders_programi.setSizePolicy(sizePolicy)
        self.Ders_programi.setMinimumSize(QtCore.QSize(0, 0))
        self.Ders_programi.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"border-radius:15px;")
        self.Ders_programi.setRowCount(15)
        self.Ders_programi.setColumnCount(15)
        self.Ders_programi.setObjectName("Ders_programi")
        self.verticalLayout_2.addWidget(self.Ders_programi)
        self.onemli_duyurular = QtWidgets.QLabel(self.centralwidget)
        self.onemli_duyurular.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.513, y1:0.284, x2:0.552239, y2:1, stop:0 rgba(82, 139, 158, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 13pt \"MS Shell Dlg 2\";\n"
"\n"
"border-radius:10px;")
        self.onemli_duyurular.setObjectName("onemli_duyurular")
        self.verticalLayout_2.addWidget(self.onemli_duyurular)
        self.onemli_duyurular_yazialani = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.onemli_duyurular_yazialani.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.527, y1:0.880591, x2:0.497, y2:0.0454545, stop:0 rgba(55, 110, 130, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"border-radius:15px;\n"
"font: 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(204, 27, 27);")
        self.onemli_duyurular_yazialani.setObjectName("onemli_duyurular_yazialani")
        self.verticalLayout_2.addWidget(self.onemli_duyurular_yazialani)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout.setSpacing(9)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Fotograf = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Fotograf.sizePolicy().hasHeightForWidth())
        self.Fotograf.setSizePolicy(sizePolicy)
        self.Fotograf.setStyleSheet("border-radius:14px;\n"
"")
        self.Fotograf.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("kullanıcı.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Fotograf.setIcon(icon)
        self.Fotograf.setIconSize(QtCore.QSize(200, 230))
        self.Fotograf.setObjectName("Fotograf")
        self.verticalLayout.addWidget(self.Fotograf)
        self.mesaj_birakin = QtWidgets.QPushButton(self.centralwidget)
        self.mesaj_birakin.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mesaj_birakin.sizePolicy().hasHeightForWidth())
        self.mesaj_birakin.setSizePolicy(sizePolicy)
        self.mesaj_birakin.setMinimumSize(QtCore.QSize(0, 0))
        self.mesaj_birakin.setBaseSize(QtCore.QSize(0, 10))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.mesaj_birakin.setFont(font)
        self.mesaj_birakin.setStatusTip("")
        self.mesaj_birakin.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mesaj_birakin.setAutoFillBackground(False)
        self.mesaj_birakin.setStyleSheet(
                                         " QPushButton {border-radius:20px ;  font: 75 15pt \"MS Shell Dlg 2\";background-color:qlineargradient(spread:pad, x1:0.527, y1:0.880591, x2:0.497, y2:0.0454545, stop:0 rgba(55, 110, 130, 255), stop:1 rgba(255, 255, 255, 255));}"
                                         "QPushButton:hover {background-color: qlineargradient(spread:pad, x1:0.527, y1:0.880591, x2:0.497, y2:0.0454545, stop:0 rgba(0, 60, 113, 255), stop:1 rgba(255, 255, 255, 255));}"
                                         )
        self.mesaj_birakin.setCheckable(False)
        self.mesaj_birakin.setAutoRepeat(False)
        self.mesaj_birakin.setAutoExclusive(True)
        self.mesaj_birakin.setAutoRepeatDelay(300)
        self.mesaj_birakin.setObjectName("mesaj_birakin")
        self.verticalLayout.addWidget(self.mesaj_birakin)
        self.Tum_Duyurular = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Tum_Duyurular.sizePolicy().hasHeightForWidth())
        self.Tum_Duyurular.setSizePolicy(sizePolicy)
        self.Tum_Duyurular.setStyleSheet( " QPushButton {border-radius:20px ;  font: 75 15pt \"MS Shell Dlg 2\";background-color:qlineargradient(spread:pad, x1:0.527, y1:0.880591, x2:0.497, y2:0.0454545, stop:0 rgba(114, 80, 141, 255), stop:1 rgba(255, 255, 255, 255));}"
                                         "QPushButton:hover {background-color: qlineargradient(spread:pad, x1:0.527, y1:0.880591, x2:0.497, y2:0.0454545, stop:0 rgba(0, 60, 113, 255), stop:1 rgba(255, 255, 255, 255));}"

                                         )
        self.Tum_Duyurular.setObjectName("Tum_Duyurular")
        self.verticalLayout.addWidget(self.Tum_Duyurular)
        self.Iletisim_Bilgileri = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Iletisim_Bilgileri.sizePolicy().hasHeightForWidth())
        self.Iletisim_Bilgileri.setSizePolicy(sizePolicy)
        self.Iletisim_Bilgileri.setStyleSheet(
                                              " QPushButton {border-radius:20px ;  font: 75 15pt \"MS Shell Dlg 2\";background-color:qlineargradient(spread:pad, x1:0.527, y1:0.880591, x2:0.497, y2:0.0454545, stop:0 rgba(88, 92, 105, 255), stop:1 rgba(255, 255, 255, 255));}"
                                              "QPushButton:hover {background-color: qlineargradient(spread:pad, x1:0.527, y1:0.880591, x2:0.497, y2:0.0454545, stop:0 rgba(0, 60, 113, 255), stop:1 rgba(255, 255, 255, 255));}"
                                              )
        self.Iletisim_Bilgileri.setObjectName("Iletisim_Bilgileri")
        self.verticalLayout.addWidget(self.Iletisim_Bilgileri)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setBaseSize(QtCore.QSize(0, 0))
        self.pushButton.setStyleSheet(

                                      " QPushButton {border-radius:20px ;  font: 75 15pt \"MS Shell Dlg 2\";background-color:qlineargradient(spread:pad, x1:0.527, y1:0.880591, x2:0.497, y2:0.0454545, stop:0 rgba(145, 103, 128, 255), stop:1 rgba(255, 255, 255, 255));}"
                                      "QPushButton:hover {background-color: qlineargradient(spread:pad, x1:0.527, y1:0.880591, x2:0.497, y2:0.0454545, stop:0 rgba(0, 60, 113, 255), stop:1 rgba(255, 255, 255, 255));}"

                                      )
        self.pushButton.setAutoRepeatInterval(100)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setStyleSheet(

                                        " QPushButton {border-radius:20px ;  font: 75 15pt \"MS Shell Dlg 2\";background-color:qlineargradient(spread:pad, x1:0.527, y1:0.880591, x2:0.497, y2:0.0454545, stop:0 rgba(108, 190, 167, 255), stop:1 rgba(255, 255, 255, 255));}"
                                        "QPushButton:hover {background-color: qlineargradient(spread:pad, x1:0.527, y1:0.880591, x2:0.497, y2:0.0454545, stop:0 rgba(0, 60, 113, 255), stop:1 rgba(255, 255, 255, 255));}"
                                        )
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.setStretch(0, 5)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 1)
        self.verticalLayout.setStretch(5, 1)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2.setStretch(0, 8)
        self.horizontalLayout_2.setStretch(1, 2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1055, 24))
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
        self.Kullanici_adi.setText(_translate("MainWindow", "   KULLANICI ADI   "))
        self.onemli_duyurular.setText(_translate("MainWindow", "  Önemli Duyurular:"))
        self.mesaj_birakin.setText(_translate("MainWindow", "Mesaj Bırakın"))
        self.Tum_Duyurular.setText(_translate("MainWindow", "Tüm Duyurular"))
        self.Iletisim_Bilgileri.setText(_translate("MainWindow", "İletişim Bilgileri"))
        self.pushButton.setText(_translate("MainWindow", "boş"))
        self.pushButton_2.setText(_translate("MainWindow", "boş"))

#import deneme_rc
