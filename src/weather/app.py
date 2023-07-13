from PyQt6.QtWidgets import QApplication
from mainwindow import MainWindow
from PyQt6.QtGui import QPalette, QColor


# Main function to run the application.
def main():
    app = QApplication([])

    palette = app.palette()
    background_color = QColor(130, 130, 130)
    palette.setColor(QPalette.ColorRole.Window, background_color)
    palette.setColor(QPalette.ColorRole.WindowText, QColor(255, 255, 255))
    app.setPalette(palette)

    window = MainWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()