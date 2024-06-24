class month:
  def __init__(self, data):
    self.data = data
    self.maxAvgTemp = 0
    
  def monthAvgTempMax(self):
    for each in self.data:
      eachAvgTemp = int(each.get('Data.Temperature.Avg Temp'))
      if eachAvgTemp > self.maxAvgTemp:
        self.maxAvgTemp = eachAvgTemp
        month = each.get('Date.Month')
        months = {
          '1' : 'January',
          '2' : 'Feburary',
          '3' : 'March',
          '4' : 'April',
          '5' : 'May',
          '6' : 'June',
          '7' : 'July',
          '8' : 'August',
          '9' : 'September',
          '10' : 'October',
          '11' : 'November',
          '12' : 'December'}
        month = months[month]
        
    return month, self.maxAvgTemp
    