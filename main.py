import date

class WeatherRecord:
  def __init__(self, date, temperature, humidity,windSpeed,rainfall):
    self.date = date
    self.temperature = temperature
    self.humidity = humidity
    self.windSpeed = windSpeed
    self.rainfall = rainfall

today = WeatherRecord("December 3rd", 76,56,98,2)
print(today.temperature)
