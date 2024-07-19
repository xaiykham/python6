# Signal & Slot
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
#ອອກແບບໜ້າຕ່າງ
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ໂປຣເເກມທົດລອງ")
        self.setFixedSize(QSize(400,250))
        #สร้าง layout และตั้งค่า
        vbox=QVBoxLayout()
        self.setLayout(vbox)
        #widget
        btn1=QPushButton("Open")
        btn1.clicked.connect(self.showName)#signal
        #add widget to layout
        vbox.addWidget(btn1)

    def showName(self): #slot
        print(self.sender().text())

#ລັນໂປຣເເກມ
app=QCoreApplication.instance()
if app is None:
    app=QApplication([])

window = MainWindow()
window.show()
app.exec()