from PySide6.QtWidgets import QMainWindow, QToolBar, QStatusBar
from PySide6.QtCore import QSize
from button import ButtonHolder


class MainWindow(QMainWindow):
	def __init__(self, app):
		super().__init__()
		self.app = app
		self.setWindowTitle("OpenTab")

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
		toolbar.setIconSize(QSize(16,16))
		self.addToolBar(toolbar)

		toolbar.addAction(close_action)
		toolbar.addAction(add_table_action)

		# status bar
		self.setStatusBar(QStatusBar(self))

		login_button = ButtonHolder("Login")

	def close_app(self):
		self.app.quit()

	def add_table(self):
		self.statusBar().showMessage("To Add a New Table", 3000)