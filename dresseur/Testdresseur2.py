# -*- coding: utf-8 -*-
"""
Created on Tue May  7 10:12:36 2024

@author: diego
"""

import sys
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QTimer

class CharacterView(QGraphicsView):
    def __init__(self):
        super().__init__()
        
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)
        
        self.character_images = {
            "up": ["haut_move2.png", "haut_move.png"],
            "down": ["bas_move2.png", "bas_move.png"],
            "left": ["gauche_move.png", "gauche_statique.png"],
            "right": ["droite_statique.png", "droite_move.png"],
            "static": ["bas_statique.png"]
        }
        
        self.direction = None
        self.current_image_index = 0
        self.static_image_index = 0  # Index de l'image statique
        self.static_image_delay = 750  # Délai avant d'afficher l'image statique
        
        self.load_images()
        self.start_timers()
        
    def load_images(self):
        self.character_pixmaps = {}
        for direction, images in self.character_images.items():
            self.character_pixmaps[direction] = [QPixmap(image) for image in images]
            
        self.character_item = self.scene.addPixmap(self.character_pixmaps["up"][0])
        
    def start_timers(self):
        # Timer pour changer d'image toutes les 150 ms
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_character)
        self.timer.start(150)
        
        # Timer pour détecter l'inactivité du joueur et afficher l'image statique
        self.inactivity_timer = QTimer()
        self.inactivity_timer.timeout.connect(self.show_static_image)
        self.inactivity_timer.start(self.static_image_delay)  # Détecte l'inactivité après 1 seconde
        
    def update_character(self):
        if self.direction:
            self.current_image_index = (self.current_image_index + 1) % len(self.character_pixmaps[self.direction])
            self.character_item.setPixmap(self.character_pixmaps[self.direction][self.current_image_index])
        
    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_Up:
            self.direction = "up"
        elif key == Qt.Key_Down:
            self.direction = "down"
        elif key == Qt.Key_Left:
            self.direction = "left"
        elif key == Qt.Key_Right:
            self.direction = "right"
            
        # Réinitialiser le timer d'inactivité à chaque pression de touche
        self.inactivity_timer.start(self.static_image_delay)
            
    def keyReleaseEvent(self, event):
        self.direction = None
        
    def show_static_image(self):
        # Afficher l'image statique "bas_statique.png"
        self.character_item.setPixmap(self.character_pixmaps["static"][self.static_image_index])
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = CharacterView()
    view.show()
    sys.exit(app.exec_())
