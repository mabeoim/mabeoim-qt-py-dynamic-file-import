import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QComboBox, QWidget


class combo(QComboBox):
    def __init__(self, title, parent):
        super(combo, self).__init__(parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        if e.mimeData().hasText():
            e.accept()
        else:
            e.ignore()

    # import config file content and execute
    # import_module might be a better alternative if this wont work with the real config file
    def dropEvent(self, e):
        config = open(e.mimeData().text()).read()
        exec(config, globals())
        print(i)
        print(strs)
        greeting()


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        lo = QtWidgets.QFormLayout()
        lo.addRow(QtWidgets.QLabel(
            "Type some text in textbox and drag it into combo box"))
        edit = QtWidgets.QLineEdit()
        edit.setDragEnabled(True)
        com = combo("Button", self)
        lo.addRow(edit, com)
        self.setLayout(lo)
        self.setWindowTitle('Simple drag & drop')


def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec()


if __name__ == '__main__':
    main()
