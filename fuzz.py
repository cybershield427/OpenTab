from pythonfuzz.main import PythonFuzz
from PySide6 import QtTest

@PythonFuzz
def fuzz(buf):
    try:
    # input string check for signup, login
    except UnicodeDecodeError:
        pass


if __name__ == '__main__':
    fuzz()
