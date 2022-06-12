from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
import sys


def main():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 500, 500)
    win.setWindowTitle("Invento | Powerhouse Digital")

    text = QLabel(win)
    text.setText("This is a Drilling Applicatin Focussing on DataStatistics")
    win.show()

    sys.exit(app.exec())


main()
