# ตกแต่ง widget ผ่าน selector
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
        vbox.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.setLayout(vbox)
        #widget
        lb=QLabel("KongRuksiam")
        btn1=QPushButton("Open")
        btn2=QPushButton("Save")
        btn3=QPushButton("Exit")
        btn3.setObjectName("danger")
        lb.setObjectName("danger")
        #add widget to layout
        vbox.addWidget(lb)
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)

#ລັນໂປຣເເກມ
app=QCoreApplication.instance()
if app is None:
    app=QApplication([])
    with open('style.qss','r') as style:
        app.setStyleSheet(style.read())

window = MainWindow()
window.show()
app.exec()