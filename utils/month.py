class month_with_max_avg_temp:
  def __init__(self, data):
    self.data = data
    self.max_avg_temp = 0
    
  def max_avg_temp_month(self):
    for each_array in self.data:
      each_avg_temp = int(each_array.get('Data.Temperature.Avg Temp'))
      if each_avg_temp > self.max_avg_temp:
        self.max_avg_temp = each_avg_temp
        month = each_array.get('Date.Month')
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
        
    return month, self.max_avg_temp
    