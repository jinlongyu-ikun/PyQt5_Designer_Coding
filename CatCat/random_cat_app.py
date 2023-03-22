# author jinyunlong
# createtime 2023/3/20 11:18
# 职业 锅炉房保安

import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QGraphicsScene, QGraphicsView, \
    QMessageBox
from PyQt5.QtGui import QPixmap, QPainter

class RandomCatApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Random Cat App')
        self.setGeometry(300, 300, 400, 400)

        layout = QVBoxLayout()

        self.get_cat_button = QPushButton('Get Random Cat', self)
        self.get_cat_button.clicked.connect(self.get_random_cat)
        layout.addWidget(self.get_cat_button)

        self.cat_view = QGraphicsView(self)
        self.cat_view.setRenderHint(QPainter.Antialiasing)
        self.cat_view.setRenderHint(QPainter.SmoothPixmapTransform)
        self.cat_view.setRenderHint(QPainter.TextAntialiasing)
        layout.addWidget(self.cat_view)

        self.setLayout(layout)

    def get_random_cat(self):
        response = requests.get('https://api.thecatapi.com/v1/images/search')
        if response.status_code == 200:
            cat_data = response.json()
            cat_url = cat_data[0]['url']
            img_response = requests.get(cat_url)
            img_data = img_response.content
            pixmap = QPixmap()
            pixmap.loadFromData(img_data)
            scene = QGraphicsScene(self)
            scene.addPixmap(pixmap)
            self.cat_view.setScene(scene)
        else:
            QMessageBox.warning(self, 'Error', 'Failed to get cat image. Please try again.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    random_cat_app = RandomCatApp()
    random_cat_app.show()
    sys.exit(app.exec_())
