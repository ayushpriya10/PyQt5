
import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtCore import QCoreApplication


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        #Creating instance of the QPushButton class.
        qbtn = QPushButton('Quit', self)

        #Connecting Action to the button.
        qbtn.clicked.connect(QCoreApplication.instance().quit)

        #Positioning the button.
        qbtn.move(50, 50)

        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Button Widget')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
