import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Change on Hover")

        # Créer une étiquette pour afficher l'image
        self.image_label = QLabel(self)
        self.image_label.setGeometry(100, 100, 200, 200)  # Définir les dimensions de l'étiquette
        self.image_label.setPixmap(QPixmap("Starter/Bulbizarre_face.png"))  # Charger l'image initiale
        self.image_label.setScaledContents(True)  # Ajuster l'image à la taille de l'étiquette

        # Connecter les signaux enterEvent et leaveEvent à leurs fonctions respectives
        self.image_label.enterEvent = self.enter_image
        self.image_label.leaveEvent = self.leave_image

    def enter_image(self, event):
        # Charger et afficher une nouvelle image lorsque la souris passe dessus
        self.image_label.setPixmap(QPixmap("Starter/Bulbizarre_clic.png"))

    def leave_image(self, event):
        # Recharger et afficher l'image d'origine lorsque la souris quitte l'image
        self.image_label.setPixmap(QPixmap("Starter/Bulbizarre_face.png"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.setGeometry(100, 100, 400, 400)  # Définir les dimensions de la fenêtre
    window.show()
    sys.exit(app.exec_())
