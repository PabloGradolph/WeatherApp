import requests
from storage import Storage
from datetime import datetime
from geopy.geocoders import Nominatim


class WeatherDataManager:
    """
    Class to manage weather data using the OpenWeatherMap API.
    """

    OPENWEATHERMAP_API_KEY = 'YourApiKey'

    @classmethod
    def is_valid_city(cls, city: str) -> bool:
        """
        Check if a given city name is valid.

        Parameters
        ----------
        city (str): Name of the city.

        Returns
        -------
        bool: True if the city name is valid, False otherwise.
        """

        geolocator = Nominatim(user_agent='my_app')
        location = geolocator.geocode(city)

        if location is not None:
            return True
        else:
            return False


    @classmethod
    def get_weather_data(cls, city: str) -> dict or None:
        """
        Get weather data for a given city.

        Parameters
        ----------
        city (str): Name of the city.

        Returns
        -------
        dict or None: Weather data for the city, or None if the data 
            is not available.
        """

        # Getting the main info.
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}\
                &appid={cls.OPENWEATHERMAP_API_KEY}"
        response = requests.get(url)
        data = response.json()

        forecast = {}
        
        # Collecting the data we are interested in.
        if 'list' in data:
            for item in data['list']:
                date = item['dt_txt'].split()[0]
                weather = item['weather'][0]['description']
                icon = item['weather'][0]['icon']
                if 'n' in icon:
                    icon = icon.replace('n', 'd')

                if date not in forecast:
                    forecast[date] = [weather, icon]

            # We have the weather and the icon
            # Now we are getting the maximum and de minimum temperatures.
            max_temp = None
            min_temp = None
            current_date = datetime.now().date().strftime("%Y-%m-%d")
            for item in data['list']:
                date = item['dt_txt'].split()[0]
                if date != current_date:
                    forecast[current_date].append(max_temp)
                    forecast[current_date].append(min_temp)
                    current_date = date
                    max_temp = None
                    min_temp = None

                temp_max = item['main']['temp_max']
                temp_min = item['main']['temp_min']

                if max_temp is None:
                    max_temp = temp_max
                else:
                    if temp_max > max_temp:
                        max_temp = temp_max
                
                if min_temp is None:
                    min_temp = temp_min
                else:
                    if temp_min < min_temp:
                        min_temp = temp_min
            
            forecast[date].append(max_temp)
            forecast[date].append(min_temp)
        return forecast


    @classmethod
    def save_info(cls, city: str) -> None:
        """
        Save weather information for a given city to a JSON file.

        Parameters
        ----------
        city (str): Name of the city.

        Returns
        -------
        None
        """

        weather_data = cls.get_weather_data(city)
        Storage.write(weather_data)
    
    @classmethod
    def get_info(cls) -> dict:
        """
        Retrieves the weather information from the storage.

        Returns
        -------
        dict: The weather information.

        """

        return Storage.read()

    @classmethod
    def get_icon(cls, icon: str) -> bytes:
        """
        Retrieves the content of the weather icon from the provided icon URL.

        Parameters
        ----------
        icon (str): The icon code.

        Returns
        -------
        bytes: The content of the weather icon.
        """
            
        url = f'http://openweathermap.org/img/wn/{icon}.png'
        response = requests.get(url)
        return response.content
