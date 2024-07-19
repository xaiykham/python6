# Multiple Windows
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
#ອອກແບບໜ້າຕ່າງ
class AboutWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ຂໍ້ມູນ")
        self.setFixedSize(QSize(400,300))
        #สร้าง layout และตั้งค่า
        vbox = QVBoxLayout()
        vbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(vbox)
        #widget
        lb=QLabel("ຜູ້ພັດທະນາໂປຣເເກມ ຊາຍຄຳ ທຳມະຈັກ")
        #add widget to layout
        vbox.addWidget(lb)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ໂປຣເເກມຂອງເຮົາ")
        self.setFixedSize(QSize(350,250))
        #สร้าง layout และตั้งค่า
        vbox = QVBoxLayout()
        vbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(vbox)
        #widget
        self.about=None
        btn1=QPushButton("ເພີ່ມເຕີມ")
        btn1.clicked.connect(self.display)
        #add widget to layout
        vbox.addWidget(btn1)

    def display(self):
        if self.about is None:
            self.about=AboutWindow()
            self.about.show()
            
#ລັນໂປຣເເກມ
app=QCoreApplication.instance()
if app is None:
    app=QApplication([])

window = MainWindow()
window.show()
app.exec()