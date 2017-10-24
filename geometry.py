import sys
from PyQt5.QtWidgets import QApplication, QWidget

#The Window class inherits from QWidget class.
class Window(QWidget):

    #Initialising Window Class.
    def __init__(self):

        #Initialising QWidget class.
        super().__init__()

        self.initUI()


    #Method to initialise the window.
    def initUI(self):

        '''
        self.resize(500, 500)
        '''

        '''
        self.move(100,100)
        '''

        '''
        self.setGeometry(1000, 1000, 50, 400)
        '''

        self.setWindowTitle('Geometry Management')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
