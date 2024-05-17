

import sys
import os
import pygame
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont, QPixmap
from PyQt5 import *

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

import Poke as poke
import ChoixPokemon as ch
import Victoire as v
import Defaite as d


def bas_image(image):
    img = image.toImage()
    hauteur = img.height()
    largeur = img.width()

    for h in range(hauteur-1, -1, -1):
        for l in range(largeur):
            color = img.pixelColor(l, h)

            if color.alpha() != 0:
                return h
            
    return 0



class Rocket_ui(object):

    def __init__(self):
        pygame.mixer.init()  # Initialisation de pygame.mixer
        self.sound = pygame.mixer.Sound("Media/Image/battle.mp3")  # Charger le son


    def setupUi(self, MainWindow):
        
        self.adversaire = self.pokemon_sauvage

        self.pokedex = poke.Pokedex()
        self.pokedex.charger_pokedex("pokemon_first_gen.csv")

        # Création de l'objet MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("Combat contre " + self.adversaire.name.split()[0])
        MainWindow.resize(1000, 750)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")



        # Création de l'arrière plan
        self.Fond = QtWidgets.QLabel(self.centralwidget)
        self.Fond.setGeometry(QtCore.QRect(0, 0, 1000, 750))
        self.Fond.setText("")
        self.Fond.setPixmap(QtGui.QPixmap("Media/Image/combat_rocket.png"))
        self.Fond.setScaledContents(True)
        self.Fond.setObjectName("Fond")

        # Ajout du type du pokemon adverse
        self.TypeEnemy = QtWidgets.QLabel(self.centralwidget)
        self.TypeEnemy.setGeometry(QtCore.QRect(409, 98, 60, 60))
        self.TypeEnemy.setPixmap(QtGui.QPixmap("Media/Types/" + self.adversaire.type.__class__.__name__ + ".png")) #
        self.TypeEnemy.setScaledContents(True)
        self.TypeEnemy.setObjectName("TypeEnemy")

        # Ajout du type de mon pokemon
        self.TypeAllie = QtWidgets.QLabel(self.centralwidget)
        self.TypeAllie.setGeometry(QtCore.QRect(605, 448, 60, 60))
        self.TypeAllie.setPixmap(QtGui.QPixmap("Media/Types/" + self.pokemon_utilise.type.__class__.__name__ + ".png")) #
        self.TypeAllie.setScaledContents(True)
        self.TypeAllie.setObjectName("TypeAllie")


        #Création de l'objet barre de vie de notre pokemon
        self.progressBarAllie = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBarAllie.setGeometry(QtCore.QRect(620, 397, 371, 23))
        self.progressBarAllie.setMaximum(self.pokedex.pokedex[self.pokemon_utilise.name.split()[0]].hp)
        self.progressBarAllie.setValue(self.pokemon_utilise.hp)
        self.progressBarAllie.setFormat("")
        self.progressBarAllie.setObjectName("progressBarAllie")

        # Créer une étiquette pour afficher les points de vie de notre pokemon
        self.label_hp_allie = QtWidgets.QLabel(self.centralwidget)
        self.label_hp_allie.setGeometry(QtCore.QRect(624, 399, 371, 23))
        self.label_hp_allie.setObjectName("label_hp_allie")
        self.label_hp_allie.setStyleSheet('color: black; font-size: 16px; font-family: "Minecraft";')
    
        # Affichage de la bar d'hp de notre pokemon
        self.affiche_progress_bar(self.progressBarAllie, self.label_hp_allie, self.pokemon_utilise.hp)


        # Création de la barre de vie de m'adversaire
        self.progressBarEnemy = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBarEnemy.setGeometry(QtCore.QRect(110, 189, 371, 23))
        self.progressBarEnemy.setMaximum(self.pokedex.pokedex[self.adversaire.name.split()[0]].hp)
        self.progressBarEnemy.setValue(self.adversaire.hp)
        self.progressBarEnemy.setFormat("")
        self.progressBarEnemy.setObjectName("progressBarEnemy")

        # Créer une étiquette pour afficher les points de vie de l'adversaire
        self.label_hp_adversaire = QtWidgets.QLabel(self.centralwidget)
        self.label_hp_adversaire.setGeometry(QtCore.QRect(114, 191, 371, 23))
        self.label_hp_adversaire.setObjectName("label_hp_adversaire")
        self.label_hp_adversaire.setStyleSheet('color: black; font-size: 16px; font-family: "Minecraft";')
        
        # Affichage de la bar d'hp de l'adversaire
        self.affiche_progress_bar(self.progressBarEnemy, self.label_hp_adversaire, self.adversaire.hp)

        # Affichage de notre pokémon
        self.image_poke = QtWidgets.QLabel(self.centralwidget)
        self.image_poke.setGeometry(QtCore.QRect(90, 230, 400, 400))
        self.image_poke.setText("")
        self.gif_poke = QtGui.QMovie("Pokemons/"+self.pokemon_utilise.name.split()[0]+"/"+self.pokemon_utilise.name.split()[0]+"_dos.gif")
        self.gif_poke.setScaledSize(QtCore.QSize(300, 300))
        self.image_poke.setMovie(self.gif_poke)
        self.gif_poke.start()
        self.image_poke.setObjectName("Pokemon inventaire_joueur")

        # Affichage pokémon adverse
        self.image_adv = QtWidgets.QLabel(self.centralwidget)
        self.image_adv.setGeometry(QtCore.QRect(640, 0, 400, 400))
        self.image_adv.setText("")
        self.gif_adv = QtGui.QMovie("Pokemons/"+self.adversaire.name.split()[0]+"/"+self.adversaire.name.split()[0]+"_face.gif")
        self.gif_adv.setScaledSize(QtCore.QSize(250, 250))
        self.image_adv.setMovie(self.gif_adv)
        self.gif_adv.start()
        self.image_adv.setObjectName("Pokemon adverse")



        # Point d'attaque et de défense de notre pokémon
        self.poke_att = QLabel(str(self.pokemon_utilise.attack), self)
        self.poke_att.setGeometry(128, 583, 200, 50)
        self.poke_att.setStyleSheet('color: black; font-size: 30px; font-family: "Hello World";')  
        self.poke_def = QLabel(str(self.pokemon_utilise.defense), self)
        self.poke_def.setGeometry(128, 657, 200, 50)
        self.poke_def.setStyleSheet('color: black; font-size: 30px; font-family: "Hello World";')

        # Point d'attaque et de défense de l'adversaire
        self.label = QLabel(str(self.adversaire.attack), self)
        self.label.setGeometry(323, -2, 200, 50)
        self.label.setStyleSheet('color: red; font-size: 25px; font-family: "Hello World";')  
        self.label = QLabel(str(self.adversaire.defense), self)
        self.label.setGeometry(339, 34, 200, 50)
        self.label.setStyleSheet('color: red; font-size: 25px; font-family: "Hello World";')

        # Bouton de l'attaque normale
        self.AttaqueNormale = QtWidgets.QPushButton(self.centralwidget)
        self.AttaqueNormale.setGeometry(QtCore.QRect(353, 558, 169, 161))
        self.AttaqueNormale.setText("")
        self.AttaqueNormale.setObjectName("AttaqueNormale")

        # Bouton de l'attaque speciale
        self.AttaqueSpeciale = QtWidgets.QPushButton(self.centralwidget)
        self.AttaqueSpeciale.setGeometry(QtCore.QRect(561, 558, 169, 161))
        self.AttaqueSpeciale.setText("")
        self.AttaqueSpeciale.setObjectName("AttaqueSpeciale")

        # Bouton pour changer de pokemon
        self.Pokedex = QtWidgets.QPushButton(self.centralwidget)
        self.Pokedex.setGeometry(QtCore.QRect(770, 558, 169, 161))
        self.Pokedex.setText("")
        self.Pokedex.setObjectName("Pokedex")

        # Bouton pour fuir
        self.Fuite = QtWidgets.QPushButton(self.centralwidget)
        self.Fuite.setGeometry(QtCore.QRect(800, 0, 300, 300))
        self.Fuite.setText("")
        self.Fuite.setObjectName("Fuite")

        

        # On met tout en avant (dans le bon ordre) pour que les objets soient au premier plan 
        self.Fond.raise_()
        self.image_poke.raise_()
        self.image_adv.raise_()

        # Affichage de notre pokémon
        self.points_attaque = QtWidgets.QLabel(self.centralwidget)
        self.points_attaque.setGeometry(QtCore.QRect(0, 0, 1000, 750))
        self.points_attaque.setText("")
        self.points_attaque.setPixmap(QtGui.QPixmap("Media/Image/combat.png"))
        self.points_attaque.setScaledContents(True)
        self.points_attaque.setObjectName("Points d'attaque")

        
        self.progressBarAllie.raise_()
        self.progressBarEnemy.raise_()
        self.AttaqueNormale.raise_()
        self.AttaqueSpeciale.raise_()
        self.Pokedex.raise_()
        self.Fuite.raise_()
        self.label_hp_adversaire.raise_()
        self.label_hp_allie.raise_()
        self.TypeEnemy.raise_()
        self.TypeAllie.raise_()


        self.AttaqueNormale.setStyleSheet("background-color: rgba(255, 255, 255, 0); border: none;")
        self.AttaqueSpeciale.setStyleSheet("background-color: rgba(255, 255, 255, 0); border: none;")
        self.Pokedex.setStyleSheet("background-color: rgba(255, 255, 255, 0); border: none;")
        self.Fuite.setStyleSheet("background-color: rgba(255, 255, 255, 0); border: none;")


        MainWindow.setCentralWidget(self.centralwidget)

        self.Fuite.clicked.connect(self.fuite_buton)

        self.tour_joueur = True
        self.tours_depuis_attaque_joueur = 2  # Tours écoulés depuis la dernière attaque spéciale du joueur
        self.tours_depuis_attaque_ordi = 2  # Tours écoulés depuis la dernière attaque spéciale de l'ordinateur

        # Affichage nom du pokémon utilisé
        self.nom_poke = QLabel(self.pokemon_utilise.name.split()[0], self)
        self.nom_poke.setGeometry(660, 432, 300, 100)  # Définir la position et la taille du QLabel
        self.nom_poke.setAlignment(Qt.AlignCenter)  # Aligner le texte au centre 
        font = QFont("Minecraft", 40)  # Police et taille
        self.nom_poke.setFont(font)
        self.nom_poke.setStyleSheet('color: black;')  

        # Affichage nom du pokémon adverse
        self.nom_poke = QLabel(self.adversaire.name.split()[0], self)
        self.nom_poke.setGeometry(93, 80, 300, 100)  # Définir la position et la taille du QLabel
        self.nom_poke.setAlignment(Qt.AlignCenter)  # Aligner le texte au centre 
        font = QFont("Minecraft", 40)  # Police et taille
        self.nom_poke.setFont(font)
        self.nom_poke.setStyleSheet("color: black;")  


        if self.tours_depuis_attaque_joueur < 2:
            self.AttaqueSpeciale.setStyleSheet("background-color: rgba(128, 128, 128, 128)")
        else:
            self.AttaqueSpeciale.setStyleSheet("background-color: rgba(128, 128, 128, 0)")

        if not self.first_combat:
            QTimer.singleShot(1500, self.tour_ordi)

        else:
            # Ajout du son dès que la fenêtre s'ouvre
            #playsound.playsound("Combat/battle.mp3", block=False)
            self.play_audio()

        if len(self.inventaire_joueur.pokedex) <= 1:
            self.Pokedex.setEnabled(False)
            self.Pokedex.setStyleSheet("background-color: rgba(128, 128, 128, 128)")

       
        # On gère les clics sur un bouton
        self.AttaqueNormale.clicked.connect(self.on_attaque_normale_clicked)
        self.AttaqueSpeciale.clicked.connect(self.on_attaque_speciale_clicked)
        self.Pokedex.clicked.connect(self.open_pokedex)



    def open_pokedex(self): 
        self.close()
        self.tours_depuis_attaque_joueur += 1
        self.pokedex_window = ch.ChoixPokemon(self.adversaire, self.inventaire_joueur, self.pokedex_sauvages, True, True)  
        self.pokedex_window.boutons[self.pokemon_utilise.name.split()[0]].setEnabled(False)
        self.pokedex_window.show()


    def fuite_buton(self):
        self.stop_audio()
        self.pokemon_utilise.hp = self.pokedex.pokedex[self.pokemon_utilise.name.split()[0]].hp
        self.adversaire.hp = self.pokedex.pokedex[self.adversaire.name.split()[0]].hp
        self.close() 

    def on_attaque_normale_clicked(self):
        self.Pokedex.setEnabled(False)
        self.Fuite.setEnabled(False)
        if self.tour_joueur:
            # Attaque normale du joueur
            degats = self.pokemon_utilise.attaquer(self.adversaire)
            self.progressBarEnemy.setValue(self.adversaire.hp)
            self.affiche_progress_bar(self.progressBarEnemy, self.label_hp_adversaire, self.adversaire.hp)
            self.affichage_attaque("Media/Image/Attaque.png", self.pokemon_utilise, self.adversaire, degats, False, True)
            

            # On désactive le bouton d'attaque pour empêcher les attaques multiples dans le même tour
            self.AttaqueNormale.setEnabled(False)

            # On incrémente le nombre de tour depuis l'ataque spéciale du joueur
            self.tours_depuis_attaque_joueur += 1

            # On passe au tour de l'ordi
            self.tour_joueur = False

            if self.adversaire.hp <= 0: # On vérifie si l'adversaire est battu
                QTimer.singleShot(5000, self.close)
                QTimer.singleShot(5000, self.open_victory)

            else:
                # L'ordi peut attaquer
                QTimer.singleShot(6000, self.tour_ordi)
        

    def on_attaque_speciale_clicked(self):
        self.Pokedex.setEnabled(False)
        self.Fuite.setEnabled(False)
        self.AttaqueNormale.setEnabled(False)
        if self.tours_depuis_attaque_joueur >= 2:
            # Attaque spéciale du joueur
            degats = self.pokemon_utilise.attaque_speciale_joueur(self.adversaire)
            self.progressBarEnemy.setValue(self.adversaire.hp)
            self.affiche_progress_bar(self.progressBarEnemy, self.label_hp_adversaire, self.adversaire.hp)
            self.affichage_attaque("Media/Image/Attaque.png", self.pokemon_utilise, self.adversaire, degats, True, True)
            

            # On désactive le bouton d'attaque spéciale pour empêcher les attaques multiples dans le même tour
            self.AttaqueSpeciale.setEnabled(False)
            self.AttaqueSpeciale.setStyleSheet("background-color: rgba(128, 128, 128, 128)")

            # On met à jour la disponibilité de l'attaque spéciale
            self.tours_depuis_attaque_joueur = 0  # On réinitialise le compteur de tours après l'attaque spéciale du joueur

            if self.adversaire.hp <= 0: # On vérifie si l'adversaire est battu
                QTimer.singleShot(5000, self.close)
                QTimer.singleShot(5000, self.open_victory)

            else:
                # On attend 6 secondes puis l'adversaire attaque
                QTimer.singleShot(6000, self.tour_ordi)

        

    def tour_ordi(self):
        # On vérifie si l'ordi a son attaque spéciale de prête 
        if self.tours_depuis_attaque_ordi >= 2:
            # Si oui alors il l'utilise
            degats = self.adversaire.attaque_speciale_joueur(self.pokemon_utilise)
            self.progressBarAllie.setValue(self.pokemon_utilise.hp)
            self.affiche_progress_bar(self.progressBarAllie, self.label_hp_allie, self.pokemon_utilise.hp)
            self.affichage_attaque("Media/Image/Attaque.png", self.adversaire, self.pokemon_utilise, degats, True, False)

            # Mettez à jour l'état de disponibilité de l'attaque spéciale de l'ordinateur
            self.tours_depuis_attaque_ordi = 0  # Réinitialisez le compteur de tours depuis l'attaque spéciale


        else:
            # Si l'attaque spéciale n'est pas disponible alors l'adversaire attaque normalement 
            degats = self.adversaire.attaquer(self.pokemon_utilise)
            self.progressBarAllie.setValue(self.pokemon_utilise.hp)
            self.affiche_progress_bar(self.progressBarAllie, self.label_hp_allie, self.pokemon_utilise.hp)
            self.affichage_attaque("Media/Image/Attaque.png", self.adversaire, self.pokemon_utilise, degats, False, False)


            # On incrémente le compteur de tours depuis la dernière attaque spéciale de l'adversaire
            self.tours_depuis_attaque_ordi += 1

        if self.tours_depuis_attaque_joueur >= 2: # On met à jour si besoin le bouton d'attaque spéciale
            self.AttaqueSpeciale.setEnabled(True)
            self.AttaqueSpeciale.setStyleSheet("background-color: rgba(255, 255, 255, 0); border: none;")

        if self.pokemon_utilise.hp <= 0: # On vérifie si le joueur a perdu
                self.AttaqueNormale.setEnabled(False)
                self.AttaqueSpeciale.setEnabled(False)
                self.Pokedex.setEnabled(False)
                self.Fuite.setEnabled(False)

                if self.inventaire_joueur.toujours_vivant() :
                    QTimer.singleShot(3000, self.pokemon_KO)
                else:
                    QTimer.singleShot(5000, self.close)
                    self.pokemon_utilise.hp = self.pokedex.pokedex[self.pokemon_utilise.name.split()[0]].hp
                    self.adversaire.hp = self.pokedex.pokedex[self.adversaire.name.split()[0]].hp
                    QTimer.singleShot(5000, self.open_loose)
                        

        else:
            QTimer.singleShot(3000, self.update_variable)


    def pokemon_KO(self):
        self.close()
        self.pokedex_window = ch.ChoixPokemon(self.adversaire, self.inventaire_joueur, self.pokedex_sauvages, False, True)  
        self.pokedex_window.show()

    def update_variable(self):
        self.AttaqueNormale.setEnabled(True)
        self.Pokedex.setEnabled(True)
        self.Fuite.setEnabled(True)

        # On passe au tour du joueur
        self.tour_joueur = True


    def affiche_progress_bar(self, bar, label, hp):
        if hp <= 0.25 * bar.maximum():
            bar.setStyleSheet("""                                                                
                QProgressBar {
                    border: 2px solid grey;
                    border-radius: 5px;
                    background-color: #FFFFFF; /* Couleur de fond de la barre de progression */
                }
                    
                QProgressBar::chunk {
                    background-color: #FF0000; /* Couleur de la barre de progression */   
                    border-radius: 100px;
                }                                
            """) 
        
        else:
            bar.setStyleSheet("""   
                QProgressBar { color: red;}                                                            
                QProgressBar {                            
                    border: 2px solid grey;
                    border-radius: 5px;
                    background-color: #FFFFFF; /* Couleur de fond de la barre de progression */
                }

                QProgressBar::chunk {
                    background-color: #00FF00; /* Couleur de la barre de progression */
                    border-radius: 100px;
                }                                                             
            """)
        # On met à jour le texte de l'étiquette des points de vie de notre pokemon
        label.setText(str(hp))
        label.raise_()


    def open_victory(self):
        self.stop_audio()
        self.victory_window = v.Victoire(self.adversaire, self.pokedex_sauvages, self.inventaire_joueur, self.pokemon_utilise, self.pokedex)
        self.victory_window.show()

    def open_loose(self):
        self.stop_audio()
        self.Pokedex.setEnabled(False)
        self.Fuite.setEnabled(False)
        self.victory_window = d.Defaite(self.adversaire, self.pokedex_sauvages, self.inventaire_joueur, self.pokemon_utilise, self.pokedex)
        self.victory_window.show()

    def affichage_attaque(self, chemin_image, attaquant, defenseur, degats, speciale, joueur):
        # Afficher l'image d'attaque
        self.image_label = QLabel(self.centralwidget)
        self.image_label.setGeometry(0, 0, 1000, 750)
        pixmap = QPixmap(chemin_image)
        pixmap = pixmap.scaled(1000, 750)  
        self.image_label.setPixmap(pixmap)
        self.image_label.setScaledContents(True) 
        self.image_label.show()
        QTimer.singleShot(3000, self.image_label.close)

        # Afficher le texte d'attaque
        if defenseur.hp <=0:
            if speciale:
                text = attaquant.name.split()[0] + " utilise son attaque speciale contre son adversaire et lui porte un coup fatal ! " + defenseur.name.split()[0] + " est K.O !"
            else:
                text = attaquant.name.split()[0] + " attaque son adversaire et lui porte un coup fatal ! " + defenseur.name.split()[0] + " est K.O !"
        elif degats != 0:
            if speciale:
                text = attaquant.name.split()[0] + " utilise son attaque speciale contre " + defenseur.name.split()[0] + " et lui inflige " + str(degats) + " de degats !"
            else:
                text = attaquant.name.split()[0] + " attaque " + defenseur.name.split()[0] + " et lui inflige " + str(degats) + " de degats !"
        else:
            if speciale:
                text = attaquant.name.split()[0] + " utilise son attaque speciale contre " + defenseur.name.split()[0] + " mais ce n'est pas tres efficace " + str(degats) + " degats sont infliges !"
            else:
                text = attaquant.name.split()[0] + " attaque " + defenseur.name.split()[0] + " mais ce n'est pas tres efficace " + str(degats) + " degats sont infliges !"

        self.text_label = QLabel(text, self.centralwidget)
        self.text_label.setGeometry(160, 565, 680, 145)  # Remplacez x, y, largeur et hauteur par les coordonnées et dimensions souhaitées
        self.text_label.setAlignment(Qt.AlignCenter)  # Alignement du texte au centre
        if joueur:
            self.text_label.setStyleSheet('color: black; font-size: 35px; font-family: "Minecraft";') 
        else:
            self.text_label.setStyleSheet('color: #CA453B; font-size: 35px; font-family: "Minecraft";') 
        self.text_label.setWordWrap(True)
        self.text_label.show()
        self.image_label.raise_()
        self.text_label.raise_()
        self.poke_att.lower()
        self.poke_def.lower()
        QTimer.singleShot(3000, self.text_label.close)
        QTimer.singleShot(3000, self.new_raise)

    def stop_audio(self):
        pygame.mixer.stop()  # Arrêt du son

    def play_audio(self):
        self.sound.play()  # Lancement du son

    def new_raise(self):
        self.poke_att.raise_()
        self.poke_def.raise_()

  


