import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import cv2
from matplotlib import pyplot as plt

people = cv2.imread("C:/Users/user/Documents/GitHub/Face Mask Detector/Photo/people1.jpg")
people_1 = cv2.resize (people, (400, 400))

class test(QMainWindow):
    def __init__ (self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.lbl = QLabel(self)

        self.lbl.resize(1088, 808)
        #이미지를 보여주기 위해 출력될 label의 크기를 400x400으로 설정

        pixmap = QPixmap("C:/Users/user/Documents/GitHub/Face Mask Detector/Photo/people1.jpg")
        #pixmap = people_1
        self.lbl.setPixmap(QPixmap(pixmap))

        self.resize(1088, 808)
        # 이미지를 보여주기 위해 출력될 창의 크기를 400x400으로 설정
        self.show()

if __name__ == '__main__' :
    app = QApplication(sys.argv)
    test = test()
    sys.exit(app.exec_())