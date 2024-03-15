from PyQt6.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem
from PyQt6.uic import loadUi


class DatabaseWindow(QMainWindow):
    def __init__(self, data):
        super(DatabaseWindow, self).__init__()
        loadUi("../UI/database.ui", self)
        self.setWindowTitle("Database Contents")
        # self.setGeometry(0, 0, 400, 300)

        self.tableWidget = QTableWidget(self)
        # self.tableWidget.setGeometry(10, 10, 381, 271)
        self.tableWidget.setGeometry(10, 10, 750, 600)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(7)  # Set the number of columns

        # Set column names
        column_names = ["username", "email", "password", "full-name", "branch", "specialization", "Phone"]
        self.tableWidget.setHorizontalHeaderLabels(column_names)

        self.populate_table(data)

    def populate_table(self, data):
        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(len(data[0]))

        # Populate table with data
        for row_num, row_data in enumerate(data):
            for col_num, cell_data in enumerate(row_data):
                self.tableWidget.setItem(row_num, col_num, QTableWidgetItem(str(cell_data)))
