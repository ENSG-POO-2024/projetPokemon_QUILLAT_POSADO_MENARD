from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget, QScrollArea, QGridLayout, QLabel
from PyQt5 import QtCore, QtGui, QtWidgets
class ScrollableButtonWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Scrollable Button Example")
        self.setGeometry(0, 0, 1000, 750)

        # Créer un widget central
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Créer un layout vertical
        layout = QVBoxLayout(central_widget)

        # Créer une QScrollArea
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)  # Permettre à la zone de défilement de redimensionner son contenu

        # Créer un widget pour contenir les boutons
        button_widget = QWidget(scroll_area)
        button_layout = QGridLayout(button_widget)
        button_widget.setLayout(button_layout)

        # Créer et ajouter des boutons et des labels au layout
        for i in range(20):  # 4 colonnes x 3 lignes = 12 boutons
            bouton = QPushButton()
            bouton.setStyleSheet("QPushButton { border: 2px solid black; } QPushButton QLabel { qproperty-alignment: AlignCenter; } ")
            label = QLabel(f"Button {i+1}")
            label.setAlignment(QtCore.Qt.AlignCenter)
            vbox = QVBoxLayout()
            vbox.addWidget(bouton)
            vbox.addWidget(label)
            button_layout.addLayout(vbox, i // 4, i % 4)  # Organiser les boutons et les labels dans une grille 4x3
            bouton.setFixedSize(200, 200)

        # Définir le widget contenu de la QScrollArea
        scroll_area.setWidget(button_widget)

        # Ajouter la QScrollArea au layout principal
        layout.addWidget(scroll_area)

if __name__ == "__main__":
    app = QApplication([])
    window = ScrollableButtonWindow()
    window.show()
    app.exec_()
