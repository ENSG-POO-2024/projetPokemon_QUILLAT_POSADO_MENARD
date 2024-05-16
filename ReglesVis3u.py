
import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton, QMainWindow, QApplication
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

import test_graph as t
import Starter.StarterVis3u as s
import Poke as poke
import Accueil.AccueilVis3u as ac

script_dir = os.path.dirname(__file__)

class Regles_ui(object):
    def setupUi(self, MainWindow):


        # On crée la fenêtre Victoire
        MainWindow.setWindowTitle("Règles du jeu")
        MainWindow.resize(1000, 750)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        # Création du fond
        self.Back = QtWidgets.QLabel(self.centralwidget)
        self.Back.setGeometry(QtCore.QRect(0, 0, 1000, 750))
        self.Back.setText("")
        self.Back.setPixmap(QtGui.QPixmap("Combat/Outils/Victoire.png"))
        self.Back.setScaledContents(True)
        self.Back.setObjectName("Back")
        

        # Création du bouton pour partir 
        self.PartirButton = QtWidgets.QPushButton(self.centralwidget)
        self.PartirButton.setGeometry(QtCore.QRect(0, 0, 200, 120))
        self.PartirButton.setObjectName("PartirButton")

        MainWindow.setCentralWidget(self.centralwidget)

        # On rend les boutons invisibles
        self.PartirButton.setStyleSheet("background-color: rgba(255, 255, 255, 0); border: none;")

        self.PartirButton.clicked.connect(self.open_acceuil)

    def open_acceuil(self):
        video_path = os.path.join(script_dir, "Image", "video.mp4")
        self.close()
        self.acceuil_window = t.AccueilWindow(video_path)
        self.acceuil_window.show()


class ReglesWindow(QMainWindow, Regles_ui):
    def __init__(self, parent=None):
        super(ReglesWindow, self).__init__(parent)
        self.setupUi(self)



if __name__ == "__main__":
    def run_app():
        app = QApplication(sys.argv)
        regles = ReglesWindow()
        regles.setWindowTitle("Exemple de la page règles")
        regles.show()
        app.exec_()
    run_app()