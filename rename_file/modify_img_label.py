# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import sys, os
import random

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.setWindowTitle("modifyImgName")
        self.setWindowIcon(QtGui.QIcon("icon.png"))
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("modify file name"))
        MainWindow.resize(800, 432)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        
        self.path_label = QtWidgets.QLabel(self.centralwidget)
        self.path_label.setGeometry(QtCore.QRect(70, 40, 51, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yu Gothic UI Semibold"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.path_label.setFont(font)
        self.path_label.setObjectName(_fromUtf8("path_label"))
        
        self.path_text = QtWidgets.QTextEdit(self.centralwidget)
        self.path_text.setGeometry(QtCore.QRect(140, 40, 531, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sim sun"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(75)
        self.path_text.setFont(font)
        self.path_text.setObjectName(_fromUtf8("path_text"))

        self.img_label = QtWidgets.QLabel(self.centralwidget)
        self.img_label.setGeometry(QtCore.QRect(70, 80, 71, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yu Gothic UI Semibold"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.img_label.setFont(font)
        self.img_label.setObjectName(_fromUtf8("img_label"))
        
        self.img = QtWidgets.QLabel(self.centralwidget)
        self.img.setGeometry(QtCore.QRect(140, 40, 531, 161))
        self.img.setObjectName(_fromUtf8("img"))
        
        self.ok = QtWidgets.QPushButton(self.centralwidget)
        self.ok.setGeometry(QtCore.QRect(440, 350, 101, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yu Gothic UI Semibold"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ok.setFont(font)
        self.ok.setObjectName(_fromUtf8("ok"))
        
        self.name = QtWidgets.QTextEdit(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(140, 260, 531, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yu Gothic UI Semibold"))
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.name.setFont(font)
        self.name.setObjectName(_fromUtf8("name"))
        
        self.img_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.img_label_2.setGeometry(QtCore.QRect(60, 260, 81, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yu Gothic UI Semibold"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.img_label_2.setFont(font)
        self.img_label_2.setObjectName(_fromUtf8("img_label_2"))
        
        self.change = QtWidgets.QPushButton(self.centralwidget)
        self.change.setGeometry(QtCore.QRect(260, 350, 101, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yu Gothic UI Semibold"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.change.setFont(font)
        self.change.setObjectName(_fromUtf8("change"))
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.change.clicked.connect(self.change_picture)
        self.ok.clicked.connect(self.save)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.ok.setText(_translate("MainWindow", "ok", None))
        self.img_label.setText(_translate("MainWindow", "image:", None))
        self.img_label_2.setText(_translate("MainWindow", "content:", None))
        self.change.setText(_translate("MainWindow", "change", None))
        self.path_label.setText(_translate("MainWindow", "path:", None))
        
    def change_picture(self):
        path = self.path_text.toPlainText()
        self.path = str(path)
        pics = os.listdir(self.path)
        n = len(pics)
        num = random.randint(0, n) # 随机取
        self.pic = pics[num]
        with open(os.path.join(self.path, self.pic), 'rb') as f:
            self.image = f.read()
        picture = QtGui.QImage()
        picture.loadFromData(self.image)
        self.img.setPixmap(QtGui.QPixmap(picture))
    
    def save(self):
        name = self.name.toPlainText()
        name = unicode(name)
        ftype = os.path.splitext(self.pic)[1]
        os.rename(os.path.join(self.path, self.pic), os.path.join(self.path, name+ftype))
        self.name.clear()
        self.change_picture()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    modify = Ui_MainWindow()
    modify.show()
    app.exec_()