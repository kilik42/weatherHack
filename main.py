
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

today = WeatherRecord("December 3rd", 76,56,98,2)
print(today.item_list)
