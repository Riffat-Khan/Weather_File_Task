class DayMaxTemp:
  def __init__(self, data):
    self.data = data
    self.max_avg_temp = 0
    
  def day_avg_temp_max(self):
    for each_array in self.data:
      each_avg_temp = int(each_array.get('Data.Temperature.Avg Temp'))
      if each_avg_temp > self.max_avg_temp:
        self.max_avg_temp = each_avg_temp
        day = each_array.get('Date.Week of')
        
    return day, self.max_avg_temp
    