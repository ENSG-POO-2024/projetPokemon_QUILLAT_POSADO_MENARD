import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtGui import QPixmap
from DresseurVis3u import CharacterView  # Importez la classe CharacterView depuis votre fichier où elle est définie

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Créez une instance de CharacterView
        self.character_view = CharacterView()

        # Ajoutez l'instance de CharacterView à une mise en page verticale
        layout = QVBoxLayout()
        layout.addWidget(self.character_view)
        self.setLayout(layout)

        self.setWindowTitle("MainWindow")
        self.setGeometry(0, 0, 800, 600)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
