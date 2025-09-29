import sys
from PyQt5.QtWidgets import *

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        window = QWidget()
        layout = QVBoxLayout()
        
        table = QTableWidget(3, 2)
        table.setHorizontalHeaderLabels(["이름", "나이"])
        
        table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        data_list = [
            ["홍길동", 25],
            ["김철수", 30],
            ["이영희", 28]
        ]
        
        for row, (name, age) in enumerate(data_list):
            table.setItem(row, 0, QTableWidgetItem(name))
            table.setItem(row, 1, QTableWidgetItem(str(age)))
            
        layout.addWidget(table)
        window.setLayout(layout)
        self.setCentralWidget(window)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = Window()
    myWindow.show()
    app.exec_()
