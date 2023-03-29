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

	# Return True if all requirements are met, False otherwisepy
	return length_check and letter_check and number_check and symbol_check


class Signup(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Signup")
		self.setMinimumSize(512, 512)

		# create a database instance
		self.db = Database()

		# create the labels and line edits
		self.fields = {
			"Username": QLineEdit(),
			"Password": QLineEdit(),
			"Retype Password": QLineEdit(),
			"First Name": QLineEdit(),
			"Last Name": QLineEdit(),
			"Phone Number": QLineEdit(),
		}

		# set the password fields to be in password mode
		self.fields["Password"].setEchoMode(QLineEdit.EchoMode.Password)
		self.fields["Retype Password"].setEchoMode(QLineEdit.EchoMode.Password)

		# create submit and cancel buttons
		submit_button = QPushButton("Submit")
		cancel_button = QPushButton("Cancel")

		# create the layouts and add widgets to them
		v_layout = QVBoxLayout()
		message_layout = QHBoxLayout()
		self.message_label = QLabel()
		# self.message_label.setStyleSheet('color: red')
		self.message_label.setMaximumWidth(300)
		self.message_label.setMaximumHeight(60)
		self.message_label.setWordWrap(True)
		message_layout.addWidget(self.message_label)

		for field, widget in self.fields.items():
			layout = QHBoxLayout()
			label = QLabel(field)
			layout.addWidget(label)
			layout.addWidget(widget)
			v_layout.addLayout(layout)

		v_layout.addLayout(message_layout)
		# add submit and cancel buttons to a layout
		button_layout = QHBoxLayout()
		button_layout.addWidget(submit_button)
		button_layout.addWidget(cancel_button)
		v_layout.addLayout(button_layout)

		# set the main layout of the window
		self.setLayout(v_layout)

		# connect submit and cancel buttons to their respective functions
		submit_button.clicked.connect(self.submit)
		cancel_button.clicked.connect(self.close)

	def submit(self):
		# get the input values from the fields
		username = self.fields["Username"].text()
		password = self.fields["Password"].text()
		retype_password = self.fields["Retype Password"].text()
		first_name = self.fields["First Name"].text()
		last_name = self.fields["Last Name"].text()
		phone_number = self.fields["Phone Number"].text()

		self.message_label.setStyleSheet('color: red')

		# check if any fields are empty
		if not all((username, password, retype_password, first_name, last_name, phone_number)):
			self.message_label.setText("Please fill in all fields.")
			return

		if not check_password(password):
			self.message_label.setText(
				"Password has to be at least 8 characters long, "
				"with combination of letters, numbers and special characters, "
				"and at least 1 capitalized letter."
			)
			return

		# check if passwords match
		if password != retype_password:
			self.message_label.setText("Passwords do not match.")
			return

		# validate phone number
		if not re.match(r'^\d{10}$', phone_number):
			self.message_label.setText("Invalid phone number. Must be 10 digits.")
			return

		if self.db.check_user(username):
			self.message_label.setText("Username already exists.")
			return

		# add the user to the database
		self.db.insert_user(username, password, first_name, last_name, phone_number)

		# show success message
		self.message_label.setStyleSheet('color: green')
		self.message_label.setText(f"Signed up correctly for user {username}")
		for field in self.fields.values():
			field.clear()
