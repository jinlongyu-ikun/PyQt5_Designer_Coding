# author jinyunlong
# createtime 2023/3/16 9:52
# 职业 锅炉房保安
import os
import time

from PyQt5.QtCore import QFile, QTextStream
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QFileDialog, QMessageBox
from utils.img_to_char_scale import img2charTxt
from utils.gif_to_char import gif2char


class CharApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Image、GIF转换字符画工具')
        self.setGeometry(100, 100, 600, 300)
        self.setMinimumSize(500, 300)

        file = QFile("ui/style.css")
        file.open(QFile.ReadOnly | QFile.Text)
        stream = QTextStream(file)
        self.setStyleSheet(stream.readAll())

        # 设置应用程序的图标
        icon = QIcon('ui/icon.jpg')
        self.setWindowIcon(icon)

        # 添加各种窗口部件
        self.label = QLabel('选择图片：', self)
        self.label.move(20, 20)
        self.label.resize(120, 20)

        self.filepath_edit = QLineEdit(self)
        self.filepath_edit.move(150, 20)
        self.filepath_edit.resize(250, 20)

        self.select_button = QPushButton('选择', self)
        self.select_button.move(410, 20)
        self.select_button.resize(80, 20)
        self.select_button.clicked.connect(self.select_file)

        self.scale_label = QLabel('缩放比例：', self)
        self.scale_label.move(20, 60)
        self.scale_label.resize(120, 20)

        self.scale_edit = QLineEdit(self)
        self.scale_edit.move(150, 60)
        self.scale_edit.resize(80, 20)
        self.scale_edit.setText('0.6')

        self.output_label = QLabel('输出文件：', self)
        self.output_label.move(20, 100)
        self.output_label.resize(120, 20)

        self.output_edit = QLineEdit(self)
        self.output_edit.move(150, 100)
        self.output_edit.resize(250, 20)
        self.output_edit.setText('图片转字符画后建议用notepad打开哦')

        self.output_button = QPushButton('保存', self)
        self.output_button.move(410, 100)
        self.output_button.resize(80, 20)
        self.output_button.clicked.connect(self.output_file)

        self.convert_button = QPushButton('图片转字符画', self)
        self.convert_button.move(150, 150)
        self.convert_button.resize(150, 50)
        self.convert_button.clicked.connect(self.convert_image_to_char)

        self.gif_button = QPushButton('GIF转字符画', self)
        self.gif_button.move(350, 150)
        self.gif_button.resize(150, 50)
        self.gif_button.clicked.connect(self.convert_gif_to_char)

    def select_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, '选择文件', '', 'Images (*.png *.xpm *.jpg *.bmp *.gif)')
        if filename:
            self.filepath_edit.setText(filename)
            output_dir = os.path.dirname(filename)
            self.output_edit.setText(os.path.join(output_dir, 'output.txt'))
            self.output_edit.setEnabled(False)

    def output_file(self):
        filename, _ = QFileDialog.getSaveFileName(self, '保存文件', '', 'Text files (*.txt)')
        if filename:
            self.output_edit.setText(filename)

    def convert_image_to_char(self):
        try:
            filename = self.filepath_edit.text()
            scale = float(self.scale_edit.text())
            output_file = self.output_edit.text()

            # 调用图片转字符画函数
            img2charTxt(filename, scale, output_file)
            output_path = os.getcwd()
            output_path = os.path.abspath(output_path)
            new_gif_path = os.path.join(output_path, output_file)

            # 成功处理提示框
            QMessageBox.information(self, '成功', '处理成功！')
            QMessageBox.information(self, '完成', f'字符画已保存至{new_gif_path}！')

            # 打开txt文件
            if os.path.exists(output_file):
                os.startfile(output_file)

        except Exception as e:
            # 处理失败提示框
            QMessageBox.warning(self, '失败', str(e))

    def convert_gif_to_char(self):
        try:
            # 获取输入和输出文件路径
            input_filename = self.filepath_edit.text()
            scale = float(self.scale_edit.text())
            # output_filename = self.output_edit.text()

            # 判断输入文件是否为gif格式
            if not input_filename.lower().endswith('.gif'):
                raise ValueError('输入文件必须为gif格式！')

            # 判断输出文件是否为gif格式，如果不是，则自动加上后缀名
            # if not output_filename.lower().endswith('.gif'):
            #     output_filename += '.gif'

            QMessageBox().information(self,'请等待','点击"OK"开始处理,请等待"处理成功"提示出现...')

            # 调用GIF转字符画函数
            output_filename = gif2char(input_filename, scale, font_file='arial.ttf')
            output_path = os.getcwd()
            output_path = os.path.abspath(output_path)
            new_gif_path = os.path.join(output_path, output_filename)

            # 成功处理提示框
            QMessageBox.information(self, '成功', '处理成功！')
            QMessageBox.information(self, '完成', f'字符画已保存至{new_gif_path}！')
            time.sleep(1)
            os.startfile(new_gif_path)

        except Exception as e:
            # 处理失败提示框
            QMessageBox.warning(self, '失败', str(e))


if __name__ == '__main__':
    app_window = QApplication([])
    mainWindow = CharApp()
    mainWindow.show()
    app_window.exec_()
