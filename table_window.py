from PySide6.QtWidgets import QMainWindow, QToolBar, QStatusBar, QPushButton, \
	QVBoxLayout, QWidget, QSizePolicy, QHBoxLayout
from PySide6.QtCore import QSize
from assigncustomer import Assign


class TableWindow(QMainWindow):
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

		place_holder_button = QPushButton("Assign Table")
		h_layout = QHBoxLayout()
		v_layout = QVBoxLayout()

		h_layout.addWidget(place_holder_button)
		v_layout.addLayout(h_layout)

		size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		place_holder_button.setSizePolicy(size_policy)

		central_widget = QWidget(self)
		central_widget.setLayout(v_layout)

		self.setCentralWidget(central_widget)
		self.assign_customer = None
		place_holder_button.clicked.connect(self.add_table)

	def add_table(self):
		self.assign_customer = Assign()
		self.assign_customer.show()

	def close_app(self):
		self.app.quit()
