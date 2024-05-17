
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication

import Poke as poke


class Defaite_ui(object):
    
    def setupUi(self, MainWindow):

        # Création de la fenêtre
        MainWindow.setWindowTitle("Défaite")
        MainWindow.resize(1000, 750)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Création de l'arrière plan
        self.Back = QtWidgets.QLabel(self.centralwidget)
        self.Back.setGeometry(QtCore.QRect(0, 0, 1001, 751))
        self.Back.setText("")
        self.Back.setPixmap(QtGui.QPixmap("Media/Image/Defaite.png"))
        self.Back.setScaledContents(False)
        self.Back.setObjectName("Back")

        # Création du bouton pour sortir de la fenêtre
        self.Sortir = QtWidgets.QPushButton(self.centralwidget)
        self.Sortir.setGeometry(QtCore.QRect(390, 520, 221, 41))
        self.Sortir.setText("")
        self.Sortir.setObjectName("Sortir")


        MainWindow.setCentralWidget(self.centralwidget)

        for nom_poke, pokemon in self.inventaire_joueur.pokedex.items():
                pokemon.hp = self.pokedex.pokedex[pokemon.name.split()[0]].hp
        self.adversaire.hp = self.pokedex.pokedex[self.adversaire.name.split()[0]].hp

        # On rend le (ou les) boutons invisibles
        self.Sortir.setStyleSheet("background-color: rgba(255, 255, 255, 0); border: none;")

        self.Sortir.clicked.connect(MainWindow.close)




class Defaite(QMainWindow, Defaite_ui):
    def __init__(self, adversaire, pokedex_sauvages, inventaire_joueur, pokemon_utilise, pokedex, parent=None):
        self.adversaire = adversaire
        self.pokedex_sauvages = pokedex_sauvages
        self.inventaire_joueur = inventaire_joueur
        self.pokemon_utilise = pokemon_utilise
        self.pokedex = pokedex
        super(Defaite, self).__init__(parent)
        self.setupUi(self)


if __name__ == "__main__":
    def run_app():
        app = QApplication(sys.argv)
        adversaire = poke.Pokemon("Electhor",15,12,90,90,85,125,90,poke.Electrik())
        pokemon_utilise = poke.Pokemon("Dracaufeu",15,12,78,84,78,109,85,poke.Feu())
        inventaire = poke.InventaireJoueur()
        inventaire.ajout_inventaire(pokemon_utilise)
        pokedex_sauvages = poke.Pokedex()
        pokedex_sauvages.charger_pokedex('pokemon_first_gen.csv') # On le remplit avec notre fichier 
        pokedex = poke.Pokedex()
        pokedex.charger_pokedex('pokemon_first_gen.csv')
        defaite = Defaite(adversaire, pokedex_sauvages, inventaire, pokemon_utilise, pokedex)
        defaite.show()
        app.exec_()
    run_app()