import requests
import json
import dotenv
import os
import datetime

# #Data Analysis: The system should compute summary statistics across all weather records, such as temperature trends, rainfall totals, and extreme conditions.

# Data Retrieval: The system should allow users to search for weather information for a specific date quickly and efficiently.


# . Store Weather Records (25 minutes)
# Create a class WeatherRecord with the following fields:

# date (String)
# temperature (int)
# humidity (int)
# windSpeed (int)
# rainfall (int)
# Store all records using:

# List (required) → for processing all records
# Map (required) → key = date, value = WeatherRecord

# If any of the dates is invalid, that entire line should be igonred.

# how to load api key from .env file
dotenv.load_dotenv()
api_key = os.getenv("api_key")


# database_url = os.getenv("database_url")
class WeatherRecord:
  def __init__(self, date, temperature, humidity,windSpeed,rainfall):
    self.date = date
    self.temperature = temperature
    self.humidity = humidity
    self.windSpeed = windSpeed
    self.rainfall = rainfall
    self.item_list = [date, temperature, humidity, windSpeed, rainfall]
    self.item_map = {
      "date": date,
      "temperature": temperature,
      "humidity": humidity,
      "windSpeed": windSpeed,
      "rainfall": rainfall
    }   

# demo usage
store = []
record1 = WeatherRecord("December 3rd", 76,56,98,2)
record2 = WeatherRecord("December 4th", 80,60,90,0)
store.append(record1)
store.append(record2)       


today = WeatherRecord("December 3rd", 76,56,98,2)
print(today.temperature)

# class WeatherAPI:
#     def __init__(self, api_key):

#         self.api_key = api_key
#         self.base_url = "http://api.openweathermap.org/data/2.5/weather"

#     def get_weather(self, city):
#         params = {
#             'q': city,
#             'appid': self.api_key,
#             'units': 'metric'
#         }
#         #get responses
#         response = requests.get(self.base_url, params=params)
#         if response.status_code == 200:
#             return response.json()
#         else:
#             return None
# if __name__ == "__main__":
#     api_key = "your_api_key_here"
#     weather_api = WeatherAPI(api_key)
#     city = input("Enter the city name: ")
#     weather_data = weather_api.get_weather(city)
#     if weather_data:
#         print(f"Weather in {city}: {weather_data['weather'][0]['description']}")
#         print(f"Temperature: {weather_data['main']['temp']}°C")
#     else:        print("Could not retrieve weather data. Please check the city name and try again.")    
