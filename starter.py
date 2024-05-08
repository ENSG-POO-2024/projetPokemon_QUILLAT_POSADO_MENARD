import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton, QMainWindow, QApplication
from PyQt5.QtGui import QPixmap

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 750)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Fond = QtWidgets.QLabel(self.centralwidget)
        self.Fond.setGeometry(QtCore.QRect(0, 0, 1001, 751))
        self.Fond.setText("")
        self.Fond.setPixmap(QtGui.QPixmap("Starter/ChoIx du starter.png"))
        self.Fond.setScaledContents(True)
        self.Fond.setObjectName("Fond")
        self.ButtonBul = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonBul.setGeometry(QtCore.QRect(110, 320, 161, 201))
        self.ButtonBul.setText("")
        self.ButtonBul.setObjectName("ButtonBul")
        self.ButtonSal = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonSal.setGeometry(QtCore.QRect(420, 320, 161, 201))
        self.ButtonSal.setText("")
        self.ButtonSal.setObjectName("ButtonSal")
        self.ButtonCar = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonCar.setGeometry(QtCore.QRect(710, 320, 161, 201))
        self.ButtonCar.setText("")
        self.ButtonCar.setObjectName("ButtonCar")
        self.Salameche = QtWidgets.QLabel(self.centralwidget)
        self.Salameche.setGeometry(QtCore.QRect(390, 290, 231, 241))
        self.Salameche.setText("")
        self.Salameche.setPixmap(QtGui.QPixmap("Starter/Salamèche_face.png"))
        self.Salameche.setScaledContents(True)
        self.Salameche.setObjectName("Salameche")
        self.Bulbizarre = QtWidgets.QLabel(self.centralwidget)
        self.Bulbizarre.setGeometry(QtCore.QRect(80, 310, 231, 241))
        self.Bulbizarre.setText("")
        self.Bulbizarre.setPixmap(QtGui.QPixmap("Starter/Bulbizarre_face.png"))
        self.Bulbizarre.setScaledContents(True)
        self.Bulbizarre.setObjectName("Bulbizarre")
        self.Carapuce = QtWidgets.QLabel(self.centralwidget)
        self.Carapuce.setGeometry(QtCore.QRect(680, 300, 231, 241))
        self.Carapuce.setText("")
        self.Carapuce.setPixmap(QtGui.QPixmap("Starter/Carapuce_face.png"))
        self.Carapuce.setScaledContents(True)
        self.Carapuce.setObjectName("Carapuce")
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.ButtonBul.setStyleSheet("background-color: rgba(255, 255, 255, 0); border: none;")
        self.ButtonSal.setStyleSheet("background-color: rgba(255, 255, 255, 0); border: none;")
        self.ButtonCar.setStyleSheet("background-color: rgba(255, 255, 255, 0); border: none;")

        self.Bulbizarre.enterEvent = self.enter_image1
        self.Bulbizarre.leaveEvent = self.leave_image1
        self.Salameche.enterEvent = self.enter_image2
        self.Salameche.leaveEvent = self.leave_image2
        self.Carapuce.enterEvent = self.enter_image3
        self.Carapuce.leaveEvent = self.leave_image3

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def enter_image1(self, event):
        self.Bulbizarre.setPixmap(QPixmap("Starter/Bulbizarre_clic.png"))
        
    def enter_image2(self, event):
        self.Salameche.setPixmap(QPixmap("Starter/Salamèche_clic.png"))

    def enter_image3(self, event):
        self.Carapuce.setPixmap(QPixmap("Starter/Carapuce_clic.png"))

    def leave_image1(self, event):
        self.Bulbizarre.setPixmap(QPixmap("Starter/Bulbizarre_face.png"))

    def leave_image2(self, event):
        self.Salameche.setPixmap(QPixmap("Starter/Salamèche_face.png"))
    
    def leave_image3(self, event):
        self.Carapuce.setPixmap(QPixmap("Starter/Carapuce_face.png"))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


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