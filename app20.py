# Table Widget
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
        #widget
        headers=["ຊື່","ຕຳເເໜ່ງ","ເງິນເດືອນ"]
        employees=[
            ('ຊາຍ','ໂປຣເເກມເມີ້',25000),
            ('ໂຈ','ກາບຟິກ',28000),
            ('ໂນ່','ຝ່າຍການຕະຫລາດ',45000),
            ('ນ້ຳຝົນ','ຝ່າຍບັນຊີ',40000),
            ('ຟ້າ','ຝ່າຍຂາຍ',50000)
        ]
        table=QTableWidget(len(employees),len(headers))
        #set headers
        for i , h in enumerate(headers):
            table.setHorizontalHeaderItem(i,QTableWidgetItem(h))
        #set row data
        for r , rows in enumerate(employees):
            for c , data in enumerate(rows):
                if c==2:
                    item = f'{data:,}'
                else:
                    item = str(data)
                table.setItem(r,c,QTableWidgetItem(item))
        
        #table style
        table.horizontalHeader().setStyleSheet('::section{background:pink}')
        table.verticalHeader().setStyleSheet('::section{background:red}')
        #add widget to layout
        vbox.addWidget(table)

#ລັນໂປຣເເກມ
app=QCoreApplication.instance()
if app is None:
    app=QApplication([])

window = MainWindow()
window.show()
app.exec()