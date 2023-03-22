# author jinyunlong
# createtime 2023/3/20 11:22
# 职业 锅炉房保安

import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QGraphicsView, QGraphicsPixmapItem, \
    QFileDialog, QMessageBox, QGraphicsScene
from PyQt5.QtGui import QPixmap, QImageReader, QPainter
from PyQt5.QtCore import Qt, QRectF, QBuffer

class RandomCatApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.current_cat_data = None

    def init_ui(self):
        self.setWindowTitle('Random Cat App')
        self.setGeometry(300, 300, 400, 400)

        layout = QVBoxLayout()

        self.get_cat_button = QPushButton('Get Random Cat', self)
        self.get_cat_button.clicked.connect(self.get_random_cat)
        layout.addWidget(self.get_cat_button)

        self.save_cat_button = QPushButton('Save Cat Image', self)
        self.save_cat_button.clicked.connect(self.save_cat_image)
        layout.addWidget(self.save_cat_button)

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
            pixmap = pixmap.scaled(self.cat_view.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.current_cat_data = img_data
            self.update_cat_view(pixmap)
        else:
            QMessageBox.warning(self, 'Error', 'Failed to get cat image. Please try again.')

    def update_cat_view(self, pixmap):
        scene = QGraphicsScene(self)
        item = QGraphicsPixmapItem(pixmap)
        item.setPos((self.cat_view.width() - pixmap.width()) / 2, (self.cat_view.height() - pixmap.height()) / 2)
        scene.addItem(item)
        self.cat_view.setScene(scene)

    def save_cat_image(self):
        if self.current_cat_data:
            options = QFileDialog.Options()
            options |= QFileDialog.ReadOnly
            file_name, _ = QFileDialog.getSaveFileName(self, "Save Cat Image", "", "Images (*.png *.xpm *.jpg);;All Files (*)", options=options)
            if file_name:
                with open(file_name, 'wb') as f:
                    f.write(self.current_cat_data)
                QMessageBox.information(self, 'Success', f'Image saved as {file_name}')
        else:
            QMessageBox.warning(self, 'Error', 'No cat image to save. Please get a cat image first.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    random_cat_app = RandomCatApp()
    random_cat_app.show()
    sys.exit(app.exec_())
