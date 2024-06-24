class TemperatureDisplay:

  def __init__(self, data):
    self.data = data
    self.avgMaxTemp = 0
    self.avgMinTemp = 0
    self.sumWindDirection = 0
    self.sumWindSpeed = 0

  def avgMaxMinTemp(self):
    for each in self.data:
      eachAvgTemp = int(each.get('Data.Temperature.Avg Temp'))
      if eachAvgTemp > self.avgMaxTemp:
        self.avgMaxTemp = eachAvgTemp 
      
      if self.avgMinTemp > eachAvgTemp:
        self.avgMinTemp = eachAvgTemp

    return self.avgMaxTemp, self.avgMinTemp
  
  def avgWindDirection(self):
    for each in self.data:
      eachWindDirection = int(each.get('Data.Wind.Direction'))
      self.sumWindDirection += eachWindDirection

    avgWindDirection = self.sumWindDirection/len(self.data) 
    return round(avgWindDirection, 2)
  
  def avgWindSpeed(self):
    for each in self.data:
      eachWindSpeed = float(each.get('Data.Wind.Speed'))
      self.sumWindSpeed += eachWindSpeed

    avgWindSpeed = self.sumWindSpeed/len(self.data)
    return round(avgWindSpeed, 2)
   