class Rocket(QMainWindow, Rocket_ui):
    def __init__(self, pokemon_sauvage, pokemon_utilise, pokedex_sauvages, inventaire_joueur, first_combat, parent=None):
        self.pokemon_sauvage = pokemon_sauvage # Le pokémon rencontré
        self.inventaire_joueur = inventaire_joueur # L'inventaire du joueur avec ses pokémons
        self.pokemon_utilise = pokemon_utilise # Le pokémon qu'il utilise
        self.pokedex_sauvages = pokedex_sauvages # Le pokedex avec tous les pokémons sauvages
        self.first_combat = first_combat
        self.pokemon_utilise = pokemon_utilise
        super(Rocket, self).__init__(parent)
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    pokedex = poke.Pokedex()
    adversaire = poke.Pokemon("Mewtwo",0,0,106,110,90,154,90,poke.Psy())
    inventaire_joueur = poke.InventaireJoueur()
    inventaire_joueur.ajout_inventaire(poke.Pokemon("Mew",0,0,100,100,100,100,100,poke.Psy()))
    inventaire_joueur.ajout_inventaire(poke.Pokemon("Dracaufeu",15,12,78,84,78,109,85,poke.Feu()))
    inventaire_joueur.ajout_inventaire(poke.Pokemon("Ectoplasma",0,0,60,65,60,130,75, poke.Tenebres()))
    pokemon_utilise = poke.Pokemon("Mew",0,0,100,100,100,100,100,poke.Psy())
    pokedex_sauvages = poke.Pokedex()
    pokedex_sauvages.charger_pokedex("pokemon_first_gen.csv")
    pokedex.charger_pokedex("pokemon_first_gen.csv")
    fenetre = Rocket(adversaire, pokemon_utilise, pokedex_sauvages, inventaire_joueur,True)
    fenetre.setWindowTitle("Exemple de fenêtre de combat")
    fenetre.show()
    sys.exit(app.exec_())