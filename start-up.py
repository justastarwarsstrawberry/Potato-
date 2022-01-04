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
        self.show()
    
    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setObjectName("label")
        self.label.setText("Welcome to the mod maker for RW!")
        self.label.setGeometry(int(self.width()/2),int(self.height()/2),100,100)
        self.label.setFont(QtGui.QFont('Times', 20,20,True))

        self.filemenu = self.menuBar().addMenu('File')
        self.filemenu.open = self.filemenu.addAction('Open project..').triggered.connect(lambda: openFileNamesDialog(self,"Open project..","","All Files (*);;Zip Files (*.zip)"))
        self.filemenu.new = self.filemenu.addAction('New project..').triggered.connect(lambda: newProjectWindow())
        
        self.exit = QtWidgets.QAction('Exit mod maker')
        self.exit.setShortcut("Ctrl+Q")
        self.exit.triggered.connect(lambda: self.close())
        self.filemenu.addAction(self.exit)
    
    def resizeEvent(self,_):
        self.label.adjustSize()
        self.label.move(int(self.width()/2-self.label.width()/2),int(self.height()/2-self.label.height()/2))
        
    def closeEvent(self, event):
        close = QtWidgets.QMessageBox()
        close.setWindowTitle("Exiting...")
        close.setText("You sure?")
        close.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.Cancel)
        close = close.exec()
        if close == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

class newProjectWindow(QMainWindow):
    def __init__(self):
        super(newProjectWindow,self).__init__()
        self.setWindowTitle("New Project...")
        self.setMinimumSize(400,400)
        self.setCentralWidget(QtWidgets.QWidget())
        self.initUI()
        self.show()
    
    def initUI(self):
        
        self.projectName = QtWidgets.QLabel(self)
        self.projectName.setText("Enter project name:")
        self.projectName.textbox = QtWidgets.QLineEdit(self)
        self.projectName.textbox.resize(150,20)
        self.projectName.textbox.move(self.projectName.pos().x() + 150,self.projectName.pos().y() + 5)
        self.projectLocation = QtWidgets.QLabel(self)
        self.projectLocation.setText("Select project location(optinal):")
        self.projectLocation.adjustSize()
        self.projectLocation.move(self.projectName.pos().x(),self.projectName.pos().y() + 40)
        self.projectLocation.textbox = QtWidgets.QLineEdit(self)
        self.projectLocation.textbox.resize(150,20)
        self.projectLocation.textbox.move(self.projectLocation.pos().x() + self.projectLocation.width() + 20,self.projectLocation.pos().y())
        self.submit = QtWidgets.QPushButton(self)
        self.submit.move(300,200)
        self.submit.setText("Submit")
        self.submit.clicked.connect(lambda: (print(self.projectLocation.textbox.text()), self.close()))

def openFileNameDialog(self,name:str,boxtext:str = "",fileTypes:str = "All Files (*);;"):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    fileName, filetype = QFileDialog.getOpenFileName(self,name, boxtext,fileTypes, options=options)
    if fileName:
        return fileName, filetype

def openFileNamesDialog(self,name:str,boxtext:str = "",fileTypes:str = "All Files (*);;"):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    files, filetype = QFileDialog.getOpenFileNames(self,name,boxtext,fileTypes, options=options)
    if files:
        return files, filetype
    
def saveFileDialog(self,name:str,boxtext:str = "",fileTypes:str = "All Files (*);;"):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    fileName, filetype = QFileDialog.getSaveFileName(self,name,boxtext,fileTypes, options=options)
    if fileName:
        return fileName, filetype

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())