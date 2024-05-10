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
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QColor, QFont, QPainter, QPixmap
from PyQt5 import *

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

import Poke as poke
import test_graph as t #MODIFIER QUAND FICHIER DEFINITIF
import fight as f


class Combat_ui(object):

        
    def setupUi(self, MainWindow, cmp):

        self.poke_sacha = list(self.sacha.pokedex.values())[0]
        self.adversaire = self.pokemon_sauvage
        HP = self.poke_sacha.hp
        HP_adv = self.adversaire.hp

        


        # Création de l'objet MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("Combat contre " + self.pokemon_sauvage.name.split()[0])
        MainWindow.resize(1000, 750)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Création de l'arrière plan
        self.Fond = QtWidgets.QLabel(self.centralwidget)
        self.Fond.setGeometry(QtCore.QRect(0, 0, 1000, 750))
        self.Fond.setText("")
        self.Fond.setPixmap(QtGui.QPixmap("Combat/BackgroundCombat.png"))
        self.Fond.setScaledContents(True)
        self.Fond.setObjectName("Fond")


        #Création de l'objet barre de vie de notre pokemon
        self.progressBarAllie = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBarAllie.setGeometry(QtCore.QRect(620, 397, 371, 23))
        self.progressBarAllie.setMaximum(HP)
        self.progressBarAllie.setValue(self.poke_sacha.hp)
        self.progressBarAllie.setFormat("")
        self.progressBarAllie.setObjectName("progressBarAllie")
        self.label = QLabel(MainWindow)
        self.label.setGeometry(625, 392, 30, 30)  # Définir la géométrie du QLabel
        self.label.setText(str(self.poke_sacha.hp))  # Définir le texte à afficher
        # Changer la couleur du texte avec la méthode setPalette
        palette = self.label.palette()
    

        if self.poke_sacha.hp <= 0.25 * self.progressBarAllie.maximum():
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
            
        
        


        # Création de la barre de vie de m'adversaire
        self.progressBarEnemy = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBarEnemy.setGeometry(QtCore.QRect(110, 189, 371, 23))
        self.progressBarEnemy.setMaximum(HP_adv)
        self.progressBarEnemy.setValue(self.adversaire.hp)
        self.progressBarEnemy.setFormat("")
        self.progressBarEnemy.setObjectName("progressBarEnemy")

        # Créer une étiquette pour afficher les points de vie de l'adversaire
        self.label_hp_adversaire = QtWidgets.QLabel(self.centralwidget)
        self.label_hp_adversaire.setGeometry(QtCore.QRect(113, 189, 371, 23))
        self.label_hp_adversaire.setObjectName("label_hp_adversaire")
        self.label_hp_adversaire.setStyleSheet("color: black; font-size: 16px;")
        

        if self.adversaire.hp <= 0.25 * self.progressBarEnemy.maximum():
            self.progressBarEnemy.setStyleSheet("""                                                                
                QProgressBar {
                    border: 2px solid grey;
                    border-radius: 5px;
                    background-color: #FFFFFF; /* Couleur de fond de la barre de progression */
                }
                    
                QProgressBar::chunk {
                    background-color: #FF0000; /* Couleur de la barre de progression */
                }                                
            """)
            
        else:
            self.progressBarEnemy.setStyleSheet("""   
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
        # Mettre à jour le texte de l'étiquette des points de vie de l'adversaire
        self.label_hp_adversaire.setText(str(self.adversaire.hp))
        self.label_hp_adversaire.raise_()

        # Affichage de notre pokémon
        self.image_poke = QtWidgets.QLabel(self.centralwidget)
        self.image_poke.setGeometry(QtCore.QRect(60, 230, 400, 400))
        self.image_poke.setText("")
        self.image_poke.setPixmap(QtGui.QPixmap("Pokémons/"+self.poke_sacha.name.split()[0]+"/"+self.poke_sacha.name.split()[0]+"_dos.png"))
        self.image_poke.setScaledContents(True)
        self.image_poke.setObjectName("Pokemon Sacha")

        # Affichage pokémon adverse
        self.image_adv = QtWidgets.QLabel(self.centralwidget)
        self.image_adv.setGeometry(QtCore.QRect(550, 40, 400, 400))
        self.image_adv.setText("")
        self.image_adv.setPixmap(QtGui.QPixmap("Pokémons/"+self.adversaire.name.split()[0]+"/"+self.adversaire.name.split()[0]+"_face.png"))
        self.image_adv.setScaledContents(True)
        self.image_adv.setObjectName("Pokemon adverse")



        # Point d'attaque et de défense de notre pokémon
        self.label = QLabel(str(self.poke_sacha.attack), self)
        self.label.setGeometry(145, 583, 200, 50)
        self.label.setStyleSheet("color: black; font-size: 25px;")  
        self.label = QLabel(str(self.poke_sacha.defense), self)
        self.label.setGeometry(145, 657, 200, 50)
        self.label.setStyleSheet("color: black; font-size: 25px;")

        # Point d'attaque et de défense de l'adversaire
        self.label = QLabel(str(self.adversaire.attack), self)
        self.label.setGeometry(323, -2, 200, 50)
        self.label.setStyleSheet("color: red; font-size: 20px;")  
        self.label = QLabel(str(self.adversaire.defense), self)
        self.label.setGeometry(339, 34, 200, 50)
        self.label.setStyleSheet("color: red; font-size: 20px;")

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
        self.Fuite.setGeometry(QtCore.QRect(800, 0, 300, 300))
        self.Fuite.setText("")
        self.Fuite.setObjectName("Fuite")

        # On met tout en avant (dans le bon ordre) pour que les objets soient au premier plan 
        self.Fond.raise_()
        self.image_poke.raise_()
        self.image_adv.raise_()
        self.progressBarAllie.raise_()
        self.progressBarEnemy.raise_()
        self.AttaqueNormale.raise_()
        self.AttaqueSpeciale.raise_()
        self.Pokedex.raise_()
        self.Fuite.raise_()
        self.label_hp_adversaire.raise_()


        self.AttaqueNormale.setStyleSheet("background-color: rgba(255, 255, 255, 0); border: none;")
        self.AttaqueSpeciale.setStyleSheet("background-color: rgba(255, 255, 255, 0); border: none;")
        self.Pokedex.setStyleSheet("background-color: rgba(255, 255, 255, 0); border: none;")
        self.Fuite.setStyleSheet("background-color: rgba(255, 255, 255, 0); border: none;")


        MainWindow.setCentralWidget(self.centralwidget)

        self.Fuite.clicked.connect(MainWindow.close)

        self.tour_joueur = True  # Variable pour suivre l'état du tour

        # Connectez le signal clicked du bouton à la méthode correspondante
        self.AttaqueNormale.clicked.connect(self.on_attaque_normale_clicked)

    def on_attaque_normale_clicked(self):
        if self.tour_joueur:
            # Action du joueur (par exemple, attaque normale)
            self.poke_sacha.attaquer(self.adversaire)
            self.progressBarEnemy.setValue(self.adversaire.hp)
            if self.adversaire.hp <= 0.25 * self.progressBarEnemy.maximum():
                self.progressBarEnemy.setStyleSheet("""                                                                
                    QProgressBar {
                        border: 2px solid grey;
                        border-radius: 5px;
                        background-color: #FFFFFF; /* Couleur de fond de la barre de progression */
                    }
                        
                    QProgressBar::chunk {
                        background-color: #FF0000; /* Couleur de la barre de progression */
                    }                                
                """)
                
            else:
                self.progressBarEnemy.setStyleSheet("""   
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

            # Mettre à jour le texte de l'étiquette des points de vie de l'adversaire
            self.label_hp_adversaire.setText(str(self.adversaire.hp))
            self.label_hp_adversaire.raise_()


            # Désactivez le bouton pour empêcher les attaques multiples dans le même tour
            self.AttaqueNormale.setEnabled(False)

            # Passez au tour de l'ordinateur
            self.tour_joueur = False

            # Délai avant l'attaque de l'ordinateur (par exemple, 2 secondes)
            QTimer.singleShot(2000, self.attaque_ordinateur)

    def attaque_ordinateur(self):
        # Action de l'ordinateur (à remplacer par votre logique d'attaque de l'ordinateur)
        print("Attaque de l'ordinateur")

        # Après l'attaque de l'ordinateur, réactivez le bouton pour permettre au joueur de jouer au prochain tour
        self.AttaqueNormale.setEnabled(True)

        # Passez au tour du joueur
        self.tour_joueur = True

    def print_ok(self):
        cmp = False
        print("ok")

    def print_spe(self):
        cmp = False
        print("spe")




class FightWindow(QMainWindow, Combat_ui):
    def __init__(self, pokemon_sauvage, sacha, parent=None):
        self.pokemon_sauvage = pokemon_sauvage
        self.sacha = sacha
        cmp = True
        super(FightWindow, self).__init__(parent)
        self.setupUi(self, cmp)
        

# if __name__ == "__main__":
#     def run_app():
#         app = QApplication(sys.argv)
#         mainWin = FightWindow()
#         mainWin.show()
#         app.exec_()
#     run_app()