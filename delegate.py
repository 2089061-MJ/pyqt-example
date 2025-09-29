import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QStandardItemModel, QStandardItem

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        window = QWidget()
        layout = QVBoxLayout()
        
        # 테이블 생성
        table_view = QTableView()

        # 모델 생성 (행, 열)
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(["이름", "가입 여부"])
        
        # 행, 열 너비를 창 너비에 맞게 늘리기
        table_view.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
                
        # 리스트 데이터 출력
        data_list = [
            ["홍길동", True],
            ["김철수", False],
            ["이영희", True]
        ]

        for name, joined in data_list:
            name_item = QStandardItem(name)
            check_item = QStandardItem()
            check_item.setCheckable(True)  # 체크박스로 표시
            check_item.setCheckState(2 if joined else 0)  # 2=Checked, 0=Unchecked
            model.appendRow([name_item, check_item])

        table_view.setModel(model)

        layout.addWidget(table_view)
        window.setLayout(layout)
        self.setCentralWidget(window)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = Window()
    myWindow.show()
    app.exec_()