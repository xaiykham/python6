# LineEdit & TextEdit
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
#ອອກແບບໜ້າຕ່າງ
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ໂປຣເເກມທົດລອງ")
        self.setFixedSize(QSize(350,250))
        #ສ້າງ layout ແລະຕັ້ງຄ່າ
        vbox = QVBoxLayout()
        vbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(vbox)
        #nested layout
        grid = QGridLayout()
        grid.setAlignment(Qt.AlignmentFlag.AlignTop)
        grid.setSpacing(10)
        vbox.addLayout(grid)

        #Input Name
        grid.addWidget(QLabel('ຊື່-ນາມສະກຸນ'),0,0)
        self.editName=QLineEdit()
        self.editName.textChanged.connect(self.previewData)
        grid.addWidget(self.editName,0,1)
        #Input Address
        grid.addWidget(QLabel('ທີ່ຢູ່'),1,0)
        self.editAddress=QTextEdit()
        self.editAddress.textChanged.connect(self.previewData)
        grid.addWidget(self.editAddress,1,1)

        #ສະເເດງຜົນ
        vbox.addWidget(QLabel('Preview'))
        self.showName = QLabel()
        self.showAddress = QLabel()
        vbox.addWidget(self.showName)
        vbox.addWidget(self.showAddress)

    def previewData(self):
        sender = self.sender()
        if sender==self.editName:
            self.showName.setText(sender.text())
        elif sender==self.editAddress:
            self.showAddress.setText(sender.toPlainText())


#ລັນໂປຣເເກມ
app=QCoreApplication.instance()
if app is None:
    app=QApplication([])

window = MainWindow()
window.show()
app.exec()