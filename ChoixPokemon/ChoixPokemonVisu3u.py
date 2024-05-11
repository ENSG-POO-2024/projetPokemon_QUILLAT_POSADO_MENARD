
import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QPushButton, QHBoxLayout, QWidget, QLabel, QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

import Poke as poke
import Combat.CombatVis3u as c


  ###OKKKKKK


class ChoixPokemon_ui(object):

    def setupUi(self, MainWindow):

        # Création de l'objet MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("test")
        MainWindow.resize(1000, 750)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Affichage du fond
        self.label = QLabel(self)
        self.label.setGeometry(0, 0, 1000, 750)  # Position et taille de l'image
        self.pixmap = QPixmap("Image/test.png")
        self.label.setPixmap(self.pixmap)
        self.label.setScaledContents(True)

        # # Créer et positionner les boutons
        # self.bouton_1 = QPushButton("Bouton 1", self)
        # self.bouton_1.setGeometry(100, 100, 100, 50)  # Position (100, 100), taille (100, 50)
        # self.bouton_1.setStyleSheet("background-color: rgba(0, 255, 255, 0.7); border: 2px solid black;")

        
        # self.bouton_2 = QPushButton("Bouton 2", self)
        # self.bouton_2.setGeometry(250, 200, 100, 50)  # Position (250, 200), taille (100, 50)
        # self.bouton_2.setStyleSheet("background-color: rgba(0, 255, 255, 0.7); border: 2px solid black;")


        # self.bouton_1.raise_()
        # self.bouton_2.raise_()

        self.boutons = {} # Pour pouvoir créer plusieurs boutons avec chacun son noms
        self.x = 50  # Position x initiale du premier bouton
        self.y = 50  # Position y initiale du premier bouton
        self.largeur = 100  # Largeur des boutons
        self.hauteur = 100  # Hauteur des boutons

        for nom_poke, pokemon in self.inventaire_joueur.pokedex.items():
            base_name = pokemon.name.split()[0] # Pour gérer le cas avec plusieurs fois le même pokémon
            self.label = QLabel(self)
            self.label.setGeometry(self.x, self.y-10, self.largeur, self.hauteur)  # Position et taille de l'image
            self.pixmap = QPixmap("Pokémons/"+base_name+"/"+base_name+"_face.png")
            self.label.setPixmap(self.pixmap)
            self.label.setScaledContents(True)
            self.creer_bouton(pokemon)

        for nom_bouton, bouton in self.boutons.items():
            bouton.clicked.connect(lambda checked, nom=nom_bouton: MainWindow.close())
            bouton.clicked.connect(lambda checked, nom=nom_bouton: self.open_combat(self.inventaire_joueur.pokedex[nom]))


    def open_combat(self, pokemon_choisi):
        self.fight_window = c.FightWindow(self.pokemon_sauvage, pokemon_choisi, self.pokedex_sauvages, self.inventaire_joueur)
        self.fight_window.show()


    def creer_bouton(self, pokemon):
        self.boutons[pokemon.name] = QPushButton(self)
        self.boutons[pokemon.name].setGeometry(self.x, self.y, self.largeur, self.hauteur)
        self.boutons[pokemon.name].setStyleSheet("background-color: rgba(0, 0, 0, 0); border: 2px solid black;")
        self.label_nom = QtWidgets.QLabel(self)
        self.label_nom.setGeometry(QtCore.QRect(self.x, self.y+33, self.largeur, self.hauteur))
        self.label_nom.setObjectName("label_nom_pokémon")
        self.label_nom.setStyleSheet("color: black; font-size: 16px;")
        self.label_nom.setText(str(pokemon.name))
        self.label_nom.setAlignment(Qt.AlignCenter)  # Centrer le texte dans le QLabel
        self.label_nom.raise_()
        self.boutons[pokemon.name].raise_()

         # Incrémentation de la position x et X
        self.x += 110

        # Si la position x dépasse la largeur de la fenêtre, réinitialisation de x et incrémentation de y
        if self.x >= self.width():
            self.x = 50
            self.y += 120



class ChoixPokemonWindow(QMainWindow, ChoixPokemon_ui):
    def __init__(self, pokemon_sauvage, inventaire_joueur, pokedex_sauvages, parent=None):
        self.pokemon_sauvage = pokemon_sauvage # Le pokémon rencontré
        self.inventaire_joueur = inventaire_joueur # L'inventaire du joueur avec ses pokémons
        self.pokedex_sauvages = pokedex_sauvages # Le pokedex avec tous les pokémons sauvages
        super(ChoixPokemonWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    inventaire = poke.InventaireJoueur()
    inventaire.inventory(poke.Pokemon("Pikachu",15,12,15,12,10,10,10,poke.Eau(),False))
    inventaire.inventory(poke.Pokemon("Bulbizarre",10,10,10,10,10,10,10,poke.Eau(),False))
    inventaire.inventory(poke.Pokemon("Bulbizarre",10,10,10,10,10,10,10,poke.Eau(),False))
    poke_sauvge = poke.Pokemon("Rattata",15,12,15,12,10,10,10,poke.Eau(),False)
    pokedex_sauvages = poke.Pokedex()
    pokedex_sauvages.charger_pokedex('pokemons_a_capturer.csv') # On le remplit avec notre fichier 
    fenetre = ChoixPokemonWindow(poke_sauvge, inventaire, pokedex_sauvages)
    fenetre.setWindowTitle("Exemple de fenêtre avec boutons par-dessus une image de fond")
    fenetre.show()
    sys.exit(app.exec_())
