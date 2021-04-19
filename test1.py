''''## Ex 5-1. QPushButton.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton('Button1', self)
        btn1.setCheckable(True)
        #btn1.toggle()

        btn2 = QPushButton('Button2', self)
        btn2.setCheckable(True)
        #btn2.setText('Button2')

        btn3 = QPushButton('Button3', self)
        btn3.setCheckable(True)
        #btn3.setEnabled(False)

        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)

        self.setLayout(vbox)
        self.setWindowTitle('QPushButton')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())'''

## Ex 5-2. QLabel.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import cv2

#img = cv2.imread("C:/Users/user/Documents/GitHub/Face Mask Detector/Photo/people1.jpg")
#pixmap = cv2.resize(img, 272, 202)

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        pixmap1 = QPixmap("C:/Users/user/Documents/GitHub/Face Mask Detector/Photo/people1.jpg")
        pixmap2 = QPixmap("C:/Users/user/Documents/GitHub/Face Mask Detector/Photo/people mask.jpg")

        label1 = QLabel()

        label1.lbl_img = QLabel()
        #label1.lbl_img.resize(272, 202)
        label1.lbl_img.setPixmap(pixmap1)
        label1.lbl_size = QLabel('Width: ' + str(pixmap1.width()) + ', Height: ' + str(pixmap1.height()))
        label1.lbl_size.setAlignment(Qt.AlignCenter)

        label2 = QLabel()

        label2.lbl_img = QLabel()
        # label1.lbl_img.resize(272, 202)
        label2.lbl_img.setPixmap(pixmap2)
        label2.lbl_size = QLabel('Width: ' + str(pixmap2.width()) + ', Height: ' + str(pixmap2.height()))
        label2.lbl_size.setAlignment(Qt.AlignCenter)

        #label2 = QLabel('Second Label', self)
        #label2.setAlignment(Qt.AlignVCenter)

        #font2 = label2.font()
        #font2.setFamily('Times New Roman')
        #font2.setBold(True)

        #label2.setFont(font2)

        btn1 = QPushButton('Button1', self)
        btn1.setCheckable(True)
        # btn1.toggle()

        btn2 = QPushButton('Button2', self)
        btn2.setCheckable(True)
        # btn2.setText('Button2')

        btn3 = QPushButton('Button3', self)
        btn3.setCheckable(True)
        # btn3.setEnabled(False)

        vbox = QVBoxLayout()
        vbox.addWidget(label1.lbl_img)
        vbox.addWidget(label1.lbl_size)
        vbox.addWidget(label2.lbl_img)
        vbox.addWidget(label2.lbl_size)
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)

        self.setLayout(vbox)
        self.setWindowTitle('QPixmap')
        self.move(300, 300)

        self.setGeometry(300, 300, 300, 200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())