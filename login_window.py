from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton


class LoginWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Login")
		self.setMinimumSize(256, 256)

		username = QLabel("Username:")
		self.user_edit = QLineEdit()
		self.user_edit.textEdited.connect(self.take_input)

		password = QLabel("Password:")
		self.pass_edit = QLineEdit()

		login_button = QPushButton("Login")
		cancel_button = QPushButton("Cancel")

		user_layout = QHBoxLayout()
		user_layout.addWidget(username)
		user_layout.addWidget(self.user_edit)
		pass_layout = QHBoxLayout()
		pass_layout.addWidget(password)
		pass_layout.addWidget(self.pass_edit)

		button_layout = QHBoxLayout()
		button_layout.addWidget(login_button)
		button_layout.addWidget(cancel_button)

		v_layout = QVBoxLayout()
		v_layout.addLayout(user_layout)
		v_layout.addLayout(pass_layout)
		v_layout.addLayout(button_layout)

		self.setLayout(v_layout)

	def take_input(self, new_text):
		print("new text is ", new_text)

