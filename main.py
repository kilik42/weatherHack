import requests
import json
import dotenv
import os
from datetime import datetime


# Load environment variables -- dont need this
# dotenv.load_dotenv()
# api_key = os.getenv("api_key")

# Configuration for NWS API
HEADERS = {
    'User-Agent': '(myweatherapp.com, contact@email.com)'
}

class WeatherRecord:
    def __init__(self, date, temperature, humidity, windSpeed, rainfall):
        self.date = date
        self.temperature = temperature
        self.humidity = humidity
        self.windSpeed = windSpeed
        self.rainfall = rainfall
        
        # storeing items in a list and a map for easy access
        self.item_list = [date, temperature, humidity, windSpeed, rainfall]
        self.item_map = {
            "date": date,
            "temperature": temperature,
            "humidity": humidity,
            "windSpeed": windSpeed,
            "rainfall": rainfall
        }   

        # API Logic
        
with open('weather_data.txt', 'r') as file:
    for line in file:
        print(line.rstrip().split(",")[0])