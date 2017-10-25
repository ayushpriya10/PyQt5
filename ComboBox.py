import sys
from PyQt5.QtWidgets import QWidget, QLabel, QComboBox, QApplication

class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.label = QLabel("Ubuntu", self)

        #Creating the instance os the QcomboBox class.
        self.combo = QComboBox(self)

        #Adding items to the combo box.
        self.combo.addItem("Ubuntu")
        self.combo.addItem("Mandriva")
        self.combo.addItem("Fedora")
        self.combo.addItem("Arch")
        self.combo.addItem("Gentoo")

        self.combo.move(50, 50)
        self.label.move(50, 150)

        self.combo.activated.connect(self.onActivated)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QComboBox')
        self.show()


    def onActivated(self, index):

        #Retreiving item value at given index.
        text = self.combo.itemText(index)

        self.label.setText(text)
        self.label.adjustSize()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
