from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def loadUi():
    label = QtWidgets.QLabel(win)
    label.setObjectName("label")
    label.setText("Welcome to the mod maker for RW!")
    label.setGeometry(int(win.width()/2),int(win.height()/2),100,100)
    filemenu = win.menuBar().addMenu('file')
    filemenu.open = filemenu.addMenu('open')
    exit = QtWidgets.QAction('exit app',win)
    exit.setShortcut('Ctrl+Q')
    exit.triggered.connect(lambda: QApplication.quit())
    filemenu.addAction(exit)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.resize(800, 600)
    win.setWindowTitle("RW modmaker!")
    win.setCentralWidget(QtWidgets.QWidget(win))
    loadUi()
    win.show()
    sys.exit(app.exec_())