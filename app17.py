# Combobox
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
#ອອກແບບໜ້າຕ່າງ
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ໂປຣເເກມທົດລອງ")
        self.setFixedSize(QSize(400,250))
        #ສະບາຍດີ layout และตั้งค่า
        vbox=QVBoxLayout()
        self.setLayout(vbox)
        #widget
        self.data=["Python","C#","PHP","Java"]
        self.combobox = QComboBox()
        self.combobox.addItems(self.data)
        #signal 
        self.combobox.currentIndexChanged.connect(self.saveData)
        #add widget to layout
        vbox.addWidget(self.combobox)
    
    def saveData(self):
        index = self.combobox.currentIndex()
        QMessageBox.information(self,"ເເຈ້ງເຕືອນ",'ລາຍການທີ່ເລືອກ = '+self.data[index])


#ລັນໂປຣເເກມ
app=QCoreApplication.instance()
if app is None:
    app=QApplication([])

window = MainWindow()
window.show()
app.exec()