from weather.getinfo import WeatherDataManager
from weather.storage import Storage
import requests
import pytest
import datetime
import os
import json


def test_is_valid_city():
    assert WeatherDataManager.is_valid_city("Madrid") == True
    assert WeatherDataManager.is_valid_city("añldhfadjfha") == False


def test_get_weather_data_returns_type():
    city1 = "Madrid"
    city2 = "añldhfadjfha"
    assert type(WeatherDataManager.get_weather_data(city=city1)) == dict
    assert type(WeatherDataManager.get_weather_data(city=city2)) == dict


@pytest.mark.parametrize('city', ['London', 'Paris', 'New York'])
def test_save_info(city):
    WeatherDataManager.save_info(city)
    data = Storage.retrieve_from_json()
    current_date = datetime.date.today().strftime("%Y-%m-%d")
    assert len(data) == 6
    assert list(data.keys())[0] == current_date


def test_get_info():
    if os.path.exists(Storage.file_name):
        with open(Storage.file_name, 'r') as file:
            file_data = json.load(file)
    
    else:
        pytest.skip(f"{Storage.file_name} does not exist.")

    method_data = WeatherDataManager.get_info()
    assert file_data == method_data

def test_get_icon():
    icon_code = "04d"
    expected_url = f"http://openweathermap.org/img/wn/{icon_code}.png"
    content = requests.get(expected_url).content

    icon_content = WeatherDataManager.get_icon(icon_code)

    assert icon_content == content
    assert type(icon_content) == bytes