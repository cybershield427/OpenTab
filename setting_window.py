from PySide6.QtWidgets import QWidget
class SettingWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Settings")
        self.setMinimumSize(256, 256)