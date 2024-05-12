import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QPushButton, QHBoxLayout, QWidget, QLabel, QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import Poke as poke


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

        self.pokemon = list(self.inventaire_joueur.pokedex.values())[0]
        self.poke2 = poke.Pokemon("bulbi",10,10,10,10,10,10,10,poke.Eau(),False)
        self.boutons = {} # Pour pouvoir créer plusieurs boutons avec chacun son noms
        self.x = 50  # Position x initiale du premier bouton
        self.y = 50  # Position y initiale du premier bouton
        self.largeur = 100  # Largeur des boutons
        self.hauteur = 50  # Hauteur des boutons

        self.creer_bouton(self.pokemon)
        self.creer_bouton(self.poke2)

        for nom_bouton, bouton in self.boutons.items():
            bouton.clicked.connect(lambda checked, nom=nom_bouton: self.afficher_message(nom))


    def afficher_message(self, nom_bouton):
        print(f"Vous avez cliqué sur {nom_bouton}")


    def creer_bouton(self, pokemon):
        self.boutons[pokemon.name] = QPushButton(pokemon.name, self)
        self.boutons[pokemon.name].setGeometry(self.x, self.y, self.largeur, self.hauteur)
        self.boutons[pokemon.name].setStyleSheet("background-color: rgba(0, 255, 255, 0.7); border: 2px solid black;")
        self.boutons[pokemon.name].raise_()
         # Incrémentation de la position x
        self.x += 200

        # Si la position x dépasse la largeur de la fenêtre, réinitialisation de x et incrémentation de y
        if self.x >= self.width():
            self.x = 0
            self.y += 200



class ChoixPokemonWindow(QMainWindow, ChoixPokemon_ui):
    def __init__(self, inventaire_joueur, parent=None):
        self.inventaire_joueur = inventaire_joueur
        super(ChoixPokemonWindow, self).__init__(parent)
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    inventaire = poke.InventaireJoueur()
    inventaire.inventory(poke.Pokemon("pika",10,10,10,10,10,10,10,poke.Eau(),False))
    fenetre = ChoixPokemonWindow(inventaire)
    fenetre.setWindowTitle("Exemple de fenêtre avec boutons par-dessus une image de fond")
    fenetre.show()
    sys.exit(app.exec_())
