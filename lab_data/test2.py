## Ex 4-2. 박스 레이아웃.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        pixmap1 = QPixmap("C:/Users/user/Documents/GitHub/Face Mask Detector/Photo/people1.jpg")
        pixmap2 = QPixmap("C:/Users/user/Documents/GitHub/Face Mask Detector/Photo/people mask.jpg")

        okButton = QPushButton('OK')
        cancelButton = QPushButton('Cancel')

        label1 = QLabel()

        label1.lbl_img = QLabel()
        #label1.lbl_img.resize(272, 202)
        label1.lbl_img.setPixmap(pixmap1)
        #label1.setContentsMargins(10, 10, 10, 10)
        #label1.lbl_size = QLabel('Width: ' + str(pixmap1.width()) + ', Height: ' + str(pixmap1.height()))
        #label1.lbl_size.setAlignment(Qt.AlignCenter)

        label2 = QLabel()

        label2.lbl_img = QLabel()
        # label1.lbl_img.resize(272, 202)
        label2.lbl_img.setPixmap(pixmap2)
        #label2.setContentsMargins(10, 10, 10, 10)
        #label2.lbl_size = QLabel('Width: ' + str(pixmap2.width()) + ', Height: ' + str(pixmap2.height()))
        #label2.lbl_size.setAlignment(Qt.AlignCenter)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(label1.lbl_img)

        hbox.addWidget(label2.lbl_img)
        hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(3)
        vbox.addLayout(hbox)
        vbox.addWidget(okButton)
        vbox.addWidget(cancelButton)
        vbox.addStretch(1)

        self.setLayout(vbox)

        self.setWindowTitle('Box Layout')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())