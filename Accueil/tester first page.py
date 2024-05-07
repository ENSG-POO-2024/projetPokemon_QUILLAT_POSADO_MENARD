import sys
import cv2
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer
from FirstOnePage import Ui_MainWindow  # Importer la classe Ui_MainWindow du fichier mainwindow.py


class VideoPlayer(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()  # Instancier la classe Ui_MainWindow
        self.ui.setupUi(self)  # Configurer le MainWindow à l'aide de Ui_MainWindow
        self.loop_video = True  # Définir loop_video à True par défaut
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Video Player")
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.video_path = "Fonds/Pikachu Pixel Animated Loop.mp4"  # Replace with your video file path
        self.cap = cv2.VideoCapture(self.video_path)
        self.start_video()

    def start_video(self):
        self.timer.start(30)  # 30 ms per frame

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb_image.shape
            bytes_per_line = ch * w
            q_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(q_image)
            self.ui.Pokemon2.setPixmap(pixmap)  # Afficher la vidéo sur l'étiquette label
            self.ui.Pokemon2.resize(w, h)  # Redimensionner l'étiquette pour s'adapter à la taille de la vidéo

            # Afficher l'image Pokémon_logo.png au-dessus de la vidéo
            

        else:
            if self.loop_video:
                self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            else:
                self.stop_video()

    def stop_video(self):
        self.timer.stop()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VideoPlayer()
    window.show()
    window.resize(app.desktop().size())  # Redimensionner la fenêtre pour couvrir tout l'écran
    window.showNormal()
    sys.exit(app.exec_())
