import sys
import cv2
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer


### IMPORTANT: IL FAUT INSTALLER OPENCV AVEC LA COMMANDE SUIVANTE: pip install opencv-python


class VideoPlayer(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.loop_video = True  # Définir loop_video à True par défaut
        
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle("Video Player")
        
        # Create a timer for video playback
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        
        # Load video from file
        self.video_path = "Fonds/Pikachu Pixel Animated Loop.mp4"  # Replace with your video file path
        self.cap = cv2.VideoCapture(self.video_path)
        
        # Start video playback
        self.start_video()
        
        # Create a layout for the player
        layout = QVBoxLayout(self)
        self.label = QLabel(self)
        layout.addWidget(self.label)
        
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
            self.label.setPixmap(pixmap)
            
            # Resize the window to match the size of the video
            self.resize(w, h)
        else:
            # Rewind video to the beginning if looping is enabled
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
    sys.exit(app.exec_())
