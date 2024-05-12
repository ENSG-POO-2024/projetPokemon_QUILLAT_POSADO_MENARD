
### LUI FONCTIONNE ###

### Import des bibliothèques ###
import sys
import numpy as np
import os
import cv2

### Import des objets PyQt ###
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGraphicsView, QGraphicsScene
from PyQt5.QtGui import QPainter, QPixmap, QImage
from PyQt5.QtCore import Qt, QTimer

### Import des fichiers ###
import Poke as poke
from test_dresseurbis import Dresseur
import coord_pokemon as coo
import affichage_dresseur as ad

### Import du chemin d'accès au fichier python actuel ###
script_dir = os.path.dirname(__file__)


class PokemonWindow(QWidget): # Fenêtre de rencontre des pokémons sauvages

    def __init__(self, pokemon):
        super().__init__()

        self.pokemon = pokemon # Pokémon sauvage rencontré

        nom_poke = pokemon.name.split()[0]

        self.setWindowTitle("Rencontre avec un Pokémon") # On crée la fenêtre
        self.setGeometry(300, 100, 1000, 750) # On la place


        self.label = QLabel(self)
        image_path = os.path.join(script_dir, "Image", "test.png")
        pixmap = QPixmap(image_path) # On charge l'image de fond
        self.label.setPixmap(pixmap)
        self.label.setAlignment(Qt.AlignCenter)
        # Ajoutez du contenu à votre fenêtre, par exemple un QLabel avec le nom du Pokémon
        self.text_label = QLabel("Vous avez rencontré " + nom_poke + " !", self)
        self.text_label.setAlignment(Qt.AlignCenter)
        self.text_label.setStyleSheet("color: red;")

    def mousePressEvent(self, event):
        """
        Fonction qui permet de gérer l'évenement: clic gauche
        """
        # On récupère les coordonnées du clic de la souris
        mouse_x = event.x()
        mouse_y = event.y()

        if self.bouton_sortie(mouse_x, mouse_y):  # On vérifie si il est dans une certaine zone
            self.close()                                    # Si oui on ferme la fenêtre
        if self.bouton_combat(mouse_x, mouse_y): # Si il est dans une autre zone défini
            self.close()                                    # On ferme la fenêtre
            self.open_combat_window()                       # Puis on ouvre la fenêtre Combat
            

    def bouton_sortie(self, x, y):
        """
        Fonction qui teste si le clic est dans la zone pour fermer la fenêtre
        """
        zone_sortie_x = 90
        zone_sortie_y = 260
        if zone_sortie_x <= x <= (zone_sortie_x + 275) and zone_sortie_y <= y <= (zone_sortie_y + 200):
            return True 
        
    def bouton_combat(self, x, y):
        """
        Fonction qui teste si le clic est dans la zone pour lancer le combat
        """
        zone_sortie_x = 636
        zone_sortie_y = 260
        if zone_sortie_x <= x <= (zone_sortie_x + 275) and zone_sortie_y <= y <= (zone_sortie_y + 200):
            return True 
        
    def open_combat_window(self):
        """
        Fonction qui ouvre la fenêtre de combat
        """
        self.combat_window = CombatWindow(self.pokemon) # On crée cette fenêtre
        self.combat_window.show()                       # On l'affiche


class CombatWindow(QWidget): # Fenêtre de combat

    def __init__(self, pokemon):
        super().__init__()

        nom_poke = pokemon.name.split()[0]

        self.setWindowTitle("Combat contre " + nom_poke) 
        self.setGeometry(300, 100, 1000, 750) # On place notre fenêtre


        self.label = QLabel(self)
        image_path = os.path.join(script_dir, "Image", "combat.png")
        pixmap = QPixmap(image_path) # On charge l'image de fond pour le combat
        self.label.setPixmap(pixmap)
        self.label.setAlignment(Qt.AlignCenter)

    def mousePressEvent(self, event):
        """
        Fonction qui permet de gérer l'évenement: clic gauche
        """
        # On récupère les coordonnées du clic de la souris
        mouse_x = event.x()
        mouse_y = event.y()

        if self.bouton_sortie(mouse_x, mouse_y): # On vérifie si le joueur quitte le combat
            self.close()                         # Si oui: on ferme la fenêtre
            

    def bouton_sortie(self, x, y):
        """
        Fonction qui teste si le clic est dans la zone pour quitter le combat et donc fermer la fenêtre
        """
        zone_sortie_x = 778
        zone_sortie_y = 23
        if zone_sortie_x <= x <= (zone_sortie_x + 200) and zone_sortie_y <= y <= (zone_sortie_y + 150):
            return True 
        
        

