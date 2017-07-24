# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 14:15:01 2017

@author: lyuww
"""

import sys
from PyQt4 import QtGui

class Icon(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QtGui.QIcon('./icon.png'))

app = QtGui.QApplication(sys.argv)
icon = Icon()
icon.show()
sys.exit(app.exec_())