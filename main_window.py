from PySide6.QtWidgets import QMainWindow, QToolBar, QStatusBar, QPushButton, \
	QVBoxLayout, QWidget, QSizePolicy, QHBoxLayout
from PySide6.QtCore import QSize
from login_window import LoginWindow


class MainWindow(QMainWindow):
	def __init__(self, app):
		super().__init__()
		self.app = app
		self.setWindowTitle("OpenTab")
		self.setMinimumSize(200, 100)

		# Menubar and menus
		menu_bar = self.menuBar()
		home_menu = menu_bar.addMenu("Home")
		close_action = home_menu.addAction("Close")
		close_action.triggered.connect(self.close_app)

		table_menu = menu_bar.addMenu("Table")
		add_table_action = table_menu.addAction("Add Table")
		add_table_action.triggered.connect(self.add_table)

		window_menu = menu_bar.addMenu("Window")
		setting_menu = menu_bar.addMenu("Setting")
		help_menu = menu_bar.addMenu("Help")

		# toolbar
		toolbar = QToolBar("Toolbar")
		toolbar.setIconSize(QSize(16, 16))
		self.addToolBar(toolbar)

		toolbar.addAction(close_action)
		toolbar.addAction(add_table_action)

		# status bar
		self.setStatusBar(QStatusBar(self))

		# create 2 button
		login_button = QPushButton("Login")
		login_button.setFixedSize(200, 50)
		cancel_button = QPushButton("Cancel")
		cancel_button.setFixedSize(200, 50)

		# set the H and V layout
		login_layout = QHBoxLayout()
		login_layout.addWidget(login_button)

		cancel_layout = QHBoxLayout()
		cancel_layout.addWidget(cancel_button)

		button_layout = QVBoxLayout()
		button_layout.addLayout(login_layout)
		button_layout.addLayout(cancel_layout)

		# Make the location of the buttons change with the window size
		size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

		login_button.setSizePolicy(size_policy)
		cancel_button.setSizePolicy(size_policy)

		# put the button in the center widget
		central_widget = QWidget(self)
		central_widget.setLayout(button_layout)

		self.setCentralWidget(central_widget)

		# events for each button
		login_button.clicked.connect(self.login_clicked)
		cancel_button.clicked.connect(self.close_app)

		# create new window instance so the window can keep open
		self.new_window = None

	def login_clicked(self):
		if not self.new_window:
			self.new_window = LoginWindow()
			self.new_window.show()

	def close_app(self):
		self.app.quit()

	def add_table(self):
		self.statusBar().showMessage("To Add a New Table", 3000)
