# author jinyunlong
# createtime 2023/3/8 9:22
# 职业 锅炉房保安
import json
import re

import requests
from PyQt5.QtWidgets import QApplication
from qtpy import uic

class MainWindow:
    def __init__(self):
        #从文件中加载UI定义
        self.ui = uic.loadUi("ui/HttpTestDemo.ui")

        #绑定slot为发送请求按钮函数
        self.ui.pushButton.clicked.connect(self.request_send)
        #绑定slot为添加请求头按钮函数
        self.ui.pushButton_2.clicked.connect(self.add_header)
        #绑定slot为删除最后一行请求头按钮函数
        self.ui.pushButton_3.clicked.connect(self.delete_header)
        #绑定slot为清除返回结果按钮函数
        self.ui.pushButton_4.clicked.connect(self.clear_response)
        #绑定slot为仅显示请求返回体按钮函数
        self.ui.pushButton_5.clicked.connect(self.show_some_response)
        # 连接下拉框的信号和槽函数
        self.ui.comboBox.currentIndexChanged.connect(self.request_send)
        # 连接获取url内容的信号和槽函数
        self.ui.lineEdit.textChanged.connect(self.request_send)
        # 连接获取请求体内容的信号和槽函数
        self.ui.plainTextEdit.textChanged.connect(self.request_send)
        # 再定义一个按钮槽函数
        self.ui.pushButton.clicked.connect(self.pushButton_clicked)
        # 定义成员变量存储请求和响应信息
        self.request_response = ""
        self.selected_text = ""
        self.url = ""
        self.headers = ""
        self.params_dict = ""
        self.json_data = ""

    def request_send(self):
        try:
            #获取下拉框请求方法
            self.selected_text = self.ui.comboBox.currentText()
            #获取http url地址
            self.url = self.ui.lineEdit.text()
            #获取消息体
            resquest_body = self.ui.plainTextEdit.toPlainText()
            self.params_dict = dict(resquest_body.split('=') for resquest_body in resquest_body.split('&'))
            self.json_data = json.dumps(self.params_dict)

            # print(self.json_data)

            self.headers = {} #创建空字典存放http header

            # 遍历表格中的所有行和列
            for row in range(self.ui.tableWidget.rowCount()):
                for column in range(self.ui.tableWidget.columnCount()):
                    # 获取单元格的文本内容
                    item = self.ui.tableWidget.item(row, column)
                    key = str(self.ui.tableWidget.item(row, 0).text())  # 获取行索引为0列索引为column的单元格文本作为key
                    value = item.text()
                    self.headers[key] = value

            # print(self.headers)

        except Exception as e:
            print(e.args)

    def pushButton_clicked(self):
        try:
            if self.selected_text == "GET":
                response = requests.get(self.url, params=self.params_dict, headers=self.headers)
            elif self.selected_text == "POST":
                response = requests.post(self.url, json=self.json_data, headers=self.headers)

            self.request_response = r'发送请求为:请求方法:{},请求地址:{},请求头:{},请求参数:{}'.format(
                self.selected_text, self.url, self.headers, self.json_data)
            self.request_response += '-------------------------------------\n'
            self.request_response += r'接收返回报文为:响应头:{},返回体:{}'.format(
                response.headers, json.loads(response.content.decode('unicode_escape')))
            #
            # # 将信息输出到控制台
            # print(self.request_response)
            # 在 textBrowser 中显示请求和响应信息
            self.ui.textBrowser.append(self.request_response)
        except Exception as e:
            print(e.args)

    def clear_response(self):
        self.ui.textBrowser.clear()

    def show_some_response(self):
        try:
            #获取文本
            text_browser_content = self.ui.textBrowser.toPlainText()
            # print(text_browser_content)

            # 从请求参数中提取 JSON 数据
            request_json_str = re.search(r'请求参数:(\{.*?\})', text_browser_content).group(1)
            request_json = json.loads(request_json_str)
            # print(request_json)

            # 从返回体中提取 JSON 数据
            response_json_str = re.search(r'返回体:(\{.*?\})', text_browser_content).group(1)
            response_json = response_json_str
            # print(response_json)

            self.ui.textBrowser.clear()

            self.ui.textBrowser.append(r'请求参数:{}'.
                                       format(request_json))
            self.ui.textBrowser.append('-------------------------------------')
            self.ui.textBrowser.append(r'返回体:{}'.
                                       format(response_json))
        except Exception as e:
            print(e.args)


    def delete_header(self):
        # 获取最后一行的行数
        last_row = self.ui.tableWidget.rowCount() - 1
        # 删除最后一行
        self.ui.tableWidget.removeRow(last_row)

    def add_header(self):
        # 在表格中插入一行
        row_position = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(row_position)


if __name__ == '__main__':
    app_window = QApplication([])
    mainWindow = MainWindow()
    mainWindow.ui.show()
    app_window.exec_()
