
import sys
import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QLabel, QMainWindow, QVBoxLayout, QScrollArea, QGridLayout
from PyQt5.QtGui import QPixmap


current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

import Poke as poke
import Combat as c
import TeamRocket as t



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
        if self.rocket:
            self.pixmap = QPixmap("Media/Image/pokedex_rocket.png")
        else:
            self.pixmap = QPixmap("Media/Image/pokedex.png") 
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
            if pokemon.hp > 0:
                self.creer_bouton(pokemon)
            

        for nom_bouton, bouton in self.boutons.items():
            bouton.clicked.connect(lambda checked, nom=nom_bouton: MainWindow.close())
            if self.clic_pokedex:
                if self.rocket:
                    bouton.clicked.connect(lambda checked, nom=nom_bouton: self.open_rocket(self.inventaire_joueur.pokedex[nom]))
                else:
                    bouton.clicked.connect(lambda checked, nom=nom_bouton: self.open_combat(self.inventaire_joueur.pokedex[nom]))
            else:
                if self.rocket:
                    bouton.clicked.connect(lambda checked, nom=nom_bouton: self.open_first_rocket(self.inventaire_joueur.pokedex[nom]))
                else:
                    bouton.clicked.connect(lambda checked, nom=nom_bouton: self.open_first_combat(self.inventaire_joueur.pokedex[nom]))


    def open_combat(self, pokemon_choisi):
        self.fight_window = c.Fight(self.pokemon_sauvage, pokemon_choisi, self.pokedex_sauvages, self.inventaire_joueur, False)
        self.fight_window.AttaqueNormale.setEnabled(False)
        self.fight_window.AttaqueSpeciale.setEnabled(False)
        self.fight_window.Fuite.setEnabled(False)
        self.fight_window.Pokedex.setEnabled(False)
        self.fight_window.show()

    def open_first_combat(self, pokemon_choisi):
        self.fight_window = c.Fight(self.pokemon_sauvage, pokemon_choisi, self.pokedex_sauvages, self.inventaire_joueur, True)
        self.fight_window.show()

    def open_first_rocket(self, pokemon_choisi):
        self.rocket_window = t.Rocket(self.pokemon_sauvage, pokemon_choisi, self.pokedex_sauvages, self.inventaire_joueur, True)
        self.rocket_window.show()

    def open_rocket(self, pokemon_choisi):
        self.rocket_window = t.Rocket(self.pokemon_sauvage, pokemon_choisi, self.pokedex_sauvages, self.inventaire_joueur, False)        
        self.rocket_window.AttaqueNormale.setEnabled(False)
        self.rocket_window.AttaqueSpeciale.setEnabled(False)
        self.rocket_window.Fuite.setEnabled(False)
        self.rocket_window.Pokedex.setEnabled(False)
        self.rocket_window.show()


    def creer_bouton(self, pokemon):
        self.boutons[pokemon.name] = QPushButton()
        self.boutons[pokemon.name].setFixedSize(self.largeur, self.hauteur)


        chemin = "Pokemons/" + pokemon.name.split()[0] + "/" + pokemon.name.split()[0] + "_face.png"
        style = "border-image : url(" + chemin + ");"
        self.boutons[pokemon.name].setStyleSheet(style)

        #self.boutons[pokemon.name].setStyleSheet("background-color: rgba(0, 0, 0, 0); border: 2px solid black;")
        

        self.nb_bouton = 3 # Bouton par ligne
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





class ChoixPokemon(QMainWindow, ChoixPokemon_ui):

    def __init__(self, pokemon_sauvage, inventaire_joueur, pokedex_sauvages, clic_pokedex, rocket, parent=None):
        self.pokemon_sauvage = pokemon_sauvage # Le pokémon rencontré
        self.inventaire_joueur = inventaire_joueur # L'inventaire du joueur avec ses pokémons
        self.pokedex_sauvages = pokedex_sauvages # Le pokedex avec tous les pokémons sauvages
        self.clic_pokedex = clic_pokedex
        self.rocket = rocket
        super(ChoixPokemon, self).__init__(parent)
        self.setupUi(self)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    inventaire = poke.Pokedex()
    inventaire.charger_pokedex('pokemon_first_gen.csv')
    poke_sauvage = poke.Pokemon("Rattata",15,12,30,56,35,25,35,poke.Normal())
    pokedex_sauvages = poke.Pokedex()
    pokedex_sauvages.charger_pokedex('pokemons_a_capturer.csv') # On le remplit avec notre fichier 
    fenetre = ChoixPokemon(poke_sauvage, inventaire, pokedex_sauvages, False, False)
    fenetre.setWindowTitle("Exemple de fenêtre d'inventaire")
    fenetre.show()
    sys.exit(app.exec_())
