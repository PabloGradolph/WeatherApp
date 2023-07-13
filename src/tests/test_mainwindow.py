import pytest
from PyQt6.QtWidgets import QApplication, QMessageBox
from mainwindow import MainWindow
from weatherwindow import WeatherWindow
from getinfo import WeatherDataManager


app = QApplication([])

@pytest.fixture(scope="module")
def main_window():
    window = MainWindow()
    yield window
    window.close()


def test_main_window_creation(main_window):
    assert main_window is not None
    assert isinstance(main_window, MainWindow)
    assert main_window.windowTitle() == "WeatherApp"
    assert main_window.city_line_edit is not None

def test_open_weather_window_valid_city(main_window, mocker):
    city = "London"
    main_window.city_line_edit.setText(city)

    mocker.patch.object(WeatherDataManager, "is_valid_city", return_value=True)
    mocker.patch.object(WeatherDataManager, "save_info")
    mocker.patch.object(WeatherWindow, "exec")
    mocker.patch.object(QMessageBox, "critical")

    main_window.open_weather_window()

    WeatherDataManager.is_valid_city.assert_called_once_with(city)
    WeatherDataManager.save_info.assert_called_once_with(city)
    WeatherWindow.exec.assert_called_once()
    QMessageBox.critical.assert_not_called()

    weather_window = main_window.weather_window

    assert isinstance(weather_window, WeatherWindow)
    assert main_window.city_line_edit.text() == ""


def test_open_weather_window_invalid_city(main_window, mocker):
    city = "InvalidCity"
    main_window.city_line_edit.setText(city)

    mocker.patch.object(WeatherDataManager, "is_valid_city", 
        return_value=False)
    mocker.patch.object(WeatherDataManager, "save_info")
    mocker.patch.object(WeatherWindow, "exec")
    mocker.patch.object(QMessageBox, "critical")

    main_window.open_weather_window()

    WeatherDataManager.is_valid_city.assert_called_once_with(city)
    WeatherDataManager.save_info.assert_not_called()
    WeatherWindow.exec.assert_not_called()
    QMessageBox.critical.assert_called_once_with(main_window, "Error", 
        "The city name is not valid.")

    assert main_window.city_line_edit.text() == city


if __name__ == "__main__":
    pytest.main()