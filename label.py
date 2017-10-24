
import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QFont


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        #Creating instance of the QLabel class.
        label = QLabel('This text is within the label.', self)

        #Positioning the laebl.
        label.move(50, 50)

        #Formatting text.
        label.setFont(QFont('SansSerif', 10))

        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Label Widget')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
