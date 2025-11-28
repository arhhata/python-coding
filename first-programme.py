import requests

class WeatherFetcher:
    def __init__(self, api_key, location):
        """
        Initialize the WeatherFetcher with an API key and location.
        :param api_key: Your OpenWeatherMap API key.
        :param location: The location for which to fetch weather data.
        """
        self.api_key = api_key
        self.location = location
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

    def fetch_weather(self):
        """
        Fetch weather data for the specified location.
        :return: A dictionary containing weather data or an error message.
        """
        params = {
            "q": self.location,
            "appid": self.api_key,
            "units": "metric"  # Use "imperial" for Fahrenheit
        }
        try:
            response = requests.get(self.base_url, params=params)
            if response.status_code == 200:
                return response.json()
            else:
                return {"error": f"Failed to fetch weather data. Status Code: {response.status_code}"}
        except requests.RequestException as e:
            return {"error": str(e)}

    def print_weather(self):
        """
        Fetch and print the weather data in a readable format.
        """
        weather_data = self.fetch_weather()
        if "error" in weather_data:
            print(weather_data["error"])
        else:
            print(f"Weather in {self.location}:")
            print(f"Temperature: {weather_data['main']['temp']}°C")
            print(f"Condition: {weather_data['weather'][0]['description'].capitalize()}")
            print(f"Humidity: {weather_data['main']['humidity']}%")
            print(f"Wind Speed: {weather_data['wind']['speed']} m/s")

if __name__ == "__main__":
    api_key = "7c5391e6c22d14c5d13e70bfce2b819d"
    location = "Mickleham"  
    weather_fetcher = WeatherFetcher(api_key, location)
    weather_fetcher.print_weather()