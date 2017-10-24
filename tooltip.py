import sys
from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton, QApplication
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QFont


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        #Setting the font and size.
        QToolTip.setFont(QFont('SansSerif', 10))

        #Tooltip for the window.
        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('Quit', self)
        btn.clicked.connect(QCoreApplication.instance().quit)
        btn.move(50, 50)

        #Tooltip for the button.
        btn.setToolTip('Clicking me <b>terminates</b> the application')

        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Tooltip')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
