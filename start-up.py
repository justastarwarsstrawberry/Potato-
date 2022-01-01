from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.resize(800, 600)
        self.setWindowTitle("RW modmaker!")
        self.setCentralWidget(QtWidgets.QWidget())
        self.initUI()
    
    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setObjectName("label")
        self.label.setText("Welcome to the mod maker for RW!")
        self.label.setGeometry(int(self.width()/2),int(self.height()/2),100,100)
        self.label.setFont(QtGui.QFont('Times', 20,20,True))

        self.filemenu = self.menuBar().addMenu('File')
        self.filemenu.open = self.filemenu.addAction('Open project..').triggered.connect(lambda: self.openFileNameDialog("Open project..","","All Files (*);;Zip Files (*.zip)"))
        self.filemenu.new = self.filemenu.addAction('New project..').triggered.connect(lambda: self.newProject())
        
        self.exit = QtWidgets.QAction('Exit mod maker')
        self.exit.setShortcut("Ctrl+Q")
        self.exit.triggered.connect(lambda: QApplication.quit())
        self.filemenu.addAction(self.exit)
    
    def resizeEvent(self,_):
        self.label.adjustSize()
        self.label.move(int(self.width()/2-self.label.width()/2),int(self.height()/2-self.label.height()/2))
    
    def openFileNameDialog(self,name,boxtext,fileTypes):
        if not(boxtext):
            boxtext = ""
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,name, boxtext,fileTypes, options=options)
        if fileName:
            print(fileName)

    def openFileNamesDialog(self,name,boxtext,fileTypes):
        if not(boxtext):
            boxtext = ""
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self,name,boxtext,fileTypes, options=options)
        if files:
            print(files)
    
    def saveFileDialog(self,name,boxtext,fileTypes):
        if not(boxtext):
            boxtext = ""
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,name,boxtext,fileTypes, options=options)
        if fileName:
            print(fileName)

    def newProject(self):
        self.newProjectWindow = QMainWindow()
        self.newProjectWindow.setWindowTitle("New Project...")
        self.newProjectWindow.label = QtWidgets.QLabel(self.newProjectWindow)
        self.newProjectWindow.label.setText("Enter project name")
        self.newProjectWindow.label.textbox = QtWidgets.QMessageBox(self.newProjectWindow)
        self.newProjectWindow.show()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())