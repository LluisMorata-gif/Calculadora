# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pantalla.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSplitter, QWidget)

class Ui_Calculadora(object):
    def setupUi(self, Calculadora):
        if not Calculadora.objectName():
            Calculadora.setObjectName(u"Calculadora")
        Calculadora.resize(530, 305)
        self.centralwidget = QWidget(Calculadora)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 60, 361, 31))
        self.splitter_6 = QSplitter(self.centralwidget)
        self.splitter_6.setObjectName(u"splitter_6")
        self.splitter_6.setGeometry(QRect(50, 100, 371, 88))
        self.splitter_6.setOrientation(Qt.Orientation.Horizontal)
        self.splitter = QSplitter(self.splitter_6)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Vertical)
        self.entrada1 = QLineEdit(self.splitter)
        self.entrada1.setObjectName(u"entrada1")
        self.splitter.addWidget(self.entrada1)
        self.entrada2 = QLineEdit(self.splitter)
        self.entrada2.setObjectName(u"entrada2")
        self.splitter.addWidget(self.entrada2)
        self.resultado = QLabel(self.splitter)
        self.resultado.setObjectName(u"resultado")
        self.splitter.addWidget(self.resultado)
        self.splitter_6.addWidget(self.splitter)
        self.splitter_5 = QSplitter(self.splitter_6)
        self.splitter_5.setObjectName(u"splitter_5")
        self.splitter_5.setOrientation(Qt.Orientation.Vertical)
        self.splitter_4 = QSplitter(self.splitter_5)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setOrientation(Qt.Orientation.Horizontal)
        self.splitter_2 = QSplitter(self.splitter_4)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Orientation.Vertical)
        self.btsuma = QPushButton(self.splitter_2)
        self.btsuma.setObjectName(u"btsuma")
        self.splitter_2.addWidget(self.btsuma)
        self.btresta = QPushButton(self.splitter_2)
        self.btresta.setObjectName(u"btresta")
        self.splitter_2.addWidget(self.btresta)
        self.splitter_4.addWidget(self.splitter_2)
        self.splitter_3 = QSplitter(self.splitter_4)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Orientation.Vertical)
        self.btmulti = QPushButton(self.splitter_3)
        self.btmulti.setObjectName(u"btmulti")
        self.splitter_3.addWidget(self.btmulti)
        self.btdivi = QPushButton(self.splitter_3)
        self.btdivi.setObjectName(u"btdivi")
        self.splitter_3.addWidget(self.btdivi)
        self.splitter_4.addWidget(self.splitter_3)
        self.splitter_5.addWidget(self.splitter_4)
        self.btsalida = QPushButton(self.splitter_5)
        self.btsalida.setObjectName(u"btsalida")
        self.splitter_5.addWidget(self.btsalida)
        self.splitter_6.addWidget(self.splitter_5)
        Calculadora.setCentralWidget(self.centralwidget)
        self.splitter_6.raise_()
        self.label.raise_()

        self.retranslateUi(Calculadora)

        QMetaObject.connectSlotsByName(Calculadora)
    # setupUi

    def retranslateUi(self, Calculadora):
        Calculadora.setWindowTitle(QCoreApplication.translate("Calculadora", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("Calculadora", u"Calculadora", None))
        self.resultado.setText("")
        self.btsuma.setText(QCoreApplication.translate("Calculadora", u"+", None))
        self.btresta.setText(QCoreApplication.translate("Calculadora", u"-", None))
        self.btmulti.setText(QCoreApplication.translate("Calculadora", u"*", None))
        self.btdivi.setText(QCoreApplication.translate("Calculadora", u"/", None))
        self.btsalida.setText(QCoreApplication.translate("Calculadora", u"salir", None))
    # retranslateUi

