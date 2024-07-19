# กำหนดขนาด Widget
from PyQt6.QtCore import QCoreApplication,QSize
from PyQt6.QtWidgets import QApplication,QWidget,QPushButton,QVBoxLayout

#ອອກແບບໜ້າຕ່າງ
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ໂປຣເເກມທົດລອງ")
        self.setFixedSize(QSize(400,300))
        #สร้าง layout และตั้งค่า
        vbox = QVBoxLayout(self)
        #button widget
        btn1=QPushButton("1")
        btn2=QPushButton("2")
        btn2.setFixedSize(QSize(30,50))
        #จัดวาง widget ใน layout
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)

#ລັນໂປຣເເກມ
app=QCoreApplication.instance()
if app is None:
    app=QApplication([])

window = MainWindow()
window.show()
app.exec()