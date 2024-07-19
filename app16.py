# Radio Button
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
        self.radio1=QRadioButton("ຊາຍ")
        self.radio2=QRadioButton("ຍິງ")
        btnSave=QPushButton("ບັນທຶກ")
        #signal 
        btnSave.clicked.connect(self.saveData)
        #add widget to layout
        vbox.addWidget(self.radio1)
        vbox.addWidget(self.radio2)
        vbox.addWidget(btnSave)
    
    def saveData(self):
        if self.radio1.isChecked():
            QMessageBox.information(self,"ເເຈ້ງເຕືອນ","ລາຍການທີ່ເລືອກ = "+self.radio1.text())
        elif self.radio2.isChecked():
            QMessageBox.information(self,"ເເຈ້ງເຕືອນ","ລາຍການທີ່ເລືອກ = "+self.radio2.text())

#ລັນໂປຣເເກມ
app=QCoreApplication.instance()
if app is None:
    app=QApplication([])

window = MainWindow()
window.show()
app.exec()