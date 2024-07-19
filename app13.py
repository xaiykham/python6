# Messagebox
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
#ອອກແບບໜ້າຕ່າງ
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ໂປຣເເກມທົດລອງ")
        self.setFixedSize(QSize(400,250))
        #ສ້າງ layout ແລະຕັ້ງຄ່າ
        vbox=QVBoxLayout()
        self.setLayout(vbox)
        #widget
        self.btn1=QPushButton("Info")
        self.btn2=QPushButton("Warning")
        self.btn3=QPushButton("Error")
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
        if sender==self.btn1:
            QMessageBox.information(self,"ເເຈ້ງເຕືອນ","ລາຍລະອຽດໂປຣເເກມ")
        elif sender==self.btn2:
            QMessageBox.warning(self,"ເເຈ້ງເຕືອນ","ຂໍ້ຄວນລະວັງໃນການໃຊ້ງານ")
        elif sender==self.btn3:
            QMessageBox.critical(self,"ເເຈ້ງເຕືອນ","ເກີດຂໍ້ຜິດພາດໃນໂປຣເເກມ")

#ລັນໂປຣເເກມ
app=QCoreApplication.instance()
if app is None:
    app=QApplication([])

window = MainWindow()
window.show()
app.exec()