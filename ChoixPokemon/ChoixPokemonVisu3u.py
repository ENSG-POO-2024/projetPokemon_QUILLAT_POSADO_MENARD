
import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QPushButton, QHBoxLayout, QWidget, QLabel, QMainWindow, QVBoxLayout, QScrollArea, QGridLayout, QStackedWidget
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt, QSize, QPoint

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
        MainWindow.setWindowTitle("Pokedex Joueur")
        MainWindow.resize(1000, 750)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Affichage du fond
        self.label = QLabel(self)
        self.label.setGeometry(0, 0, 1000, 750)  # Position et taille de l'image
        self.pixmap = QPixmap("Image/pokedex.png")
        self.label.setPixmap(self.pixmap)
        self.label.setScaledContents(True)

        # Créer un widget central
        self.menu_widget = QWidget(self)
        self.setCentralWidget(self.menu_widget)

        # Créer un layout vertical
        self.menu_layout = QVBoxLayout(self.menu_widget)

        # Créer une QScrollArea
        self.scroll_area = QScrollArea()
        self.scroll_area.setGeometry(75,0, 850, 750)
        self.scroll_area.setWidgetResizable(True)  # Permettre à la zone de défilement de redimensionner son contenu
        self.scroll_area.setStyleSheet("background-color: rgba(0, 0, 0, 0);")

        # Créer un widget pour contenir les boutons
        self.button_widget = QWidget(self.scroll_area)
        self.button_layout = QGridLayout(self.button_widget)
        self.button_widget.setLayout(self.button_layout)


        self.boutons = {} # Pour pouvoir créer plusieurs boutons avec chacun son noms
        self.x = 65  # Position x initiale du premier bouton
        self.y = 50  # Position y initiale du premier bouton
        self.X = 0
        self.Y = 0
        self.i = 0
        self.largeur = 300  # Largeur des boutons
        self.hauteur = 300  # Hauteur des boutons

        for nom_poke, pokemon in self.inventaire_joueur.pokedex.items():
            # base_name = pokemon.name.split()[0] # Pour gérer le cas avec plusieurs fois le même pokémon
            # self.label = QLabel(self)
            # self.label.setGeometry(self.x, self.y-10, self.largeur, self.hauteur)  # Position et taille de l'image
            # self.pixmap = QPixmap("Pokémons/"+base_name+"/"+base_name+"_face.png")
            # self.label.setPixmap(self.pixmap)
            # self.label.setScaledContents(True)
            self.creer_bouton(pokemon)
            

        for nom_bouton, bouton in self.boutons.items():
            bouton.clicked.connect(lambda checked, nom=nom_bouton: MainWindow.close())
            bouton.clicked.connect(lambda checked, nom=nom_bouton: self.open_combat(self.inventaire_joueur.pokedex[nom]))



    def open_combat(self, pokemon_choisi):
        self.fight_window = c.FightWindow(self.pokemon_sauvage, pokemon_choisi, self.pokedex_sauvages, self.inventaire_joueur, self.tour_joueur, self.tour_depuis_attaque_joueur)
        self.fight_window.show()


    def creer_bouton(self, pokemon):
        self.boutons[pokemon.name] = QPushButton()
        self.boutons[pokemon.name].setFixedSize(self.largeur, self.hauteur)


        chemin = "Pokemons/" + pokemon.name.split()[0] + "/" + pokemon.name.split()[0] + "_face.png"
        style = "border-image : url(" + chemin + ");"
        self.boutons[pokemon.name].setStyleSheet(style)

        #self.boutons[pokemon.name].setStyleSheet("background-color: rgba(0, 0, 0, 0); border: 2px solid black;")
        

        self.nb_bouton = 3
        self.button_layout.addWidget(self.boutons[pokemon.name], self.i // self.nb_bouton, self.i % self.nb_bouton)

        self.boutons[pokemon.name].raise_()
        #self.boutons[pokemon.name].setToolTip(pokemon.name)

        

        # Incrémentation de la position x 
        self.x += self.largeur + 10
        self.i += 1

        # Si la position x dépasse la largeur de la fenêtre, réinitialisation de x et incrémentation de y
        if self.x >= self.width()-65:
            self.x = 65
            self.y += self.hauteur + 20

        # Définir le widget contenu de la QScrollArea
        self.scroll_area.setWidget(self.button_widget)

        # Ajouter la QScrollArea au layout principal
        self.menu_layout.addWidget(self.scroll_area)

    # def obtenir_coordonnees_boutons(self):
    #     for nom_bouton, bouton in self.boutons.items():
    #         pos_globale = bouton.mapToGlobal(bouton.pos())
    #         x = pos_globale.x()
    #         y = pos_globale.y()
    #         print(f"Coordonnées du bouton {nom_bouton} : x = {x}, y = {y}")




class ChoixPokemonWindow(QMainWindow, ChoixPokemon_ui):
    def __init__(self, pokemon_sauvage, inventaire_joueur, pokedex_sauvages, tour_joueur, tour_depuis_attaque_joueur, parent=None):
        self.pokemon_sauvage = pokemon_sauvage # Le pokémon rencontré
        self.inventaire_joueur = inventaire_joueur # L'inventaire du joueur avec ses pokémons
        self.pokedex_sauvages = pokedex_sauvages # Le pokedex avec tous les pokémons sauvages
        self.tour_joueur = tour_joueur
        self.tour_depuis_attaque_joueur = tour_depuis_attaque_joueur
        super(ChoixPokemonWindow, self).__init__(parent)
        self.setupUi(self)
        
    # def showEvent(self, event):
    #     super().showEvent(event)
    #     self.obtenir_coordonnees_boutons()  # Appel de la fonction pour obtenir les coordonnées des boutons après affichage



if __name__ == "__main__":
    app = QApplication(sys.argv)
    inventaire = poke.InventaireJoueur()
    inventaire.inventory(poke.Pokemon("Pikachu",15,12,15,12,10,10,10,poke.Eau(),False))
    inventaire.inventory(poke.Pokemon("Salameche",10,10,10,10,10,10,10,poke.Eau(),False))
    inventaire.inventory(poke.Pokemon("Salameche",10,10,10,10,10,10,10,poke.Eau(),False))
    inventaire.inventory(poke.Pokemon("Salameche",10,10,10,10,10,10,10,poke.Eau(),False))
    inventaire.inventory(poke.Pokemon("Salameche",10,10,10,10,10,10,10,poke.Eau(),False))
    inventaire.inventory(poke.Pokemon("Salameche",10,10,10,10,10,10,10,poke.Eau(),False))
    inventaire.inventory(poke.Pokemon("Salameche",10,10,10,10,10,10,10,poke.Eau(),False))
    inventaire.inventory(poke.Pokemon("Salameche",10,10,10,10,10,10,10,poke.Eau(),False))
    inventaire.inventory(poke.Pokemon("Salameche",10,10,10,10,10,10,10,poke.Eau(),False))
    inventaire.inventory(poke.Pokemon("Salameche",10,10,10,10,10,10,10,poke.Eau(),False))
    inventaire.inventory(poke.Pokemon("Salameche",10,10,10,10,10,10,10,poke.Eau(),False))
    inventaire.inventory(poke.Pokemon("Salameche",10,10,10,10,10,10,10,poke.Eau(),False))
    inventaire.inventory(poke.Pokemon("Salameche",10,10,10,10,10,10,10,poke.Eau(),False))
    inventaire.inventory(poke.Pokemon("Salameche",10,10,10,10,10,10,10,poke.Eau(),False))
    inventaire.inventory(poke.Pokemon("Salameche",10,10,10,10,10,10,10,poke.Eau(),False))
    inventaire.inventory(poke.Pokemon("Salameche",10,10,10,10,10,10,10,poke.Eau(),False))
    inventaire.inventory(poke.Pokemon("Salameche",10,10,10,10,10,10,10,poke.Eau(),False))
    inventaire.inventory(poke.Pokemon("Salameche",10,10,10,10,10,10,10,poke.Eau(),False))
    inventaire.inventory(poke.Pokemon("Salameche",10,10,10,10,10,10,10,poke.Eau(),False))
    inventaire.inventory(poke.Pokemon("Salameche",10,10,10,10,10,10,10,poke.Eau(),False))
    inventaire.inventory(poke.Pokemon("Salameche",10,10,10,10,10,10,10,poke.Eau(),False))
    inventaire.inventory(poke.Pokemon("Salameche",10,10,10,10,10,10,10,poke.Eau(),False))
    inventaire.inventory(poke.Pokemon("Salameche",10,10,10,10,10,10,10,poke.Eau(),False))
    inventaire.inventory(poke.Pokemon("Salameche",10,10,10,10,10,10,10,poke.Eau(),False))
    inventaire.inventory(poke.Pokemon("Salameche",10,10,10,10,10,10,10,poke.Eau(),False))
    poke_sauvge = poke.Pokemon("Rattata",15,12,15,12,10,10,10,poke.Eau(),False)
    pokedex_sauvages = poke.Pokedex()
    pokedex_sauvages.charger_pokedex('pokemons_a_capturer.csv') # On le remplit avec notre fichier 
    fenetre = ChoixPokemonWindow(poke_sauvge, inventaire, pokedex_sauvages)
    fenetre.setWindowTitle("Exemple de fenêtre avec boutons par-dessus une image de fond")
    fenetre.show()
    sys.exit(app.exec_())
