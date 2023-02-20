# The sys module is responsible for processing command line arguments
import sys
# importing the components
from PySide6.QtWidgets import QApplication
from main_window import MainWindow

app = QApplication(sys.argv)

window = MainWindow(app)
window.show()

# Start the event loop
app.exec()
