# The sys module is responsible for processing command line arguments
import sys
# importing the components
from PySide6.QtWidgets import QApplication
from button import ButtonHolder

app = QApplication(sys.argv)

window = ButtonHolder()
window.show()

# Start the event loop
app.exec()
