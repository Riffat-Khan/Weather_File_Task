class MaxTempLocState:
  def __init__(self, data):
    self.data = data
    self.max_temp_max_col = 0

  def location_state_display(self):
    for each_array in self.data:
      each_max_temp = int(each_array.get('Data.Temperature.Max Temp'))
      if each_max_temp > self.max_temp_max_col:
        self.max_temp_max_col = each_max_temp
        Location = each_array.get('Station.Location')
        State = each_array.get('Station.State')

      return self.max_temp_max_col, Location, State
    