class YearWithMinAvgTemp:
  def __init__(self, data):
    self.data = data
    self.min_avg_temp = 0
    
  def min_avg_temp_year(self):
    for each_array in self.data:
      each_avg_temp = int(each_array.get('Data.Temperature.Avg Temp'))
      if each_avg_temp > self.min_avg_temp:
        self.min_avg_temp = each_avg_temp
        year = each_array.get('Date.Year')
        
    return year, self.min_avg_temp
    