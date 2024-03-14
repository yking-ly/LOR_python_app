import sqlite3
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt6.uic import loadUi
from LOR_python_app.code.login import Login

class AdminWindow(QMainWindow):
    def __init__(self):
        super(AdminWindow, self).__init__()
        loadUi("../UI/admin.ui", self)  # Load the UI from admin.ui
        self.button_signup.clicked.connect(self.store_admin_data)

    def store_admin_data(self):
        username = self.lineedit_username.text()
        password = self.lineedit_password.text()
        professor_id = self.lineedit_professor_id.text()

        if not username or not password or not professor_id:
            print("Please fill in all fields.")
            return

        # Check if professor ID consists only of digits
        if not professor_id.isdigit():
            self.show_error_dialog("Professor ID should contain only numbers.")
            return

        # Check if professor ID is within the specified range
        try:
            professor_id_int = int(professor_id)
            if not (1 <= professor_id_int <= 100):
                raise ValueError("Professor ID should be between 1 and 100.")
        except ValueError as ve:
            self.show_error_dialog(str(ve))
            return

        try:
            connection = sqlite3.connect("../database/admin.db")
            cursor = connection.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS admins (username TEXT, password TEXT, professor_id INTEGER)")
            cursor.execute("INSERT INTO admins (username, password, professor_id) VALUES (?, ?, ?)",
                           (username, password, professor_id_int))
            connection.commit()
            connection.close()
            print("Admin data stored successfully.")

            # Open the login window and close all other windows
            self.open_login_window()
            self.close()
        except Exception as e:
            print("Error occurred while storing admin data:", e)

    def open_login_window(self):
        # Close all other windows
        for widget in QApplication.topLevelWidgets():
            if isinstance(widget, QMainWindow) and widget != self:
                widget.close()

        # Open the login window
        self.login_window = Login()
        self.login_window.show()

    def show_error_dialog(self, message):
        msg_box = QMessageBox()
        msg_box.setText(message)
        msg_box.setIcon(QMessageBox.Icon.Critical)
        msg_box.setWindowTitle("Error")
        msg_box.exec()

def main():
    app = QApplication([])
    admin_window = AdminWindow()
    admin_window.show()
    app.exec_()

if __name__ == '__main__':
    main()
