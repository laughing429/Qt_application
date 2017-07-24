# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 15:19:10 2017

@author: lyuww
"""

import sys
from PyQt4 import QtGui, QtCore

class QuitButton(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit button')
        
        quit = QtGui.QPushButton('Close', self)
        quit.setGeometry(10, 10, 64, 35)
        
#        self.connect(quit, QtCore.SIGNAL('clicked()'),
#                     QtGui.qApp, QtCore.SLOT('quit()'))
        quit.clicked.connect(self.print_ok)
    
    def print_ok(self):
        print 'OK'
                     
app = QtGui.QApplication(sys.argv)
qb = QuitButton()
qb.show()
sys.exit(app.exec_())