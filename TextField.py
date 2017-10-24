
import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QLabel, QApplication

class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        #Creating instance of QLineEdit class.
        self.textBox = QLineEdit(self)
        self.textBox.move(40, 20)

        self.btn = QPushButton('Show Text', self)
        self.btn.move(40, 75)
        self.btn.clicked.connect(self.showText)

        self.label = QLabel(self)
        self.label.move(50, 150)

        self.setGeometry(300, 300, 450, 200)
        self.setWindowTitle('Text Box')
        self.show()


    def showText(self):

        #Retrieiving entered value from the text box.
        enteredText = self.textBox.text()

        #Replacing text.
        self.label.setText(enteredText)

        #Dynamic change for label's size.
        self.label.adjustSize()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
