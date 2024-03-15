from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt


class ErrorWindow(QWidget):
    def __init__(self, message):
        super(ErrorWindow, self).__init__()
        self.setWindowTitle("Error")
        self.setGeometry(100, 100, 400, 100)

        layout = QVBoxLayout()

        label = QLabel(message)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

        self.setLayout(layout)
