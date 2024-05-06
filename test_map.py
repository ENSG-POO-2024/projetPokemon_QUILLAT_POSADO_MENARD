


import sys
from mappy import Ui_Dialog
from PyQt5.QtWidgets import QMainWindow, QApplication

class XXXXWindow (QMainWindow, Ui_Dialog):
    def __init__(self, parent=None):
        super(XXXXWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == "__main__":
    def run_app():
        app = QApplication(sys.argv)
        mainWin = XXXXWindow()
        mainWin.show()
        app.exec_()
    run_app()