import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':

    #Application Object is a neccesity.
    #sys.argv is used to obtain the parameters.
    app = QApplication(sys.argv)

    #The QWidget class is the base class for all UI.
    window = QWidget()

    #Doesn't the name gives it away? ;)
    window.setWindowTitle('First GUI!')

    #Display what you made!
    window.show()

    #app.exec_() runs the mainloop of the application.
    #sys.exit() informs the environment about the termination.
    sys.exit(app.exec_())
