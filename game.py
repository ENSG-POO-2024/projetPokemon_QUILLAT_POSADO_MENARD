import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtCore import Qt
from dresseur import Dresseur, Pokemon


class Game(QWidget):
    def __init__(self, starter, pokemons_sauvages, img_pokemons_sauvages, map):
        super().__init__()
        self.ecran_largeur = 800
        self.ecran_hauteur = 800
        self.map_largeur = 5000 #100 * self.ecran_largeur # 100 blocs de 1000x600
        self.map_hauteur = 3359 #100 * self.ecran_hauteur
        # Charger une image de fond
        self.background_image = QPixmap(map)  # Modifier le chemin avec votre propre image
        self.background_position_x = 0
        self.background_position_y = 0

        self.setGeometry(self.map_largeur//2, self.map_hauteur//2, self.ecran_largeur, self.ecran_hauteur)
        self.dresseur = Dresseur(-self.ecran_largeur//2, -self.ecran_hauteur//2, [starter])
        self.pokemons_sauvages = pokemons_sauvages

        self.combat = False
        self.id_pok_rencontre = -1

        self.image_dresseur = QPixmap("data/Dresseur_image_v1.png")
        self.img_pokemons_sauvages = img_pokemons_sauvages


    def keyPressEvent(self, event):

        #### Vérifier si on n'est pas au bord du terrain en écrivant une méthode prenant event.key() en argument
        print(self.background_position_x, self.background_position_y)

        if event.key() == Qt.Key_Right and self.background_position_x > -self.map_largeur + self.ecran_largeur + self.dresseur.speed:
            #self.dresseur.move_right()
            self.background_position_x -= self.dresseur.speed
        elif event.key() == Qt.Key_Left and self.background_position_x < 0:
            #self.dresseur.move_left()
            self.background_position_x += self.dresseur.speed
        elif event.key() == Qt.Key_Down and self.background_position_y > -self.map_hauteur + self.ecran_hauteur + self.dresseur.speed:
            #self.dresseur.move_down()
            self.background_position_y -= self.dresseur.speed
        elif event.key() == Qt.Key_Up and self.background_position_y < 0:
            #self.dresseur.move_up()
            self.background_position_y += self.dresseur.speed
        
        
        proche = self.dresseur.proche(self.pokemons_sauvages)
        if proche[0]:
            # Combat entre le dresseur et le pokemon numéro proche[1]
            self.combat = True
            self.id_pok_rencontre = proche[1]
            print("combat", proche[1])

        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.background_position_x, self.background_position_y, self.background_image)
        painter.drawPixmap(-self.dresseur.x, -self.dresseur.y, self.image_dresseur)
        print(self.dresseur.x)
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

    game = Game(starter, pokemons_sauvages, img_pk_sauvages, "data/map_v2.jpeg")
    game.show()
    sys.exit(app.exec_())


