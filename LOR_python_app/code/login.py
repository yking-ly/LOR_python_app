import sqlite3
from PyQt6.QtWidgets import QMainWindow, QLineEdit, QApplication, QMessageBox
from PyQt6.uic import loadUi
from LOR_python_app.code.database_window import DatabaseWindow
from LOR_python_app.code.details import FillDetailsWindow


class Login(QMainWindow):
    def __init__(self):
        super(Login, self).__init__()
        loadUi("../UI/login.ui", self)
        self.pushButton.clicked.connect(self.on_login_button_clicked)
        self.pushButton_2.clicked.connect(self.show_signup_window)
        self.lineEdit_2.setEchoMode(QLineEdit.EchoMode.Password)
        self.show()

    def on_login_button_clicked(self):
        # Placeholder for login functionality
        print("Login button clicked")
        username = self.lineEdit.text()
        professor_id = self.lineEdit.text()
        password = self.lineEdit_2.text()
        # print("Username:", username)
        # print("Password:", password)

        # Perform authentication
        if self.authenticate(username, password, professor_id):
            if self.check_admin(professor_id):
                self.show_database_contents()
            else:
                self.show_user_details(username)

    def show_signup_window(self):
        from signup import SignUpWindow
        self.close()
        self.signup_window = SignUpWindow()
        self.signup_window.show()

    def authenticate(self, username, password,professor_id):
        try:
            connection = sqlite3.connect("../database/admin.db")
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM admins WHERE professor_id = ? AND password = ?", (professor_id, password))
            admin = cursor.fetchone()
            connection.close()

            if admin is not None:
                return True
            else:
                # Check if the user exists in the signup database
                connection = sqlite3.connect("../database/signup.db")
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM users WHERE name = ? AND password = ?", (username, password))
                user = cursor.fetchone()
                connection.close()
                if user is not None:
                    return True
                else:
                    self.show_error("Error", "Invalid username or password.")
                    return False
        except Exception as e:
            print("Error occurred while authenticating:", e)
            return False

    def check_admin(self, professor_id):
        try:
            connection = sqlite3.connect("../database/admin.db")
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM admins WHERE professor_id = ?", (professor_id,))
            admin = cursor.fetchone()
            connection.close()
            return admin is not None
        except Exception as e:
            print("Error occurred while checking admin:", e)
            return False

    def show_database_contents(self):
        # Retrieve database contents
        connection = sqlite3.connect("../database/signup.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users")
        data = cursor.fetchall()
        connection.close()

        # Display database contents
        print("Database Contents:")
        for row in data:
            print(row)

        self.database_window = DatabaseWindow(data)
        self.database_window.show()

    def show_user_details(self, username):
        self.fill_details_window = FillDetailsWindow(username)
        self.fill_details_window.show()

    def show_error(self, title, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(QMessageBox.Icon.Critical)
        msg_box.exec()


def main():
    app = QApplication([])
    login_window = Login()
    login_window.show()
    app.exec_()


if __name__ == '__main__':
    main()
