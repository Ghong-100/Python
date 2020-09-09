import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("D:\\30_STUDY\\python\\PyQt\\Practice\\2.Notepad\\notepad.ui")[0]

class WindowClass(QMainWindow, form_class):
## Default Function
    def __init__(self):
        #  default
        super().__init__()
        self.setupUi(self)
        # MenuBar
        self.action_new.triggered.connect(self.Menu_file_new)
        self.action_open.triggered.connect(self.Menu_file_open)
        self.action_save.triggered.connect(self.Menu_file_save)
        self.action_exit.triggered.connect(self.Menu_file_exit)

## Menu Functions
    def Menu_file_new(self):
        print('new')
        self.textEdit.clear()
    
    def Menu_file_open(self):
        filename = QFileDialog.getOpenFileName(self)
        if filename[0]:
            print(filename[0])
            with open(filename[0], 'r', encoding='utf8') as f:
                data = f.read()
            self.textEdit.setText(data)
            print("open")
    
    def Menu_file_save(self):
        filename = QFileDialog.getSaveFileName(self)
        if filename[0]:
            data = self.textEdit.toPlainText()
            with open(filename[0], 'w', encoding='utf8') as f:
                f.write(data)
            print("save")

    def Menu_file_exit(self):
        self.destroy()
        print('quit')
        quit()

## Other Functions
    def func(self):
        pass


## Main 
app = QApplication(sys.argv)
mainWindow = WindowClass()
mainWindow.show()
print('init')
app.exec_()