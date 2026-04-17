import requests
import dotenv
import os

# Load environment variables
dotenv.load_dotenv()

HEADERS = {
    'User-Agent': '(myweatherapp.com, contact@email.com)'
}

class WeatherRecord:
    def __init__(self, date, temperature, humidity, windSpeed, rainfall):
        self.date = date  # This will be our Map Key
        self.temperature = temperature
        self.humidity = humidity
        self.windSpeed = windSpeed
        self.rainfall = rainfall
        
        # API logic for the specific state
        state = "IL"
        url = f'https://api.weather.gov/alerts/active?area={state}'
        
        try:
            response = requests.get(url, headers=HEADERS)
            if response.status_code == 200:
                # Logic to parse NWS data could go here
                pass 
        except Exception as e:
            print(f"API Error for {date}: {e}")

    def __repr__(self):
        return f"WeatherRecord(date='{self.date}', temp={self.temperature})"

# --- Data Storage Implementation ---

# 1. List (for processing all records sequentially)
weather_list = []

# 2. Map/Dictionary (for quick lookup by date)
weather_map = {}

def add_record(record):
    """Adds a record to both the List and the Map."""
    weather_list.append(record)
    weather_map[record.date] = record

if __name__ == "__main__":
    # Creating sample records
    r1 = WeatherRecord("2026-12-03", 76, 56, 98, 2)
    r2 = WeatherRecord("2026-12-04", 80, 60, 90, 0)
    r3 = WeatherRecord("2026-12-05", 65, 45, 10, 5)

    # Storing them
    for rec in [r1, r2, r3]:
        add_record(rec)

    # --- Demonstrating Retrieval ---

    # Example 1: Use the List to calculate average temperature
    all_temps = [r.temperature for r in weather_list]
    avg_temp = sum(all_temps) / len(all_temps)
    print(f"Average Temperature from List: {avg_temp:.2f}°F")

    # Example 2: Use the Map for quick lookup (Efficient Searching)
    search_date = "2026-12-04"
    if search_date in weather_map:
        found_record = weather_map[search_date]
        print(f"Lookup Success! Date: {found_date.date}, Temp: {found_record.temperature}°F")
    else:
        print("Date not found in Map.")