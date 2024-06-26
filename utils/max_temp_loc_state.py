class MaxTempLocState:
  def __init__(self, data):
    self.data = data
    self.max_temp_max_col = 0

  def location_state_display(self):
    for record in self.data:
      each_max_temp = int(record.get('Data.Temperature.Max Temp'))
      if each_max_temp > self.max_temp_max_col:
        self.max_temp_max_col = each_max_temp
        location = record.get('Station.Location')
        state = record.get('Station.State')

    return self.max_temp_max_col, location, state
    