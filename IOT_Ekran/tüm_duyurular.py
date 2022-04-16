# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tüm_duyurular.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(860, 573)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#centralwidget{\n"
"border-image: url(deneme2.jpg);}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 15)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.Tum_Duyurular = QtWidgets.QLabel(self.centralwidget)
        self.Tum_Duyurular.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";\n"
"background-color: qlineargradient(spread:pad, x1:0.507463, y1:0.79, x2:0.507, y2:0.0511364, stop:0 rgba(108, 190, 167, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:10px;")
        self.Tum_Duyurular.setObjectName("Tum_Duyurular")
        self.horizontalLayout_7.addWidget(self.Tum_Duyurular)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.304, y1:0.0340909, x2:1, y2:0, stop:0.0199005 rgba(157, 163, 190, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:15px;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 815, 663))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Tarih1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Tarih1.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.1, y1:0.00568182, x2:1, y2:0, stop:0 rgba(89, 71, 71, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"border-radius:15px;")
        self.Tarih1.setObjectName("Tarih1")
        self.horizontalLayout_3.addWidget(self.Tarih1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Duyuru_Baslik_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Duyuru_Baslik_1.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"\n"
"border-radius:5px;")
        self.Duyuru_Baslik_1.setText("")
        self.Duyuru_Baslik_1.setObjectName("Duyuru_Baslik_1")
        self.verticalLayout_3.addWidget(self.Duyuru_Baslik_1)
        self.Duyuru_1 = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.Duyuru_1.setObjectName("Duyuru_1")
        self.verticalLayout_3.addWidget(self.Duyuru_1)
        self.Detay1 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.Detay1.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"\n"
"border-radius:5px;\n"
"\n"
"")
        self.Detay1.setObjectName("Detay1")
        self.verticalLayout_3.addWidget(self.Detay1)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.Tarih2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Tarih2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(94, 181, 159, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"border-radius:15px;")
        self.Tarih2.setObjectName("Tarih2")
        self.horizontalLayout_3.addWidget(self.Tarih2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Duyuru_2 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.Duyuru_2.setObjectName("Duyuru_2")
        self.verticalLayout_4.addWidget(self.Duyuru_2)
        self.Detay2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.Detay2.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"\n"
"border-radius:5px;")
        self.Detay2.setObjectName("Detay2")
        self.verticalLayout_4.addWidget(self.Detay2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Tarih3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Tarih3.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(94, 181, 159, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"border-radius:15px;")
        self.Tarih3.setObjectName("Tarih3")
        self.horizontalLayout.addWidget(self.Tarih3)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.Duyuru_3 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.Duyuru_3.setObjectName("Duyuru_3")
        self.verticalLayout_11.addWidget(self.Duyuru_3)
        self.Detay3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.Detay3.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"\n"
"border-radius:5px;")
        self.Detay3.setObjectName("Detay3")
        self.verticalLayout_11.addWidget(self.Detay3)
        self.horizontalLayout.addLayout(self.verticalLayout_11)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.Tarih4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Tarih4.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.1, y1:0.00568182, x2:1, y2:0, stop:0 rgba(89, 71, 71, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"border-radius:15px;")
        self.Tarih4.setObjectName("Tarih4")
        self.horizontalLayout.addWidget(self.Tarih4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.Duyuru_4 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.Duyuru_4.setObjectName("Duyuru_4")
        self.verticalLayout_5.addWidget(self.Duyuru_4)
        self.Detay4 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.Detay4.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"\n"
"border-radius:5px;\n"
"\n"
"")
        self.Detay4.setObjectName("Detay4")
        self.verticalLayout_5.addWidget(self.Detay4)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Tarih5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Tarih5.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.1, y1:0.00568182, x2:1, y2:0, stop:0 rgba(89, 71, 71, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"border-radius:15px;")
        self.Tarih5.setObjectName("Tarih5")
        self.horizontalLayout_2.addWidget(self.Tarih5)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.Duyuru_5 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.Duyuru_5.setObjectName("Duyuru_5")
        self.verticalLayout_7.addWidget(self.Duyuru_5)
        self.Detay5 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.Detay5.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"\n"
"border-radius:5px;\n"
"\n"
"")
        self.Detay5.setObjectName("Detay5")
        self.verticalLayout_7.addWidget(self.Detay5)
        self.horizontalLayout_2.addLayout(self.verticalLayout_7)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.Tarih6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Tarih6.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(94, 181, 159, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"border-radius:15px;")
        self.Tarih6.setObjectName("Tarih6")
        self.horizontalLayout_2.addWidget(self.Tarih6)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.Duyuru_6 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.Duyuru_6.setObjectName("Duyuru_6")
        self.verticalLayout_8.addWidget(self.Duyuru_6)
        self.Detay6 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.Detay6.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"\n"
