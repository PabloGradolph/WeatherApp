from weatherwindow import WeatherWindow, WeatherDataManager
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import ( 
    QMainWindow, 
    QVBoxLayout,
    QPushButton,
    QWidget,
    QLabel,
    QLineEdit,
    QSizePolicy,
    QSpacerItem,
    QMessageBox,
)


class MainWindow(QMainWindow):
    """
    Main window of the WeatherApp.

    Attributes
    ----------
    city_line_edit : QLineEdit
        Line edit for entering the city name.

    Methods
    -------
    __init__()
        Initialize the MainWindow.
    open_weather_window() -> WeatherWindow
        Open the WeatherWindow with weather information for the entered city.

    """
        
    def __init__(self) -> None:
        """
        Initialize the MainWindow.

        Returns
        -------
        None

        """
                
        super().__init__()
        self.setWindowTitle("WeatherApp")

        # MainWindow elements:
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        title_label = QLabel("WEATHER")
        title_label.setFont(font)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.city_line_edit = QLineEdit()

        city_label = QLabel("Enter a city:")
        self.weather_button = QPushButton("View weather")
        self.weather_button.clicked.connect(self.open_weather_window)

        # Layout.
        layout = QVBoxLayout()
        spacer_top = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, 
            QSizePolicy.Policy.Expanding)
        layout.addItem(spacer_top)
        layout.addWidget(title_label)
        layout.addWidget(city_label)
        layout.addWidget(self.city_line_edit)
        layout.addWidget(self.weather_button)
        spacer_bottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, 
            QSizePolicy.Policy.Expanding)
        layout.addItem(spacer_bottom)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


    def open_weather_window(self) -> None:
        """
        Open the WeatherWindow with weather information for the entered city.

        Returns
        -------
        None

        """
        city = self.city_line_edit.text()
        if not WeatherDataManager.is_valid_city(city):
            QMessageBox.critical(self, "Error", "The city name is not valid.")
            return

        WeatherDataManager.save_info(city)
        self.weather_window = WeatherWindow(city)
        self.city_line_edit.clear()
        self.weather_window.show()
        self.weather_window.exec()
