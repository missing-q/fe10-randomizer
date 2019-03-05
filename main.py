#!python3
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import randomizedata
from functools import partial

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

        file = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        print(file)
        btn1 = QLabel("Seed", self)
        btn2 = QLineEdit("", self)
        btn3 = QPushButton("randomize", self)
        arg = partial(randomizedata.randomizedata,file, btn2.text())
        btn3.clicked.connect(arg) #VERY DANGEROUS

        #GUI Stuff
        organize = QGridLayout()
        organize.addWidget(btn1, 1, 1)
        organize.addWidget(btn2, 2, 1)
        organize.addWidget(btn3, 3, 1)
        organize.setColumnStretch(1,2)
        self.setLayout(organize)




def launchmain():
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    launchmain()
