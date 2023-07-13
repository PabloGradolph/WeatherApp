from getinfo import WeatherDataManager
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtWidgets import ( 
    QDialog,
    QVBoxLayout,
    QLabel,
    QMessageBox,
    QHBoxLayout,
)


class WeatherWindow(QDialog):
    """
    Weather Information Window.

    This window displays the weather information for a specific city.

    Parameters
    ----------
    city : str
        The name of the city for which weather information is displayed.

    Attributes
    ----------
    city_label : QLabel
        Label to display the city name.
    data : dict
        Weather data retrieved from the 'weather_data.json' file.

    Methods
    -------
    setup_ui()
        Sets up the user interface for the weather window.
    """

    def __init__(self, city: str) -> None:
        """
        Constructor of the WeatherWindow class.

        Parameters
        ----------
        city : str
            The name of the city.

        Returns
        -------
        None

        """
        super().__init__()
        self.setWindowTitle("Weather Information")

        self.city_label = QLabel(f"{city}")
        self.city_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.city_label.setFont(font)

        self.data = None

        self.setup_ui()

    def setup_ui(self) -> None:
        """
        Sets up the user interface for the weather window.

        Returns
        -------
        None

        """
        layout = QVBoxLayout()
        layout.addWidget(self.city_label)

        self.data = WeatherDataManager.get_info()

        if self.data == {}:
            QMessageBox.critical(self, "Error", "The city name is not valid.")
            return

        font = QFont()
        font.setBold(True)

        layoutH = QHBoxLayout()
        for day in self.data:
            date_label = QLabel(day)
            date_label.setFont(font)
            layoutH.addWidget(date_label)

        layout.addLayout(layoutH)

        layoutH = QHBoxLayout()
        for day in self.data:
            icon = self.data[day][1]
            response = WeatherDataManager.get_icon(icon=icon)
            pixmap = QPixmap()
            pixmap.loadFromData(response)
            icon_label = QLabel()
            icon_label.setPixmap(pixmap)
            layoutH.addWidget(icon_label)

        layout.addLayout(layoutH)

        layoutH = QHBoxLayout()
        for day in self.data:
            weather = self.data[day][0]
            weather_label = QLabel(weather)
            weather_label.setFont(font)
            layoutH.addWidget(weather_label)

        layout.addLayout(layoutH)

        layoutH = QHBoxLayout()
        for day in self.data:
            temperature = 'Max: ' + \
                str(round(self.data[day][2] - 273, 2)) + 'º'
            temperature_label = QLabel(temperature)
            layoutH.addWidget(temperature_label)

        layout.addLayout(layoutH)

        layoutH = QHBoxLayout()
        for day in self.data:
            temperature = 'Min: ' + \
                str(round(self.data[day][3] - 273, 2)) + 'º'
            temperature_label = QLabel(temperature)
            layoutH.addWidget(temperature_label)

        layout.addLayout(layoutH)

        self.setLayout(layout)