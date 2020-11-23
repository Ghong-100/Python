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
        self.action_saveas.triggered.connect(self.Menu_file_saveas)
        self.action_exit.triggered.connect(self.close)
        self.opened = False
        self.opened_file_path = '제목 없음'

        self.action_Undo.triggered.connect(self.undoFunction)
        self.action_Copy.triggered.connect(self.copyFunction)
        self.action_Cut.triggered.connect(self.cutFunction)
        self.action_Paste.triggered.connect(self.pasteFunction)

## Menu Functions
    def save_file(self, filename):
        data = self.textEdit.toPlainText()
        with open(filename, 'w', encoding='utf8') as f:
            f.write(data)
        self.opened = True
        self.opened_file_path = filename

    def open_file(self, filename):
        print(filename)
        self.opened_file_path = filename
        with open(filename, 'r', encoding='utf8') as f:
            data = f.read()
        self.textEdit.setText(data)
        self.opened = True
        self.opened_file_path = filename
        print("open")

    def Menu_file_new(self):
        print('new')
        self.textEdit.clear()
        self.opened = False
        self.opened_file_path = ''
    
    def Menu_file_open(self):
        filename = QFileDialog.getOpenFileName(self)
        if filename[0]:
            self.open_file(filename[0])
    
    def Menu_file_save(self):
        print("save")
        if self.opened:
            self.save_file(self.opened_file_path)
        else:
            self.Menu_file_saveas()

    def Menu_file_saveas(self):
        filename = QFileDialog.getSaveFileName(self)
        if filename[0]:
            self.save_file(filename[0])
        print("saveas")

    def closeEvent(self, event):    # close할때 호출되는 기본 이벤트임. 위에 action_exit에서 close(얘도 상속받은듯)를 호출했고 그게 호출될때 이 이벤트가 호출됨.
        ret = self.save_changed_data()
        if ret == 1:
            self.save_file(self.opened_file_path)
        if ret == 2:
            event.ignore()
        print("close test!")

    def save_changed_data(self):
        msgBox = QMessageBox()
        msgBox.setText("변경 내용을 {0} 에 저장하시겠습니까?".format(self.opened_file_path))
        msgBox.addButton('저장', QMessageBox.YesRole)       # 0번
        msgBox.addButton('저장 안 함', QMessageBox.NoRole)  # 1번
        msgBox.addButton('취소', QMessageBox.RejectRole)    # 2번
        ret = msgBox.exec_()
        return ret

    def undoFunction(self):
        self.plainTextEdit.undo()
        pass

    def copyFunction(self):
        self.plainTextEdit.copy()
        pass

    def cutFunction(self):
        self.plainTextEdit.cut()
        pass

    def pasteFunction(self):
        self.plainTextEdit.paste()
        pass


## Other Functions
    def func(self):
        pass


## Main 
app = QApplication(sys.argv)
mainWindow = WindowClass()
mainWindow.show()
print('init')
app.exec_()