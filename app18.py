# Image
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap
#ອອກແບບໜ້າຕ່າງ
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ໂປຣເເກມທົດລອງ")
        #ສ້າງ layout ແລະຕັ້ງຄ່າ
        hbox=QHBoxLayout()
        self.setLayout(hbox)
        #widget
        img = QPixmap("programmer.png")
        label = QLabel()
        label.setPixmap(img)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        #add widget to layout
        hbox.addWidget(label)


#ລັນໂປຣເເກມ
app=QCoreApplication.instance()
if app is None:
    app=QApplication([])

window = MainWindow()
window.show()
app.exec()