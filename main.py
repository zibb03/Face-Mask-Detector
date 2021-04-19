import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import cv2
from matplotlib import pyplot as plt
'''
#기본 코드
app = QApplication(sys.argv)
label = QLabel()
label.show()

app.exec_()
'''
'''
class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('My First Application')
        self.move(300, 300)
        self.resize(400, 200)
        self.show()


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())
'''
