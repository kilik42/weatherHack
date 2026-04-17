import requests
import json
import dotenv
import os
from datetime import datetime

# Load environment variables -- dont need this
# dotenv.load_dotenv()
# api_key = os.getenv("api_key")

# Configuration for National weather service  API
HEADERS = {
    'User-Agent': '(myweatherapp.com, contact@email.com)'
}

class WeatherRecord:
    def __init__(self, date, temperature, humidity, windSpeed, rainfall):
        self.date = date
        self.state = "IL"
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
        url = f'https://api.weather.gov/alerts/active?area={self.state}'
        
        try:
            # Make the API request to NWS
            response = requests.get(url, headers=HEADERS)
            
            # Check if the request was successful
            if response.status_code == 200:
                data = response.json()
                # Note: weather.gov/alerts returns alert data, not current temp.
            
                print(f"Successfully connected to NWS API for {self.state}")
                response_data = json.dumps(data, indent=2)
                print(f"Received data: {response_data[:500]}...")  # Print first 500 chars of response for verification
                
                # If you were using OpenWeatherMap (uncomment if needed):
                # data = response.json()
                # self.temperature = data['main']['temp']
                # self.humidity = data['main']['humidity']
                # Map (required) → key = date, value = WeatherRecord

            # if response.status_code == 200:
            #     data = response.json()
            #     self.temperature = data['main']['temp']
            #     self.humidity = data['main']['humidity'] 
            else:
                print(f"Failed to retrieve weather data. Status: {response.status_code}")
                
        except requests.exceptions.RequestException as e:
            print(f"Connection error: {e}")


  # 1. List
    weather_list = []

    # 2. Map/Dictionary (for quick lookup by date)
    weather_map = {}

  # Method to add record to both List and Map
    def add_record(self, record):
        """Adds a record to both the List and the Map."""
        self.weather_list.append(record) 
        self.weather_map[record.date] = record

if __name__ == "__main__":
    # Create a record
    today = WeatherRecord("December 3rd", 76, 56, 98, 2)

    # i need to do this..Map (required) → key = date, value = WeatherRecord
    today.add_record(today)
    # add more records to the list and map
    record1 = WeatherRecord("December 4th", 80, 60, 90, 0)
    record2 = WeatherRecord("December 5th", 65, 45, 10, 5)
    record3 = WeatherRecord("December 6th", 70, 50, 20, 1)
    record4 = WeatherRecord("December 7th", 85, 70, 15, 0)
    record5 = WeatherRecord("December 8th", 60, 40, 5, 10)

    # Add records to the List and Map
    for rec in [record1, record2, record3, record4, record5]:
        today.add_record(rec)
  
    print("\n--- Weather Records in List ---")
    for rec in today.weather_list:
        print(f"{rec.date}: {rec.temperature}°F")
    print("\n--- Weather Records in Map ---")
    for rec in today.weather_map:
        # need more than memory address, need to print the actual record
        # print(f"{rec}: {today.weather_map[rec]}")
        print(f"{rec}: {today.weather_map[rec].temperature}°F")


    #  Use the List to calculate average temperature

    total_temp = sum(rec.temperature for rec in today.weather_list)
    avg_temp = total_temp / len(today.weather_list)
    print(f"\nAverage Temperature: {avg_temp:.2f}°F")

    # Use the Map for quick lookup (Efficient Searching)
    search_date = "December 5th"
    if search_date in today.weather_map:
        found_record = today.weather_map[search_date]
        print(f"Lookup Success! Date: {found_record.date}, Temp: {found_record.temperature}°F")
    else:
        print(f"Lookup Failed! No record found for date: {search_date}")
    
   
    print(f"\n--- Weather Report for {today.date} ---")
    print(f"Temperature: {today.temperature}°F")
    print(f"Humidity:    {today.humidity}%")
    print(f"Wind Speed:  {today.windSpeed} mph")
    
    if today.temperature > 70:
        print("Status: It's warm today!")
    else:
        print("Status: It's chilly today.")
    
    #taken from the problem statement
    # After loading all records, the application reads an integer from standard input, the user enters either 1 or 2:
    # If the user enters 1 → The application displays weather statistics (Explained in Step 4)
    # If the user enters 2 → The application searchs for a specific date (Explained is Step 5)
    # For option 2, the application reads one additional line in this format: MM-DD-YYYY
    user_input = input("\nEnter 1 for Weather Statistics or 2 for Date Lookup: ")
    if user_input == "1":
        # Display weather statistics (e.g., average temperature)
        total_temp = sum(rec.temperature for rec in today.weather_list)
        avg_temp = total_temp / len(today.weather_list)
        print(f"\nAverage Temperature: {avg_temp:.2f}°F")
    elif user_input == "2":
        date_input = input("Enter a date (MM-DD-YYYY): ")
        if date_input in today.weather_map:
            found_record = today.weather_map[date_input]
            print(f"Lookup Success! Date: {found_record.date}, Temp: {found_record.temperature}°F")
        else:
            print(f"Lookup Failed! No record found for date: {date_input}")
    else:
        print("Invalid input. Please enter 1 or 2.")

