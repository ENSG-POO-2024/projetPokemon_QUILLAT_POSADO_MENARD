
import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtCore import Qt
from dresseur import Dresseur, Pokemon

class Buisson:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

class Game(QWidget):
    def __init__(self, starter, pokemons_sauvages, img_pokemons_sauvages, map):
        super().__init__()
        self.ecran_largeur = 880
        self.ecran_hauteur = 880
        self.map_largeur = 4950
        self.map_hauteur = 4950
        self.background_image = QPixmap(map)
        self.background_position_x = 0
        self.background_position_y = 0
        self.setGeometry(800, 0, self.ecran_largeur, self.ecran_hauteur)
        self.dresseur = Dresseur(self.ecran_largeur//2, self.ecran_hauteur//2, self.ecran_largeur//2, self.ecran_hauteur//2, [starter])
        self.pokemons_sauvages = pokemons_sauvages
        self.nb_bloc = (self.ecran_hauteur//2) // self.dresseur.speed
        self.combat = False
        self.id_pok_rencontre = -1
        self.image_dresseur = QPixmap("utilisateur.png")
        self.img_pokemons_sauvages = img_pokemons_sauvages

        # Créer des buissons aléatoires
        self.buissons = []
        for x in range(0, self.map_largeur, 110):
            for y in range(0, self.map_hauteur, 110):
                if np.random.random() < 0.2:  # 20% de chance d'avoir un buisson à cet emplacement
                    buisson = Buisson(x, y, QPixmap("buissons.png"))
                    self.buissons.append(buisson)

    def keyPressEvent(self, event):
        bord_droit = self.map_largeur - self.ecran_largeur - self.dresseur.speed
        bord_gauche = 0
        bord_haut = 0
        bord_bas = self.map_hauteur - self.ecran_hauteur - self.dresseur.speed

        # Sauvegarder la position du dresseur avant le déplacement
        old_dresseur_x = self.dresseur.X
        old_dresseur_y = self.dresseur.Y

        if event.key() == Qt.Key_Right and -self.background_position_x <= bord_droit and np.abs(self.dresseur.X) >= (self.nb_bloc * self.dresseur.speed):
            self.background_position_x -= self.dresseur.speed

        elif event.key() == Qt.Key_Left and -self.background_position_x > bord_gauche and np.abs(self.dresseur.X) <= (self.map_largeur - self.nb_bloc * self.dresseur.speed):
            self.background_position_x += self.dresseur.speed

        elif event.key() == Qt.Key_Down and -self.background_position_y <= bord_bas and np.abs(self.dresseur.Y) >= (self.nb_bloc * self.dresseur.speed):
            self.background_position_y -= self.dresseur.speed

        elif event.key() == Qt.Key_Up and -self.background_position_y > bord_haut and np.abs(self.dresseur.Y) <= (self.map_hauteur - self.nb_bloc * self.dresseur.speed) :
            self.background_position_y += self.dresseur.speed

        # Vérifier si la nouvelle position du dresseur est valide
        for buisson in self.buissons:
            if buisson.x <= self.dresseur.X < buisson.x + 110 and buisson.y <= self.dresseur.Y < buisson.y + 110:
                # Restaurer la position précédente si la nouvelle position est dans un buisson
                self.dresseur.X = old_dresseur_x
                self.dresseur.Y = old_dresseur_y
                break
        else:
            # Appliquer le déplacement si la nouvelle position est valide
            self.dresseur.X = self.dresseur.x - self.background_position_x
            self.dresseur.Y = self.dresseur.y - self.background_position_y

        proche = self.dresseur.proche(self.pokemons_sauvages)
        if proche[0]:
            self.combat = True
            self.id_pok_rencontre = proche[1]
            print("combat", proche[1])

        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.background_position_x, self.background_position_y, self.background_image)

        # Dessiner les buissons
        for buisson in self.buissons:
            painter.drawPixmap(buisson.x - self.background_position_x, buisson.y - self.background_position_y, buisson.image)

        painter.drawPixmap(self.dresseur.x, self.dresseur.y, self.image_dresseur)

        if self.combat:
            id_pk_rencontre = self.id_pok_rencontre
            painter.drawPixmap(self.pokemons_sauvages[id_pk_rencontre].x + 30, self.pokemons_sauvages[id_pk_rencontre].y, QPixmap(self.img_pokemons_sauvages[id_pk_rencontre]))

        self.combat = False

if __name__ == "__main__":
    app = QApplication(sys.argv)
    poke2 = Pokemon(70, 50)
    poke3 = Pokemon(90, 50)
    pokemons_sauvages = [poke2, poke3]
    img_pk_sauvages = ["data/rattata_v1.png", "data/dracaufeu_v1.jpeg"]
    starter = Pokemon(-1, -1)

    game = Game(starter, pokemons_sauvages, img_pk_sauvages, "fond2.png")
    game.show()
    sys.exit(app.exec_())
