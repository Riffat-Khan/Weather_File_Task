class MaxTempLocState:
  def __init__(self, data):
    self.data = data
    self.avgMax_MaxTemp = 0

  def LocationStateDisplay(self):
    for each in self.data:
      eachAvgMaxTemp = int(each.get('Data.Temperature.Max Temp'))
      if eachAvgMaxTemp > self.avgMax_MaxTemp:
        self.avgMax_MaxTemp = eachAvgMaxTemp
        Location = each.get('Station.Location')
        State = each.get('Station.State')

      return self.avgMax_MaxTemp, Location, State
    