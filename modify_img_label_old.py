# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\update_img_label.ui'
#
# Created: Fri Jul 21 11:10:03 2017
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)        
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 405)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.ok = QtGui.QPushButton(self.centralwidget)
        self.ok.setGeometry(QtCore.QRect(330, 280, 101, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yu Gothic UI Semibold"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ok.setFont(font)
        self.ok.setObjectName(_fromUtf8("ok"))
        self.img_label = QtGui.QLabel(self.centralwidget)
        self.img_label.setGeometry(QtCore.QRect(40, 10, 71, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yu Gothic UI Semibold"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.img_label.setFont(font)
        self.img_label.setObjectName(_fromUtf8("img_label"))
        self.label = QtGui.QTextEdit(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 190, 531, 71))
        self.label.setObjectName(_fromUtf8("label"))
        self.image = QtGui.QGraphicsView(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(110, 10, 541, 141))
        self.image.setFrameShape(QtGui.QFrame.StyledPanel)
        self.image.setFrameShadow(QtGui.QFrame.Raised)
        self.image.setObjectName(_fromUtf8("image"))
        self.img_label_2 = QtGui.QLabel(self.centralwidget)
        self.img_label_2.setGeometry(QtCore.QRect(30, 190, 81, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yu Gothic UI Semibold"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.img_label_2.setFont(font)
        self.img_label_2.setObjectName(_fromUtf8("img_label_2"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.ok.setText(_translate("MainWindow", "ok", None))
        self.img_label.setText(_translate("MainWindow", "image:", None))
        self.img_label_2.setText(_translate("MainWindow", "content:", None))
        
    def open_file(self):
        self.img_label.

    
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    modify = Ui_MainWindow()
    modify.show()
    app.exec_()