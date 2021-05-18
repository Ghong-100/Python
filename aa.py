import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

class WindowClass(QMainWindow):
    def __init__(self):
        print(1)

cc = uic.loadUiType("F:\\Python\\PyQt\\Practice\\2.Notepad\\aa.ui")

weather = "비"
aa = WindowClass()
if weather == "비":
    print("우산을 챙기세요")