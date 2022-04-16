# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hosgeldin_sahip.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(587, 439)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#centralwidget{\n"
"border-image: url(deneme2.jpg);}\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(15, -1, 15, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 15, -1, 15)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.hosgeldin = QtWidgets.QLabel(self.centralwidget)
        self.hosgeldin.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color: qlineargradient(spread:pad, x1:0.478, y1:0.00568182, x2:0.527363, y2:0.994, stop:0 rgba(127, 10, 52, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:15px;")
        self.hosgeldin.setObjectName("hosgeldin")
        self.horizontalLayout_2.addWidget(self.hosgeldin)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.kapiyi_ac = QtWidgets.QPushButton(self.centralwidget)
        self.kapiyi_ac.setStyleSheet("font: 75 15pt \"MS Shell Dlg 2\";\n"
"\n"
"border-radius:15px;\n"
"background-color: qlineargradient(spread:pad, x1:0.507463, y1:0.79, x2:0.507, y2:0.0511364, stop:0 rgba(108, 190, 167, 255), stop:1 rgba(255, 255, 255, 255));")
        self.kapiyi_ac.setObjectName("kapiyi_ac")
        self.verticalLayout.addWidget(self.kapiyi_ac)
        self.ozellik1 = QtWidgets.QPushButton(self.centralwidget)
        self.ozellik1.setStyleSheet("font: 75 15pt \"MS Shell Dlg 2\";\n"
"background-color: qlineargradient(spread:pad, x1:0.512438, y1:0.779, x2:0.488, y2:0, stop:0 rgba(170, 130, 150, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"border-radius:15px;")
        self.ozellik1.setObjectName("ozellik1")
        self.verticalLayout.addWidget(self.ozellik1)
        self.ozellik2 = QtWidgets.QPushButton(self.centralwidget)
        self.ozellik2.setStyleSheet("font: 75 15pt \"MS Shell Dlg 2\";\n"
"border-radius:15px;\n"
"background-color: qlineargradient(spread:pad, x1:0.507, y1:0.881045, x2:0.512, y2:0.0340909, stop:0 rgba(152, 116, 71, 255), stop:1 rgba(255, 255, 255, 255));")
        self.ozellik2.setObjectName("ozellik2")
        self.verticalLayout.addWidget(self.ozellik2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.kapat = QtWidgets.QPushButton(self.centralwidget)
        self.kapat.setStyleSheet("border-radius:15px;\n"
"font: 75 16pt \"MS Shell Dlg 2\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(122, 97, 93, 255), stop:1 rgba(255, 255, 255, 255));")
        self.kapat.setObjectName("kapat")
        self.horizontalLayout.addWidget(self.kapat)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(18, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 5)
        self.verticalLayout.setStretch(3, 5)
        self.verticalLayout.setStretch(4, 5)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.horizontalLayout_3.setStretch(0, 3)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 587, 26))
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
        self.hosgeldin.setText(_translate("MainWindow", "  HOŞGELDİN SAHİP  "))
        self.kapiyi_ac.setText(_translate("MainWindow", "Kapıyı Aç"))
        self.ozellik1.setText(_translate("MainWindow", "Özellik 1"))
        self.ozellik2.setText(_translate("MainWindow", "Özellik 2"))
        self.kapat.setText(_translate("MainWindow", "  Kapat  "))

#import deneme_rc
