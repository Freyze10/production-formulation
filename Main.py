import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QLineEdit, QPushButton, QSizePolicy, QCompleter, QMessageBox)
from PyQt6.QtCore import Qt, QSize, QStringListModel
from PyQt6.QtGui import QFont
from Home import MainApplicationWindow

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Production Formulation Login")
        self.setGeometry(100, 100, 500, 400)
        self.setFixedSize(500, 400)
        self.main_app_window = None # To hold the instance of the main app window
        self.setup_ui()
        self.apply_styles()
        self.center_window()

    def center_window(self):
        screen_geometry = QApplication.primaryScreen().geometry()
        window_geometry = self.geometry()
        center_x = (screen_geometry.width() - window_geometry.width()) // 2
        center_y = (screen_geometry.height() - window_geometry.height()) // 2
        self.move(center_x, center_y)

    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.login_form_widget = QWidget(self)
        self.login_form_widget.setFixedSize(350, 250)
        form_layout = QVBoxLayout(self.login_form_widget)
        form_layout.setContentsMargins(30, 20, 30, 20)
        form_layout.setSpacing(10)

        title_label = QLabel("Login")
        title_label.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        form_layout.addWidget(title_label)
        form_layout.addSpacing(10)

        username_layout = QHBoxLayout()
        username_label = QLabel("USERNAME:")
        username_label.setFont(QFont("Arial", 10))
        username_layout.addWidget(username_label)

        self.username_entry = QLineEdit()
        self.username_entry.setFont(QFont("Arial", 10))
        self.usernames_list = ["Admin", "User1 Technician", "User2 Manager", "Guest"]
        completer = QCompleter(self.usernames_list)
        completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        completer.setFilterMode(Qt.MatchFlag.MatchStartsWith)
        completer.popup().setStyleSheet("""
            QListView {
                background-color: white;
                border: 1px solid gray;
                font-size: 12px;
                padding: 4px;
            }
            QListView::item {
                padding: 6px;
            }
            QListView::item:hover{
                background-color: lightgrey;
            }
            QListView::item:selected {
                background-color: #0078d7;  /* Windows blue */
                color: white;
            }
        """)
        self.username_entry.setCompleter(completer)
        self.username_entry.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.username_entry.returnPressed.connect(self.handle_login)
        username_layout.addWidget(self.username_entry)
        form_layout.addLayout(username_layout)

        password_layout = QHBoxLayout()
        password_label = QLabel("PASSWORD:")
        password_label.setFont(QFont("Arial", 10))
        password_layout.addWidget(password_label)

        self.password_entry = QLineEdit()
        self.password_entry.setFont(QFont("Arial", 10))
        self.password_entry.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_entry.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.password_entry.returnPressed.connect(self.handle_login)
        password_layout.addWidget(self.password_entry)
        form_layout.addLayout(password_layout)
        form_layout.addSpacing(10)

        button_layout = QHBoxLayout()
        self.login_button = QPushButton("LOGIN")
        self.login_button.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        self.login_button.setFixedSize(100, 35)
        self.login_button.clicked.connect(self.handle_login)
        button_layout.addWidget(self.login_button)

        self.exit_button = QPushButton("EXIT")
        self.exit_button.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        self.exit_button.setFixedSize(100, 35)
        self.exit_button.clicked.connect(QApplication.instance().quit)
        button_layout.addWidget(self.exit_button)
        form_layout.addLayout(button_layout)
        form_layout.addStretch()

        footer_label = QLabel("MBPI - 2025")
        footer_label.setFont(QFont("Arial", 8))
        footer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        footer_label.setStyleSheet("color: gray;")
        form_layout.addWidget(footer_label)

        main_layout.addWidget(self.login_form_widget)

    def apply_styles(self):
        self.setStyleSheet("""
            QMainWindow {
                background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                                stop:0 #e0f2f7, stop:0.5 #e3f2fd, stop:1 #e0f2f7);
            }
            #login_form_widget {
                background-color: white;
                border-radius: 15px;
                box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
                border: 1px solid #e0e0e0;
            }
            QLabel {
                color: #333333;
                background: transparent;
            }
            QLineEdit {
                border: 1px solid #cccccc;
                border-radius: 5px;
                padding: 5px;
                background-color: #f8f8f8;
            }
            QLineEdit:focus {
                border: 1px solid #2196F3;
                background-color: #e3f2fd;
            }
            QPushButton {
                background-color: #2196F3;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 8px 15px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
            QPushButton#exit_button {
                background-color: #f44336;
            }
            QPushButton#exit_button:hover {
                background-color: #d32f2f;
            }
        """)
        self.login_form_widget.setObjectName("login_form_widget")
        self.exit_button.setObjectName("exit_button")


    def handle_login(self):
        username = self.username_entry.text()
        password = self.password_entry.text()

        if username.lower() not in [u.lower() for u in self.usernames_list]:
            QMessageBox.warning(self, "Login Error", "Invalid Username. Please select from the suggestions.")
            return

        if username == "Admin" and password == "admin123":
            QMessageBox.information(self, "Login Successful", f"Welcome, {username}!")
            print("Login Successful!")
            self.close() # Close the login window

            # Instantiate and show the main application window
            self.main_app_window = MainApplicationWindow(username=username)
            self.main_app_window.show()
        else:
            QMessageBox.warning(self, "Login Error", "Invalid Username or Password.")
            print("Invalid Credentials")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())