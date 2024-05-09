# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CombatVis3u.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton, QMainWindow, QApplication, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

import Poke as poke
import test_graph as t #MODIFIER QUAND FICHIER DEFINITIF
import fight as f


class Combat_ui(object):
    def setupUi(self, MainWindow):


        # Création de l'objet MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("Combat contre " + self.pokemon_sauvage.name.split()[0])
        MainWindow.resize(1000, 750)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        #Création de l'objet barre de vie de notre pokemon
        self.progressBarAllie = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBarAllie.setGeometry(QtCore.QRect(620, 397, 371, 23))
        self.progressBarAllie.setMaximum(200)
        self.progressBarAllie.setValue(self.pokemon_sauvage.hp)
        self.progressBarAllie.setFormat("")
        self.progressBarAllie.setObjectName("progressBarAllie")
        self.label = QLabel(MainWindow)
        self.label.setGeometry(625, 392, 30, 30)  # Définir la géométrie du QLabel
        self.label.setText(str(self.pokemon_sauvage.hp))  # Définir le texte à afficher
        # Changer la couleur du texte avec la méthode setPalette
        palette = self.label.palette()
    

        if self.pokemon_sauvage.hp <= 0.25 * self.progressBarAllie.maximum():
            self.progressBarAllie.setStyleSheet("""                                                                
                QProgressBar {
                    border: 2px solid grey;
                    border-radius: 5px;
                    background-color: #FFFFFF; /* Couleur de fond de la barre de progression */
                }
                    
                QProgressBar::chunk {
                    background-color: #FF0000; /* Couleur de la barre de progression */
                }                                
            """)
            palette.setColor(self.label.foregroundRole(), QColor("dark"))  
            
        else:
            self.progressBarAllie.setStyleSheet("""   
                QProgressBar { color: red;}                                                            
                QProgressBar {                            
                    border: 2px solid grey;
                    border-radius: 5px;
                    background-color: #FFFFFF; /* Couleur de fond de la barre de progression */
                }

                QProgressBar::chunk {
                    background-color: #00FF00; /* Couleur de la barre de progression */
                }                                                             
            """)
            palette.setColor(self.label.foregroundRole(), QColor("yellow")) 
            
        self.label.setPalette(palette)
        


        # Création de l'arrière plan
        self.Fond = QtWidgets.QLabel(self.centralwidget)
        self.Fond.setGeometry(QtCore.QRect(0, 0, 1001, 751))
        self.Fond.setText("")
        self.Fond.setPixmap(QtGui.QPixmap("Combat/BackgroundCombat.png"))
        self.Fond.setScaledContents(True)
        self.Fond.setObjectName("Fond")

        # Création de la barre de vie de m'adversaire
        self.progressBarEnemy = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBarEnemy.setGeometry(QtCore.QRect(110, 189, 371, 23))
        self.progressBarEnemy.setMaximum(100)
        self.progressBarEnemy.setValue(40)
        self.progressBarEnemy.setFormat("")
        self.progressBarEnemy.setObjectName("progressBarEnemy")
        self.progressBarEnemy.setStyleSheet("""
            QProgressBar {
                border: 2px solid grey;
                border-radius: 5px;
                background-color: #FFFFFF; /* Couleur de fond de la barre de progression */
            }

            QProgressBar::chunk {
                background-color: #00FF00; /* Couleur de la barre de progression */
            }
        """)

        # Bouton de l'attaque normale
        self.AttaqueNormale = QtWidgets.QPushButton(self.centralwidget)
        self.AttaqueNormale.setGeometry(QtCore.QRect(370, 560, 171, 161))
        self.AttaqueNormale.setText("")
        self.AttaqueNormale.setObjectName("AttaqueNormale")

        # Bouton de l'attaque speciale
        self.AttaqueSpeciale = QtWidgets.QPushButton(self.centralwidget)
        self.AttaqueSpeciale.setGeometry(QtCore.QRect(570, 560, 171, 161))
        self.AttaqueSpeciale.setText("")
        self.AttaqueSpeciale.setObjectName("AttaqueSpeciale")

        # Bouton pour changer de pokemon
        self.Pokedex = QtWidgets.QPushButton(self.centralwidget)
        self.Pokedex.setGeometry(QtCore.QRect(780, 560, 171, 161))
        self.Pokedex.setText("")
        self.Pokedex.setObjectName("Pokedex")

        # Bouton pour fuir
        self.Fuite = QtWidgets.QPushButton(self.centralwidget)
        self.Fuite.setGeometry(QtCore.QRect(840, 10, 141, 61))
        self.Fuite.setText("")
        self.Fuite.setObjectName("Fuite")

        # On met tout en avant (dans le bon ordre) pour que les objets soient au premier plan 
        self.Fond.raise_()
        self.progressBarAllie.raise_()
        self.progressBarEnemy.raise_()
        self.AttaqueNormale.raise_()
        self.AttaqueSpeciale.raise_()
        self.Pokedex.raise_()
        self.Fuite.raise_()


        self.AttaqueNormale.setStyleSheet("background-color: rgba(255, 255, 255, 0); border: none;")
        self.AttaqueSpeciale.setStyleSheet("background-color: rgba(255, 255, 255, 0); border: none;")
        self.Pokedex.setStyleSheet("background-color: rgba(255, 255, 255, 0); border: none;")
        self.Fuite.setStyleSheet("background-color: rgba(255, 255, 255, 0); border: none;")


        MainWindow.setCentralWidget(self.centralwidget)

        self.Fuite.clicked.connect(MainWindow.close)




class FightWindow(QMainWindow, Combat_ui):
    def __init__(self, pokemon_sauvage, sacha, parent=None):
        self.pokemon_sauvage = pokemon_sauvage
        self.sacha = sacha
        super(FightWindow, self).__init__(parent)
        self.setupUi(self)
        



# if __name__ == "__main__":
#     def run_app():
#         app = QApplication(sys.argv)
#         mainWin = FightWindow()
#         mainWin.show()
#         app.exec_()
#     run_app()