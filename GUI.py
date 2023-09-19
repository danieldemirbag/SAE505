from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class TextEditDemo(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.i = 0
        self.setWindowTitle("︻╦╤─")
        self.resize(500, 470)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = TextEditDemo()
    win.show()
    sys.exit(app.exec_())