from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exemple de coordonnées de QPushButton")
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()  # Utiliser QVBoxLayout pour organiser les boutons verticalement

        # Créer et ajouter des boutons à la VBox
        for i in range(5):  # Par exemple, 5 boutons
            bouton = QPushButton(f"Bouton {i+1}", self)
            layout.addWidget(bouton)  # Ajouter le bouton à la VBox

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def obtenir_coordonnees_boutons(self):
        layout = self.centralWidget().layout()  # Récupérer le layout de la fenêtre principale
        for i in range(layout.count()):  # Parcourir tous les éléments de la VBox
            bouton = layout.itemAt(i).widget()  # Récupérer chaque bouton
            pos = bouton.pos()  # Obtenir les coordonnées du coin supérieur gauche du bouton
            x = pos.x()
            y = pos.y()
            print(f"Coordonnées du bouton {i} : x = {x}, y = {y}")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    window.obtenir_coordonnees_boutons()  # Appel de la fonction pour obtenir les coordonnées des boutons
    app.exec_()
