import argparse

class arg_parser:

  def __init__(self):
    self.parser = argparse.ArgumentParser(description="A csv file!")
    self.__addArguments()
  
  def __addArguments(self):
    self.parser.add_argument(
      '-f', '--file',
      type=str,
      help='Path to csv file'
    )
    self.parser.add_argument(
      '-c', '--city',
      type=str,
      help='city station '
    )
    self.parser.add_argument(
      '-fr', '--dateFrom',
      type=str,
      help='range start'
    )
    self.parser.add_argument(
      '-end', '--dateTo',
      type=str,
      help='range till'
    )
    self.parser.add_argument(
      '-m', '--maxmin',
      type=str,
      help='the value i.e max/min '
    )
    self.parser.add_argument(
      '-t', '--tempwind',
      type=str,
      help='what to find '
    )
    

  def parse_args(self):
    return self.parser.parse_args()