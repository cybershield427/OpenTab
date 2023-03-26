from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton, QApplication
from user_db import Database
from table_window import TableWindow


class LoginWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Login")
		self.setMinimumSize(256, 256)

		# create a database instance
		self.db = Database()
		# create the user table if not exist
		self.db.create_table()

		username = QLabel("Username:")
		self.user_edit = QLineEdit()
		# self.user_edit.textEdited.connect(self.take_input)

		password = QLabel("Password:")
		self.pass_edit = QLineEdit()
		self.pass_edit.setEchoMode(QLineEdit.Password)

		login_button = QPushButton("Login")
		cancel_button = QPushButton("Cancel")

		user_layout = QHBoxLayout()
		user_layout.addWidget(username)
		user_layout.addWidget(self.user_edit)
		pass_layout = QHBoxLayout()
		pass_layout.addWidget(password)
		pass_layout.addWidget(self.pass_edit)

		message_layout = QHBoxLayout()
		self.message_label = QLabel()
		self.message_label.setStyleSheet('color: red')
		self.message_label.setMaximumWidth(200)
		self.message_label.setMaximumHeight(20)
		self.message_label.setWordWrap(True)
		message_layout.addWidget(self.message_label)

		button_layout = QHBoxLayout()
		button_layout.addWidget(login_button)
		button_layout.addWidget(cancel_button)

		v_layout = QVBoxLayout()
		v_layout.addLayout(user_layout)
		v_layout.addLayout(pass_layout)
		v_layout.addLayout(message_layout)
		v_layout.addLayout(button_layout)

		self.setLayout(v_layout)

		login_button.clicked.connect(self.login)
		cancel_button.clicked.connect(self.close)

		self.table_window = None

	def login(self):
		username = self.user_edit.text()
		password = self.pass_edit.text()
		user = self.db.get_user(username, password)
		if user:
			print("Login successful!")
			self.db.close_connection()
			QApplication.closeAllWindows()
			app = QApplication.instance()
			self.table_window = TableWindow(app)
			self.table_window.show()
			self.hide()
		else:
			self.message_label.setText("Invalid username or password.")
