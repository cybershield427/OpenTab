# The sys module is responsible for processing command line arguments
import sys

# importing the components
from PySide6.QtWidgets import QApplication
from main_window import MainWindow

def trace_lines(frame, event, arg):
    if event != 'line':
        return
    co = frame.f_code
    func_name = co.co_name
    line_no = frame.f_lineno
    filename = co.co_filename
    print('  %s line %s' % (func_name, line_no))

def trace_calls(frame, event, arg):
    if event != 'call':
        return
    co = frame.f_code
    func_name = co.co_name
    if func_name == 'write':
        # Ignore write() calls from print statements
        return
    line_no = frame.f_lineno
    filename = co.co_filename
    print('Call to %s on line %s of %s' % (func_name, line_no, filename))
    if func_name in TRACE_INTO:
        # Trace into this function
        return trace_lines
    return

TRACE_INTO = ['b']

sys.settrace(trace_calls)

app = QApplication(sys.argv)

window = MainWindow(app)
window.show()

# Start the event loop
app.exec()