import pytest
from PyQt6.QtWidgets import QApplication, QDialog
from weatherwindow import WeatherWindow


app = QApplication([])

@pytest.fixture(scope="module")
def weather_window():
    window = WeatherWindow("City")
    yield window
    window.close()


def test_weather_window_creation(weather_window):
    assert isinstance(weather_window, QDialog)
    assert weather_window.windowTitle() == "Weather Information"


if __name__ == "__main__":
    pytest.main()