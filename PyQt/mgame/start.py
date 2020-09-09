import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QSplitter, QFrame, QHBoxLayout, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import *

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Mgame NameCard')
        self.setWindowIcon(QIcon('d:/30_STUDY/python/PyQt/icon.jpg'))
        self.setGeometry(150,150,500,600)
        # self.move(250, 100)
        #self.resize(400, 200)
        # Button
        
        #btn = QPushButton("Quit", self)
        #btn.setToolTip('This is a <b>Button</b>ddddd www')
        #btn.move(50,50)
        #btn.resize(btn.sizeHint())
        #btn.clicked.connect(QCoreApplication.instance().quit)

        hbox = QHBoxLayout()

        m_topFrame = QFrame()
        m_topFrame.setFrameShape(QFrame.StyledPanel)
        
        m_bottomFrame = QFrame()
        m_bottomFrame.setFrameShape(QFrame.StyledPanel)
        
        splitter = QSplitter(Qt.Vertical)
        splitter.addWidget(m_topFrame)
        splitter.addWidget(m_bottomFrame)

        pixmap = QPixmap("D:\30_STUDY\python\PyQt\card.gif")
        img = QLabel()
        img.setPixmap(pixmap)
        img.show()

        splitter.addWidget(img)

        hbox.addWidget(splitter)
        img.show()
        splitter.show()
        #self.setLayout(hbox)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())