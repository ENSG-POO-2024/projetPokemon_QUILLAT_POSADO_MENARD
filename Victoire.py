
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPixmap

import Poke as poke

class Victoire_ui(object):
    def setupUi(self, MainWindow):

        self.base_name = self.adversaire.name.split()[0]

        # On crée la fenêtre Victoire
        MainWindow.setWindowTitle("Victoire contre " + self.base_name)
        MainWindow.resize(1000, 750)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        # Création du fond
        self.Back = QtWidgets.QLabel(self.centralwidget)
        self.Back.setGeometry(QtCore.QRect(0, 0, 1000, 750))
        self.Back.setText("")
        self.Back.setPixmap(QtGui.QPixmap("Media/Image/Victoire.png"))
        self.Back.setScaledContents(True)
        self.Back.setObjectName("Back")
        

        # Ajout de la Pokéball ouverte
        self.Pokeball = QtWidgets.QLabel(self.centralwidget)
        self.Pokeball.setGeometry(QtCore.QRect(388, 271, 224, 293))
        self.Pokeball.setText("")
        self.Pokeball.setPixmap(QtGui.QPixmap("Media/Image/PokeballOpen.png"))
        self.Pokeball.setScaledContents(False)
        self.Pokeball.setObjectName("Pokeball")

        # Ajout du pokémon capturé
        self.capture = QtWidgets.QLabel(self.centralwidget)
        self.capture.setGeometry(QtCore.QRect(390, 300, 231, 241))
        self.capture.setPixmap(QtGui.QPixmap("Pokemons/"+self.base_name+"/"+self.base_name+"_face.png"))
        self.capture.setScaledContents(True)
        self.capture.setObjectName("Pokémon capturé")

        # Création du bouton pour partir 
        self.PartirButton = QtWidgets.QPushButton(self.centralwidget)
        self.PartirButton.setGeometry(QtCore.QRect(250, 675, 495, 40))
        self.PartirButton.setObjectName("PartirButton")

        
        MainWindow.setCentralWidget(self.centralwidget)

        # On rend les boutons invisibles
        self.PartirButton.setStyleSheet("background-color: rgba(255, 255, 255, 0); border: none;")



        self.Pokeball.enterEvent = self.enter_image
        self.Pokeball.leaveEvent = self.leave_image
        self.capture.enterEvent = self.enter_image
        self.capture.leaveEvent = self.leave_image
        self.Pokeball.mousePressEvent = self.click_image 

        self.PartirButton.clicked.connect(self.quitte_sans_pokemon)

    
    
    def enter_image(self, event):
        self.Pokeball.setPixmap(QPixmap("Media/Image/PokeballClosed.png"))
        self.capture.setPixmap(QPixmap(""))

    def leave_image(self, event):
        self.Pokeball.setPixmap(QPixmap("Media/Image/PokeballOpen.png"))
        self.capture.setPixmap(QPixmap("Pokemons/"+self.base_name+"/"+self.base_name+"_face.png"))

    def click_image(self, event):
        self.inventaire_joueur.capturer_pokemon(self.adversaire, self.pokedex_sauvages, self.pokedex)
        for nom_poke, pokemon in self.inventaire_joueur.pokedex.items():
            pokemon.hp = self.pokedex.pokedex[pokemon.name.split()[0]].hp
        self.close()

    def quitte_sans_pokemon(self):
        for nom_poke, pokemon in self.inventaire_joueur.pokedex.items():
            pokemon.hp = self.pokedex.pokedex[pokemon.name.split()[0]].hp
        self.adversaire.hp = self.pokedex.pokedex[self.adversaire.name.split()[0]].hp
        self.close()

    def mousePressEvent(self, event):
        """
        Fonction qui permet de gérer l'évenement: clic gauche
        """
        # On récupère les coordonnées du clic de la souris
        mouse_x = event.x()
        mouse_y = event.y()

        if self.clic(mouse_x, mouse_y, 388, 612, 271, 564): 
            for nom_poke, pokemon in self.inventaire_joueur.pokedex.items():
                pokemon.hp = self.pokedex.pokedex[pokemon.name.split()[0]].hp
            self.inventaire_joueur.capturer_pokemon(self.adversaire, self.pokedex_sauvages, self.pokedex)
            self.close() 

    def clic(self, x, y, x_inf, x_sup, y_inf, y_sup):
        """
        Fonction qui teste si le clic est dans la zone entre x_inf et x_sup et entre y_inf et y_sup
        """
        if x_inf <= x <= x_sup and y_inf <= y <= y_sup:
            return True


   


class Victoire(QMainWindow, Victoire_ui):
    def __init__(self, adversaire, pokedex_sauvages, inventaire_joueur, pokemon_utilise, pokedex, parent=None):
        self.adversaire = adversaire
        self.pokedex_sauvages = pokedex_sauvages
        self.inventaire_joueur = inventaire_joueur
        self.pokemon_utilise = pokemon_utilise
        self.pokedex = pokedex
        super(Victoire, self).__init__(parent)
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
        victoire = Victoire(adversaire, pokedex_sauvages, inventaire, pokemon_utilise, pokedex)
        victoire.show()
        app.exec_()
    run_app()