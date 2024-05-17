### POUR TESTER LES NOUVEAUX GRAPH ET EVITER DE PERDRE L'ANCIEN ###

### LUI FONCTIONNE ###

### Import des bibliothèques ###
import sys
import numpy as np
import os
import cv2

### Import des objets PyQt ###
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPainter, QPixmap, QImage
from PyQt5.QtCore import Qt, QTimer
from PyQt5 import QtTest

### Import des fichiers ###
import Poke as poke
from dresseur import Dresseur
import Coord_pokemon as coo
import Starter.Starter as s
import Sauvage as sau
import Regles as re
import RencontreRocket as r

### Import du chemin d'accès au fichier python actuel ###
script_dir = os.path.dirname(__file__)



class Accueil(QWidget): # On arrive sur la page d'acceuil et on peut cliquer sur Jouer ou Règles
    def __init__(self, video_path):
        super().__init__()

        ## Création de la fenêtre d'acceuil
        self.setWindowTitle("Accueil")
        self.setGeometry(250, 100, 1000, 750)

        ## Affichage de la vidéo d'acceuil
        self.label = QLabel(self)
        self.label.setGeometry(0, 0, 1000, 750)

        self.video_path = video_path
        self.cap = cv2.VideoCapture(video_path)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)  
        self.loop_video = True

        self.mouse_clicked = False  # Pour suivre si le clic de souris a eu lieu
        self.label.mousePressEvent = self.mousePressEvent  # Redéfinition de la méthode mousePressEvent



    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame_rgb.shape
            bytes_per_line = ch * w
            q_image = QImage(frame_rgb.data, w, h, bytes_per_line, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(q_image)
            self.label.setPixmap(pixmap)

        else:
            if self.loop_video:
                self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            else:
                self.stop_video()

    def stop_video(self):
        self.timer.stop()

    def mousePressEvent(self, event):
        # Si le clic de souris a eu lieu dans une certaine zone de la fenêtre on arrive sur la map
        if event.x() >= 60 and event.x() <= 380 and event.y() >= 295 and event.y() <= 390:
            self.timer.stop()  # On arrête la mise à jour de la vidéo avant d'ouvrir la fenêtre de jeu
            self.cap.release()  
            self.starter_window = s.Starter()
            self.starter_window.show()
            self.close()

        if event.x() >= 600 and event.x() <= 980 and event.y() >= 306 and event.y() <= 375:
            self.timer.stop()  # On arrête la mise à jour de la vidéo avant d'ouvrir la fenêtre des règles
            self.cap.release()  
            self.regles_window = re.Regles()
            self.regles_window.show()
            self.close()


class background():
    def __init__(self, image_path, x, y):
        self.x = x
        self.y = y
        self.image = QPixmap(image_path)
    


class Map(QWidget): # Si on a cliqué sur Jouer on arrive sur la map

    def __init__(self, starter, sauvages_csv): # Starter représente le premier pokémon du joueur
        super().__init__()                     # sauvages_csv est le fichier csv avec les pokemons sauvages présents au début du jeu


        # Les pokémons apparaissent aléatoirement à chaque début de partie
        coo.poke_coord('pokemon_first_gen.csv', 'pokemons_a_capturer.csv', 100) # 100 pokémons seront sur la map

        # Initialisation des constantes visuelles
        self.ecran_largeur = 880 
        self.ecran_hauteur = 880 
        self.map_largeur = 4950 
        self.map_hauteur = 4950 

        # Mise en place de l'affichage de la map
        image_path = os.path.join(script_dir, "Media/Image", "map.png")
        self.background = background(image_path, 0, 0) # On charge notre image de fond
        #self.background.x = 0 # On initialise sa position
        #self.background.y = 0 
        self.setWindowTitle("Votre pokémon starter est " + starter.name)
        self.setGeometry(800, 0, self.ecran_largeur, self.ecran_hauteur)  # On place notre fenêtre principale

        # Pour retourner sur l'acceuil
        self.retour_img = QPixmap("Media/Image/retour.png")

        # Mise en place de l'affichage du dresseur
        self.image_dresseur = {
            "up": [QPixmap("Media/Dresseur/Sacha_haut2.png"), QPixmap("Media/Dresseur/Sacha_haut3.png")],
            "down": [QPixmap("Media/Dresseur/Sacha_bas2.png"), QPixmap("Media/Dresseur/Sacha_bas3.png")],
            "left": [QPixmap("Media/Dresseur/Sacha_gauche2.png"), QPixmap("Media/Dresseur/Sacha_gauche1.png")],
            "right": [QPixmap("Media/Dresseur/Sacha_droite2.png"), QPixmap("Media/Dresseur/Sacha_droite1.png")],
            "static": [QPixmap("Media/Dresseur/Sacha_bas1.png")]
        }

        self.img_fin = ["data/Fin de jeu/1.png", "data/Fin de jeu/2.png", "data/Fin de jeu/3.png", "data/Fin de jeu/4.png",
                        "data/Fin de jeu/5.png", "data/Fin de jeu/6.png", "data/Fin de jeu/7.png", "data/Fin de jeu/8.png"]


        self.index_img = 0

        # Création de l'inventaire du joueur
        self.inventaire_joueur = poke.InventaireJoueur()
        self.inventaire_joueur.ajout_inventaire(starter) # Ajout du starter à son inventaire
        
        # Création du pokedex contenant les pokémons sauvages de la map
        self.pokedex_sauvages = poke.Pokedex()
        self.pokedex_sauvages.charger_pokedex(sauvages_csv) # On le remplit avec notre fichier 

        # Création de notre dresseur
        self.dresseur_pos = self.ecran_largeur//2 # On place le dresseur au milieu de l'écran
        self.dresseur = Dresseur(self.dresseur_pos, self.dresseur_pos, self.dresseur_pos, self.dresseur_pos, self.inventaire_joueur)
        self.nb_bloc = (self.ecran_hauteur//2) // self.dresseur.speed
        self.current_direction = None
        self.current_image_index = 0
        self.delay_timer = QTimer(self)
        self.delay_timer.timeout.connect(self.reset_direction)


        self.fin = False



    def mousePressEvent(self, event):
        # Si le clic de souris a eu lieu dans une certaine zone de la fenêtre on arrive sur la map
        if event.x() >= 0 and event.x() <= 205 and event.y() >= 0 and event.y() <= 50: 
            video_path = os.path.join(script_dir, "Media/Image", "video.mp4")
            self.retour_acceuil = Accueil(video_path)
            self.retour_acceuil.show()
            self.close()


    def keyPressEvent(self, event):

        bord_droit = self.map_largeur - self.ecran_largeur - self.dresseur.speed
        bord_gauche = 0
        bord_haut = 0
        bord_bas = self.map_hauteur - self.ecran_hauteur - self.dresseur.speed


        if np.abs(self.dresseur.x) ==  self.ecran_largeur//2 and np.abs(self.dresseur.y) == self.ecran_hauteur//2:

            if event.key() == Qt.Key_Right and -self.background.x <= bord_droit and np.abs(self.dresseur.x):
                self.background.x -= self.dresseur.speed
                for nom_pokemon, pokemon in self.pokedex_sauvages.pokedex.items():
                    pokemon.x -= self.dresseur.speed
                    self.current_direction = "right"

            elif event.key() == Qt.Key_Left and -self.background.x > bord_gauche :
                self.background.x += self.dresseur.speed
                for nom_pokemon, pokemon in self.pokedex_sauvages.pokedex.items():
                    pokemon.x += self.dresseur.speed
                    self.current_direction = "left"

            elif event.key() == Qt.Key_Down and -self.background.y <= bord_bas and np.abs(self.dresseur.y):
                self.background.y -= self.dresseur.speed
                for nom_pokemon, pokemon in self.pokedex_sauvages.pokedex.items():
                    pokemon.y -= self.dresseur.speed
                    self.current_direction = "down"

            elif event.key() == Qt.Key_Up and -self.background.y > bord_haut and np.abs(self.dresseur.y):
                self.background.y += self.dresseur.speed
                for nom_pokemon, pokemon in self.pokedex_sauvages.pokedex.items():
                    pokemon.y += self.dresseur.speed
                    self.current_direction = "up"

        if event.key() == Qt.Key_Left and 1760 <= -self.background.y <= 1870 and -self.background.x <= bord_gauche :
                self.dresseur.x -= self.dresseur.speed
                self.dresseur.X -= self.dresseur.speed
                self.current_direction = "left"
                self.fin = True


        if self.dresseur.proche(self.pokedex_sauvages)[0]:
            #self.inventaire_joueur.afficher_pokedex()
            self.pokemon_sauvage = self.dresseur.proche(self.pokedex_sauvages)[1]
            self.pokemon_window = sau.Sauvage(self.pokemon_sauvage, self.inventaire_joueur, self.pokedex_sauvages)
            self.pokemon_window.show()

        if  1760 <= -self.background.y <= 1980 and -self.background.x == 4070:
            self.rocket_window = r.RencontreRocket()
            self.rocket_window.show()


        self.update()
        self.delay_timer.start(750)


    def paintEvent(self, event): # Fonction pour afficher les images 
        painter = QPainter(self)
        painter.drawPixmap(self.background.x, self.background.y, self.background.image) # Affichage de la map
        for cle_pokemons, poke_sauvage in self.pokedex_sauvages.pokedex.items(): # On affiche tous les pokémons sauvages
            if self.dresseur.proche_affichage(poke_sauvage):
                base_name = poke_sauvage.name.split()[0] # Pour gérer le cas avec plusieurs fois le même pokémon
                image_path = os.path.join(script_dir, "Pokemons/" + base_name, base_name + "_face.png")
                pixmap = QPixmap(image_path)
                painter.drawPixmap(poke_sauvage.x, poke_sauvage.y, pixmap) 
        
        painter.setRenderHint(QPainter.SmoothPixmapTransform)

        painter.drawPixmap(5, -75, self.retour_img)

        if self.current_direction:
            pixmap = self.image_dresseur[self.current_direction][self.current_image_index]
        else:
            pixmap = self.image_dresseur["static"][0]  # Utilisez l'image vers le bas par défaut lorsque le joueur ne se déplace pas

        painter.drawPixmap(self.dresseur.x+10, self.dresseur.y, pixmap.scaled(90,90))

        if self.fin:
            QTimer.singleShot(2000, self.close)



    def update(self):
        if self.current_direction:
            self.current_image_index = (self.current_image_index + 1) % len(self.image_dresseur[self.current_direction])
        else:
            self.current_image_index = 0
        self.repaint()

    def reset_direction(self):
        self.current_direction = None
        self.update()

             



if __name__ == "__main__":
    app = QApplication(sys.argv) 

    video_path = os.path.join(script_dir, "Media/Image", "video.mp4")
    accueil = Accueil(video_path)
    accueil.show()


    sys.exit(app.exec_())
