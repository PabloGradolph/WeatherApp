import pytest
from PyQt6.QtWidgets import QApplication, QLabel
from weather.app import main
from weather.mainwindow import MainWindow


@pytest.fixture
def app(qapp):
    """
    Fixture for creating a QApplication instance.
    """
    return qapp


def test_main_window_creation(app, qtbot):
    """
    Test the creation of the main window.
    """
    main_window = MainWindow()
    qtbot.addWidget(main_window)

    assert isinstance(main_window, MainWindow)
    assert main_window.windowTitle() == "WeatherApp"

    main_window.close()


if __name__ == '__main__':
    pytest.main(['-v'])