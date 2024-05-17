
import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

import Poke as poke
import ChoixPokemon as ch


class RencontreRocket_ui(object):

    def setupUi(self, MainWindow):

        #self.pokemon_utilise = list(self.inventaire_joueur.pokedex.values())[0]
        self.adversaire = poke.Pokemon("Mewtwo",0,0,106,110,90,154,90,poke.Psy())

        self.pokedex = poke.Pokedex()
        self.pokedex.charger_pokedex("pokemon_first_gen.csv")

        self.inventaire_joueur = poke.InventaireJoueur()
        self.inventaire_joueur.ajout_inventaire(poke.Pokemon("Mew",0,0,100,100,100,100,100,poke.Psy()))
        self.inventaire_joueur.ajout_inventaire(poke.Pokemon("Dracaufeu",15,12,78,84,78,109,85,poke.Feu()))
        self.inventaire_joueur.ajout_inventaire(poke.Pokemon("Ectoplasma",0,0,60,65,60,130,75, poke.Tenebres()))


        self.pokedex_sauvages = poke.Pokedex()
        self.pokedex_sauvages.charger_pokedex("pokemon_first_gen.csv")

        # Création de l'objet MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("Rencontre avec " + self.adversaire.name.split()[0])
        MainWindow.resize(1000, 750)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Création de l'arrière plan
        self.Fond = QtWidgets.QLabel(self.centralwidget)
        self.Fond.setGeometry(QtCore.QRect(0, 0, 1000, 750))
        self.Fond.setText("")
        self.Fond.setPixmap(QtGui.QPixmap("Media/Image/rocket.png"))
        self.Fond.setScaledContents(True)
        self.Fond.setObjectName("Fond")

       

        # Affichage du pokemon rencontré
        self.label_poke = QtWidgets.QLabel(self.centralwidget)
        self.label_poke.setAlignment(Qt.AlignCenter)
        self.label_poke.setGeometry(QtCore.QRect(45, 200, 1000, 270))
        self.label_poke.setText("")
        self.gif_poke = QtGui.QMovie("Pokemons/"+self.adversaire.name.split()[0]+"/"+self.adversaire.name.split()[0]+"_face.gif")
        self.gif_poke.setScaledSize(QtCore.QSize(250, 250))
        self.label_poke.setMovie(self.gif_poke)
        self.gif_poke.start()
        self.label_poke.setObjectName("Pokemon rencontré")
        self.label_text = QLabel(self.adversaire.name.split()[0], self)
        self.label_text.setAlignment(Qt.AlignCenter)
        self.label_text.setGeometry(0, 500, 1000, 55)
        self.font = QFont("Minecraft", 50)  
        self.label_text.setFont(self.font)
        self.label_text.setStyleSheet("color: white;")  


        # Bouton pour combattre
        self.fight_buton = QtWidgets.QPushButton(self.centralwidget)
        self.fight_buton.setGeometry(QtCore.QRect(105, 587, 365, 77))
        self.fight_buton.setText("")
        self.fight_buton.setObjectName("Fuite")

        # Bouton pour fuir
        self.fuite = QtWidgets.QPushButton(self.centralwidget)
        self.fuite.setGeometry(QtCore.QRect(530, 587, 365, 77))
        self.fuite.setText("")
        self.fuite.setObjectName("Fuite")

        # On met tout en avant (dans le bon ordre) pour que les objets soient au premier plan 
        self.Fond.raise_()
        self.label_poke.raise_()
        self.fuite.raise_()
        self.fight_buton.raise_()

        # On rend les boutons invisibles
        self.fight_buton.setStyleSheet("background-color: rgba(255, 255, 255, 0); border: none;")
        self.fuite.setStyleSheet("background-color: rgba(255, 255, 255, 0); border: none;")

        MainWindow.setCentralWidget(self.centralwidget)

        self.fuite.clicked.connect(MainWindow.close)
        self.fight_buton.clicked.connect(MainWindow.close)
        self.fight_buton.clicked.connect(self.open_choix_pokemon)

    def open_choix_pokemon(self):
        self.choix = ch.ChoixPokemon(self.adversaire, self.inventaire_joueur, self.pokedex_sauvages, False, True)
        self.choix.show()



class RencontreRocket(QMainWindow, RencontreRocket_ui):
    def __init__(self, parent=None):
        self.adversaire = poke.Pokemon("Mewtwo",0,0,106,110,90,154,90,poke.Psy())

        self.inventaire_joueur = poke.InventaireJoueur()
        self.inventaire_joueur.ajout_inventaire(poke.Pokemon("Mew",0,0,100,100,100,100,100,poke.Psy()))
        self.inventaire_joueur.ajout_inventaire(poke.Pokemon("Dracaufeu",15,12,78,84,78,109,85,poke.Feu()))
        self.inventaire_joueur.ajout_inventaire(poke.Pokemon("Ectoplasma",0,0,60,65,60,130,75, poke.Tenebres()))


        self.pokedex_sauvages = poke.Pokedex()
        self.pokedex_sauvages.charger_pokedex("pokemon_first_gen.csv")
        super(RencontreRocket, self).__init__(parent)
        self.setupUi(self)


if __name__ == "__main__":
    def run_app():
        app = QApplication(sys.argv)
        rocket = RencontreRocket()
        rocket.show()
        app.exec_()
    run_app()