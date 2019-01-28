#!python3
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Main(QWidget):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        #UI Stuff
        self.resize(250, 150)
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        self.setWindowTitle('FE9 Randomizer')
        self.setWindowIcon(QIcon('Assets/icon.gif'))

        #Button Stuff
        btn1 = QPushButton("a", self)
        #btn1.clicked.connect(randomize)
        btn2 = QPushButton("b", self)
        btn3 = QPushButton("c", self)

        #GUI Stuff
        organize = QGridLayout()
        organize.addWidget(btn1, 1, 1)
        organize.addWidget(btn2, 1, 2)
        organize.addWidget(btn3, 1, 3)
        self.setLayout(organize)




def launchmain():
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    launchmain()
