from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.resize(800, 600)
        self.setWindowTitle("RW modmaker!")
        self.setCentralWidget(QtWidgets.QWidget(self))
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setObjectName("label")
        self.label.setText("Welcome to the mod maker for RW!")
        self.label.setGeometry(int(self.width()/2),int(self.height()/2),100,100)
        self.label.adjustSize()

        self.filemenu = self.menuBar().addMenu('File')
        self.filemenu.open = self.filemenu.addAction('Open project..')
        self.filemenu.new = self.filemenu.addAction('New project..')

        #filemenu.open.triggered.connect(lambda: })
        self.exit = QtWidgets.QAction('exit app',self)
        self.exit.setShortcut("Ctrl+Q")
        self.exit.triggered.connect(lambda: QApplication.quit())
        self.filemenu.addAction(self.exit)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())