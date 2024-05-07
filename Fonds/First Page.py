# -*- coding: utf-8 -*-
"""
Created on Tue May  7 11:24:05 2024

@author: diego
"""

import sys
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene
from PyQt5.QtGui import QMovie, QPixmap
from PyQt5.QtCore import Qt, QTimer

class GifViewer(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle("GIF Viewer")
        self.setGeometry(100, 100, 400, 300)  # Taille de la fenêtre
        
        # Créer une scène graphique pour afficher le GIF
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)
        
        # Charger le GIF
        self.movie = QMovie("Fonds/Pikachu Pixel Animated Loop.gif")  # Remplacez "your_gif_file.gif" par le chemin de votre GIF
        self.movie.frameChanged.connect(self.update_frame)
        
        # Créer un élément de l'image animée
        self.gif_item = self.scene.addPixmap(QPixmap())
        
        # Démarrer l'animation du GIF
        self.movie.start()
        
    def update_frame(self):
        pixmap = self.movie.currentPixmap()
        self.gif_item.setPixmap(pixmap)
        self.setSceneRect(0, 0, pixmap.width(), pixmap.height())  # Ajuster la taille de la scène à celle de l'image
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = GifViewer()
    viewer.show()
    sys.exit(app.exec_())
