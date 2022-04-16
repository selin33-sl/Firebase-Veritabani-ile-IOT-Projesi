# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'yüz_tanıma_alanı.ui'
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
        self.centralwidget.setStyleSheet("#centralwidget{border-image: url(deneme2.jpg);}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(40, 40, 40, 40)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.yuz_tanima_alani = QtWidgets.QLabel(self.centralwidget)
        self.yuz_tanima_alani.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"background-color: qlineargradient(spread:pad, x1:0.502, y1:0.716227, x2:0.522388, y2:0.051, stop:0 rgba(145, 103, 128, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:15px;")
        self.yuz_tanima_alani.setObjectName("yuz_tanima_alani")
        self.horizontalLayout_2.addWidget(self.yuz_tanima_alani)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.yuz_tanima = QtWidgets.QTextEdit(self.centralwidget)
        self.yuz_tanima.setObjectName("yuz_tanima")
        self.horizontalLayout.addWidget(self.yuz_tanima)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.kapat = QtWidgets.QPushButton(self.centralwidget)
        self.kapat.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color: qlineargradient(spread:pad, x1:0.502, y1:0.716227, x2:0.522388, y2:0.051, stop:0 rgba(145, 103, 128, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:15px;")
        self.kapat.setObjectName("kapat")
        self.horizontalLayout_3.addWidget(self.kapat)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 4)
        self.verticalLayout.setStretch(2, 2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
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
        self.yuz_tanima_alani.setText(_translate("MainWindow", "   Yüz Tanıma Alanı   "))
        self.kapat.setText(_translate("MainWindow", "  Kapat  "))

#import deneme_rc
