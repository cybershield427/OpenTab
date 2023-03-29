from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton
from restaurant_db import Database
import re

table_status = {"1": True, "2": True, "3": True}

def check_credit(credit_card):
	# Define the regular expressions for each requirement
	length_regex = re.compile('.{16,}')
	number_regex = re.compile('[0-9]')

	# Check each requirement using the regular expressions
	length_check = length_regex.search(credit_card)
	number_check = number_regex.search(credit_card)

	# Return True if all requirements are met, False otherwisepy
	return length_check and number_check


class Assign(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Assign Customer")
		self.setMinimumSize(512, 512)

		# create a database instance
		self.db = Database()

		# create the labels and line edits
		self.fields = {
			"Table Number": QLineEdit(),
			"Full Name": QLineEdit(),
			"Phone": QLineEdit(),
			"Credit Card Number": QLineEdit(),
			"Attendant": QLineEdit(),
		}

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
		table_number = self.fields["Table Number"].text()
		customer_name = self.fields["Full Name"].text()
		phone = self.fields["Phone"].text()
		credit_card = self.fields["Credit Card Number"].text()
		attendant = self.fields["Attendant"].text()

		self.message_label.setStyleSheet('color: red')

		# check if any fields are empty
		if not all((customer_name, phone, credit_card)):
			self.message_label.setText("Please fill in all fields.")
			return

		if not check_credit(credit_card):
			self.message_label.setText(
				"Credit Card has to be at least 16 characters long."
			)
			return

		# validate phone number
		if not re.match(r'^\d{10}$', phone):
			self.message_label.setText("Invalid phone number. Must be 10 digits.")
			return

		# add the customer to the database

		# create the customer table if not exist
		#self.db.create_table()
		self.db.insert_customer(table_number, customer_name, phone, credit_card, attendant)

		# show success message
		self.message_label.setStyleSheet('color: green')
		self.message_label.setText(f"Signed up correctly for customer {customer_name}")
		for field in self.fields.values():
			field.clear()
