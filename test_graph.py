import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Exemple PyQt')
        self.setGeometry(100, 100, 300, 200)

        self.label = QLabel('Bonjour PyQt !', self)
        self.label.move(50, 50)

        self.button = QPushButton('Cliquez-moi', self)
        self.button.move(50, 100)
        self.button.clicked.connect(self.on_button_click)

    def on_button_click(self):
        self.label.setText('Bouton cliqué !')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
