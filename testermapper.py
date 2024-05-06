# -*- coding: utf-8 -*-
"""
Created on Sat May  4 10:15:04 2024

@author: diego
"""

import sys
from mapper2 import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication

class XXXXWindow (QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(XXXXWindow, self).__init__(parent)
        self.setupUi(self)
# ...
if __name__ == "__main__":
    def run_app():
        app = QApplication(sys.argv)
        mainWin = XXXXWindow()
        mainWin.show()
        app.exec_()
    run_app()