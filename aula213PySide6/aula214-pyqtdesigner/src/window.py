<<<<<<< HEAD:aula213PySide6/aula214-pyqtdesigner/src/window.py
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    Qt,
    QTime,
    QUrl,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMenuBar,
    QPushButton,
    QSizePolicy,
    QStatusBar,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.labelResult = QLabel(self.centralwidget)
        self.labelResult.setObjectName("labelResult")
        font = QFont()
        font.setPointSize(40)
        self.labelResult.setFont(font)
        self.labelResult.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelResult, 0, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineName = QLineEdit(self.centralwidget)
        self.lineName.setObjectName("lineName")
        font1 = QFont()
        font1.setPointSize(30)
        self.lineName.setFont(font1)

        self.gridLayout_2.addWidget(self.lineName, 0, 1, 1, 1)

        self.labelName = QLabel(self.centralwidget)
        self.labelName.setObjectName("labelName")
        self.labelName.setFont(font1)

        self.gridLayout_2.addWidget(self.labelName, 0, 0, 1, 1)

        self.buttonSend = QPushButton(self.centralwidget)
        self.buttonSend.setObjectName("buttonSend")
        self.buttonSend.setFont(font1)

        self.gridLayout_2.addWidget(self.buttonSend, 0, 2, 1, 1)

        self.gridLayout.addLayout(self.gridLayout_2, 1, 0, 1, 1)

        self.horizontalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.labelResult.setText(
            QCoreApplication.translate("MainWindow", "Nothing here!", None)
        )
        self.lineName.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Digite seu nome...", None)
        )
        self.labelName.setText(
            QCoreApplication.translate("MainWindow", "Seu nome:", None)
        )
        self.buttonSend.setText(
            QCoreApplication.translate("MainWindow", "Enviar", None)
        )

    # retranslateUi
=======
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    Qt,
    QTime,
    QUrl,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMenuBar,
    QPushButton,
    QSizePolicy,
    QStatusBar,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.labelResult = QLabel(self.centralwidget)
        self.labelResult.setObjectName("labelResult")
        font = QFont()
        font.setPointSize(40)
        self.labelResult.setFont(font)
        self.labelResult.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelResult, 0, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineName = QLineEdit(self.centralwidget)
        self.lineName.setObjectName("lineName")
        font1 = QFont()
        font1.setPointSize(30)
        self.lineName.setFont(font1)

        self.gridLayout_2.addWidget(self.lineName, 0, 1, 1, 1)

        self.labelName = QLabel(self.centralwidget)
        self.labelName.setObjectName("labelName")
        self.labelName.setFont(font1)

        self.gridLayout_2.addWidget(self.labelName, 0, 0, 1, 1)

        self.buttonSend = QPushButton(self.centralwidget)
        self.buttonSend.setObjectName("buttonSend")
        self.buttonSend.setFont(font1)

        self.gridLayout_2.addWidget(self.buttonSend, 0, 2, 1, 1)

        self.gridLayout.addLayout(self.gridLayout_2, 1, 0, 1, 1)

        self.horizontalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.labelResult.setText(
            QCoreApplication.translate("MainWindow", "Nothing here!", None)
        )
        self.lineName.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Digite seu nome...", None)
        )
        self.labelName.setText(
            QCoreApplication.translate("MainWindow", "Seu nome:", None)
        )
        self.buttonSend.setText(
            QCoreApplication.translate("MainWindow", "Enviar", None)
        )

    # retranslateUi
>>>>>>> 73989d2f88d5bb45946e332d6c3d836d872ea3b5:aula214-pyqtdesigner/src/window.py