"border-radius:5px;")
        self.Detay6.setObjectName("Detay6")
        self.verticalLayout_8.addWidget(self.Detay6)
        self.horizontalLayout_2.addLayout(self.verticalLayout_8)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Tarih7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Tarih7.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(94, 181, 159, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"border-radius:15px;")
        self.Tarih7.setObjectName("Tarih7")
        self.horizontalLayout_5.addWidget(self.Tarih7)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.Duyuru_7 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.Duyuru_7.setObjectName("Duyuru_7")
        self.verticalLayout_9.addWidget(self.Duyuru_7)
        self.Detay7 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.Detay7.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"\n"
"border-radius:5px;")
        self.Detay7.setObjectName("Detay7")
        self.verticalLayout_9.addWidget(self.Detay7)
        self.horizontalLayout_5.addLayout(self.verticalLayout_9)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.Tarih8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Tarih8.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.1, y1:0.00568182, x2:1, y2:0, stop:0 rgba(89, 71, 71, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"border-radius:15px;")
        self.Tarih8.setObjectName("Tarih8")
        self.horizontalLayout_5.addWidget(self.Tarih8)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.Duyuru_8 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.Duyuru_8.setObjectName("Duyuru_8")
        self.verticalLayout_6.addWidget(self.Duyuru_8)
        self.Detay8 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.Detay8.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"\n"
"border-radius:5px;\n"
"\n"
"")
        self.Detay8.setObjectName("Detay8")
        self.verticalLayout_6.addWidget(self.Detay8)
        self.horizontalLayout_5.addLayout(self.verticalLayout_6)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.Tarih9 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Tarih9.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.1, y1:0.00568182, x2:1, y2:0, stop:0 rgba(89, 71, 71, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"border-radius:15px;")
        self.Tarih9.setObjectName("Tarih9")
        self.horizontalLayout_6.addWidget(self.Tarih9)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.Duyuru_9 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.Duyuru_9.setObjectName("Duyuru_9")
        self.verticalLayout_10.addWidget(self.Duyuru_9)
        self.Detay9 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.Detay9.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"\n"
"border-radius:5px;\n"
"\n"
"")
        self.Detay9.setObjectName("Detay9")
        self.verticalLayout_10.addWidget(self.Detay9)
        self.horizontalLayout_6.addLayout(self.verticalLayout_10)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.Tarih10 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Tarih10.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(94, 181, 159, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"border-radius:15px;")
        self.Tarih10.setObjectName("Tarih10")
        self.horizontalLayout_6.addWidget(self.Tarih10)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.Duyuru_10 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.Duyuru_10.setObjectName("Duyuru_10")
        self.verticalLayout_12.addWidget(self.Duyuru_10)
        self.Detay10 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.Detay10.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"\n"
"border-radius:5px;")
        self.Detay10.setObjectName("Detay10")
        self.verticalLayout_12.addWidget(self.Detay10)
        self.horizontalLayout_6.addLayout(self.verticalLayout_12)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.kapat = QtWidgets.QPushButton(self.centralwidget)
        self.kapat.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.507463, y1:0.79, x2:0.507, y2:0.0511364, stop:0 rgba(108, 190, 167, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 16pt \"MS Shell Dlg 2\";\n"
"border-radius:10px;")
        self.kapat.setObjectName("kapat")
        self.horizontalLayout_4.addWidget(self.kapat)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout_13.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 860, 26))
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
        self.Tum_Duyurular.setText(_translate("MainWindow", "       TÜM DUYURULAR       "))
        self.Tarih1.setText(_translate("MainWindow", "  3 Temmuz  "))
        self.Detay1.setText(_translate("MainWindow", "                                          Detay.."))
        self.Tarih2.setText(_translate("MainWindow", "  3 Temmuz  "))
        self.Detay2.setText(_translate("MainWindow", "                                             Detay.."))
        self.Tarih3.setText(_translate("MainWindow", "  3 Temmuz  "))
        self.Detay3.setText(_translate("MainWindow", "                                          Detay.."))
        self.Tarih4.setText(_translate("MainWindow", "  3 Temmuz  "))
        self.Detay4.setText(_translate("MainWindow", "                                             Detay.."))
        self.Tarih5.setText(_translate("MainWindow", "  3 Temmuz  "))
        self.Detay5.setText(_translate("MainWindow", "                                          Detay.."))
        self.Tarih6.setText(_translate("MainWindow", "  3 Temmuz  "))
        self.Detay6.setText(_translate("MainWindow", "                                             Detay.."))
        self.Tarih7.setText(_translate("MainWindow", "  3 Temmuz  "))
        self.Detay7.setText(_translate("MainWindow", "                                          Detay.."))
        self.Tarih8.setText(_translate("MainWindow", "  3 Temmuz  "))
        self.Detay8.setText(_translate("MainWindow", "                                             Detay.."))
        self.Tarih9.setText(_translate("MainWindow", "  3 Temmuz  "))
        self.Detay9.setText(_translate("MainWindow", "                                          Detay.."))
        self.Tarih10.setText(_translate("MainWindow", "  3 Temmuz  "))
        self.Detay10.setText(_translate("MainWindow", "                                             Detay.."))
        self.kapat.setText(_translate("MainWindow", "  Kapat  "))

#import deneme_rc
