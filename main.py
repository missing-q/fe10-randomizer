#!python3
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import randomize
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
        self.setWindowTitle('FE10 Randomizer')
        self.setWindowIcon(QIcon('Assets/icon.gif'))

        #Button Stuff

        file = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        print(file)
        btn1 = QLabel("Seed", self)
        btn2 = QLineEdit("", self)
        btn3 = QPushButton("Randomize!", self)

        group1 = QGroupBox("Parameters", self)
        btn4 = QLabel("% Variance", group1)
        btn5 = QLineEdit("", group1)
        btn6 = QCheckBox("Randomize lords?")
        btn7 = QCheckBox("Randomize skills?")
        btn8 = QCheckBox("Randomize weapon stats?")
        btn9 = QCheckBox("Randomize weapon effects?")

        layout = QVBoxLayout(self)
        layout.addWidget(btn4)
        layout.addWidget(btn5)
        layout.addWidget(btn6)
        layout.addWidget(btn7)
        layout.addWidget(btn8)
        layout.addWidget(btn9)
        group1.setLayout(layout)

        intrestrict = QIntValidator(0, 99, self)
        btn5.setValidator(intrestrict)

        group2 = QGroupBox("Options", self)
        btn10 = QCheckBox("Lock characters to class tier")
        btn11 = QCheckBox("Add nonplayables to class pool with randomized weapons")

        layout2 = QVBoxLayout(self)
        layout2.addWidget(btn10)
        layout2.addWidget(btn11)
        group2.setLayout(layout2)

        def grab():
            print(btn2.text())
            randomize.randomizer(file, btn2.text(), {'Variance': btn5.text(), 'Lords': btn6.isChecked(), 'Skills' : btn7.isChecked(), 'Stats': btn8.isChecked(), 'Effects': btn9.isChecked()})
            msg = QMessageBox()
            msg.setText("Randomization complete!")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
        btn3.clicked.connect(grab) #VERY DANGEROUS

        #GUI Stuff
        organize = QGridLayout()
        organize.addWidget(btn1, 1, 1)
        organize.addWidget(btn2, 1, 2)
        organize.addWidget(group1, 2, 1)
        organize.addWidget(group2, 2, 2)
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
