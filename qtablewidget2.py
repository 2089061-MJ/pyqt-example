import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QStandardItemModel, QStandardItem

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        window = QWidget()
        layout = QVBoxLayout()
        
        table_view = QTableView()
        
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(["이름", "나이"])
        
        table_view.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        data_list = [
            ["홍길동", 25],
            ["김철수", 30],
            ["이영희", 28]
        ]
        
        for row in data_list:
            items = [QStandardItem(str(field)) for field in row]
            model.appendRow(items)
            
            table_view.setModel(model)
            
            layout.addWidget(table_view)
            window.setLayout(layout)
            self.setCentralWidget(window)
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = Window()
    myWindow.show()
    app.exec_()