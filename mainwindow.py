# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 500)
        font = QtGui.QFont()
        font.setPointSize(16)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tbxLink = QtWidgets.QLineEdit(self.centralwidget)
        self.tbxLink.setGeometry(QtCore.QRect(30, 30, 791, 39))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.tbxLink.setFont(font)
        self.tbxLink.setObjectName("tbxLink")
        self.btnBul = QtWidgets.QPushButton(self.centralwidget)
        self.btnBul.setGeometry(QtCore.QRect(860, 30, 145, 42))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.btnBul.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnBul.setFont(font)
        self.btnBul.setObjectName("btnBul")
        self.btnTemizle = QtWidgets.QPushButton(self.centralwidget)
        self.btnTemizle.setEnabled(False)
        self.btnTemizle.setGeometry(QtCore.QRect(1010, 30, 145, 42))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnTemizle.setFont(font)
        self.btnTemizle.setObjectName("btnTemizle")
        self.lblVideoTitle = QtWidgets.QLabel(self.centralwidget)
        self.lblVideoTitle.setGeometry(QtCore.QRect(400, 100, 700, 100))
        self.lblVideoTitle.setText("")
        self.lblVideoTitle.setWordWrap(True)
        self.lblVideoTitle.setObjectName("lblVideoTitle")
        self.labelimg = QtWidgets.QLabel(self.centralwidget)
        self.labelimg.setGeometry(QtCore.QRect(30, 100, 320, 240))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelimg.sizePolicy().hasHeightForWidth())
        self.labelimg.setSizePolicy(sizePolicy)
        self.labelimg.setText("")
        self.labelimg.setScaledContents(True)
        self.labelimg.setObjectName("labelimg")
        self.cbxStreams = QtWidgets.QComboBox(self.centralwidget)
        self.cbxStreams.setEnabled(True)
        self.cbxStreams.setGeometry(QtCore.QRect(400, 225, 700, 39))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.cbxStreams.setFont(font)
        self.cbxStreams.setObjectName("cbxStreams")
        self.btnIndir = QtWidgets.QPushButton(self.centralwidget)
        self.btnIndir.setEnabled(False)
        self.btnIndir.setGeometry(QtCore.QRect(400, 300, 145, 42))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.btnIndir.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnIndir.setFont(font)
        self.btnIndir.setObjectName("btnIndir")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 43))
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
        self.btnBul.setText(_translate("MainWindow", "Bul"))
        self.btnTemizle.setText(_translate("MainWindow", "Temizle"))
        self.btnIndir.setText(_translate("MainWindow", "İndir"))
