import sys
from PyQt5.QtWidgets import QWidget, QLabel, QCheckBox, QApplication
from PyQt5.QtCore import Qt

class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        #Creating the instance of QCheckBox class.
        checkBox = QCheckBox('This is a CheckBox', self)
        checkBox.move(150, 20)

        #Toggle method to check state.
        checkBox.toggle()
        checkBox.stateChanged.connect(self.changeText)

        self.label = QLabel(self)
        self.label.move(150, 100)

        self.setGeometry(300, 300, 550, 200)
        self.setWindowTitle('CheckBox Widget')
        self.show()


    def changeText(self, state):

        #Comparing state of checkbox with Qt's checked state indicator.
        if state == Qt.Checked:
            self.label.setText('Checked! :)')
        else:
            self.label.setText('Unchecked! :(')

        self.label.adjustSize()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
