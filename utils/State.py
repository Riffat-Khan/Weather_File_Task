class state:
  def __init__(self, data):
    self.data = data
    self.maxTemp = 0
    self.maxWindSpeed = 0
    self.minTemp = 0
    self.minWindSpeed = 0
    
  def StateMaxTemp(self):
    for each in self.data:
      eachMaxTemp = int(each.get('Data.Temperature.Max Temp'))
      if eachMaxTemp > self.maxTemp:
        self.maxTemp = eachMaxTemp
        city = each.get('Station.City')
        location = each.get('Station.Location')
        code = each.get('Station.Code')
        state = each.get('Station.State')
        
    return self.maxTemp, city, location, code, state
        
  def StateMaxWindSpeed(self):
    for each in self.data:
      eachMaxWindSpeed = float(each.get('Data.Wind.Speed'))
      if eachMaxWindSpeed > self.maxWindSpeed:
        self.maxWindSpeed = eachMaxWindSpeed
        city = each.get('Station.City')
        location = each.get('Station.Location')
        code = each.get('Station.Code')
        state = each.get('Station.State')
 
    return self.maxWindSpeed, city, location, code, state
  
  def StateMinTemp(self):
    for each in self.data:
      eachMinTemp = int(each.get('Data.Temperature.Min Temp'))
      if eachMinTemp > self.minTemp:
        self.minTemp = eachMinTemp
        city = each.get('Station.City')
        location = each.get('Station.Location')
        code = each.get('Station.Code')
        state = each.get('Station.State')
 
    return self.minTemp, city, location, code, state
  
  def StateMinWindSpeed(self):
    for each in self.data:
      eachMinWindSpeed = float(each.get('Data.Wind.Speed'))
      if self.minWindSpeed < eachMinWindSpeed:
        self.minWindSpeed = eachMinWindSpeed
        city = each.get('Station.City')
        location = each.get('Station.Location')
        code = each.get('Station.Code')
        state = each.get('Station.State')
 
    return self.minWindSpeed, city, location, code, state
  

# Find the state with maximum temperature, maximum wind speed, minimum temperature and minimum speed. Export there city, location, code, state