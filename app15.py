# Checkbox
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
        self.check1=QCheckBox("Youtube")
        self.check2=QCheckBox("Facebook")
        self.lbStatus = QLabel("ສະຖານະ")
        self.btnSave = QPushButton("ບັນທຶກ")
        #signal 
        self.check1.stateChanged.connect(self.checkStatus)
        self.check2.stateChanged.connect(self.checkStatus)
        self.btnSave.clicked.connect(self.saveData)

        #add widget to layout
        vbox.addWidget(self.check1)
        vbox.addWidget(self.check2)
        vbox.addWidget(self.lbStatus)
        vbox.addWidget(self.btnSave)
    
    def checkStatus(self):
        sender = self.sender()
        self.lbStatus.setText("ສະຖານະ = " + sender.text()+" : "+str(sender.isChecked()))

    def saveData(self):
        items=[]
        if self.check1.isChecked():
            items.append(self.check1.text())
        if self.check2.isChecked():
            items.append(self.check2.text())
        text = "ລາຍການທີ່ເລືອກ \n"+",".join(items)
        QMessageBox.information(self,"ເເຈ້ງເຕືອນ",text)


#ລັນໂປຣເເກມ
app=QCoreApplication.instance()
if app is None:
    app=QApplication([])

window = MainWindow()
window.show()
app.exec()