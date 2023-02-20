from PySide6.QtWidgets import QPushButton, QVBoxLayout


class ButtonHolder(QPushButton):
	def __init__(self, name):
		super().__init__()
		login_button = QPushButton(name)
		QVBoxLayout(login_button)
		login_button.clicked.connect(self.login_clicked)

	def login_clicked(self):
		print("login button clicked")
