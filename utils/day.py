class day:
  def __init__(self, data):
    self.data = data
    self.maxAvgTemp = 0
    
  def dayAvgTempMax(self):
    for each in self.data:
      eachAvgTemp = int(each.get('Data.Temperature.Avg Temp'))
      if eachAvgTemp > self.maxAvgTemp:
        self.maxAvgTemp = eachAvgTemp
        day = each.get('Date.Week of')
        
    return day, self.maxAvgTemp
    