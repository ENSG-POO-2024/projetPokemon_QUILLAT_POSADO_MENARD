
import sys
import numpy as np
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtCore import Qt, pyqtSignal, QRect
import Poke as poke
from dresseur import Dresseur

class RencontreWindow(QWidget):
    closed = pyqtSignal()  # Signal pour indiquer que la fenêtre a été fermée

    def __init__(self):
        super().__init__()

        self.setGeometry(300, 100, 1000, 750)
        self.setWindowTitle("Pokemon sauvage rencontré")

        label = QLabel(self)
        pixmap = QPixmap("test.png")
        label.setPixmap(pixmap)
        label.setAlignment(Qt.AlignCenter)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:  # Vérifie si le clic est le bouton gauche de la souris
            if self.is_in_specific_zone(event.pos()):  # Vérifie si le clic est dans la zone spécifique
                self.close()  # Ferme la fenêtre
                self.closed.emit()  # Émet le signal de fermeture
                self.open_combat_window()  # Ouvre la fenêtre de combat

    def is_in_specific_zone(self, pos):
        # Définissez ici les coordonnées de la zone spécifique
        # Par exemple, la zone centrée dans la fenêtre avec une taille de 100x100
        zone_rect = QRect(0, 0, 100, 100)
        return zone_rect.contains(pos)

    def open_combat_window(self):
        self.combat_window = CombatWindow()
        self.combat_window.show()

class CombatWindow(QWidget):
    closed = pyqtSignal()  # Signal pour indiquer que la fenêtre a été fermée

    def __init__(self):
        super().__init__()

        self.setGeometry(300, 100, 1000, 750)
        self.setWindowTitle("Combat")

        label = QLabel(self)
        pixmap = QPixmap("combat.png")
        label.setPixmap(pixmap)
        label.setAlignment(Qt.AlignCenter)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:  # Vérifie si le clic est le bouton gauche de la souris
            if self.is_in_specific_zone(event.pos()):  # Vérifie si le clic est dans la zone spécifique
                self.close()  # Ferme la fenêtre
                self.closed.emit()  # Émet le signal de fermeture

    def is_in_specific_zone(self, pos):
        # Définissez ici les coordonnées de la zone spécifique
        # Par exemple, la zone centrée dans la fenêtre avec une taille de 100x100
        zone_rect = QRect(0, 0, 100, 100)
        return zone_rect.contains(pos)

class Game(QWidget):
    def __init__(self, sacha, sauvages_csv):
        super().__init__()

        self.ecran_largeur = 880 
        self.ecran_hauteur = 880 
        self.map_largeur = 4950 
        self.map_hauteur = 4950 
        
        self.background_image = QPixmap("fond2.png")  
        self.background_position_x = 0 
        self.background_position_y = 0 

        self.setGeometry(800, 0, self.ecran_largeur, self.ecran_hauteur) 

        self.sauvages = poke.Pokedex()
        self.sauvages.charger_pokedex(sauvages_csv)
        self.sauvages.afficher_pokedex()

        self.dresseur_pos = self.ecran_largeur//2 
        self.dresseur = Dresseur(self.dresseur_pos, self.dresseur_pos, self.dresseur_pos, self.dresseur_pos, sacha)
        self.nb_bloc = (self.ecran_hauteur//2) // self.dresseur.speed
        self.image_dresseur = QPixmap("utilisateur.png") 

        self.pokemon_window = None  # Référence à la fenêtre RencontreWindow
        self.combat_window = None   # Référence à la fenêtre CombatWindow

        self.check_for_wild_pokemon()  # Vérifie dès le début s'il y a un Pokémon sauvage

    def keyPressEvent(self, event):
        if self.pokemon_window or self.combat_window:  # Si l'une des fenêtres est ouverte, retourne sans traiter l'événement de la touche
            return

        bord_droit = self.map_largeur - self.ecran_largeur - self.dresseur.speed
        bord_gauche = 0
        bord_haut = 0
        bord_bas = self.map_hauteur - self.ecran_hauteur - self.dresseur.speed

        if event.key() == Qt.Key_Right and -self.background_position_x <= bord_droit and np.abs(self.dresseur.X) >= (self.nb_bloc * self.dresseur.speed):
            self.background_position_x -= self.dresseur.speed
            for nom_pokemon, pokemon in self.sauvages.pokedex.items():
                pokemon.x -= self.dresseur.speed

        elif event.key() == Qt.Key_Left and -self.background_position_x > bord_gauche and np.abs(self.dresseur.X) <= (self.map_largeur - self.nb_bloc * self.dresseur.speed):
            self.background_position_x += self.dresseur.speed
            for nom_pokemon, pokemon in self.sauvages.pokedex.items():
                pokemon.x += self.dresseur.speed

        elif event.key() == Qt.Key_Down and -self.background_position_y <= bord_bas and np.abs(self.dresseur.Y) >= (self.nb_bloc * self.dresseur.speed):
            self.background_position_y -= self.dresseur.speed
            for nom_pokemon, pokemon in self.sauvages.pokedex.items():
                pokemon.y -= self.dresseur.speed

        elif event.key() == Qt.Key_Up and -self.background_position_y > bord_haut and np.abs(self.dresseur.Y) <= (self.map_hauteur - self.nb_bloc * self.dresseur.speed):
            self.background_position_y += self.dresseur.speed
            for nom_pokemon, pokemon in self.sauvages.pokedex.items():
                pokemon.y += self.dresseur.speed

        self.check_for_wild_pokemon()  # Vérifie s'il y a un Pokémon sauvage après chaque déplacement
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.background_position_x, self.background_position_y, self.background_image) 
        painter.drawPixmap(self.dresseur.x, self.dresseur.y, self.image_dresseur) 
        script_dir = os.path.dirname(__file__)
        for cle_pokemons, poke_sauvage in self.sauvages.pokedex.items():
            image_path = os.path.join(script_dir, "Pokémons/"+poke_sauvage.name, poke_sauvage.name + "_face.png")
            pixmap = QPixmap(image_path)
            painter.drawPixmap(poke_sauvage.x, poke_sauvage.y, pixmap)  

    def show_pokemon_window(self):
        self.pokemon_window = RencontreWindow()
        self.pokemon_window.show()
        self.pokemon_window.closed.connect(self.on_pokemon_window_closed)

    def show_combat_window(self):
        self.combat_window = CombatWindow()
        self.combat_window.show()
        self.combat_window.closed.connect(self.on_combat_window_closed)

    def on_pokemon_window_closed(self):
        self.pokemon_window = None

    def on_combat_window_closed(self):
        self.combat_window = None

    def check_for_wild_pokemon(self):
        sauvage = self.dresseur.proche(self.sauvages)[0]
        if sauvage:
            self.show_pokemon_window()  # Affiche la fenêtre avec l'image du Pokemon sauvage
            # Pour afficher la fenêtre de combat, remplacez show_pokemon_window() par show_combat_window()

if __name__ == "__main__":
    app = QApplication(sys.argv) 

    poke_sauvages = "pokemons_a_capturer.csv"
    magicarpe = poke.Pokemon.creer_pokemon("Magicarpe", 550, 550, 50, 20, 10, 35, 15, poke.Eau(), False)
    sacha = poke.InventaireJoueur()
    sacha.inventory(magicarpe)
    
    game = Game(sacha, poke_sauvages)
    game.show()

    sys.exit(app.exec_())
