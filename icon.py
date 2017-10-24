import sys
from PyQt5.QtWidgets import QApplication, QWidget

#A new Import!
from PyQt5.QtGui import QIcon

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle('Icon!')

    #Converting the image.
    icon = QIcon('gdg.png')

    #Adding the icon to the window.
    window.setWindowIcon(icon)

    window.show()
    sys.exit(app.exec_())
