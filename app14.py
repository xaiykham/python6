# Input Dialog
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
        self.btn1=QPushButton("ປ້ອນຊື່")
        self.btn2=QPushButton("ປ້ອນທີ່ຢູ່")
        self.btn3=QPushButton("ເລືອກເພດ")
        #signal 
        self.btn1.clicked.connect(self.showMessage)
        self.btn2.clicked.connect(self.showMessage)
        self.btn3.clicked.connect(self.showMessage)
        #add widget to layout
        vbox.addWidget(self.btn1)
        vbox.addWidget(self.btn2)
        vbox.addWidget(self.btn3)

    def showMessage(self): #slot
        sender = self.sender()
        if sender == self.btn1:
           text,submit = QInputDialog.getText(self,"ເເຈ້ງເຕືອນ","ກະລຸນາລະບຸຊື່")
           if submit:
               QMessageBox.information(self,"ເເຈ້ງເຕືອນ","ສະບາຍດີ"+text)
        elif sender==self.btn2:
            text , submit = QInputDialog.getMultiLineText(self,"ເເຈ້ງເຕືອນ","ລະບຸທີ່ຢູ່ຂອງເຈົ້າ")
            if submit:
                QMessageBox.information(self,"ເເຈ້ງເຕືອນ","ທີ່ຢູ່ຂອງເຈົ້າ "+text)
        elif sender==self.btn3:
            items=["ຊາຍ","ຍິງ","ບໍ່ລະບຸ"]
            text,submit = QInputDialog.getItem(self,"ເເຈ້ງເຕືອນ","ເລືອກເພດ",items)
            if submit:
                QMessageBox.information(self,"ເເຈ້ງເຕືອນ","ເພດຂອງເຈົ້າ "+text)

#ລັນໂປຣເເກມ
app=QCoreApplication.instance()
if app is None:
    app=QApplication([])

window = MainWindow()
window.show()
app.exec()