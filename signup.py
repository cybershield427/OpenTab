from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton
from user_db import Database
import re


def check_password(password):
	# Define the regular expressions for each requirement
	length_regex = re.compile('.{8,}')
	letter_regex = re.compile('[a-zA-Z]')
	number_regex = re.compile('[0-9]')
	symbol_regex = re.compile('[^a-zA-Z0-9]')

	# Check each requirement using the regular expressions
	length_check = length_regex.search(password)
	letter_check = letter_regex.search(password)
	number_check = number_regex.search(password)
	symbol_check = symbol_regex.search(password)

	# Return True if all requirements are met, False otherwise
	return length_check and letter_check and number_check and symbol_check


class Signup(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("SignUp")
		self.setMinimumSize(512, 512)

		# create a database instance
		self.db = Database()

		username = QLabel("Username:")
		self.user_edit = QLineEdit()

		password = QLabel("Password:")
		self.pass_edit = QLineEdit()
		self.pass_edit.setEchoMode(QLineEdit.Password)

		password2 = QLabel("Retype Password:")
		self.pass_edit2 = QLineEdit()
		self.pass_edit2.setEchoMode(QLineEdit.Password)

		firstname = QLabel("Fist Name:")
		self.firstname_edit = QLineEdit()

		lastname = QLabel("Last Name:")
		self.lastname_edit = QLineEdit()

		phone = QLabel("Phone Number:")
		self.phone_edit = QLineEdit()

		submit_button = QPushButton("Submit")
		cancel_button = QPushButton("Cancel")

		user_layout = QHBoxLayout()
		user_layout.addWidget(username)
		user_layout.addWidget(self.user_edit)
		pass_layout = QHBoxLayout()
		pass_layout.addWidget(password)
		pass_layout.addWidget(self.pass_edit)
		pass2_layout = QHBoxLayout()
		pass2_layout.addWidget(password2)
		pass2_layout.addWidget(self.pass_edit2)
		firstname_layout = QHBoxLayout()
		firstname_layout.addWidget(firstname)
		firstname_layout.addWidget(self.firstname_edit)
		lastname_layout = QHBoxLayout()
		lastname_layout.addWidget(lastname)
		lastname_layout.addWidget(self.lastname_edit)
		phone_layout = QHBoxLayout()
		phone_layout.addWidget(phone)
		phone_layout.addWidget(self.phone_edit)
		button_layout = QHBoxLayout()
		button_layout.addWidget(submit_button)
		button_layout.addWidget(cancel_button)

		message_layout = QHBoxLayout()
		self.message_label = QLabel()
		self.message_label.setStyleSheet('color: red')
		self.message_label.setMaximumWidth(300)
		self.message_label.setMaximumHeight(60)
		self.message_label.setWordWrap(True)
		message_layout.addWidget(self.message_label)

		v_layout = QVBoxLayout()
		v_layout.addLayout(user_layout)
		v_layout.addLayout(pass_layout)
		v_layout.addLayout(pass2_layout)
		v_layout.addLayout(firstname_layout)
		v_layout.addLayout(lastname_layout)
		v_layout.addLayout(phone_layout)
		v_layout.addLayout(message_layout)
		v_layout.addLayout(button_layout)

		self.setLayout(v_layout)

		submit_button.clicked.connect(self.submit)
		cancel_button.clicked.connect(self.close)

	def submit(self):
		self.message_label.setText("")
		username = self.user_edit.text()
		password = self.pass_edit.text()
		re_password = self.pass_edit2.text()
		firstname = self.firstname_edit.text()
		lastname = self.lastname_edit.text()
		phone = self.phone_edit.text()

		if not check_password(password):
			self.message_label.setText(
				"Password has to be at least 8 characters long, "
				"with combination of letters, numbers and special characters, "
				"and at least 1 capitalized letter."
			)
		else:
			if password != re_password:
				self.message_label.setText("The retyped password does not match")
			else:
				if not phone.isdigit():
					self.message_label.setText("Please input only numbers for phone number")
				elif len(phone) != 10:
					self.message_label.setText("Please only enter 10 numbers for phone number")
				else:
					self.db.insert_user(username, password, firstname, lastname, phone)
					self.message_label.setText(f"Signed up correctly for user {username}")
					self.user_edit.clear()
					self.pass_edit.clear()
					self.pass_edit2.clear()
					self.firstname_edit.clear()
					self.lastname_edit.clear()
					self.phone_edit.clear()
