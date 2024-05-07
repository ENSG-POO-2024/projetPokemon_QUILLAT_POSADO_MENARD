

import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtCore import Qt
from dresseur import Dresseur, Pokemon


class Game(QWidget):
    def __init__(self, starter, pokemons_sauvages, img_pokemons_sauvages, map):
        super().__init__()
        self.ecran_largeur = 880 # On fixe la largeur de notre fenêtre (celle dans laquelle se déplace le joueur)
        self.ecran_hauteur = 880 # On fixe sa hauteur
        self.map_largeur = 4950 # On fixe la largeur de la map (le terrain de jeu maximal du joueur)
        self.map_hauteur = 4950 # On fixe sa hauteur
        # Charger une image de fond
        self.background_image = QPixmap(map)  # On charge l'image map
        self.background_position_x = 0 # On place le coin haut gauche de notre background en X de notre fenêtre
        self.background_position_y = 0 # Pareil en Y

        self.setGeometry(800,0, self.ecran_largeur, self.ecran_hauteur) # Place la fenêtre à un endroit sur l'écran du joueur
        self.dresseur = Dresseur(self.ecran_largeur//2, self.ecran_hauteur//2, self.ecran_largeur//2, self.ecran_hauteur//2, [starter])
        self.pokemons_sauvages = pokemons_sauvages
        self.nb_bloc = (self.ecran_hauteur//2) // self.dresseur.speed

        

        self.combat = False
        self.id_pok_rencontre = -1

        self.image_dresseur = QPixmap("utilisateur.png") # On charge l'image du dresseur
        self.img_pokemons_sauvages = img_pokemons_sauvages


    def keyPressEvent(self, event):

        #### Vérifier si on n'est pas au bord du terrain en écrivant une méthode prenant event.key() en argument
        print(f"background X: {self.background_position_x} background Y : {self.background_position_y}")

        bord_droit = self.map_largeur - self.ecran_largeur - self.dresseur.speed
        bord_gauche = 0
        bord_haut = 0
        bord_bas = self.map_hauteur - self.ecran_hauteur - self.dresseur.speed

        if event.key() == Qt.Key_Right and -self.background_position_x <= bord_droit and np.abs(self.dresseur.X) >= (self.nb_bloc * self.dresseur.speed):
            self.background_position_x -= self.dresseur.speed
            self.dresseur.X = self.dresseur.x - self.background_position_x # On met à jour la position du dresseur dans le background

        elif event.key() == Qt.Key_Left and -self.background_position_x > bord_gauche and np.abs(self.dresseur.X) <= (self.map_largeur - self.nb_bloc * self.dresseur.speed):
            self.background_position_x += self.dresseur.speed
            self.dresseur.X = self.dresseur.x + self.background_position_x # On met à jour la position du dresseur dans le background


        elif event.key() == Qt.Key_Down and -self.background_position_y <= bord_bas and np.abs(self.dresseur.Y) >= (self.nb_bloc * self.dresseur.speed):
            self.background_position_y -= self.dresseur.speed
            self.dresseur.Y = self.dresseur.y - self.background_position_y # On met à jour la position du dresseur dans le background

        elif event.key() == Qt.Key_Up and -self.background_position_y > bord_haut and np.abs(self.dresseur.Y) <= (self.map_hauteur - self.nb_bloc * self.dresseur.speed) :
            print(self.nb_bloc)
            self.background_position_y += self.dresseur.speed
            self.dresseur.Y = self.dresseur.y + self.background_position_y # On met à jour la position du dresseur dans le background
    
        else:
            if bord_droit <= self.dresseur.X < bord_droit + 2*self.nb_bloc*self.dresseur.speed and event.key() == Qt.Key_Right:
                self.dresseur.move_right()
                self.dresseur.X = self.dresseur.x - self.background_position_x

            elif bord_droit <= self.dresseur.X <= bord_droit + 2*self.nb_bloc*self.dresseur.speed and event.key() == Qt.Key_Left:
                self.dresseur.move_left()
                self.dresseur.X = (-self.background_position_x + self.dresseur.x)
            
            elif bord_gauche < self.dresseur.X <= bord_gauche + self.nb_bloc*self.dresseur.speed and event.key() == Qt.Key_Left:
                self.dresseur.move_left()
                self.dresseur.X = (-self.background_position_x + self.dresseur.x)
            
            elif bord_gauche <= self.dresseur.X <= bord_gauche + self.nb_bloc*self.dresseur.speed and event.key() == Qt.Key_Right:
                self.dresseur.move_right()
                self.dresseur.X = self.dresseur.x - self.background_position_x

            elif bord_haut < self.dresseur.Y <= bord_haut + self.nb_bloc*self.dresseur.speed and event.key() == Qt.Key_Up:
                self.dresseur.move_up()
                self.dresseur.Y = (-self.background_position_y + self.dresseur.y)
            
            elif bord_haut <= self.dresseur.Y <= bord_haut + self.nb_bloc*self.dresseur.speed and event.key() == Qt.Key_Down:
                self.dresseur.move_down()
                self.dresseur.Y = self.dresseur.y - self.background_position_y

            elif bord_bas <= self.dresseur.Y < (bord_bas + 2*self.nb_bloc*self.dresseur.speed) and event.key() == Qt.Key_Down:
                self.dresseur.move_down()
                self.dresseur.Y = self.dresseur.y - self.background_position_y
            
            elif bord_bas <= self.dresseur.Y <= (bord_bas + 2*self.nb_bloc*self.dresseur.speed) and event.key() == Qt.Key_Up:
                self.dresseur.move_up()
                self.dresseur.Y = (-self.background_position_y + self.dresseur.y)



            
        
        proche = self.dresseur.proche(self.pokemons_sauvages)
        if proche[0]:
            # Combat entre le dresseur et le pokemon numéro proche[1]
            self.combat = True
            self.id_pok_rencontre = proche[1]
            print("combat", proche[1])

        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.background_position_x, self.background_position_y, self.background_image) # On dessine l'image "background_image"
        print(f"back X: {self.background_position_x} back Y: {self.background_position_y}")
        painter.drawPixmap(self.dresseur.x, self.dresseur.y, self.image_dresseur) # On dessine l'image "image_dresseur"
        print(f"dresseur X: {self.dresseur.X} dresseur Y: {self.dresseur.Y}")
        print(f"dresseur x: {self.dresseur.x} dresseur y: {self.dresseur.y}")
        # Dessiner les buissons
        painter = QPainter(self)
        for buisson in self.buissons:
            painter.drawPixmap(buisson.x - self.background_position_x, buisson.y - self.background_position_y, self.image_buisson)

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