
import sys
import os
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QMovie

class GIFWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Affichage d'un GIF")
        self.setGeometry(100, 100, 300, 300)

        # Création du QLabel pour afficher le GIF
        script_dir = os.path.dirname(__file__)
        image_path = os.path.join(script_dir, "Pokémons/Pikachu", "Pikachu_face.gif")
        self.gif_label = QLabel(self)
        self.gif_label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.gif_label)

        # Chargement du GIF
        self.movie = QMovie(image_path)
        self.gif_label.setMovie(self.movie)

        # Démarre la lecture du GIF
        self.movie.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gif_window = GIFWindow()
    gif_window.show()
    sys.exit(app.exec_())
