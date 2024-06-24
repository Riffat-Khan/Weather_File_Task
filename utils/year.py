class year:
  def __init__(self, data):
    self.data = data
    self.minAvgTemp = 0
    
  def YearAvgTempMin(self):
    for each in self.data:
      eachAvgTemp = int(each.get('Data.Temperature.Avg Temp'))
      if self.minAvgTemp > eachAvgTemp:
        self.minAvgTemp = eachAvgTemp
        year = each.get('Date.Year')
        
    return year, self.minAvgTemp
    