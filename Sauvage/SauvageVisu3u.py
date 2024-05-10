
import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton, QMainWindow, QApplication, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QFont, QPainter, QPixmap

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

import Poke as poke
import test_graph as t #MODIFIER QUAND FICHIER DEFINITIF
import Combat.CombatVis3u as c


class Sauvage_ui(object):

        
    def setupUi(self, MainWindow):


        # Création de l'objet MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("Rencontre avec " + self.pokemon_sauvage.name.split()[0])
        MainWindow.resize(1000, 750)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Création de l'arrière plan
        self.Fond = QtWidgets.QLabel(self.centralwidget)
        self.Fond.setGeometry(QtCore.QRect(0, 0, 1000, 750))
        self.Fond.setText("")
        self.Fond.setPixmap(QtGui.QPixmap("Image/test.png"))
        self.Fond.setScaledContents(True)
        self.Fond.setObjectName("Fond")

        # Affichage du pokemon rencontré
        self.image_poke = QtWidgets.QLabel(self.centralwidget)
        self.image_poke.setGeometry(QtCore.QRect(320, 10, 400, 400))
        self.image_poke.setText("")
        self.image_poke.setPixmap(QtGui.QPixmap("Pokémons/"+self.pokemon_sauvage.name.split()[0]+"/"+self.pokemon_sauvage.name.split()[0]+"_face.png"))
        #self.image_poke.setPixmap(QtGui.QPixmap("Pokémons/Pikachu/Pikachu_face.png"))
        self.image_poke.setScaledContents(True)
        self.image_poke.setObjectName("Pokemon rencontré")


        # Bouton pour fuir
        self.fight_buton = QtWidgets.QPushButton(self.centralwidget)
        self.fight_buton.setGeometry(QtCore.QRect(630, 365, 260, 460))
        self.fight_buton.setText("")
        self.fight_buton.setObjectName("Fuite")

        # Bouton pour fuir
        self.fuite = QtWidgets.QPushButton(self.centralwidget)
        self.fuite.setGeometry(QtCore.QRect(90, 365, 260, 460))
        self.fuite.setText("")
        self.fuite.setObjectName("Fuite")

        # On met tout en avant (dans le bon ordre) pour que les objets soient au premier plan 
        self.Fond.raise_()
        self.image_poke.raise_()
        self.fuite.raise_()
        self.fight_buton.raise_()


        self.fight_buton.setStyleSheet("background-color: rgba(255, 255, 255, 0); border: none;")
        self.fuite.setStyleSheet("background-color: rgba(255, 255, 255, 0); border: none;")

        MainWindow.setCentralWidget(self.centralwidget)

        self.fuite.clicked.connect(MainWindow.close)

        self.fight_buton.clicked.connect(MainWindow.close)
        self.fight_buton.clicked.connect(self.open_fight_window)

    def open_fight_window(self):
        self.fight_window = c.FightWindow(self.pokemon_sauvage, self.sacha)
        self.fight_window.show()






class SauvageWindow(QMainWindow, Sauvage_ui):
    def __init__(self, pokemon_sauvage, sacha, parent=None):
        self.pokemon_sauvage = pokemon_sauvage
        self.sacha = sacha
        super(SauvageWindow, self).__init__(parent)
        self.setupUi(self)