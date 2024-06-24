class MaxStateOccurance:
  def __init__(self, data):
    self.data = data
    self.state_count = {}

  def MaxStateOccur(self):
    for each in self.data:
      state = each.get('Station.State')
      if state in self.state_count:
        self.state_count[state] += 1
      else:
        self.state_count[state] = 1

    max_state = max(self.state_count, key=self.state_count.get)

    return max_state, self.state_count[max_state]
  