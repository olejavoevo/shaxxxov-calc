# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledxyCxTp.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"Калькулятор долгов Шаховстану")
        MainWindow.resize(489, 196)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 0, 471, 41))
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 50, 321, 61))
        font1 = QFont()
        font1.setPointSize(15)
        self.lineEdit.setFont(font1)
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(340, 50, 141, 61))
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setPlaceholderText(u"\u041f\u0420\u041e\u0416\u0418\u0422\u041e")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 120, 471, 61))
        self.pushButton.setFont(font)
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("LLIAXOBCTAH", u"LLIAXOBCTAH", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0435\u043b\u0438\u043a\u0438\u0439 \u0428\u0430\u0445\u043e\u0432\u0441\u0442\u0430\u043d\u0441\u043a\u0438\u0439 \u041a\u0430\u043b\u044c\u043a\u0443\u043b\u044f\u0442\u043e\u0440 (C)", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0426\u0415\u041d\u0410 \u041f\u041e\u0427\u0415\u041a \u0414\u041e\u041b\u0416\u041d\u0418\u041a\u0410", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0410\u0413\u041d\u0410\u0422\u042c \u0412 \u0414\u041e\u041b\u0413\u0418", None))
    # retranslateUi