class Game(QWidget):
    def __init__(self, sacha, sauvages_csv):
        super().__init__()

        self.ecran_largeur = 880 
        self.ecran_hauteur = 880 
        self.map_largeur = 4950 
        self.map_hauteur = 4950 
        
        image_path = os.path.join(script_dir, "Image", "fond2.png")
        self.background_image = QPixmap(image_path) # On charge notre image de fond
        self.background_position_x = 0 # On initialise sa position
        self.background_position_y = 0 

        self.setGeometry(800, 0, self.ecran_largeur, self.ecran_hauteur)  # On place notre fenêtre principale

        self.sauvages = poke.Pokedex() # On initialise le pokedex des pokemons sauvages qui seront présents sur la map
        self.sauvages.charger_pokedex(sauvages_csv) # On le remplit avec notre fichier 
        #self.sauvages.afficher_pokedex()

        # self.dresseur_pos = self.ecran_largeur//2 # On place le dresseur au milieu de l'écran
        # self.dresseur = Dresseur(self.dresseur_pos, self.dresseur_pos, self.dresseur_pos, self.dresseur_pos, sacha)
        # self.nb_bloc = (self.ecran_hauteur//2) // self.dresseur.speed
        # image_path = os.path.join(script_dir, "Image", "utilisateur.png")
        # self.image_dresseur = QPixmap(image_path) 

        self.dresseur = Dresseur(self.ecran_largeur // 2, self.ecran_hauteur // 2,self.ecran_largeur // 2, self.ecran_hauteur // 2, self.map_largeur, self.map_hauteur, sacha)
        # Chargez les images du dresseur
        self.dresseur_images = {direction: [QPixmap(image) for image in images] for direction, images in self.dresseur.images.items()}
        # Définissez un timer pour mettre à jour l'image du dresseur
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_dresseur_image)
        self.timer.start(150)  # Mettez à jour l'image toutes les 150 ms
        self.nb_bloc = (self.ecran_hauteur//2) // self.dresseur.speed



    def keyPressEvent(self, event):

        bord_droit = self.map_largeur - self.ecran_largeur - self.dresseur.speed
        bord_gauche = 0
        bord_haut = 0
        bord_bas = self.map_hauteur - self.ecran_hauteur - self.dresseur.speed



        if event.key() == Qt.Key_Right and -self.background_position_x <= bord_droit and np.abs(self.dresseur.X) >= (self.nb_bloc * self.dresseur.speed):
            self.background_position_x -= self.dresseur.speed
            for nom_pokemon, pokemon in self.sauvages.pokedex.items():
                pokemon.x -= self.dresseur.speed
                self.dresseur.move("right")

        elif event.key() == Qt.Key_Left and -self.background_position_x > bord_gauche and np.abs(self.dresseur.X) <= (self.map_largeur - self.nb_bloc * self.dresseur.speed):
            self.background_position_x += self.dresseur.speed
            for nom_pokemon, pokemon in self.sauvages.pokedex.items():
                pokemon.x += self.dresseur.speed
                self.dresseur.move("left")

        elif event.key() == Qt.Key_Down and -self.background_position_y <= bord_bas and np.abs(self.dresseur.Y) >= (self.nb_bloc * self.dresseur.speed):
            self.background_position_y -= self.dresseur.speed
            for nom_pokemon, pokemon in self.sauvages.pokedex.items():
                pokemon.y -= self.dresseur.speed
                self.dresseur.move("down")

        elif event.key() == Qt.Key_Up and -self.background_position_y > bord_haut and np.abs(self.dresseur.Y) <= (self.map_hauteur - self.nb_bloc * self.dresseur.speed):
            self.background_position_y += self.dresseur.speed
            for nom_pokemon, pokemon in self.sauvages.pokedex.items():
                pokemon.y += self.dresseur.speed
                self.dresseur.move("up")




        if self.dresseur.proche(self.sauvages)[0]:
            pokemon_name = self.dresseur.proche(self.sauvages)[1]
            self.open_pokemon_window(pokemon_name)

        self.update()

    def update_dresseur_image(self):
        # Mettez à jour l'image du dresseur en fonction de sa direction
        self.dresseur.current_image_index = (self.dresseur.current_image_index + 1) % 2
        self.update()  # Actualisez l'affichage



    def paintEvent(self, event): # Fonction pour afficher les images 
        painter = QPainter(self)
        painter.drawPixmap(self.background_position_x, self.background_position_y, self.background_image) # Affichage map
        painter.drawPixmap(self.dresseur.x, self.dresseur.y, self.dresseur_images[self.dresseur.direction][self.dresseur.current_image_index]) # Affichage dresseur
        script_dir = os.path.dirname(__file__)
        for cle_pokemons, poke_sauvage in self.sauvages.pokedex.items(): # On affiche tous les pokémons sauvages
            base_name = poke_sauvage.name.split()[0] # Pour gérer le cas avec plusieurs fois le même pokémon
            image_path = os.path.join(script_dir, "Pokémons/" + base_name, base_name + "_face.png")
            pixmap = QPixmap(image_path)
            painter.drawPixmap(poke_sauvage.x, poke_sauvage.y, pixmap) 
             

    def open_pokemon_window(self, pokemon_name): # Ouverture de la fenêtre Rencontre lors de la rencontre avec un pokémon sauvage
        self.pokemon_window = PokemonWindow(pokemon_name)
        self.pokemon_window.show()


class AccueilWindow(QWidget):
    def __init__(self, video_path):
        super().__init__()

        self.setWindowTitle("Accueil")
        self.setGeometry(300, 100, 1000, 700)

        self.label = QLabel(self)
        self.label.setGeometry(0, 0, 1000, 700)

        self.video_path = video_path
        self.cap = cv2.VideoCapture(video_path)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)  # Mettez à jour la vidéo toutes les 30 millisecondes

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

    def open_game_window(self):
        self.timer.stop()  # Arrêter la mise à jour de la vidéo avant d'ouvrir la fenêtre de jeu
        self.cap.release()  # Libérer la ressource vidéo
        self.game_window = Game(sacha, poke_sauvages)
        self.game_window.show()
        self.close()

    def mousePressEvent(self, event):
        # Si le clic de souris a eu lieu dans une certaine zone de la fenêtre, commencez le jeu
        if event.x() >= 0 and event.x() <= 200 and event.y() >= 0 and event.y() <= 200:
            self.timer.stop()  # Arrêter la mise à jour de la vidéo avant d'ouvrir la fenêtre de jeu
            self.cap.release()  # Libérer la ressource vidéo
            self.game_window = Game(sacha, poke_sauvages)
            self.game_window.show()
            self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv) 

    coo.poke_coord('pokemon_first_gen.csv', 'pokemons_a_capturer.csv', 100)
    poke_sauvages = "pokemons_a_capturer.csv"
    magicarpe = poke.Pokemon.creer_pokemon("Magicarpe", 550, 550, 50, 20, 10, 35, 15, poke.Eau(), False)
    sacha = poke.InventaireJoueur()
    sacha.inventory(magicarpe)

    
    # game = Game(sacha, poke_sauvages)
    # game.show()

    video_path = os.path.join(script_dir, "Image", "video.mp4")  # Remplacez ceci par le chemin vers votre fichier vidéo
    accueil = AccueilWindow(video_path)
    accueil.show()


    sys.exit(app.exec_())
