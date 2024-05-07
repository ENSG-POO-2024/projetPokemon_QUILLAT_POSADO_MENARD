

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtCore import Qt
from dresseur import Dresseur, Pokemon


class Game(QWidget):
    def __init__(self, starter, pokemons_sauvages, img_pokemons_sauvages, map):
        super().__init__()
        self.ecran_largeur = 800 # On fixe la largeur de notre fenêtre (celle dans laquelle se déplace le joueur)
        self.ecran_hauteur = 800 # On fixe sa hauteur
        self.map_largeur = 9600 # On fixe la largeur de la map (le terrain de jeu maximal du joueur)
        self.map_hauteur = 9600 # On fixe sa hauteur
        # Charger une image de fond
        self.background_image = QPixmap(map)  # On charge l'image map
        self.background_position_x = 0 # On place le coin haut gauche de notre background en X de notre fenêtre
        self.background_position_y = 0 # Pareil en Y

        self.setGeometry(800,0, self.ecran_largeur, self.ecran_hauteur) # Place la fenêtre à un endroit sur l'écran du joueur
        self.dresseur = Dresseur(self.ecran_largeur//2, self.ecran_hauteur//2, self.ecran_largeur//2, self.ecran_hauteur//2, [starter])
        self.pokemons_sauvages = pokemons_sauvages

        self.combat = False
        self.id_pok_rencontre = -1

        self.image_dresseur = QPixmap("utilisateur.png") # On charge l'image du dresseur
        self.image_dresseur = self.image_dresseur.scaled(self.ecran_largeur // 10, self.ecran_hauteur // 10)
        self.img_pokemons_sauvages = img_pokemons_sauvages


    def keyPressEvent(self, event):
        # Déterminer la direction du mouvement demandé
        key = event.key()
        dx, dy = 0, 0
        if key == Qt.Key_Left:
            dx = -self.dresseur.speed
        elif key == Qt.Key_Right:
            dx = self.dresseur.speed
        elif key == Qt.Key_Up:
            dy = -self.dresseur.speed
        elif key == Qt.Key_Down:
            dy = self.dresseur.speed

        # Calculer la nouvelle position de l'utilisateur
        new_x = self.dresseur.X + dx
        new_y = self.dresseur.Y + dy

        # Déplacer le fond si nécessaire
        if new_x < 0 or new_x > self.map_largeur:
            self.background_position_x -= dx
            new_x = self.dresseur.x  # Ne pas déplacer l'utilisateur horizontalement
        if new_y < 0 or new_y > self.map_hauteur:
            self.background_position_y -= dy
            new_y = self.dresseur.y  # Ne pas déplacer l'utilisateur verticalement

        # Mettre à jour la position de l'utilisateur
        
        self.update()



    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.background_position_x, self.background_position_y, self.background_image) # On dessine l'image "background_image"
        print(f"back X: {self.background_position_x} back Y: {self.background_position_y}")
        painter.drawPixmap(self.dresseur.x, self.dresseur.y, self.image_dresseur) # On dessine l'image "image_dresseur"
        print(f"dresseur X: {self.dresseur.X} dresseur Y: {self.dresseur.Y}")
        print(f"dresseur x: {self.dresseur.x} dresseur y: {self.dresseur.y}")
        if self.combat:
            id_pk_rencontre = self.id_pok_rencontre
            painter.drawPixmap(self.pokemons_sauvages[id_pk_rencontre].x+30, self.pokemons_sauvages[id_pk_rencontre].y, QPixmap(self.img_pokemons_sauvages[id_pk_rencontre]))
        #painter.drawPicture(self.dresseur.x, self.dresseur.y, "data/Dresseur_image_v1.png")
        self.combat=False

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Initialisation des pokemons
    poke2 = Pokemon(70, 50)
    poke3 = Pokemon(90, 50)
    pokemons_sauvages = [poke2, poke3]
    img_pk_sauvages = ["data/rattata_v1.png","data/dracaufeu_v1.jpeg"]
    starter = Pokemon(-1,-1)

    game = Game(starter, pokemons_sauvages, img_pk_sauvages, "fond2.png")
    game.show()
    sys.exit(app.exec_())