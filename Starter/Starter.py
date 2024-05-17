
import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPixmap

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

import Poke as poke
import Jeu as j


class Starter_ui(object):

    def setupUi(self, MainWindow):
        
        # Création de la fenêtre du starter
        MainWindow.setWindowTitle("Choix du starter")
        MainWindow.resize(1000, 750)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Création de l'objet fond
        self.Fond = QtWidgets.QLabel(self.centralwidget)
        self.Fond.setGeometry(QtCore.QRect(0, 0, 1000, 750))
        self.Fond.setText("")
        self.Fond.setPixmap(QtGui.QPixmap("Starter/ChoIx du starter.png"))
        self.Fond.setScaledContents(True)
        self.Fond.setObjectName("Fond")

        # Création de l'objet Bulbizarre
        self.ButtonBul = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonBul.setGeometry(QtCore.QRect(80, 310, 231, 241))
        self.ButtonBul.setText("")
        self.ButtonBul.setObjectName("ButtonBul")

        # Création de l'objet Salamèche
        self.ButtonSal = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonSal.setGeometry(QtCore.QRect(420, 320, 161, 201))
        self.ButtonSal.setText("")
        self.ButtonSal.setObjectName("ButtonSal")

        # Création de l'objet Carapuce
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

        self.ButtonBul.setStyleSheet("background-color: rgba(0, 0, 0, 0); border: none;")
        self.ButtonSal.setStyleSheet("background-color: rgba(255, 255, 255, 0); border: none;")
        self.ButtonCar.setStyleSheet("background-color: rgba(255, 255, 255, 0); border: none;")

        self.Bulbizarre.enterEvent = self.enter_image1
        self.Bulbizarre.leaveEvent = self.leave_image1
        self.Salameche.enterEvent = self.enter_image2
        self.Salameche.leaveEvent = self.leave_image2
        self.Carapuce.enterEvent = self.enter_image3
        self.Carapuce.leaveEvent = self.leave_image3



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



class Starter(QMainWindow, Starter_ui):
    def __init__(self, parent=None):
        super(Starter, self).__init__(parent)
        self.setupUi(self)

    def mousePressEvent(self, event):
        """
        Fonction qui permet de gérer l'évenement: clic gauche
        """
        # On récupère les coordonnées du clic de la souris
        mouse_x = event.x()
        mouse_y = event.y()

        if self.clic(mouse_x, mouse_y, 80, 311, 310, 551): 
            self.poke = poke.Pokemon('Bulbizarre',None, None,45,49,49,65,65,poke.Plante()) 
            self.map_window = j.Map(self.poke, "pokemons_a_capturer.csv")
            self.map_window.show()
            self.close()     

        if self.clic(mouse_x, mouse_y, 390, 621, 290, 531): 
            self.poke = poke.Pokemon('Salameche',None, None,39,52,43,60,50,poke.Feu()) 
            self.map_window = j.Map(self.poke, "pokemons_a_capturer.csv")
            self.map_window.show()
            self.close()  

        if self.clic(mouse_x, mouse_y, 680, 911, 300, 541): 
            self.poke = poke.Pokemon('Carapuce',None, None,44,48,65,50,64,poke.Eau()) 
            self.map_window = j.Map(self.poke, "pokemons_a_capturer.csv")
            self.map_window.show()
            self.close()  

    def clic(self, x, y, x_inf, x_sup, y_inf, y_sup):
        """
        Fonction qui teste si le clic est dans la zone entre x_inf et x_sup et entre y_inf et y_sup
        """
        if x_inf <= x <= x_sup and y_inf <= y <= y_sup:
            return True
            

     
if __name__ == "__main__":
    def run_app():
        app = QApplication(sys.argv)
        mainWin = Starter()
        mainWin.show()
        app.exec_()
    run_app()