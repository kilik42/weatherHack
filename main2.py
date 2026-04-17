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
    slit_list = []
    for line in file:
        # i want to print the data into separate columns, so i will split the line by comma and print the first item (date)
        print(line.rstrip().split(",")[0])
        # for example, to print the temperature:
        print(line.rstrip().split(",")[1])
        # to print humidity: 
        print(line.rstrip().split(",")[2])           
        # to print windSpeed:
        print(line.rstrip().split(",")[3])
        # to print rainfall:
        print(line.rstrip().split(",")[4]) 
        # i want to store the data in a list of WeatherRecord objects, so i will split the line by comma and create a WeatherRecord object with the data
        record = WeatherRecord(line.rstrip().split(",")[0], line.rstrip().split(",")[1], line.rstrip().split(",")[2], line.rstrip().split(",")[3], line.rstrip().split(",")[4])
        slit_list.append(record)
        # print the record to verify it was created correctly
        print(record.item_map)
        #want to join them all to gether in a list of WeatherRecord objects, so i will create a list of WeatherRecord objects and append the record to the list
        # i want to print the list of WeatherRecord objects to verify it was created correctly .. no memory data
    for record in slit_list:
        print(record.item_map)
