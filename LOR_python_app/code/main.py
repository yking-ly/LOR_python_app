from PyQt6.QtWidgets import QApplication
from LOR_python_app.code.login import Login

def main():
    app = QApplication([])
    login_window = Login()
    # login_window.show()
    app.exec()

if __name__ == '__main__':
    main()
