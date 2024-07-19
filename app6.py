# grid layout
from PyQt6.QtCore import QCoreApplication
from PyQt6.QtWidgets import QApplication,QWidget,QPushButton,QGridLayout

#ອອກແບບໜ້າຕ່າງ
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ໂປຣເເກມ")
        #ສ້າງ layout ແລະຕັ້ງຄ່າ
        grid = QGridLayout()
        self.setLayout(grid)
        #button widget
        btn1=QPushButton("1")
        btn2=QPushButton("2")
        btn3=QPushButton("3")
        btn4=QPushButton("4")
        #จัดวาง widget ใน layout
        grid.addWidget(btn1,0,0)
        grid.addWidget(btn2,0,1)
        grid.addWidget(btn3,1,0)
        grid.addWidget(btn4,1,1)

#ລັນໂປຣເເກມ
app=QCoreApplication.instance()
if app is None:
    app=QApplication([])

window = MainWindow()
window.show()
app.exec()