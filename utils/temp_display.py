class TemperatureDisplay:

  def __init__(self, data):
    self.data = data
    self.sum_max_temp = 0
    self.sum_min_temp = 0
    self.sum_wind_direction = 0
    self.sum_wind_speed = 0

  def avg_max_temp(self):
    for record in self.data:
      each_avg_max_temp = int(record.get('Data.Temperature.Max Temp'))
      self.sum_max_temp += each_avg_max_temp 
        
    avg_max_temp = self.sum_max_temp/len(self.data)
    return avg_max_temp
  
  def avg_min_temp(self):
    for record in self.data:
      each_avg_min_temp = int(record.get('Data.Temperature.Min Temp'))
      self.sum_min_temp += each_avg_min_temp 
        
    avg_min_temp = self.sum_min_temp/len(self.data)
    return avg_min_temp
  
  def avg_wind_direction(self):
    for record in self.data:
      each_wind_direction = int(record.get('Data.Wind.Direction'))
      self.sum_wind_direction += each_wind_direction

    avg_wind_direction = self.sum_wind_direction/len(self.data) 
    return round(avg_wind_direction, 2)
  
  def avg_wind_speed(self):
    for record in self.data:
      eachWindSpeed = float(record.get('Data.Wind.Speed'))
      self.sum_wind_speed += eachWindSpeed

    avgWindSpeed = self.sum_wind_speed/len(self.data)
    return round(avgWindSpeed, 2)
   