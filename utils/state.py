class StateData:
  def __init__(self, data):
    self.data = data
    self.max_temp = 0
    self.max_wind_speed = 0
    self.min_temp = 0
    self.min_wind_speed = 0
    
  def state_max_temp(self):
    for each_array in self.data:
      each_max_temp = int(each_array.get('Data.Temperature.Max Temp'))
      if each_max_temp > self.max_temp:
        self.max_temp = each_max_temp
        city = each_array.get('Station.City')
        location = each_array.get('Station.Location')
        code = each_array.get('Station.Code')
        state = each_array.get('Station.State')
        
    return self.max_temp, city, location, code, state
        
  def state_max_wind_speed(self):
    for each_array in self.data:
      each_max_wind_speed = float(each_array.get('Data.Wind.Speed'))
      if each_max_wind_speed > self.max_wind_speed:
        self.max_wind_speed = each_max_wind_speed
        city = each_array.get('Station.City')
        location = each_array.get('Station.Location')
        code = each_array.get('Station.Code')
        state = each_array.get('Station.State')
 
    return self.max_wind_speed, city, location, code, state
  
  def state_min_temp(self):
    for each_array in self.data:
      each_min_temp = int(each_array.get('Data.Temperature.Min Temp'))
      if each_min_temp < self.min_temp:
        self.min_temp = each_min_temp
        city = each_array.get('Station.City')
        location = each_array.get('Station.Location')
        code = each_array.get('Station.Code')
        state = each_array.get('Station.State')
 
    return self.min_temp, city, location, code, state
  
  def state_min_wind_speed(self):
    for each_array in self.data:
      each_min_wind_speed = float(each_array.get('Data.Wind.Speed'))
      if each_min_wind_speed < self.min_wind_speed:
        self.min_wind_speed = each_min_wind_speed
        city = each_array.get('Station.City')
        location = each_array.get('Station.Location')
        code = each_array.get('Station.Code')
        state = each_array.get('Station.State')
 
    return self.min_wind_speed, city, location, code, state
  

# Find the state with maximum temperature, maximum wind speed, minimum temperature and minimum speed. Export there city, location, code, state